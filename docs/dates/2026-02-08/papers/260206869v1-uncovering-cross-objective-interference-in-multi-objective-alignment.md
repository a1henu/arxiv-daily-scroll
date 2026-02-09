---
layout: default
title: Uncovering Cross-Objective Interference in Multi-Objective Alignment
---

# Uncovering Cross-Objective Interference in Multi-Objective Alignment
**arXiv**：[2602.06869v1](https://arxiv.org/abs/2602.06869) · [PDF](https://arxiv.org/pdf/2602.06869.pdf)  
**作者**：Yining Lu, Meng Jiang  

**一句话要点**：提出CTWA方法以缓解大语言模型多目标对齐中的跨目标干扰问题

**关键词**：多目标对齐, 跨目标干扰, 协方差定律, 大语言模型, 标量化优化, 全局收敛

## 3 点简述
- 研究多目标对齐中训练导致部分目标性能下降的跨目标干扰现象
- 基于局部协方差定律分析干扰机制，并提出CTWA方法维持正协方差以缓解干扰
- 通过实验验证CTWA在经典标量化算法中的有效性，并补充全局收敛分析

## 摘要（原文）

> We study a persistent failure mode in multi-objective alignment for large language models (LLMs): training improves performance on only a subset of objectives while causing others to degrade. We formalize this phenomenon as cross-objective interference and conduct the first systematic study across classic scalarization algorithms, showing that interference is pervasive and exhibits strong model dependence.
>   To explain this phenomenon, we derive a local covariance law showing that an objective improves at first order when its reward exhibits positive covariance with the scalarized score. We extend this analysis to clipped surrogate objectives used in modern alignment, demonstrating that the covariance law remains valid under mild conditions despite clipping. Building on this analysis, we propose Covariance Targeted Weight Adaptation (CTWA), a plug-and-play method that maintains positive covariance between objective rewards and the training signal to effectively mitigate cross-objective interference. Finally, we complement these local improvement conditions with a global convergence analysis under the Polyak--Łojasiewicz condition, establishing when non-convex scalarized optimization achieves global convergence and how cross-objective interference depends on specific model geometric properties.

