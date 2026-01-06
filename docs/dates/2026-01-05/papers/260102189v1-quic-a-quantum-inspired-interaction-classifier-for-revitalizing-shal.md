---
layout: default
title: QuIC: A Quantum-Inspired Interaction Classifier for Revitalizing Shallow CNNs in Fine-Grained Recognition
---

# QuIC: A Quantum-Inspired Interaction Classifier for Revitalizing Shallow CNNs in Fine-Grained Recognition
**arXiv**：[2601.02189v1](https://arxiv.org/abs/2601.02189) · [PDF](https://arxiv.org/pdf/2601.02189.pdf)  
**作者**：Cheng Ying Wu, Yen Jui Chang  

**一句话要点**：提出量子启发的交互分类器QuIC，以增强浅层CNN在细粒度识别中的性能

**关键词**：细粒度视觉分类, 浅层卷积神经网络, 量子启发模型, 特征交互, 轻量级模块, 端到端训练

## 3 点简述
- 核心问题：浅层CNN在细粒度视觉分类中因全局平均池化忽略高阶特征交互而性能不足
- 方法要点：QuIC模拟量子态交互，通过可学习观测算子捕获二阶特征协方差，作为轻量级即插即用模块
- 实验或效果：QuIC显著提升VGG16准确率近20%，在ResNet18上优于SE-Block，并通过可视化验证其增强类内聚类

## 摘要（原文）

> Deploying deep learning models for Fine-Grained Visual Classification (FGVC) on resource-constrained edge devices remains a significant challenge. While deep architectures achieve high accuracy on benchmarks like CUB-200-2011, their computational cost is often prohibitive. Conversely, shallow networks (e.g., AlexNet, VGG) offer efficiency but fail to distinguish visually similar sub-categories. This is because standard Global Average Pooling (GAP) heads capture only first-order statistics, missing the subtle high-order feature interactions required for FGVC. While Bilinear CNNs address this, they suffer from high feature dimensionality and instability during training. To bridge this gap, we propose the Quantum-inspired Interaction Classifier (QuIC). Drawing inspiration from quantum mechanics, QuIC models feature channels as interacting quantum states and captures second-order feature covariance via a learnable observable operator. Designed as a lightweight, plug-and-play module, QuIC supports stable, single-stage end-to-end training without exploding feature dimensions. Experimental results demonstrate that QuIC significantly revitalizes shallow backbones: it boosts the Top-1 accuracy of VGG16 by nearly 20% and outperforms state-of-the-art attention mechanisms (SE-Block) on ResNet18. Qualitative analysis, including t-SNE visualization, further confirms that QuIC resolves ambiguous cases by explicitly attending to fine-grained discriminative features and enforcing compact intra-class clustering.

