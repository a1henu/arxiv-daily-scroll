---
layout: default
title: No Validation, No Problem: Predicting Model Performance from a Single Gradient
---

# No Validation, No Problem: Predicting Model Performance from a Single Gradient
**arXiv**：[2601.16874v1](https://arxiv.org/abs/2601.16874) · [PDF](https://arxiv.org/pdf/2601.16874.pdf)  
**作者**：Fangzheng Wu, Brian Summa  

**一句话要点**：提出基于单批次梯度范数的验证无关检查点选择方法，用于预测模型性能

**关键词**：验证无关训练, 梯度范数代理, 检查点选择, 性能预测, 轻量监控

## 3 点简述
- 核心问题：无需验证集时如何高效选择最佳检查点或监控训练进度
- 方法要点：使用分类头梯度的Frobenius范数作为代理指标，通过单次前向-反向传播计算
- 实验或效果：在ImageNet-1k和COCO等任务上，该方法接近oracle性能，并适用于扩散模型

## 摘要（原文）

> We propose a validation-free checkpointing signal from a single forward-backward pass: the Frobenius norm of the classifier-head gradient on one detached-feature batch, \|\|g\|\|_F = \|\|dL/dW\|\|_F. Across ImageNet-1k CNNs and Transformers, this proxy is strongly negative with Top-1 and positive with loss. Selecting the checkpoint with the minimum head gradient in a short tail window closes most of the gap to the oracle (4.24% +/- 2.00% with a universal setup, about 1.12% with light per-family tuning). For practical deployment, a head-scale normalization is more stable within classic CNN families (e.g., ResNets), while a feature-scale normalization works well for Transformers and modern CNNs. The same one-batch probe also predicts COCO detection/segmentation mAP. In diffusion (UNet/DDPM on CIFAR-10), it tracks progress and enables near-oracle tail-window selection; it is positively correlated with same-distribution probe MSE and negatively with FID (lower is better), so it can be used as a lightweight, label-free monitor. Validation labels are never used beyond reporting. The probe adds much less than 0.1% of an epoch and works as a drop-in for validation-free checkpoint selection and early stopping.

