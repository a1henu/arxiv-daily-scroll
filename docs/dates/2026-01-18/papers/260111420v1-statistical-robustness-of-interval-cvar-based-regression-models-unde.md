---
layout: default
title: Statistical Robustness of Interval CVaR Based Regression Models under Perturbation and Contamination
---

# Statistical Robustness of Interval CVaR Based Regression Models under Perturbation and Contamination
**arXiv**：[2601.11420v1](https://arxiv.org/abs/2601.11420) · [PDF](https://arxiv.org/pdf/2601.11420.pdf)  
**作者**：Yulei You, Junyi Liu  

**一句话要点**：分析基于区间条件风险价值的非线性回归模型在扰动和污染下的统计鲁棒性

**关键词**：鲁棒回归, 区间条件风险价值, 统计学习, 非线性模型, 分布污染, 扰动分析

## 3 点简述
- 研究扰动和污染下统计学习的鲁棒性问题，聚焦区间条件风险价值方法
- 量化污染下的分布崩溃点，分析扰动下的定性鲁棒性，覆盖多种回归模型
- 理论结合数值实验，展示区间条件风险价值在鲁棒回归中的优势

## 摘要（原文）

> Robustness under perturbation and contamination is a prominent issue in statistical learning. We address the robust nonlinear regression based on the so-called interval conditional value-at-risk (In-CVaR), which is introduced to enhance robustness by trimming extreme losses. While recent literature shows that the In-CVaR based statistical learning exhibits superior robustness performance than classical robust regression models, its theoretical robustness analysis for nonlinear regression remains largely unexplored. We rigorously quantify robustness under contamination, with a unified study of distributional breakdown point for a broad class of regression models, including linear, piecewise affine and neural network models with $\ell_1$, $\ell_2$ and Huber losses. Moreover, we analyze the qualitative robustness of the In-CVaR based estimator under perturbation. We show that under several minor assumptions, the In-CVaR based estimator is qualitatively robust in terms of the Prokhorov metric if and only if the largest portion of losses is trimmed. Overall, this study analyzes robustness properties of In-CVaR based nonlinear regression models under both perturbation and contamination, which illustrates the advantages of In-CVaR risk measure over conditional value-at-risk and expectation for robust regression in both theory and numerical experiments.

