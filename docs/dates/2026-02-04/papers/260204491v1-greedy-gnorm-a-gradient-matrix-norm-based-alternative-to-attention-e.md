---
layout: default
title: Greedy-Gnorm: A Gradient Matrix Norm-Based Alternative to Attention Entropy for Head Pruning
---

# Greedy-Gnorm: A Gradient Matrix Norm-Based Alternative to Attention Entropy for Head Pruning
**arXiv**：[2602.04491v1](https://arxiv.org/abs/2602.04491) · [PDF](https://arxiv.org/pdf/2602.04491.pdf)  
**作者**：Yuxi Guo, Paul Sheridan  

**一句话要点**：提出Greedy-Gnorm算法，通过动态梯度范数评分改进Transformer注意力头剪枝，以提升模型压缩效果。

**关键词**：注意力头剪枝, Transformer模型压缩, 动态重要性评分, 梯度范数, 绿色AI, 模型部署优化

## 3 点简述
- 核心问题：现有注意力头剪枝方法依赖静态重要性评分，无法捕捉迭代移除过程中头的动态变化。
- 方法要点：基于验证集估计Q/K/V梯度块的l2范数元素积，在贪婪剪枝步骤中动态更新头重要性评分。
- 实验或效果：在BERT等模型上验证，Greedy-Gnorm在大量头移除下保持准确性，优于注意力熵方法。

## 摘要（原文）

> Attention head pruning has emerged as an effective technique for transformer model compression, an increasingly important goal in the era of Green AI. However, existing pruning methods often rely on static importance scores, which fail to capture the evolving role of attention heads during iterative removal. We propose Greedy-Gradient norm (Greedy-Gnorm), a novel head pruning algorithm that dynamically recalculates head importance after each pruning step. Specifically, each head is scored by the elementwise product of the l2-norms of its Q/K/V gradient blocks, as estimated from a hold-out validation set and updated at every greedy iteration. This dynamic approach to scoring mitigates against stale rankings and better reflects gradient-informed importance as pruning progresses. Extensive experiments on BERT, ALBERT, RoBERTa, and XLM-RoBERTa demonstrate that Greedy-Gnorm consistently preserves accuracy under substantial head removal, outperforming attention entropy. By effectively reducing model size while maintaining task performance, Greedy-Gnorm offers a promising step toward more energy-efficient transformer model deployment.

