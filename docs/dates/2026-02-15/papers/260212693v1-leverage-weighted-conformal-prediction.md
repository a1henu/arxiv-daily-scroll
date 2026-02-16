---
layout: default
title: Leverage-Weighted Conformal Prediction
---

# Leverage-Weighted Conformal Prediction
**arXiv**：[2602.12693v1](https://arxiv.org/abs/2602.12693) · [PDF](https://arxiv.org/pdf/2602.12693.pdf)  
**作者**：Shreyas Fadnavis  

**一句话要点**：提出杠杆加权共形预测以解决传统方法区间宽度恒定导致的覆盖不均问题

**关键词**：共形预测, 条件覆盖, 统计杠杆, 分布自由保证, 预测区间, 异方差性

## 3 点简述
- 传统分割共形预测产生恒定宽度区间，在低方差区域过覆盖、高方差区域欠覆盖
- LWCP利用设计矩阵几何的统计杠杆加权非共形分数，无需训练辅助模型
- 理论证明保持有限样本边际有效性，实验显示显著减少条件覆盖差异

## 摘要（原文）

> Split conformal prediction provides distribution-free prediction intervals with finite-sample marginal coverage, but produces constant-width intervals that overcover in low-variance regions and undercover in high-variance regions. Existing adaptive methods require training auxiliary models. We propose Leverage-Weighted Conformal Prediction (LWCP), which weights nonconformity scores by a function of the statistical leverage -- the diagonal of the hat matrix -- deriving adaptivity from the geometry of the design matrix rather than from auxiliary model fitting. We prove that LWCP preserves finite-sample marginal validity for any weight function; achieves asymptotically optimal conditional coverage at essentially no width cost when heteroscedasticity factors through leverage; and recovers the form and width of classical prediction intervals under Gaussian assumptions while retaining distribution-free guarantees. We further establish that randomized leverage approximations preserve coverage exactly with controlled width perturbation, and that vanilla CP suffers a persistent, sample-size-independent conditional coverage gap that LWCP eliminates. The method requires no hyperparameters beyond the choice of weight function and adds negligible computational overhead to vanilla CP. Experiments on synthetic and real data confirm the theoretical predictions, demonstrating substantial reductions in conditional coverage disparity across settings.

