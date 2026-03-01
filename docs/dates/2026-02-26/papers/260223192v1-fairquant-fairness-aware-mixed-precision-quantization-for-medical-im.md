---
layout: default
title: FairQuant: Fairness-Aware Mixed-Precision Quantization for Medical Image Classification
---

# FairQuant: Fairness-Aware Mixed-Precision Quantization for Medical Image Classification
**arXiv**：[2602.23192v1](https://arxiv.org/abs/2602.23192) · [PDF](https://arxiv.org/pdf/2602.23192.pdf)  
**作者**：Thomas Woergaard, Raghavendra Selvan  

**一句话要点**：提出FairQuant框架，在医疗图像分类中实现公平感知的混合精度量化。

**关键词**：医疗图像分类, 混合精度量化, 算法公平性, 位感知量化, 模型压缩

## 3 点简述
- 核心问题：现有量化方法未考虑算法公平性，可能影响模型在不同群体间的性能。
- 方法要点：结合群体感知重要性分析、预算混合精度分配和可学习的位感知量化模式，联合优化权重和位分配。
- 实验或效果：在Fitzpatrick17k和ISIC2019数据集上，平均4-6位精度恢复大部分8位精度，同时改善最差群体性能。

## 摘要（原文）

> Compressing neural networks by quantizing model parameters offers useful trade-off between performance and efficiency. Methods like quantization-aware training and post-training quantization strive to maintain the downstream performance of compressed models compared to the full precision models. However, these techniques do not explicitly consider the impact on algorithmic fairness. In this work, we study fairness-aware mixed-precision quantization schemes for medical image classification under explicit bit budgets. We introduce FairQuant, a framework that combines group-aware importance analysis, budgeted mixed-precision allocation, and a learnable Bit-Aware Quantization (BAQ) mode that jointly optimizes weights and per-unit bit allocations under bitrate and fairness regularization. We evaluate the method on Fitzpatrick17k and ISIC2019 across ResNet18/50, DeiT-Tiny, and TinyViT. Results show that FairQuant configurations with average precision near 4-6 bits recover much of the Uniform 8-bit accuracy while improving worst-group performance relative to Uniform 4- and 8-bit baselines, with comparable fairness metrics under shared budgets.

