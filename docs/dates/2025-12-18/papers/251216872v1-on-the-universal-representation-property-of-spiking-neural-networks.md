---
layout: default
title: On the Universal Representation Property of Spiking Neural Networks
---

# On the Universal Representation Property of Spiking Neural Networks
**arXiv**：[2512.16872v1](https://arxiv.org/abs/2512.16872) · [PDF](https://arxiv.org/pdf/2512.16872.pdf)  
**作者**：Shayan Hundrieser, Philipp Tuchel, Insung Kong, Johannes Schmidt-Hieber  

**一句话要点**：建立脉冲神经网络的通用表示性质，分析其在序列处理中的定量构造与适用场景。

**关键词**：脉冲神经网络, 通用表示性质, 序列处理, 定量分析, 复合函数, 脉冲序列分类

## 3 点简述
- 核心问题：分析SNN作为脉冲序列处理器的表示能力，探讨其通用表示性质。
- 方法要点：通过定量构造方法，证明SNN在特定脉冲序列函数类中具有近优的权重和神经元需求。
- 实验或效果：揭示SNN适用于输入少、时间复杂度低或复合函数，并应用于脉冲序列分类。

## 摘要（原文）

> Inspired by biology, spiking neural networks (SNNs) process information via discrete spikes over time, offering an energy-efficient alternative to the classical computing paradigm and classical artificial neural networks (ANNs). In this work, we analyze the representational power of SNNs by viewing them as sequence-to-sequence processors of spikes, i.e., systems that transform a stream of input spikes into a stream of output spikes. We establish the universal representation property for a natural class of spike train functions. Our results are fully quantitative, constructive, and near-optimal in the number of required weights and neurons. The analysis reveals that SNNs are particularly well-suited to represent functions with few inputs, low temporal complexity, or compositions of such functions. The latter is of particular interest, as it indicates that deep SNNs can efficiently capture composite functions via a modular design. As an application of our results, we discuss spike train classification. Overall, these results contribute to a rigorous foundation for understanding the capabilities and limitations of spike-based neuromorphic systems.

