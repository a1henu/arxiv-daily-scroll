---
layout: default
title: Grasynda: Graph-based Synthetic Time Series Generation
---

# Grasynda: Graph-based Synthetic Time Series Generation
**arXiv**：[2601.19668v1](https://arxiv.org/abs/2601.19668) · [PDF](https://arxiv.org/pdf/2601.19668.pdf)  
**作者**：Luis Amorim, Moises Santos, Paulo J. Azevedo, Carlos Soares, Vitor Cerqueira  

**一句话要点**：提出基于图的合成时间序列生成方法Grasynda以增强时间序列预测的数据扩充效果

**关键词**：时间序列生成, 图表示学习, 数据扩充, 时间序列预测, 深度学习

## 3 点简述
- 核心问题：现有时间序列数据扩充方法在保持数据属性方面存在不足，影响深度学习模型的泛化能力。
- 方法要点：将单变量时间序列转换为网络结构，节点表示状态，有向边表示转移，并通过转移概率矩阵编码时间动态。
- 实验或效果：在六个基准数据集上使用三种神经网络变体评估，Grasynda一致优于其他方法，包括最先进的时间序列基础模型所用方法。

## 摘要（原文）

> Data augmentation is a crucial tool in time series forecasting, especially for deep learning architectures that require a large training sample size to generalize effectively. However, extensive datasets are not always available in real-world scenarios. Although many data augmentation methods exist, their limitations include the use of transformations that do not adequately preserve data properties. This paper introduces Grasynda, a novel graph-based approach for synthetic time series generation that: (1) converts univariate time series into a network structure using a graph representation, where each state is a node and each transition is represented as a directed edge; and (2) encodes their temporal dynamics in a transition probability matrix. We performed an extensive evaluation of Grasynda as a data augmentation method for time series forecasting. We use three neural network variations on six benchmark datasets. The results indicate that Grasynda consistently outperforms other time series data augmentation methods, including ones used in state-of-the-art time series foundation models. The method and all experiments are publicly available.

