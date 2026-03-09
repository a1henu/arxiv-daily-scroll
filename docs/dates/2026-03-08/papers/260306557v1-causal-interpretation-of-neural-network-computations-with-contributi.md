---
layout: default
title: Causal Interpretation of Neural Network Computations with Contribution Decomposition
---

# Causal Interpretation of Neural Network Computations with Contribution Decomposition
**arXiv**：[2603.06557v1](https://arxiv.org/abs/2603.06557) · [PDF](https://arxiv.org/pdf/2603.06557.pdf)  
**作者**：Joshua Brendan Melander, Zaki Alaoui, Shenghua Liu, Surya Ganguli, Stephen A. Baccus  

**一句话要点**：提出CODEC方法以分解神经网络隐藏神经元贡献，揭示因果过程并增强可解释性。

**关键词**：神经网络可解释性, 贡献分解, 稀疏自编码器, 因果分析, 图像分类, 视网膜模型

## 3 点简述
- 核心问题：现有方法依赖激活模式分析，难以直接理解隐藏神经元如何驱动网络输出。
- 方法要点：使用稀疏自编码器分解网络行为为稀疏贡献模式，揭示因果计算过程。
- 实验或效果：应用于图像分类和视网膜模型，发现贡献稀疏性增加、正负效应解耦，并支持因果操控和可视化。

## 摘要（原文）

> Understanding how neural networks transform inputs into outputs is crucial for interpreting and manipulating their behavior. Most existing approaches analyze internal representations by identifying hidden-layer activation patterns correlated with human-interpretable concepts. Here we take a direct approach to examine how hidden neurons act to drive network outputs. We introduce CODEC (Contribution Decomposition), a method that uses sparse autoencoders to decompose network behavior into sparse motifs of hidden-neuron contributions, revealing causal processes that cannot be determined by analyzing activations alone. Applying CODEC to benchmark image-classification networks, we find that contributions grow in sparsity and dimensionality across layers and, unexpectedly, that they progressively decorrelate positive and negative effects on network outputs. We further show that decomposing contributions into sparse modes enables greater control and interpretation of intermediate layers, supporting both causal manipulations of network output and human-interpretable visualizations of distinct image components that combine to drive that output. Finally, by analyzing state-of-the-art models of neural activity in the vertebrate retina, we demonstrate that CODEC uncovers combinatorial actions of model interneurons and identifies the sources of dynamic receptive fields. Overall, CODEC provides a rich and interpretable framework for understanding how nonlinear computations evolve across hierarchical layers, establishing contribution modes as an informative unit of analysis for mechanistic insights into artificial neural networks.

