# 🐟 Fish Detection with YOLOv5

A computer vision project that uses a **custom-trained YOLOv5s object-detection model** to detect fish in aquarium images.

## ✨ What this project does

Upload an aquarium image and the model will:

1. Detect the fish.
2. Draw a bounding box around each detection.
3. Display the class name and confidence score.
4. Report the total number of detected fish.
5. Save the annotated image to `results/`.

## 📌 Model

| Setting | Value |
|---|---|
| Architecture | YOLOv5s |
| Image size | 640 × 640 |
| Training epochs | 60 |
| Batch size | 16 |
| Training images | 444 |
| Validation images | 157 |
| Custom checkpoint | `weights/best.pt` |

The supplied training log records a later validation result of approximately **0.87 mAP@0.5** and **0.452 mAP@0.5:.95**. These are historical values recorded by the original run, not a newly reproduced benchmark.

## 📁 Repository Structure

```text
fish-detection-yolov5/
├── fish_detection_yolov5.ipynb
├── detect_fish.py
├── test_images/
│   └── aquarium_test_01.png
├── results/
├── weights/
│   └── best.pt
├── requirements.txt
├── PROJECT_STRUCTURE.md
├── .gitignore
└── README.md
```

> The original training dataset is not included.

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/HBE-2206/fish-detection-yolov5.git
cd fish-detection-yolov5
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run detection

```bash
python detect_fish.py \
  --image test_images/aquarium_test_01.png \
  --weights weights/best.pt \
  --output results/aquarium_test_01_detection.jpg
```

The script prints the number of detected fish and saves the annotated result.

## ☁️ Google Colab

Open `fish_detection_yolov5.ipynb`.

The notebook lets you upload **any aquarium image** and runs the custom model on it. The annotated result is saved automatically.

## 🧪 Test Image

A sample aquarium image is included under:

```text
test_images/aquarium_test_01.png
```

This image is an **input test image**. It is not presented as a model-generated result.

## 🏋️ Training

Training is optional and requires the original YOLO-format dataset and configuration file.

The original training command was:

```bash
python train.py --img 640 --batch 16 --epochs 60 --data custom_data.yaml --weights yolov5s.pt --cache
```

## 🛠️ Technologies

- Python
- PyTorch
- YOLOv5
- OpenCV
- Jupyter Notebook
- Google Colab

## 📚 References

- [YOLOv5](https://github.com/ultralytics/yolov5)
- [Ultralytics Documentation](https://docs.ultralytics.com)

## 👤 Author

**Hazem Elshafey**
