---
layout: default
title: Autoencoder-based Denoising Defense against Adversarial Attacks on Object Detection
---

# Autoencoder-based Denoising Defense against Adversarial Attacks on Object Detection
**arXiv**：[2512.16123v1](https://arxiv.org/abs/2512.16123) · [PDF](https://arxiv.org/pdf/2512.16123.pdf)  
**作者**：Min Geun Song, Gang Min Kim, Woonmin Kim, Yongsik Kim, Jeonghyun Sim, Sangbeom Park, Huy Kang Kim  

**一句话要点**：提出基于自编码器的去噪防御方法，以恢复对抗攻击下目标检测模型的性能。

**关键词**：目标检测, 对抗攻击防御, 自编码器去噪, Perlin噪声, YOLOv5, COCO数据集

## 3 点简述
- 核心问题：基于深度学习的目标检测模型易受对抗样本攻击，影响自动驾驶等应用。
- 方法要点：使用单层卷积自编码器去除Perlin噪声生成的对抗扰动，无需模型重训练。
- 实验效果：在COCO数据集上，bbox mAP从0.1640恢复至0.1700，部分防御效果得到验证。

## 摘要（原文）

> Deep learning-based object detection models play a critical role in real-world applications such as autonomous driving and security surveillance systems, yet they remain vulnerable to adversarial examples. In this work, we propose an autoencoder-based denoising defense to recover object detection performance degraded by adversarial perturbations. We conduct adversarial attacks using Perlin noise on vehicle-related images from the COCO dataset, apply a single-layer convolutional autoencoder to remove the perturbations, and evaluate detection performance using YOLOv5. Our experiments demonstrate that adversarial attacks reduce bbox mAP from 0.2890 to 0.1640, representing a 43.3% performance degradation. After applying the proposed autoencoder defense, bbox mAP improves to 0.1700 (3.7% recovery) and bbox mAP@50 increases from 0.2780 to 0.3080 (10.8% improvement). These results indicate that autoencoder-based denoising can provide partial defense against adversarial attacks without requiring model retraining.

