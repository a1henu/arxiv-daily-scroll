---
layout: default
title: Robust Multi-Disease Retinal Classification via Xception-Based Transfer Learning and W-Net Vessel Segmentation
---

# Robust Multi-Disease Retinal Classification via Xception-Based Transfer Learning and W-Net Vessel Segmentation
**arXiv**：[2512.10608v1](https://arxiv.org/abs/2512.10608) · [PDF](https://arxiv.org/pdf/2512.10608.pdf)  
**作者**：Mohammad Sadegh Gholizadeh, Amir Arsalan Rezapour  

**一句话要点**：提出基于Xception迁移学习和W-Net血管分割的稳健多疾病视网膜分类方法，以提升临床部署可行性。

**关键词**：视网膜分类, 迁移学习, 血管分割, 可解释性, 深度学习, 医学图像分析

## 3 点简述
- 核心问题：眼病发病率上升，需可扩展且准确的自动诊断方案，同时解决CNN黑盒限制。
- 方法要点：结合深度特征提取与可解释图像处理模块，利用高保真视网膜血管分割作为辅助任务指导分类。
- 实验或效果：旨在通过临床相关形态特征减少假阳性，提高算法输出与医学验证的匹配度。

## 摘要（原文）

> In recent years, the incidence of vision-threatening eye diseases has risen dramatically, necessitating scalable and accurate screening solutions. This paper presents a comprehensive study on deep learning architectures for the automated diagnosis of ocular conditions. To mitigate the "black-box" limitations of standard convolutional neural networks (CNNs), we implement a pipeline that combines deep feature extraction with interpretable image processing modules. Specifically, we focus on high-fidelity retinal vessel segmentation as an auxiliary task to guide the classification process. By grounding the model's predictions in clinically relevant morphological features, we aim to bridge the gap between algorithmic output and expert medical validation, thereby reducing false positives and improving deployment viability in clinical settings.

