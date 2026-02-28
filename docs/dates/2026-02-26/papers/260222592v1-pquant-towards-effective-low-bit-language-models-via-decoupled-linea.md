---
layout: default
title: pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training
---

# pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training
**arXiv**：[2602.22592v1](https://arxiv.org/abs/2602.22592) · [PDF](https://arxiv.org/pdf/2602.22592.pdf)  
**作者**：Wenzheng Zhang, Bingzheng Liu, Yang Hu, Xiaoying Bai, Wentao Zhang, Bin Cui  

**一句话要点**：提出pQuant方法，通过解耦线性量化感知训练解决极低比特语言模型的参数民主化问题。

**关键词**：语言模型量化, 量化感知训练, 低比特权重, 参数解耦, 边缘计算

## 3 点简述
- 核心问题：现有方法在极低比特量化中因参数民主化效应导致精度和可扩展性不足。
- 方法要点：将线性层拆分为1比特主导分支和高精度分支，通过特征缩放引导敏感参数分配。
- 实验或效果：在极低比特量化中实现最先进性能，支持高效边缘部署。

## 摘要（原文）

> Quantization-Aware Training from scratch has emerged as a promising approach for building efficient large language models (LLMs) with extremely low-bit weights (sub 2-bit), which can offer substantial advantages for edge deployment. However, existing methods still fail to achieve satisfactory accuracy and scalability. In this work, we identify a parameter democratization effect as a key bottleneck: the sensitivity of all parameters becomes homogenized, severely limiting expressivity. To address this, we propose pQuant, a method that decouples parameters by splitting linear layers into two specialized branches: a dominant 1-bit branch for efficient computation and a compact high-precision branch dedicated to preserving the most sensitive parameters. Through tailored feature scaling, we explicitly guide the model to allocate sensitive parameters to the high-precision branch. Furthermore, we extend this branch into multiple, sparsely-activated experts, enabling efficient capacity scaling. Extensive experiments indicate our pQuant achieves state-of-the-art performance in extremely low-bit quantization.

