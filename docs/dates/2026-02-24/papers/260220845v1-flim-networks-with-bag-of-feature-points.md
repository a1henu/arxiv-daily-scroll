---
layout: default
title: FLIM Networks with Bag of Feature Points
---

# FLIM Networks with Bag of Feature Points
**arXiv**：[2602.20845v1](https://arxiv.org/abs/2602.20845) · [PDF](https://arxiv.org/pdf/2602.20845.pdf)  
**作者**：João Deltregia Martinelli, Marcelo Luis Rodrigues Filho, Felipe Crispim da Rocha Salvagnini, Gilson Junior Soares, Jefersson A. dos Santos, Alexandre X. Falcão  

**一句话要点**：提出FLIM-BoFP以加速显著目标检测，应用于光学显微镜寄生虫检测。

**关键词**：显著目标检测, 特征学习, 无反向传播训练, 光学显微镜图像, 寄生虫检测, 滤波器估计

## 3 点简述
- 卷积网络依赖大量图像标注，成本高且耗时。
- FLIM-BoFP通过单次聚类生成特征点袋，直接定义所有块滤波器，无需反向传播。
- 相比FLIM-Cluster，FLIM-BoFP在效率、效果和泛化性上表现更优。

## 摘要（原文）

> Convolutional networks require extensive image annotation, which can be costly and time-consuming. Feature Learning from Image Markers (FLIM) tackles this challenge by estimating encoder filters (i.e., kernel weights) from user-drawn markers on discriminative regions of a few representative images without traditional optimization. Such an encoder combined with an adaptive decoder comprises a FLIM network fully trained without backpropagation. Prior research has demonstrated their effectiveness in Salient Object Detection (SOD), being significantly lighter than existing lightweight models. This study revisits FLIM SOD and introduces FLIM-Bag of Feature Points (FLIM-BoFP), a considerably faster filter estimation method. The previous approach, FLIM-Cluster, derives filters through patch clustering at each encoder's block, leading to computational overhead and reduced control over filter locations. FLIM-BoFP streamlines this process by performing a single clustering at the input block, creating a bag of feature points, and defining filters directly from mapped feature points across all blocks. The paper evaluates the benefits in efficiency, effectiveness, and generalization of FLIM-BoFP compared to FLIM-Cluster and other state-of-the-art baselines for parasite detection in optical microscopy images.

