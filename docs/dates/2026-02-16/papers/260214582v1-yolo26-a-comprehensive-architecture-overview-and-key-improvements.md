---
layout: default
title: YOLO26: A Comprehensive Architecture Overview and Key Improvements
---

# YOLO26: A Comprehensive Architecture Overview and Key Improvements
**arXiv**：[2602.14582v1](https://arxiv.org/abs/2602.14582) · [PDF](https://arxiv.org/pdf/2602.14582.pdf)  
**作者**：Priyanto Hidayatullah, Refdinal Tubagus  

**一句话要点**：提出YOLO26架构以提升CPU推理速度并扩展计算机视觉任务能力

**关键词**：YOLO26架构, CPU推理优化, 端到端无NMS, 标签分配策略, 计算机视觉任务扩展

## 3 点简述
- 核心问题：YOLO系列在CPU或边缘设备上实现实时性能的挑战，需优化推理速度与任务多样性。
- 方法要点：通过消除DFL、引入端到端无NMS推理、ProgLoss+STAL标签分配及MuSGD优化器，提升效率。
- 实验或效果：声称在CPU模式下推理速度提升43%，支持实例分割、姿态估计和定向边界框解码等任务。

## 摘要（原文）

> You Only Look Once (YOLO) has been the prominent model for computer vision in deep learning for a decade. This study explores the novel aspects of YOLO26, the most recent version in the YOLO series. The elimination of Distribution Focal Loss (DFL), implementation of End-to-End NMS-Free Inference, introduction of ProgLoss + Small-Target-Aware Label Assignment (STAL), and use of the MuSGD optimizer are the primary enhancements designed to improve inference speed, which is claimed to achieve a 43% boost in CPU mode. This is designed to allow YOLO26 to attain real-time performance on edge devices or those without GPUs. Additionally, YOLO26 offers improvements in many computer vision tasks, including instance segmentation, pose estimation, and oriented bounding box (OBB) decoding. We aim for this effort to provide more value than just consolidating information already included in the existing technical documentation. Therefore, we performed a rigorous architectural investigation into YOLO26, mostly using the source code available in its GitHub repository and its official documentation. The authentic and detailed operational mechanisms of YOLO26 are inside the source code, which is seldom extracted by others. The YOLO26 architectural diagram is shown as the outcome of the investigation. This study is, to our knowledge, the first one presenting the CNN-based YOLO26 architecture, which is the core of YOLO26. Our objective is to provide a precise architectural comprehension of YOLO26 for researchers and developers aspiring to enhance the YOLO model, ensuring it remains the leading deep learning model in computer vision.

