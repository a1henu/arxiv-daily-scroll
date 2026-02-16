---
layout: default
title: Uncertainty in Federated Granger Causality: From Origins to Systemic Consequences
---

# Uncertainty in Federated Granger Causality: From Origins to Systemic Consequences
**arXiv**：[2602.13004v1](https://arxiv.org/abs/2602.13004) · [PDF](https://arxiv.org/pdf/2602.13004.pdf)  
**作者**：Ayush Mohanty, Nazal Mohamed, Nagi Gebraeel  

**一句话要点**：提出联邦格兰杰因果不确定性量化方法，提升分布式因果推断的可靠性与可解释性。

**关键词**：联邦学习, 格兰杰因果, 不确定性量化, 分布式系统, 因果推断, 收敛分析

## 3 点简述
- 核心问题：联邦格兰杰因果算法仅提供确定性点估计，忽略不确定性，影响可靠性。
- 方法要点：系统分类不确定性来源，推导闭式递归建模不确定性传播，定义收敛条件。
- 实验或效果：在合成和真实工业数据集上验证，不确定性表征显著改善因果推断性能。

## 摘要（原文）

> Granger Causality (GC) provides a rigorous framework for learning causal structures from time-series data. Recent federated variants of GC have targeted distributed infrastructure applications (e.g., smart grids) with distributed clients that generate high-dimensional data bound by data-sovereignty constraints. However, Federated GC algorithms only yield deterministic point estimates of causality and neglect uncertainty. This paper establishes the first methodology for rigorously quantifying uncertainty and its propagation within federated GC frameworks. We systematically classify sources of uncertainty, explicitly differentiating aleatoric (data noise) from epistemic (model variability) effects. We derive closed-form recursions that model the evolution of uncertainty through client-server interactions and identify four novel cross-covariance components that couple data uncertainties with model parameter uncertainties across the federated architecture. We also define rigorous convergence conditions for these uncertainty recursions and obtain explicit steady-state variances for both server and client model parameters. Our convergence analysis demonstrates that steady-state variances depend exclusively on client data statistics, thus eliminating dependence on initial epistemic priors and enhancing robustness. Empirical evaluations on synthetic benchmarks and real-world industrial datasets demonstrate that explicitly characterizing uncertainty significantly improves the reliability and interpretability of federated causal inference.

