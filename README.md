# 🐟 Fish Detection with YOLOv5

A computer vision project that uses a **custom-trained YOLOv5s object-detection model** to detect fish in aquarium images.

## ✨ What this project does

Upload an aquarium image and the model will:

1. Detect fish.
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
| Checkpoint | `weights/best.pt` |

The supplied training log records a later validation result of approximately **0.87 mAP@0.5** and **0.452 mAP@0.5:.95**. These are historical values from the supplied run, not a newly reproduced benchmark.

## 📁 Repository Structure

```text
fish-detection-yolov5/
│
├── README.md
├── fish_detection_yolov5.ipynb
├── detect_fish.py
├── requirements.txt
├── weights/
│   └── best.pt
│
├── test_images/
│   ├── original/
│   │   └── aquarium_test_01.jpg
│   │
│   └── results/
│       └── aquarium_detection_01.jpg
│
└── results/
    ├── training/
    │   ├── results.png
    │   └── confusion_matrix.png
    │
    └── samples/
        └── detection_result.jpg
```

> The original training dataset is not included in this repository.

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

### 3. Run detection on an image

```bash
python detect_fish.py --image path/to/aquarium.jpg
```

Optional arguments:

```bash
python detect_fish.py \
  --image path/to/aquarium.jpg \
  --weights weights/best.pt \
  --output results/aquarium_detection.jpg \
  --confidence 0.25
```
## Detection Result

### Original Image
<img width="1268" height="786" alt="Screenshot 2026-09-02 121848" src="https://github.com/user-attachments/assets/8815c200-db69-445e-b5b7-954ccf8bd599" />


### Detection Result
<img width="1268" height="786" alt="fish_detection" src="https://github.com/user-attachments/assets/46ad81de-e393-4654-9cc0-117a9e44a717" />


The annotated image is written to `results/` and the console reports the number of detections.

## ☁️ Google Colab

Open `fish_detection_yolov5.ipynb`.

The notebook lets you upload **any aquarium image** and runs the custom model on it automatically. It then displays the image with bounding boxes, confidence scores, and the total fish count, and saves the annotated result.

## 🧪 Testing

Use `test_images/` for aquarium images used in evaluation or demonstration. The image you supplied in the conversation can be used as a test input, but it has **not been committed to GitHub by the current integration**.

To test locally:

```bash
python detect_fish.py --image test_images/aquarium_test_01.jpg
```

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
- Matplotlib
- Jupyter Notebook
- Google Colab

## 📚 References

- [YOLOv5](https://github.com/ultralytics/yolov5)
- [Ultralytics Documentation](https://docs.ultralytics.com)

## 👤 Author

**Hazem Elshafey**
