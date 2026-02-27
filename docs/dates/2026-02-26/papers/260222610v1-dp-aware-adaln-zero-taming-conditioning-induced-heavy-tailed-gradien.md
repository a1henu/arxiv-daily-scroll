---
layout: default
title: DP-aware AdaLN-Zero: Taming Conditioning-Induced Heavy-Tailed Gradients in Differentially Private Diffusion
---

# DP-aware AdaLN-Zero: Taming Conditioning-Induced Heavy-Tailed Gradients in Differentially Private Diffusion
**arXiv**：[2602.22610v1](https://arxiv.org/abs/2602.22610) · [PDF](https://arxiv.org/pdf/2602.22610.pdf)  
**作者**：Tao Huang, Jiayang Meng, Xu Yang, Chen Hou, Hong Chen  

**一句话要点**：提出DP-aware AdaLN-Zero以解决差分隐私扩散模型中条件注入导致的梯度重尾问题

**关键词**：差分隐私扩散模型, 条件注入, 梯度重尾, AdaLN调制, 时间序列预测, 隐私保护训练

## 3 点简述
- 核心问题：异构条件上下文在差分隐私随机梯度下降中引发重尾梯度，导致全局裁剪偏差和效用下降
- 方法要点：通过有界重参数化联合约束条件表示幅度和AdaLN调制参数，抑制极端梯度尾部事件
- 实验或效果：在真实世界电力数据集和公共ETT基准上，匹配隐私设置下提升插补/插值和预测性能

## 摘要（原文）

> Condition injection enables diffusion models to generate context-aware outputs, which is essential for many time-series tasks. However, heterogeneous conditional contexts (e.g., observed history, missingness patterns or outlier covariates) can induce heavy-tailed per-example gradients. Under Differentially Private Stochastic Gradient Descent (DP-SGD), these rare conditioning-driven heavy-tailed gradients disproportionately trigger global clipping, resulting in outlier-dominated updates, larger clipping bias, and degraded utility under a fixed privacy budget. In this paper, we propose DP-aware AdaLN-Zero, a drop-in sensitivity-aware conditioning mechanism for conditional diffusion transformers that limits conditioning-induced gain without modifying the DP-SGD mechanism. DP-aware AdaLN-Zero jointly constrains conditioning representation magnitude and AdaLN modulation parameters via bounded re-parameterization, suppressing extreme gradient tail events before gradient clipping and noise injection. Empirically, DP-SGD equipped with DP-aware AdaLN-Zero improves interpolation/imputation and forecasting under matched privacy settings. We observe consistent gains on a real-world power dataset and two public ETT benchmarks over vanilla DP-SGD. Moreover, gradient diagnostics attribute these improvements to conditioning-specific tail reshaping and reduced clipping distortion, while preserving expressiveness in non-private training. Overall, these results show that sensitivity-aware conditioning can substantially improve private conditional diffusion training without sacrificing standard performance.

