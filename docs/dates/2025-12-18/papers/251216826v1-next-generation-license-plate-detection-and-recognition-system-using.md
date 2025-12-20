---
layout: default
title: Next-Generation License Plate Detection and Recognition System using YOLOv8
---

# Next-Generation License Plate Detection and Recognition System using YOLOv8
**arXiv**：[2512.16826v1](https://arxiv.org/abs/2512.16826) · [PDF](https://arxiv.org/pdf/2512.16826.pdf)  
**作者**：Arslan Amin, Rafia Mumtaz, Muhammad Jawad Bashir, Syed Mohammad Hassan Zaidi  

**一句话要点**：提出基于YOLOv8的优化车牌检测与识别系统，以提升智能交通系统中的实时准确性和计算效率。

**关键词**：车牌检测, 字符识别, YOLOv8, 智能交通系统, 实时处理, 边缘设备部署

## 3 点简述
- 核心问题：车牌检测与识别在多样化环境中实时准确性不足，影响智能交通系统部署。
- 方法要点：采用YOLOv8 Nano进行车牌检测，YOLOv8 Small进行字符识别，并引入基于x轴位置的字符排序方法。
- 实验或效果：YOLOv8 Nano在车牌检测任务中精度达0.964，YOLOv8 Small在字符识别任务中精度达0.92，系统兼顾高精度与计算效率。

## 摘要（原文）

> In the evolving landscape of traffic management and vehicle surveillance, efficient license plate detection and recognition are indispensable. Historically, many methodologies have tackled this challenge, but consistent real-time accuracy, especially in diverse environments, remains elusive. This study examines the performance of YOLOv8 variants on License Plate Recognition (LPR) and Character Recognition tasks, crucial for advancing Intelligent Transportation Systems. Two distinct datasets were employed for training and evaluation, yielding notable findings. The YOLOv8 Nano variant demonstrated a precision of 0.964 and mAP50 of 0.918 on the LPR task, while the YOLOv8 Small variant exhibited a precision of 0.92 and mAP50 of 0.91 on the Character Recognition task. A custom method for character sequencing was introduced, effectively sequencing the detected characters based on their x-axis positions. An optimized pipeline, utilizing YOLOv8 Nano for LPR and YOLOv8 Small for Character Recognition, is proposed. This configuration not only maintains computational efficiency but also ensures high accuracy, establishing a robust foundation for future real-world deployments on edge devices within Intelligent Transportation Systems. This effort marks a significant stride towards the development of smarter and more efficient urban infrastructures.

