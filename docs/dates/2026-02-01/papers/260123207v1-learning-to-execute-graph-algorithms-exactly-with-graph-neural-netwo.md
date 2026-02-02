---
layout: default
title: Learning to Execute Graph Algorithms Exactly with Graph Neural Networks
---

# Learning to Execute Graph Algorithms Exactly with Graph Neural Networks
**arXiv**：[2601.23207v1](https://arxiv.org/abs/2601.23207) · [PDF](https://arxiv.org/pdf/2601.23207.pdf)  
**作者**：Muhammad Fetrat Qharabagh, Artur Back de Luca, George Giapitzakis, Kimon Fountoulakis  

**一句话要点**：提出基于图神经网络精确执行图算法的学习框架，在有限度与精度约束下证明可学习性。

**关键词**：图神经网络, 算法学习, 神经正切核, 分布式计算, 精确执行, 有限度约束

## 3 点简述
- 核心问题：探究图神经网络学习执行算法的能力，解决理论挑战。
- 方法要点：通过训练多层感知机集合学习节点本地指令，结合神经正切核理论确保无误差执行。
- 实验或效果：在LOCAL模型中证明可学习性，并应用于消息泛洪、广度优先搜索等算法。

## 摘要（原文）

> Understanding what graph neural networks can learn, especially their ability to learn to execute algorithms, remains a central theoretical challenge. In this work, we prove exact learnability results for graph algorithms under bounded-degree and finite-precision constraints. Our approach follows a two-step process. First, we train an ensemble of multi-layer perceptrons (MLPs) to execute the local instructions of a single node. Second, during inference, we use the trained MLP ensemble as the update function within a graph neural network (GNN). Leveraging Neural Tangent Kernel (NTK) theory, we show that local instructions can be learned from a small training set, enabling the complete graph algorithm to be executed during inference without error and with high probability. To illustrate the learning power of our setting, we establish a rigorous learnability result for the LOCAL model of distributed computation. We further demonstrate positive learnability results for widely studied algorithms such as message flooding, breadth-first and depth-first search, and Bellman-Ford.

