# Fish Detection with YOLOv5

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/YOLOv5-Object%20Detection-7B61FF?style=for-the-badge" alt="YOLOv5"/>
  <img src="https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Google Colab"/>
</p>

A computer-vision project using a custom-trained YOLOv5s detector to locate fish in aquarium images. Given an image, the workflow predicts bounding boxes, class labels, confidence scores, and a total detection count, then saves an annotated image.

> **Project status:** Educational / portfolio project. The metrics described below are from an existing training log; they have not been independently reproduced in this update. Detection counts depend on image quality, the training data, and the confidence threshold.

## Demo

**Example input and output**

### Original image
<img width="900" alt="Original aquarium image" src="https://github.com/user-attachments/assets/8815c200-db69-445e-b5b7-954ccf8bd599" />

### Annotated detection
<img width="900" alt="Aquarium image with fish detections" src="https://github.com/user-attachments/assets/46ad81de-e393-4654-9cc0-117a9e44a717" />

## Model details

| Setting | Value |
|---|---|
| Architecture | YOLOv5s |
| Input size | 640 × 640 |
| Recorded training epochs | 60 |
| Recorded batch size | 16 |
| Training images (reported) | 444 |
| Validation images (reported) | 157 |
| Checkpoint | `weights/best.pt` |
| Reported validation mAP@0.5 | approximately 0.87 |
| Reported validation mAP@0.5:0.95 | approximately 0.452 |

The metrics are historical values described by the repository's prior documentation, not a new evaluation run. The original training dataset and configuration are not included, so another user may not be able to reproduce the exact result from this repository alone.

## Repository structure

```text
fish-detection-yolov5/
├── README.md
├── PROJECT_STRUCTURE.md
├── detect_fish.py
├── fish_detection_yolov5.ipynb
├── requirements.txt
├── weights/
│   └── best.pt
├── test_images/
│   ├── original/
│   └── results/
└── results/
    ├── training/
    └── samples/
```

Generated result images and large training artifacts may be excluded from Git using `.gitignore`; confirm the files are present before linking to them.

## Run on Google Colab

[**Open the notebook in Google Colab**](https://colab.research.google.com/github/HBE-2206/fish-detection-yolov5/blob/main/fish_detection_yolov5.ipynb)

1. Open the notebook and connect to a runtime.
2. Run the setup cells to download the YOLOv5 source and dependencies.
3. Ensure the custom checkpoint `weights/best.pt` is available at the expected path.
4. Upload an aquarium/fish image when prompted.
5. Run inference to view the annotated image, detections, and count.
6. Download the result image from the final cell.

Colab runtimes are temporary. Files created in the runtime may be lost when the session ends unless downloaded or saved to persistent storage.

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/HBE-2206/fish-detection-yolov5.git
cd fish-detection-yolov5
```

### 2. Install dependencies

Create and activate a virtual environment (recommended), then install:

```bash
python -m pip install -r requirements.txt
```

YOLOv5 and PyTorch dependencies can be sensitive to Python and CUDA versions. If installation fails, use a supported Python version and follow the official [YOLOv5 installation guidance](https://github.com/ultralytics/yolov5).

### 3. Run inference

```bash
python detect_fish.py --image path/to/aquarium.jpg
```

With optional settings:

```bash
python detect_fish.py \
  --image path/to/aquarium.jpg \
  --weights weights/best.pt \
  --output results/fish_detection.jpg \
  --confidence 0.25
```

The confidence threshold defaults to `0.25`. Increase it to reduce weaker detections or lower it to inspect more candidate detections; evaluate the effect on representative images before choosing a final setting.

## Training

Training requires the original labeled YOLO-format dataset and its dataset YAML, which are not included here. The historical command recorded for the project was:

```bash
python train.py --img 640 --batch 16 --epochs 60 --data custom_data.yaml --weights yolov5s.pt --cache
```

Run this from a compatible YOLOv5 source checkout and replace `custom_data.yaml` with the actual dataset configuration. This command is provided as historical context; it has not been executed as part of the current README update.

## Technologies

- Python
- PyTorch
- YOLOv5
- OpenCV
- NumPy and Matplotlib
- Jupyter Notebook / Google Colab

## References

- [YOLOv5 source repository](https://github.com/ultralytics/yolov5)
- [Ultralytics documentation](https://docs.ultralytics.com)

## Author

**Hazem Elshafey**

- GitHub: [@HBE-2206](https://github.com/HBE-2206)
- LinkedIn: [Hazem Elshafey](https://www.linkedin.com/in/hazem-el-shafey-b56405331)
- Email: [hm2502630@gmail.com](mailto:hm2502630@gmail.com)
