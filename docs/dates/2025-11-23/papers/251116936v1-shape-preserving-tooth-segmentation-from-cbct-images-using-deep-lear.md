---
layout: default
title: Shape-preserving Tooth Segmentation from CBCT Images Using Deep Learning with Semantic and Shape Awareness
---

# Shape-preserving Tooth Segmentation from CBCT Images Using Deep Learning with Semantic and Shape Awareness
**arXiv**：[2511.16936v1](https://arxiv.org/abs/2511.16936) · [PDF](https://arxiv.org/pdf/2511.16936.pdf)  
**作者**：Zongrui Ji, Zhiming Cui, Na Li, Qianhan Zheng, Miaojing Shi, Ke Deng, Jingyang Zhang, Chaoyuan Li, Xuepeng Chen, Yi Dong, Lei Ma  

**一句话要点**：提出语义与形状感知深度学习框架以解决CBCT图像中牙齿粘连导致的形状失真问题

**关键词**：牙齿分割, CBCT图像, 深度学习, 形状保持, 语义建模, 多任务学习

## 3 点简述
- 核心问题：CBCT图像中牙齿粘连导致解剖形状失真，影响分割准确性
- 方法要点：集成语义关系建模与形态约束，通过多任务学习优化分割与形状保持
- 实验或效果：在内外数据集上显著优于现有方法，有效减少形状失真

## 摘要（原文）

> Background:Accurate tooth segmentation from cone beam computed tomography (CBCT) images is crucial for digital dentistry but remains challenging in cases of interdental adhesions, which cause severe anatomical shape distortion.
>   Methods:
>   To address this, we propose a deep learning framework that integrates semantic and shape awareness for shape-preserving segmentation. Our method introduces a target-tooth-centroid prompted multi-label learning strategy to model semantic relationships between teeth, reducing shape ambiguity. Additionally, a tooth-shape-aware learning mechanism explicitly enforces morphological constraints to preserve boundary integrity. These components are unified via multi-task learning, jointly optimizing segmentation and shape preservation.
>   Results: Extensive evaluations on internal and external datasets demonstrate that our approach significantly outperforms existing methods.
>   Conclusions: Our approach effectively mitigates shape distortions and providing anatomically faithful tooth boundaries.

