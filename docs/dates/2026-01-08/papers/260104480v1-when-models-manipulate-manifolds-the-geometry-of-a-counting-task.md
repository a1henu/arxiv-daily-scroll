---
layout: default
title: When Models Manipulate Manifolds: The Geometry of a Counting Task
---

# When Models Manipulate Manifolds: The Geometry of a Counting Task
**arXiv**：[2601.04480v1](https://arxiv.org/abs/2601.04480) · [PDF](https://arxiv.org/pdf/2601.04480.pdf)  
**作者**：Wes Gurnee, Emmanuel Ameisen, Isaac Kauvar, Julius Tarng, Adam Pearce, Chris Olah, Joshua Batson  

**一句话要点**：揭示Claude 3.5 Haiku在固定宽度文本换行任务中的几何机制与特征表示

**关键词**：语言模型机制解释, 几何表示学习, 注意力算法, 特征流形, 视觉错觉, 因果干预

## 3 点简述
- 核心问题：语言模型如何仅凭词元序列感知文本视觉属性，如字符计数和换行决策
- 方法要点：通过机制性分析发现字符计数在低维弯曲流形上表示，注意力头扭曲流形估计边界距离
- 实验或效果：通过因果干预验证机制，并发现能劫持计数机制的视觉错觉序列

## 摘要（原文）

> Language models can perceive visual properties of text despite receiving only sequences of tokens-we mechanistically investigate how Claude 3.5 Haiku accomplishes one such task: linebreaking in fixed-width text. We find that character counts are represented on low-dimensional curved manifolds discretized by sparse feature families, analogous to biological place cells. Accurate predictions emerge from a sequence of geometric transformations: token lengths are accumulated into character count manifolds, attention heads twist these manifolds to estimate distance to the line boundary, and the decision to break the line is enabled by arranging estimates orthogonally to create a linear decision boundary. We validate our findings through causal interventions and discover visual illusions--character sequences that hijack the counting mechanism. Our work demonstrates the rich sensory processing of early layers, the intricacy of attention algorithms, and the importance of combining feature-based and geometric views of interpretability.

