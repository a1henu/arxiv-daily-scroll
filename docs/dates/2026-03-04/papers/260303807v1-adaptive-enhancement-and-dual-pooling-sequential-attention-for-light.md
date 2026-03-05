---
layout: default
title: Adaptive Enhancement and Dual-Pooling Sequential Attention for Lightweight Underwater Object Detection with YOLOv10
---

# Adaptive Enhancement and Dual-Pooling Sequential Attention for Lightweight Underwater Object Detection with YOLOv10
**arXiv**：[2603.03807v1](https://arxiv.org/abs/2603.03807) · [PDF](https://arxiv.org/pdf/2603.03807.pdf)  
**作者**：Md. Mushibur Rahman, Umme Fawzia Rahim, Enam Ahmed Taufik  

**一句话要点**：提出自适应增强与双池化序列注意力机制，以提升轻量级水下目标检测性能。

**关键词**：水下目标检测, 轻量级模型, 注意力机制, 图像增强, YOLOv10, 损失函数优化

## 3 点简述
- 核心问题：水下图像因光吸收、散射和低对比度导致视觉退化，影响目标检测精度。
- 方法要点：集成多阶段自适应增强模块、双池化序列注意力机制和Focal Generalized IoU损失，优化特征表示与定位。
- 实验或效果：在RUOD和DUO数据集上mAP分别达88.9%和88.0%，相比基线提升超6%，参数仅2.8M。

## 摘要（原文）

> Underwater object detection constitutes a pivotal endeavor within the realms of marine surveillance and autonomous underwater systems; however, it presents significant challenges due to pronounced visual impairments arising from phenomena such as light absorption, scattering, and diminished contrast. In response to these formidable challenges, this manuscript introduces a streamlined yet robust framework for underwater object detection, grounded in the YOLOv10 architecture. The proposed method integrates a Multi-Stage Adaptive Enhancement module to improve image quality, a Dual-Pooling Sequential Attention (DPSA) mechanism embedded into the backbone to strengthen multi-scale feature representation, and a Focal Generalized IoU Objectness (FGIoU) loss to jointly improve localization accuracy and objectness prediction under class imbalance. Comprehensive experimental evaluations conducted on the RUOD and DUO benchmark datasets substantiate that the proposed DPSA_FGIoU_YOLOv10n attains exceptional performance, achieving mean Average Precision (mAP) scores of 88.9% and 88.0% at IoU threshold 0.5, respectively. In comparison to the baseline YOLOv10n, this represents enhancements of 6.7% for RUOD and 6.2% for DUO, all while preserving a compact model architecture comprising merely 2.8M parameters. These findings validate that the proposed framework establishes an efficacious equilibrium among accuracy, robustness, and real-time operational efficiency, making it suitable for deployment in resource-constrained underwater settings.

