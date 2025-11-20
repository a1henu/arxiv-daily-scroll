---
layout: default
title: MaskMed: Decoupled Mask and Class Prediction for Medical Image Segmentation
---

# MaskMed: Decoupled Mask and Class Prediction for Medical Image Segmentation
**arXiv**：[2511.15603v1](https://arxiv.org/abs/2511.15603) · [PDF](https://arxiv.org/pdf/2511.15603.pdf)  
**作者**：Bin Xie, Gady Agam  

**一句话要点**：提出MaskMed方法，通过解耦掩码与类别预测改进医学图像分割。

**关键词**：医学图像分割, 解耦预测, 变形注意力, 全尺度融合, 对象查询

## 3 点简述
- 医学图像分割中，点式卷积头将输出通道与类别绑定，限制特征共享与语义泛化。
- 采用解耦分割头，分离类无关掩码预测与类别预测，并使用共享对象查询。
- 在AMOS 2022和BTCV数据集上，Dice分数分别超越nnUNet +2.0%和+6.9%。

## 摘要（原文）

> Medical image segmentation typically adopts a point-wise convolutional segmentation head to predict dense labels, where each output channel is heuristically tied to a specific class. This rigid design limits both feature sharing and semantic generalization. In this work, we propose a unified decoupled segmentation head that separates multi-class prediction into class-agnostic mask prediction and class label prediction using shared object queries. Furthermore, we introduce a Full-Scale Aware Deformable Transformer module that enables low-resolution encoder features to attend across full-resolution encoder features via deformable attention, achieving memory-efficient and spatially aligned full-scale fusion. Our proposed method, named MaskMed, achieves state-of-the-art performance, surpassing nnUNet by +2.0% Dice on AMOS 2022 and +6.9% Dice on BTCV.

