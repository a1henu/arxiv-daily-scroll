---
layout: default
title: The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology
---

# The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology
**arXiv**：[2603.05228v1](https://arxiv.org/abs/2603.05228) · [PDF](https://arxiv.org/pdf/2603.05228.pdf)  
**作者**：Alper Yıldırım  

**一句话要点**：通过修改架构拓扑加速Transformer在循环模加法任务中的grokking现象

**关键词**：grokking现象, 架构拓扑, Transformer, 循环模加法, 泛化加速, 对称性对齐

## 3 点简述
- 研究grokking现象，即Transformer在循环模加法任务中延迟泛化的问题
- 引入球形拓扑和均匀注意力消融，移除架构自由度以加速泛化
- 实验表明加速依赖于任务对称性与架构先验的对齐，而非通用优化稳定器

## 摘要（原文）

> Mechanistic interpretability typically relies on post-hoc analysis of trained networks. We instead adopt an interventional approach: testing hypotheses a priori by modifying architectural topology to observe training dynamics. We study grokking - delayed generalization in Transformers trained on cyclic modular addition (Zp) - investigating if specific architectural degrees of freedom prolong the memorization phase.
>   We identify two independent structural factors in standard Transformers: unbounded representational magnitude and data-dependent attention routing. First, we introduce a fully bounded spherical topology enforcing L2 normalization throughout the residual stream and an unembedding matrix with a fixed temperature scale. This removes magnitude-based degrees of freedom, reducing grokking onset time by over 20x without weight decay. Second, a Uniform Attention Ablation overrides data-dependent query-key routing with a uniform distribution, reducing the attention layer to a Continuous Bag-of-Words (CBOW) aggregator. Despite removing adaptive routing, these models achieve 100% generalization across all seeds and bypass the grokking delay entirely.
>   To evaluate whether this acceleration is a task-specific geometric alignment rather than a generic optimization stabilizer, we use non-commutative S5 permutation composition as a negative control. Enforcing spherical constraints on S5 does not accelerate generalization. This suggests eliminating the memorization phase depends strongly on aligning architectural priors with the task's intrinsic symmetries. Together, these findings provide interventional evidence that architectural degrees of freedom substantially influence grokking, suggesting a predictive structural perspective on training dynamics.

