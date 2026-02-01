---
layout: default
title: Bulk-Calibrated Credal Ambiguity Sets: Fast, Tractable Decision Making under Out-of-Sample Contamination
---

# Bulk-Calibrated Credal Ambiguity Sets: Fast, Tractable Decision Making under Out-of-Sample Contamination
**arXiv**：[2601.21324v1](https://arxiv.org/abs/2601.21324) · [PDF](https://arxiv.org/pdf/2601.21324.pdf)  
**作者**：Mengqi Chen, Thomas B. Berrett, Theodoros Damoulas, Michele Caprio  

**一句话要点**：提出批量校准信度模糊集，以解决分布鲁棒优化中样本外污染导致的无限风险问题。

**关键词**：分布鲁棒优化, 信度模糊集, 样本外污染, 鲁棒决策, 线性锥规划, 上期望

## 3 点简述
- 核心问题：传统Huber污染模型在模糊集中可能导致最坏情况风险无限，需强假设限制。
- 方法要点：从数据学习高概率批量集，分离处理污染和尾部贡献，实现闭式鲁棒目标。
- 实验或效果：在库存控制、房价回归和文本分类中展示鲁棒性与准确性的平衡及高效优化。

## 摘要（原文）

> Distributionally robust optimisation (DRO) minimises the worst-case expected loss over an ambiguity set that can capture distributional shifts in out-of-sample environments. While Huber (linear-vacuous) contamination is a classical minimal-assumption model for an $\varepsilon$-fraction of arbitrary perturbations, including it in an ambiguity set can make the worst-case risk infinite and the DRO objective vacuous unless one imposes strong boundedness or support assumptions. We address these challenges by introducing bulk-calibrated credal ambiguity sets: we learn a high-mass bulk set from data while considering contamination inside the bulk and bounding the remaining tail contribution separately. This leads to a closed-form, finite $\mathrm{mean}+\sup$ robust objective and tractable linear or second-order cone programs for common losses and bulk geometries. Through this framework, we highlight and exploit the equivalence between the imprecise probability (IP) notion of upper expectation and the worst-case risk, demonstrating how IP credal sets translate into DRO objectives with interpretable tolerance levels. Experiments on heavy-tailed inventory control, geographically shifted house-price regression, and demographically shifted text classification show competitive robustness-accuracy trade-offs and efficient optimisation times, using Bayesian, frequentist, or empirical reference distributions.

