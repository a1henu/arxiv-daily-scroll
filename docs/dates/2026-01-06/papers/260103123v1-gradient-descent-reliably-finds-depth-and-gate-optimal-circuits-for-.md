---
layout: default
title: Gradient descent reliably finds depth- and gate-optimal circuits for generic unitaries
---

# Gradient descent reliably finds depth- and gate-optimal circuits for generic unitaries
**arXiv**：[2601.03123v1](https://arxiv.org/abs/2601.03123) · [PDF](https://arxiv.org/pdf/2601.03123.pdf)  
**作者**：Janani Gomathi, Alex Meiburg  

**一句话要点**：提出梯度下降法可靠找到通用酉算子的深度和门最优量子电路

**关键词**：量子电路合成, 梯度下降, 酉算子优化, 深度最优电路, 门最优电路, 通用酉算子

## 3 点简述
- 核心问题：量子电路合成中，高效找到最小电路对通用酉算子仍具挑战性
- 方法要点：避免随机选择参数不足的电路骨架，使用简单梯度下降优化
- 实验或效果：在受限芯片连接下，梯度下降可靠实现深度和门最优电路合成

## 摘要（原文）

> When the gate set has continuous parameters, synthesizing a unitary operator as a quantum circuit is always possible using exact methods, but finding minimal circuits efficiently remains a challenging problem. The landscape is very different for compiled unitaries, which arise from programming and typically have short circuits, as compared with generic unitaries, which use all parameters and typically require circuits of maximal size. We show that simple gradient descent reliably finds depth- and gate-optimal circuits for generic unitaries, including in the presence of restricted chip connectivity. This runs counter to earlier evidence that optimal synthesis required combinatorial search, and we show that this discrepancy can be explained by avoiding the random selection of certain parameter-deficient circuit skeletons.

