---
layout: default
title: Batch Normalization-Free Fully Integer Quantized Neural Networks via Progressive Tandem Learning
---

# Batch Normalization-Free Fully Integer Quantized Neural Networks via Progressive Tandem Learning
**arXiv**：[2512.16476v1](https://arxiv.org/abs/2512.16476) · [PDF](https://arxiv.org/pdf/2512.16476.pdf)  
**作者**：Pengfei Sun, Wenyu Jiang, Piew Yoong Chee, Paul Devos, Dick Botteldooren  

**一句话要点**：提出渐进串联学习以构建无需批归一化的全整数量化神经网络，适用于边缘设备部署。

**关键词**：量化神经网络, 批归一化移除, 整数推理, 蒸馏训练, 边缘计算

## 3 点简述
- 核心问题：量化神经网络依赖批归一化层，阻碍纯整数推理部署。
- 方法要点：通过层间蒸馏和渐进补偿，从教师模型训练无批归一化的学生模型。
- 实验或效果：在ImageNet上，AlexNet模型在激进量化下保持竞争性Top-1准确率。

## 摘要（原文）

> Quantised neural networks (QNNs) shrink models and reduce inference energy through low-bit arithmetic, yet most still depend on a running statistics batch normalisation (BN) layer, preventing true integer-only deployment. Prior attempts remove BN by parameter folding or tailored initialisation; while helpful, they rarely recover BN's stability and accuracy and often impose bespoke constraints. We present a BN-free, fully integer QNN trained via a progressive, layer-wise distillation scheme that slots into existing low-bit pipelines. Starting from a pretrained BN-enabled teacher, we use layer-wise targets and progressive compensation to train a student that performs inference exclusively with integer arithmetic and contains no BN operations. On ImageNet with AlexNet, the BN-free model attains competitive Top-1 accuracy under aggressive quantisation. The procedure integrates directly with standard quantisation workflows, enabling end-to-end integer-only inference for resource-constrained settings such as edge and embedded devices.

