---
layout: default
title: Enhanced Landmark Detection Model in Pelvic Fluoroscopy using 2D/3D Registration Loss
---

# Enhanced Landmark Detection Model in Pelvic Fluoroscopy using 2D/3D Registration Loss
**arXiv**：[2511.21575v1](https://arxiv.org/abs/2511.21575) · [PDF](https://arxiv.org/pdf/2511.21575.pdf)  
**作者**：Chou Mo, Yehyun Suh, J. Ryan Martin, Daniel Moyer  

**一句话要点**：提出结合2D/3D配准损失的U-Net框架，以解决骨盆透视中患者姿态变化导致的标志检测问题

**关键词**：骨盆透视, 标志检测, 2D/3D配准, U-Net模型, 姿态估计损失, 医学影像分析

## 3 点简述
- 核心问题：骨盆透视中患者姿态常偏离标准视图，影响自动化标志检测准确性。
- 方法要点：在U-Net训练中引入2D/3D标志配准损失，提升模型对姿态变化的鲁棒性。
- 实验或效果：比较基线U-Net、姿态估计损失训练和微调模型，评估可变姿态下的检测精度。

## 摘要（原文）

> Automated landmark detection offers an efficient approach for medical professionals to understand patient anatomic structure and positioning using intra-operative imaging. While current detection methods for pelvic fluoroscopy demonstrate promising accuracy, most assume a fixed Antero-Posterior view of the pelvis. However, orientation often deviates from this standard view, either due to repositioning of the imaging unit or of the target structure itself. To address this limitation, we propose a novel framework that incorporates 2D/3D landmark registration into the training of a U-Net landmark prediction model. We analyze the performance difference by comparing landmark detection accuracy between the baseline U-Net, U-Net trained with Pose Estimation Loss, and U-Net fine-tuned with Pose Estimation Loss under realistic intra-operative conditions where patient pose is variable.

