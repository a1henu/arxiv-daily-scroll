---
layout: default
title: Pseudodata-guided Invariant Representation Learning Boosts the Out-of-Distribution Generalization in Enzymatic Kinetic Parameter Prediction
---

# Pseudodata-guided Invariant Representation Learning Boosts the Out-of-Distribution Generalization in Enzymatic Kinetic Parameter Prediction
**arXiv**：[2601.07261v1](https://arxiv.org/abs/2601.07261) · [PDF](https://arxiv.org/pdf/2601.07261.pdf)  
**作者**：Haomin Wu, Zhiwei Nie, Hongyu Zhang, Zhixiang Ren  

**一句话要点**：提出O²DENet模块以增强酶动力学参数预测的分布外泛化能力

**关键词**：酶动力学预测, 分布外泛化, 不变表示学习, 扰动增强, 酶-底物相互作用

## 3 点简述
- 核心问题：现有深度学习模型在序列差异大的分布外酶-底物相互作用预测中性能下降。
- 方法要点：通过生物化学启发的扰动增强和不变表示学习，提升模型对分布偏移的鲁棒性。
- 实验或效果：在严格序列身份基准上，O²DENet集成后显著改善k_cat和K_m预测，达到最优准确性和鲁棒性。

## 摘要（原文）

> Accurate prediction of enzyme kinetic parameters is essential for understanding catalytic mechanisms and guiding enzyme engineering.However, existing deep learning-based enzyme-substrate interaction (ESI) predictors often exhibit performance degradation on sequence-divergent, out-of-distribution (OOD) cases, limiting robustness under biologically relevant perturbations.We propose O$^2$DENet, a lightweight, plug-and-play module that enhances OOD generalization via biologically and chemically informed perturbation augmentation and invariant representation learning.O$^2$DENet introduces enzyme-substrate perturbations and enforces consistency between original and augmented enzyme-substrate-pair representations to encourage invariance to distributional shifts.When integrated with representative ESI models, O$^2$DENet consistently improves predictive performance for both $k_{cat}$ and $K_m$ across stringent sequence-identity-based OOD benchmarks, achieving state-of-the-art results among the evaluated methods in terms of accuracy and robustness metrics.Overall, O$^2$DENet provides a general and effective strategy to enhance the stability and deployability of data-driven enzyme kinetics predictors for real-world enzyme engineering applications.

