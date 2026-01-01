---
layout: default
title: Fairness-Aware Insurance Pricing: A Multi-Objective Optimization Approach
---

# Fairness-Aware Insurance Pricing: A Multi-Objective Optimization Approach
**arXiv**：[2512.24747v1](https://arxiv.org/abs/2512.24747) · [PDF](https://arxiv.org/pdf/2512.24747.pdf)  
**作者**：Tim J. Boonen, Xinyue Fan, Zixiao Quan  

**一句话要点**：提出多目标优化框架以解决保险定价中公平性与准确性的权衡问题

**关键词**：保险定价, 公平性优化, 多目标优化, NSGA-II算法, 机器学习公平性

## 3 点简述
- 核心问题：机器学习提升保险定价准确性，但加剧了不同公平标准间的冲突，难以平衡盈利与公平
- 方法要点：使用NSGA-II算法联合优化准确性、群体公平、个体公平和反事实公平，生成帕累托前沿
- 实验或效果：XGBoost准确性高但公平性差，正交模型和合成控制模型在特定公平性上表现优，本方法实现更均衡的妥协

## 摘要（原文）

> Machine learning improves predictive accuracy in insurance pricing but exacerbates trade-offs between competing fairness criteria across different discrimination measures, challenging regulators and insurers to reconcile profitability with equitable outcomes. While existing fairness-aware models offer partial solutions under GLM and XGBoost estimation methods, they remain constrained by single-objective optimization, failing to holistically navigate a conflicting landscape of accuracy, group fairness, individual fairness, and counterfactual fairness. To address this, we propose a novel multi-objective optimization framework that jointly optimizes all four criteria via the Non-dominated Sorting Genetic Algorithm II (NSGA-II), generating a diverse Pareto front of trade-off solutions. We use a specific selection mechanism to extract a premium on this front. Our results show that XGBoost outperforms GLM in accuracy but amplifies fairness disparities; the Orthogonal model excels in group fairness, while Synthetic Control leads in individual and counterfactual fairness. Our method consistently achieves a balanced compromise, outperforming single-model approaches.

