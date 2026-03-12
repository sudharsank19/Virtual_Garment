# 👕 Virtual Garment Try-On System
### AI Powered Virtual Clothing Simulation using Deep Learning

![Python](https://img.shields.io/badge/Python-3.9-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green)
![Status](https://img.shields.io/badge/Project-FinalYear-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 📌 Project Overview

The **Virtual Garment Try-On System** is an AI-based application that allows users to **virtually try clothes using computer vision and deep learning techniques**.

Instead of physically wearing clothes, users can upload an image and visualize how garments will look on them.

This system uses **pose estimation, human segmentation, and garment warping networks** to generate a realistic image of a person wearing the selected clothing.

---

## 🎯 Objectives

• Provide a virtual fitting experience for online shoppers  
• Reduce return rates in e-commerce platforms  
• Improve user shopping experience  
• Demonstrate real-world application of deep learning in fashion technology  

---

## 🧠 System Architecture

The pipeline of the Virtual Try-On system is shown below.

![Architecture](docs/architecture.png)

### Processing Pipeline

1️⃣ User Image Input  
2️⃣ Clothing Image Input  
3️⃣ Human Pose Detection  
4️⃣ Body Segmentation  
5️⃣ Cloth Mask Generation  
6️⃣ Garment Warping  
7️⃣ Final Rendering  

The output is a **realistic image of the user wearing the selected garment**.

---

## 📷 Example Results

### Input Image

| Person Image | Clothing Image |
|--------------|---------------|
| ![Person](docs/input_person.jpg) | ![Cloth](docs/cloth.jpg) |

### Output

| Virtual Try-On Result |
|----------------------|
| ![Output](docs/output_tryon.jpg) |

---

## 🧰 Technologies Used

### Programming Languages

• Python  
• JavaScript  

### Computer Vision

• OpenCV  
• NumPy  

### Deep Learning Framework

• PyTorch  

### AI Models

• OpenPose — Human Pose Estimation  
• Graphonomy — Human Segmentation  
• SCHP — Self-Correction Human Parsing  
• VITON-HD — Virtual Try-On Network  

---

## 📂 Project Structure

```
Virtual_Garment
│
├── Graphonomy
├── SCHP
├── VITONHD
├── openpose
│
├── frontend
├── backend
│
├── docs
│   ├── architecture.png
│   ├── input_person.jpg
│   └── output_tryon.jpg
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sudharsank19/Virtual_Garment.git
cd Virtual_Garment
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Download Pretrained Models

Due to **GitHub file size limits**, pretrained model weights are not included in the repository.

Download the models from the following sources:

Graphonomy  
https://github.com/Gaoyiminggithub/Graphonomy

OpenPose  
https://github.com/CMU-Perceptual-Computing-Lab/openpose

VITON-HD  
https://github.com/shadow2496/VITON-HD

SCHP  
https://github.com/GoGoDuck912/Self-Correction-Human-Parsing

After downloading, place them inside:

```
Graphonomy/checkpoints/
SCHP/checkpoints/
VITONHD/checkpoints/
openpose/models/
```

---

## ▶️ Running the Project

After installing dependencies and downloading models:

```bash
python inference.py
```

The system will generate a **virtual try-on image**.

---

## 📊 Applications

• Online clothing stores  
• Virtual fitting rooms  
• Fashion AI platforms  
• E-commerce applications  
• AI-based shopping assistants  

---

## 🚀 Future Improvements

• Real-time webcam virtual try-on  
• 3D body shape estimation  
• Mobile application version  
• Multi-garment try-on support  
• Improved cloth deformation realism  

---

## 📚 Research Background

The project is inspired by research works in:

• Virtual Try-On Networks (VITON)  
• Human Pose Estimation  
• Image-based Clothing Transfer  
• Human Parsing Networks  

---

## 👨‍💻 Author

**Sudharsan K**

B.Tech Information Technology  
Final Year Project

GitHub  
https://github.com/sudharsank19

---

## ⭐ Acknowledgements

This project is built using open-source contributions from:

• OpenPose  
• VITON-HD  
• Graphonomy  
• SCHP Human Parsing  

---

## 📜 License

This project is developed for **educational and research purposes only**.

---

⭐ If you find this project useful, please consider **starring the repository**.
