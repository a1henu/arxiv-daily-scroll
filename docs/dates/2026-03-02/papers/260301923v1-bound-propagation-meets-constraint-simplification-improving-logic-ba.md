---
layout: default
title: Bound Propagation meets Constraint Simplification: Improving Logic-based XAI for Neural Networks
---

# Bound Propagation meets Constraint Simplification: Improving Logic-based XAI for Neural Networks
**arXiv**：[2603.01923v1](https://arxiv.org/abs/2603.01923) · [PDF](https://arxiv.org/pdf/2603.01923.pdf)  
**作者**：Ronaldo Gomes, Jairo Ribeiro, Luiz Queiroz, Thiago Alves Rocha  

**一句话要点**：结合边界传播与约束简化，提升神经网络逻辑解释方法的效率

**关键词**：神经网络解释, 逻辑方法, 边界传播, 约束简化, 计算效率, 可解释人工智能

## 3 点简述
- 核心问题：逻辑解释方法计算成本高，尤其在大规模网络中。
- 方法要点：通过边界传播推导约束简化，收紧神经元边界并消除冗余变量。
- 实验或效果：实验显示解释时间最多减少89.26%，对大型网络效果显著。

## 摘要（原文）

> Logic-based methods for explaining neural network decisions offer formal guarantees of correctness and non-redundancy, but they often suffer from high computational costs, especially for large networks. In this work, we improve the efficiency of such methods by combining bound propagation with constraint simplification. These simplifications, derived from the propagation, tighten neuron bounds and eliminate unnecessary binary variables, making the explanation process more efficient. Our experiments suggest that combining these techniques reduces explanation time by up to 89.26\%, particularly for larger neural networks.

