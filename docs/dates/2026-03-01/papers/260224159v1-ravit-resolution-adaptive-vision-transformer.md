---
layout: default
title: RAViT: Resolution-Adaptive Vision Transformer
---

# RAViT: Resolution-Adaptive Vision Transformer
**arXiv**：[2602.24159v1](https://arxiv.org/abs/2602.24159) · [PDF](https://arxiv.org/pdf/2602.24159.pdf)  
**作者**：Martial Guidez, Stefan Duffner, Christophe Garcia  

**一句话要点**：提出RAViT多分支框架，通过分辨率自适应和早期退出机制降低视觉Transformer的计算成本。

**关键词**：视觉Transformer, 多分支网络, 分辨率自适应, 早期退出机制, 图像分类, 计算效率

## 3 点简述
- 核心问题：视觉Transformer计算成本高，相比卷积神经网络效率较低。
- 方法要点：采用多分支网络处理不同分辨率图像副本，结合早期退出机制实现运行时精度与计算量的权衡。
- 实验或效果：在CIFAR-10、Tiny ImageNet和ImageNet上，以约70%FLOPs达到传统视觉Transformer的同等精度。

## 摘要（原文）

> Vision transformers have recently made a breakthrough in computer vision showing excellent performance in terms of precision for numerous applications. However, their computational cost is very high compared to alternative approaches such as Convolutional Neural Networks. To address this problem, we propose a novel framework for image classification called RAViT based on a multi-branch network that operates on several copies of the same image with different resolutions to reduce the computational cost while preserving the overall accuracy. Furthermore, our framework includes an early exit mechanism that makes our model adaptive and allows to choose the appropriate trade-off between accuracy and computational cost at run-time. For example in a two-branch architecture, the original image is first resized to reduce its resolution, then a prediction is performed on it using a first transformer and the resulting prediction is reused together with the original-size image to perform a final prediction on a second transformer with less computation than a classical Vision transformer architecture. The early-exit process allows the model to make a final prediction at intermediate branches, saving even more computation. We evaluated our approach on CIFAR-10, Tiny ImageNet, and ImageNet. We obtained an equivalent accuracy to the classical Vision transformer model with only around 70% of FLOPs.

