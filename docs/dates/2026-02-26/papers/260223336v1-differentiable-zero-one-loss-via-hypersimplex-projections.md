---
layout: default
title: Differentiable Zero-One Loss via Hypersimplex Projections
---

# Differentiable Zero-One Loss via Hypersimplex Projections
**arXiv**：[2602.23336v1](https://arxiv.org/abs/2602.23336) · [PDF](https://arxiv.org/pdf/2602.23336.pdf)  
**作者**：Camilo Gomez, Pengyang Wang, Liansheng Tang  

**一句话要点**：提出Soft-Binary-Argmax算子，通过超单纯形投影实现零一损失的可微近似，以提升大批次训练泛化性能。

**关键词**：可微优化, 零一损失, 超单纯形投影, Soft-Binary-Argmax, 大批次训练, 泛化性能

## 3 点简述
- 核心问题：零一损失作为分类性能黄金标准，因不可微性无法用于基于梯度的优化。
- 方法要点：基于约束优化框架，构建平滑保序的超单纯形投影，实现可微零一损失近似。
- 实验或效果：在大批次训练中，通过几何一致性约束输出logits，显著缩小泛化性能差距。

## 摘要（原文）

> Recent advances in machine learning have emphasized the integration of structured optimization components into end-to-end differentiable models, enabling richer inductive biases and tighter alignment with task-specific objectives. In this work, we introduce a novel differentiable approximation to the zero-one loss-long considered the gold standard for classification performance, yet incompatible with gradient-based optimization due to its non-differentiability. Our method constructs a smooth, order-preserving projection onto the n,k-dimensional hypersimplex through a constrained optimization framework, leading to a new operator we term Soft-Binary-Argmax. After deriving its mathematical properties, we show how its Jacobian can be efficiently computed and integrated into binary and multiclass learning systems. Empirically, our approach achieves significant improvements in generalization under large-batch training by imposing geometric consistency constraints on the output logits, thereby narrowing the performance gap traditionally observed in large-batch training.

