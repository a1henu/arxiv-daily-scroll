---
layout: default
title: Transformers learn factored representations
---

# Transformers learn factored representations
**arXiv**：[2602.02385v1](https://arxiv.org/abs/2602.02385) · [PDF](https://arxiv.org/pdf/2602.02385.pdf)  
**作者**：Adam Shai, Loren Amdahl-Culleton, Casper L. Christensen, Henry R. Bigelow, Fernando E. Rosas, Alexander B. Boyd, Eric A. Alt, Kyle J. Ray, Paul M. Riechers  

**一句话要点**：提出Transformer通过因子化表示学习分解世界，揭示维度效率与准确性的权衡。

**关键词**：Transformer表示学习, 因子化表示, 正交子空间, 条件独立性, 维度效率, 合成数据实验

## 3 点简述
- 核心问题：Transformer预训练中表示形式是乘积空间还是正交子空间因子化表示。
- 方法要点：形式化两种表示假设，推导激活几何结构预测，包括子空间数量和维度。
- 实验或效果：在合成过程上测试，模型在条件独立时学习因子化表示，早期训练偏向因子化。

## 摘要（原文）

> Transformers pretrained via next token prediction learn to factor their world into parts, representing these factors in orthogonal subspaces of the residual stream. We formalize two representational hypotheses: (1) a representation in the product space of all factors, whose dimension grows exponentially with the number of parts, or (2) a factored representation in orthogonal subspaces, whose dimension grows linearly. The factored representation is lossless when factors are conditionally independent, but sacrifices predictive fidelity otherwise, creating a tradeoff between dimensional efficiency and accuracy. We derive precise predictions about the geometric structure of activations for each, including the number of subspaces, their dimensionality, and the arrangement of context embeddings within them. We test between these hypotheses on transformers trained on synthetic processes with known latent structure. Models learn factored representations when factors are conditionally independent, and continue to favor them early in training even when noise or hidden dependencies undermine conditional independence, reflecting an inductive bias toward factoring at the cost of fidelity. This provides a principled explanation for why transformers decompose the world into parts, and suggests that interpretable low dimensional structure may persist even in models trained on complex data.

