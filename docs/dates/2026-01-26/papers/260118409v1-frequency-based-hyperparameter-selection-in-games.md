---
layout: default
title: Frequency-Based Hyperparameter Selection in Games
---

# Frequency-Based Hyperparameter Selection in Games
**arXiv**：[2601.18409v1](https://arxiv.org/abs/2601.18409) · [PDF](https://arxiv.org/pdf/2601.18409.pdf)  
**作者**：Aniket Sanyal, Baraah A. M. Sidahmed, Rebekka Burkholz, Tatjana Chavdarova  

**一句话要点**：提出模态前瞻算法以自适应选择游戏学习中的超参数

**关键词**：游戏学习, 超参数选择, 频率分析, 模态前瞻算法, 旋转动力学

## 3 点简述
- 游戏学习因旋转动力学使经典超参数调优失效，问题未充分探索
- 基于频率估计分析振荡动态，扩展前瞻算法为模态前瞻以自适应调参
- 实验表明模态前瞻加速训练，在旋转和混合游戏中有效且计算开销小

## 摘要（原文）

> Learning in smooth games fundamentally differs from standard minimization due to rotational dynamics, which invalidate classical hyperparameter tuning strategies. Despite their practical importance, effective methods for tuning in games remain underexplored. A notable example is LookAhead (LA), which achieves strong empirical performance but introduces additional parameters that critically influence performance. We propose a principled approach to hyperparameter selection in games by leveraging frequency estimation of oscillatory dynamics. Specifically, we analyze oscillations both in continuous-time trajectories and through the spectrum of the discrete dynamics in the associated frequency-based space. Building on this analysis, we introduce \emph{Modal LookAhead (MoLA)}, an extension of LA that selects the hyperparameters adaptively to a given problem. We provide convergence guarantees and demonstrate in experiments that MoLA accelerates training in both purely rotational games and mixed regimes, all with minimal computational overhead.

