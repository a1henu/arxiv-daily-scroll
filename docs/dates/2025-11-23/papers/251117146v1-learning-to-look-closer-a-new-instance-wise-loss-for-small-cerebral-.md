---
layout: default
title: Learning to Look Closer: A New Instance-Wise Loss for Small Cerebral Lesion Segmentation
---

# Learning to Look Closer: A New Instance-Wise Loss for Small Cerebral Lesion Segmentation
**arXiv**：[2511.17146v1](https://arxiv.org/abs/2511.17146) · [PDF](https://arxiv.org/pdf/2511.17146.pdf)  
**作者**：Luc Bouteille, Alexander Jaus, Jens Kleesiek, Rainer Stiefelhagen, Lukas Heine  

**一句话要点**：提出CC-DiceCE损失函数以解决小脑病变分割中的欠分割问题

**关键词**：医学图像分割, 损失函数, 小病变检测, nnU-Net框架, 实例级评估

## 3 点简述
- 传统损失函数如Dice对小病变分割效果差，因其体积小对整体损失贡献低
- CC-DiceCE基于CC-Metrics框架，在nnU-Net中与blob loss和DiceCE基准对比
- 实验显示CC-DiceCE提高检测召回率，分割性能稳定，但假阳性略有增加

## 摘要（原文）

> Traditional loss functions in medical image segmentation, such as Dice, often under-segment small lesions because their small relative volume contributes negligibly to the overall loss. To address this, instance-wise loss functions and metrics have been proposed to evaluate segmentation quality on a per-lesion basis. We introduce CC-DiceCE, a loss function based on the CC-Metrics framework, and compare it with the existing blob loss. Both are benchmarked against a DiceCE baseline within the nnU-Net framework, which provides a robust and standardized setup. We find that CC-DiceCE loss increases detection (recall) with minimal to no degradation in segmentation performance, albeit at the cost of slightly more false positives. Furthermore, our multi-dataset study shows that CC-DiceCE generally outperforms blob loss.

