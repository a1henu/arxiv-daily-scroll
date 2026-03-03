---
layout: default
title: Co-optimization for Adaptive Conformal Prediction
---

# Co-optimization for Adaptive Conformal Prediction
**arXiv**：[2603.01719v1](https://arxiv.org/abs/2603.01719) · [PDF](https://arxiv.org/pdf/2603.01719.pdf)  
**作者**：Xiaoyi Su, Zhixin Zhou, Rui Luo  

**一句话要点**：提出CoCP框架，通过联合优化中心和半径以提升异方差和偏态下的共形预测效率

**关键词**：共形预测, 区间优化, 异方差处理, 条件覆盖, 机器学习理论

## 3 点简述
- 标准共形预测在异方差和偏态下效率低，区间可能偏离高密度区域
- CoCP交替学习半径和中心，使用软覆盖目标校正中心，无需估计全条件密度
- 实验显示CoCP产生更短区间，在条件覆盖诊断上达到先进水平

## 摘要（原文）

> Conformal prediction (CP) provides finite-sample, distribution-free marginal coverage, but standard conformal regression intervals can be inefficient under heteroscedasticity and skewness. In particular, popular constructions such as conformalized quantile regression (CQR) often inherit a fixed notion of center and enforce equal-tailed errors, which can displace the interval away from high-density regions and produce unnecessarily wide sets. We propose Co-optimization for Adaptive Conformal Prediction (CoCP), a framework that learns prediction intervals by jointly optimizing a center $m(x)$ and a radius $h(x)$.CoCP alternates between (i) learning $h(x)$ via quantile regression on the folded absolute residual around the current center, and (ii) refining $m(x)$ with a differentiable soft-coverage objective whose gradients concentrate near the current boundaries, effectively correcting mis-centering without estimating the full conditional density. Finite-sample marginal validity is guaranteed by split-conformal calibration with a normalized nonconformity score. Theory characterizes the population fixed point of the soft objective and shows that, under standard regularity conditions, CoCP asymptotically approaches the length-minimizing conditional interval at the target coverage level as the estimation error and smoothing vanish. Experiments on synthetic and real benchmarks demonstrate that CoCP yields consistently shorter intervals and achieves state-of-the-art conditional-coverage diagnostics.

