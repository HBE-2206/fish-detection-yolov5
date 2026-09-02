import argparse
from pathlib import Path

import cv2
import torch


def load_model(model_path: str, confidence: float):
    model = torch.hub.load(
        "ultralytics/yolov5",
        "custom",
        path=model_path,
        force_reload=False,
    )
    model.conf = confidence
    return model


def detect_image(model, image_path: str, output_path: str):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    results = model(image)
    rendered = results.render()[0]
    rendered_bgr = cv2.cvtColor(rendered, cv2.COLOR_RGB2BGR)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output), rendered_bgr)

    detections = results.xyxy[0]
    count = int(len(detections))

    print(f"Fish detected: {count}")
    print(f"Result saved to: {output.resolve()}")


def main():
    parser = argparse.ArgumentParser(
        description="Detect fish in an aquarium image using a custom YOLOv5 model."
    )
    parser.add_argument("--image", required=True, help="Path to the input aquarium image.")
    parser.add_argument("--weights", default="weights/best.pt", help="Path to trained checkpoint.")
    parser.add_argument("--output", default="results/fish_detection.jpg", help="Annotated output path.")
    parser.add_argument("--confidence", type=float, default=0.25, help="Minimum confidence threshold.")
    args = parser.parse_args()

    model = load_model(args.weights, args.confidence)
    detect_image(model, args.image, args.output)


if __name__ == "__main__":
    main()
