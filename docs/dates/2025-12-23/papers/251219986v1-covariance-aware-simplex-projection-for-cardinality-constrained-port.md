---
layout: default
title: Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization
---

# Covariance-Aware Simplex Projection for Cardinality-Constrained Portfolio Optimization
**arXiv**：[2512.19986v1](https://arxiv.org/abs/2512.19986) · [PDF](https://arxiv.org/pdf/2512.19986.pdf)  
**作者**：Nikolaos Iliopoulos  

**一句话要点**：提出协方差感知单纯形投影以改进基数约束投资组合优化中的修复算子。

**关键词**：投资组合优化, 基数约束, 修复算子, 协方差感知, 元启发式算法, 风险控制

## 3 点简述
- 核心问题：标准欧几里得投影忽略资产协方差结构，可能导致投资组合风险较高和分散性不足。
- 方法要点：CASP采用两阶段修复算子，先基于波动率归一化评分选择资产，再用协方差感知几何投影权重。
- 实验或效果：在S&P 500数据上，CASP显著降低投资组合方差，改进具有统计显著性，且可提升夏普比率。

## 摘要（原文）

> Metaheuristic algorithms for cardinality-constrained portfolio optimization require repair operators to map infeasible candidates onto the feasible region. Standard Euclidean projection treats assets as independent and can ignore the covariance structure that governs portfolio risk, potentially producing less diversified portfolios. This paper introduces Covariance-Aware Simplex Projection (CASP), a two-stage repair operator that (i) selects a target number of assets using volatility-normalized scores and (ii) projects the candidate weights using a covariance-aware geometry aligned with tracking-error risk. This provides a portfolio-theoretic foundation for using a covariance-induced distance in repair operators. On S&P 500 data (2020-2024), CASP-Basic delivers materially lower portfolio variance than standard Euclidean repair without relying on return estimates, with improvements that are robust across assets and statistically significant. Ablation results indicate that volatility-normalized selection drives most of the variance reduction, while the covariance-aware projection provides an additional, consistent improvement. We further show that optional return-aware extensions can improve Sharpe ratios, and out-of-sample tests confirm that gains transfer to realized performance. CASP integrates as a drop-in replacement for Euclidean projection in metaheuristic portfolio optimizers.

