# 🐟 Fish Detection with YOLOv5

A computer vision project for **fish detection** using a custom-trained **YOLOv5s** object-detection model.

The repository contains the trained model checkpoint and a cleaned Jupyter/Google Colab notebook for running inference on images and videos.

## ✨ Features

- Custom YOLOv5s fish detector
- Image detection
- Video detection
- Google Colab compatible workflow
- Included trained checkpoint: `weights/best.pt`
- Reproducible inference commands

## 🧠 Model

The supplied training run used:

| Setting | Value |
|---|---|
| Architecture | YOLOv5s |
| Image size | 640 × 640 |
| Epochs | 60 |
| Batch size | 16 |
| Starting weights | `yolov5s.pt` |
| Training images | 444 |
| Validation images | 157 |

The training log shows a later-epoch validation result of approximately **0.87 mAP@0.5** and **0.452 mAP@0.5:.95**. These are results recorded in the supplied notebook, not a freshly reproduced benchmark.

## 📁 Repository Structure

```text
fish-detection-yolov5/
├── fish_detection_yolov5.ipynb
├── weights/
│   └── best.pt
├── requirements.txt
├── .gitignore
├── PROJECT_STRUCTURE.md
└── README.md
```

> The original training dataset is not included in this repository.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/HBE-2206/fish-detection-yolov5.git
cd fish-detection-yolov5
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Windows:

```bash
.venv\\Scripts\\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Open the notebook

Open `fish_detection_yolov5.ipynb`.

The notebook clones YOLOv5, installs its dependencies, and uses `weights/best.pt` for inference.

## 🔍 Inference

After cloning YOLOv5 inside the notebook, an image can be processed with:

```bash
python detect.py --weights ../weights/best.pt --img 640 --conf 0.25 --source path/to/image.jpg
```

For a video:

```bash
python detect.py --weights ../weights/best.pt --img 640 --conf 0.25 --source path/to/video.mp4
```

Detection results are written to YOLOv5's `runs/detect/` directory.

## ☁️ Google Colab

The notebook is designed to work with Google Colab. Run the setup cells, then upload an image/video or provide a source path and run the detection command.

## 🏋️ Training (Optional)

Training requires the original custom dataset and its YOLO-format configuration file. They are intentionally not committed because the supplied project files do not include the dataset itself.

The original training command was:

```bash
python train.py --img 640 --batch 16 --epochs 60 --data custom_data.yaml --weights yolov5s.pt --cache
```

## 📊 Dataset

The supplied notebook records:

- **444** training images
- **157** validation images

The training log also records several JPEG files being repaired during dataset scanning.

## 🛠️ Technologies

- Python
- PyTorch
- YOLOv5
- OpenCV
- Jupyter Notebook
- Google Colab

## 📌 Notes

- `weights/best.pt` is the trained checkpoint supplied with this project.
- The dataset is not included.
- The repository uses YOLOv5 for inference rather than copying the entire YOLOv5 source tree into this repository.
- Model performance can vary depending on the input data and inference settings.

## 📚 References

- [YOLOv5](https://github.com/ultralytics/yolov5)
- [Ultralytics Documentation](https://docs.ultralytics.com)

## 👤 Author

**Hazem Mohamed**
