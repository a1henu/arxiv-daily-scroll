---
layout: default
title: Gradient Flow Polarizes Softmax Outputs towards Low-Entropy Solutions
---

# Gradient Flow Polarizes Softmax Outputs towards Low-Entropy Solutions
**arXiv**：[2603.06248v1](https://arxiv.org/abs/2603.06248) · [PDF](https://arxiv.org/pdf/2603.06248.pdf)  
**作者**：Aditya Varre, Mark Rofin, Nicolas Flammarion  

**一句话要点**：分析梯度流驱动softmax输出向低熵解极化，以解释Transformer训练动态

**关键词**：梯度流分析, softmax极化, Transformer训练动态, 低熵解, 注意力机制, 非凸优化

## 3 点简述
- 研究softmax模型在非凸训练中的梯度流动态，聚焦值-softmax结构
- 揭示梯度流固有地推动优化向低熵输出解，适用于多种损失函数
- 理论结果解释注意力汇和大激活等经验现象，提供形式化机制

## 摘要（原文）

> Understanding the intricate non-convex training dynamics of softmax-based models is crucial for explaining the empirical success of transformers. In this article, we analyze the gradient flow dynamics of the value-softmax model, defined as ${L}(\mathbf{V} σ(\mathbf{a}))$, where $\mathbf{V}$ and $\mathbf{a}$ are a learnable value matrix and attention vector, respectively. As the matrix times softmax vector parameterization constitutes the core building block of self-attention, our analysis provides direct insight into transformer's training dynamics. We reveal that gradient flow on this structure inherently drives the optimization toward solutions characterized by low-entropy outputs. We demonstrate the universality of this polarizing effect across various objectives, including logistic and square loss. Furthermore, we discuss the practical implications of these theoretical results, offering a formal mechanism for empirical phenomena such as attention sinks and massive activations.

