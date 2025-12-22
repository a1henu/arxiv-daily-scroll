---
layout: default
title: Resource-efficient medical image classification for edge devices
---

# Resource-efficient medical image classification for edge devices
**arXiv**：[2512.17515v1](https://arxiv.org/abs/2512.17515) · [PDF](https://arxiv.org/pdf/2512.17515.pdf)  
**作者**：Mahsa Lavaei, Zahra Abadi, Salar Beigzad, Alireza Maleki  

**一句话要点**：提出量化技术以解决边缘设备上医学图像分类的资源效率问题

**关键词**：医学图像分类, 模型量化, 边缘计算, 资源效率, 量化感知训练, 后训练量化

## 3 点简述
- 核心问题：边缘设备资源受限，部署深度学习模型面临计算和内存挑战
- 方法要点：采用模型量化技术，包括量化感知训练和后训练量化，降低模型精度
- 实验或效果：量化模型显著减小模型大小和推理延迟，保持临床可接受的诊断准确性

## 摘要（原文）

> Medical image classification is a critical task in healthcare, enabling accurate and timely diagnosis. However, deploying deep learning models on resource-constrained edge devices presents significant challenges due to computational and memory limitations. This research investigates a resource-efficient approach to medical image classification by employing model quantization techniques. Quantization reduces the precision of model parameters and activations, significantly lowering computational overhead and memory requirements without sacrificing classification accuracy. The study focuses on the optimization of quantization-aware training (QAT) and post-training quantization (PTQ) methods tailored for edge devices, analyzing their impact on model performance across medical imaging datasets. Experimental results demonstrate that quantized models achieve substantial reductions in model size and inference latency, enabling real-time processing on edge hardware while maintaining clinically acceptable diagnostic accuracy. This work provides a practical pathway for deploying AI-driven medical diagnostics in remote and resource-limited settings, enhancing the accessibility and scalability of healthcare technologies.

