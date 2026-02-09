---
layout: default
title: Explaining Grokking in Transformers through the Lens of Inductive Bias
---

# Explaining Grokking in Transformers through the Lens of Inductive Bias
**arXiv**：[2602.06702v1](https://arxiv.org/abs/2602.06702) · [PDF](https://arxiv.org/pdf/2602.06702.pdf)  
**作者**：Jaisidh Singh, Diganta Misra, Antonio Orvieto  

**一句话要点**：通过归纳偏置视角解释Transformer中的顿悟现象，揭示架构与优化影响

**关键词**：顿悟现象, 归纳偏置, Transformer架构, 层归一化, 优化策略, 特征压缩性

## 3 点简述
- 研究Transformer中顿悟现象，聚焦归纳偏置如何影响网络偏好解决方案
- 分析层归一化位置等架构选择对顿悟速度的调制作用，关联捷径学习与注意力熵
- 探讨优化设置如学习率和权重衰减对顿悟的复杂影响，挑战先前控制假设

## 摘要（原文）

> We investigate grokking in transformers through the lens of inductive bias: dispositions arising from architecture or optimization that let the network prefer one solution over another. We first show that architectural choices such as the position of Layer Normalization (LN) strongly modulates grokking speed. This modulation is explained by isolating how LN on specific pathways shapes shortcut-learning and attention entropy. Subsequently, we study how different optimization settings modulate grokking, inducing distinct interpretations of previously proposed controls such as readout scale. Particularly, we find that using readout scale as a control for lazy training can be confounded by learning rate and weight decay in our setting. Accordingly, we show that features evolve continuously throughout training, suggesting grokking in transformers can be more nuanced than a lazy-to-rich transition of the learning regime. Finally, we show how generalization predictably emerges with feature compressibility in grokking, across different modulators of inductive bias. Our code is released at https://tinyurl.com/y52u3cad.

