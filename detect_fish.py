import argparse
from pathlib import Path

import cv2
import torch


def load_model(model_path: str, confidence: float):
    """Load the custom YOLOv5 checkpoint and configure inference confidence."""
    path = Path(model_path)
    if not path.is_file():
        raise FileNotFoundError(
            f"Checkpoint not found: {path}. Download the trained weights to this path first."
        )
    if not 0.0 <= confidence <= 1.0:
        raise ValueError("--confidence must be between 0.0 and 1.0")

    model = torch.hub.load(
        "ultralytics/yolov5",
        "custom",
        path=str(path),
        force_reload=False,
    )
    model.conf = confidence
    return model


def detect_image(model, image_path: str, output_path: str):
    """Run inference, save the annotated image, and print detection details."""
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    results = model(image)
    detections = results.xyxy[0].detach().cpu().numpy()
    annotated_rgb = results.render()[0]

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    # YOLOv5 render output is RGB; OpenCV writes BGR.
    if not cv2.imwrite(str(output), cv2.cvtColor(annotated_rgb, cv2.COLOR_RGB2BGR)):
        raise OSError(f"Could not write annotated image to: {output}")

    count = len(detections)
    print(f"Fish detected: {count}")
    print(f"Result saved to: {output.resolve()}")
    for idx, detection in enumerate(detections, start=1):
        x1, y1, x2, y2, confidence, class_id = detection
        class_name = model.names[int(class_id)]
        print(
            f"{idx}. {class_name} | confidence={confidence:.3f} | "
            f"box=({int(x1)}, {int(y1)}, {int(x2)}, {int(y2)})"
        )
    return detections


def main():
    parser = argparse.ArgumentParser(
        description="Detect fish in an aquarium image using a custom YOLOv5 model."
    )
    parser.add_argument("--image", required=True, help="Path to the input aquarium image.")
    parser.add_argument("--weights", default="weights/best.pt", help="Path to trained checkpoint.")
    parser.add_argument("--output", default="results/fish_detection.jpg", help="Annotated output path.")
    parser.add_argument(
        "--confidence", type=float, default=0.25,
        help="Minimum confidence threshold between 0 and 1 (default: 0.25).",
    )
    args = parser.parse_args()

    model = load_model(args.weights, args.confidence)
    detect_image(model, args.image, args.output)


if __name__ == "__main__":
    main()
