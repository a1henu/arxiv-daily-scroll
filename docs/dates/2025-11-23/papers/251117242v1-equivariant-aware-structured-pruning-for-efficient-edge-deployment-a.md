---
layout: default
title: Equivariant-Aware Structured Pruning for Efficient Edge Deployment: A Comprehensive Framework with Adaptive Fine-Tuning
---

# Equivariant-Aware Structured Pruning for Efficient Edge Deployment: A Comprehensive Framework with Adaptive Fine-Tuning
**arXiv**：[2511.17242v1](https://arxiv.org/abs/2511.17242) · [PDF](https://arxiv.org/pdf/2511.17242.pdf)  
**作者**：Mohammed Alnemari  

**一句话要点**：提出等变感知结构化剪枝框架，用于资源受限边缘部署，结合自适应微调。

**关键词**：等变卷积网络, 结构化剪枝, 自适应微调, 模型压缩, 几何变换鲁棒性, 边缘部署

## 3 点简述
- 核心问题：资源受限环境中，保持几何变换不变性的模型压缩需求。
- 方法要点：结合G-CNNs与等变感知结构化剪枝，保留等变属性并减少参数。
- 实验效果：在EuroSAT等数据集上，参数减少29.3%，精度恢复显著。

## 摘要（原文）

> This paper presents a novel framework combining group equivariant convolutional neural networks (G-CNNs) with equivariant-aware structured pruning to produce compact, transformation-invariant models for resource-constrained environments. Equivariance to rotations is achieved through the C4 cyclic group via the e2cnn library,enabling consistent performance under geometric transformations while reducing computational overhead.
>   Our approach introduces structured pruning that preserves equivariant properties by analyzing e2cnn layer structure and applying neuron-level pruning to fully connected components. To mitigate accuracy degradation, we implement adaptive fine-tuning that automatically triggers when accuracy drop exceeds 2%, using early stopping and learning rate scheduling for efficient recovery. The framework includes dynamic INT8 quantization and a comprehensive pipeline encompassing training, knowledge distillation, structured pruning, fine-tuning, and quantization.
>   We evaluate our method on satellite imagery (EuroSAT) and standard benchmarks (CIFAR-10, Rotated MNIST) demonstrating effectiveness across diverse domains. Experimental results show 29.3% parameter reduction with significant accuracy recovery, demonstrating that structured pruning of equivariant networks achieves substantial compression while maintaining geometric robustness. Our pipeline provides a reproducible framework for optimizing equivariant models, bridging the gap between group-theoretic network design and practical deployment constraints, with particular relevance to satellite imagery analysis and geometric vision tasks.

