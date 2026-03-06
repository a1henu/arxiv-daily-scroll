---
layout: default
title: The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology
---

# The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology
**arXiv**：[2603.05228v1](https://arxiv.org/abs/2603.05228) · [PDF](https://arxiv.org/pdf/2603.05228.pdf)  
**作者**：Alper Yıldırım  

**一句话要点**：通过修改架构拓扑消除记忆阶段，加速Transformer在循环模加法任务中的泛化

**关键词**：Transformer架构, 延迟泛化, 球形拓扑, 均匀注意力, 循环模加法, 对称性对齐

## 3 点简述
- 研究Transformer在循环模加法任务中延迟泛化（grokking）的机制，关注架构自由度如何延长记忆阶段
- 引入球形拓扑约束和均匀注意力消融，分别消除幅度自由度和数据依赖路由，显著加速泛化
- 在非交换S5排列组合任务中验证加速效果非通用，表明架构先验与任务对称性对齐是关键

## 摘要（原文）

> Mechanistic interpretability typically relies on post-hoc analysis of trained networks. We instead adopt an interventional approach: testing hypotheses a priori by modifying architectural topology to observe training dynamics. We study grokking - delayed generalization in Transformers trained on cyclic modular addition (Zp) - investigating if specific architectural degrees of freedom prolong the memorization phase.
>   We identify two independent structural factors in standard Transformers: unbounded representational magnitude and data-dependent attention routing. First, we introduce a fully bounded spherical topology enforcing L2 normalization throughout the residual stream and an unembedding matrix with a fixed temperature scale. This removes magnitude-based degrees of freedom, reducing grokking onset time by over 20x without weight decay. Second, a Uniform Attention Ablation overrides data-dependent query-key routing with a uniform distribution, reducing the attention layer to a Continuous Bag-of-Words (CBOW) aggregator. Despite removing adaptive routing, these models achieve 100% generalization across all seeds and bypass the grokking delay entirely.
>   To evaluate whether this acceleration is a task-specific geometric alignment rather than a generic optimization stabilizer, we use non-commutative S5 permutation composition as a negative control. Enforcing spherical constraints on S5 does not accelerate generalization. This suggests eliminating the memorization phase depends strongly on aligning architectural priors with the task's intrinsic symmetries. Together, these findings provide interventional evidence that architectural degrees of freedom substantially influence grokking, suggesting a predictive structural perspective on training dynamics.

