---
layout: default
title: Recurrent Graph Neural Networks and Arithmetic Circuits
---

# Recurrent Graph Neural Networks and Arithmetic Circuits
**arXiv**：[2603.05140v1](https://arxiv.org/abs/2603.05140) · [PDF](https://arxiv.org/pdf/2603.05140.pdf)  
**作者**：Timon Barlag, Vivian Holzapfel, Laura Strieker, Jonni Virtema, Heribert Vollmer  

**一句话要点**：建立循环图神经网络与实数算术电路之间的表达能力等价性

**关键词**：循环图神经网络, 算术电路, 计算能力表征, 实数运算, 图神经网络表达能力

## 3 点简述
- 核心问题：表征循环图神经网络的计算能力，不限于特定类型如聚合-组合GNN
- 方法要点：引入循环算术电路模型，作为算术类比，使用记忆门存储迭代间数据
- 实验或效果：通过双向构造证明循环GNN与循环算术电路在实数上的精确对应

## 摘要（原文）

> We characterise the computational power of recurrent graph neural networks (GNNs) in terms of arithmetic circuits over the real numbers. Our networks are not restricted to aggregate-combine GNNs or other particular types. Generalizing similar notions from the literature, we introduce the model of recurrent arithmetic circuits, which can be seen as arithmetic analogues of sequential or logical circuits. These circuits utilise so-called memory gates which are used to store data between iterations of the recurrent circuit. While (recurrent) GNNs work on labelled graphs, we construct arithmetic circuits that obtain encoded labelled graphs as real valued tuples and then compute the same function. For the other direction we construct recurrent GNNs which are able to simulate the computations of recurrent circuits. These GNNs are given the circuit-input as initial feature vectors and then, after the GNN-computation, have the circuit-output among the feature vectors of its nodes. In this way we establish an exact correspondence between the expressivity of recurrent GNNs and recurrent arithmetic circuits operating over real numbers.

