---
layout: default
title: CPR: Causal Physiological Representation Learning for Robust ECG Analysis under Distribution Shifts
---

# CPR: Causal Physiological Representation Learning for Robust ECG Analysis under Distribution Shifts
**arXiv**：[2512.24564v1](https://arxiv.org/abs/2512.24564) · [PDF](https://arxiv.org/pdf/2512.24564.pdf)  
**作者**：Shunbo Jia, Caizhi Liao  

**一句话要点**：提出因果生理表示学习以提升心电图分析在分布偏移下的鲁棒性

**关键词**：心电图分析, 因果表示学习, 对抗鲁棒性, 分布偏移, 结构因果模型

## 3 点简述
- 核心问题：深度学习心电图诊断模型易受对抗扰动攻击，现有防御方法在鲁棒性与效率间存在权衡。
- 方法要点：通过结构因果模型分离不变病理特征与非因果伪影，引入生理结构先验进行因果解缠。
- 实验或效果：在PTB-XL数据集上，CPR在平滑对抗扰动攻击下F1分数达0.632，优于中值平滑，同时保持单次推理效率。

## 摘要（原文）

> Deep learning models for Electrocardiogram (ECG) diagnosis have achieved remarkable accuracy but exhibit fragility against adversarial perturbations, particularly Smooth Adversarial Perturbations (SAP) that mimic biological morphology. Existing defenses face a critical dilemma: Adversarial Training (AT) provides robustness but incurs a prohibitive computational burden, while certified methods like Randomized Smoothing (RS) introduce significant inference latency, rendering them impractical for real-time clinical monitoring. We posit that this vulnerability stems from the models' reliance on non-robust spurious correlations rather than invariant pathological features. To address this, we propose Causal Physiological Representation Learning (CPR). Unlike standard denoising approaches that operate without semantic constraints, CPR incorporates a Physiological Structural Prior within a causal disentanglement framework. By modeling ECG generation via a Structural Causal Model (SCM), CPR enforces a structural intervention that strictly separates invariant pathological morphology (P-QRS-T complex) from non-causal artifacts. Empirical results on PTB-XL demonstrate that CPR significantly outperforms standard clinical preprocessing methods. Specifically, under SAP attacks, CPR achieves an F1 score of 0.632, surpassing Median Smoothing (0.541 F1) by 9.1%. Crucially, CPR matches the certified robustness of Randomized Smoothing while maintaining single-pass inference efficiency, offering a superior trade-off between robustness, efficiency, and clinical interpretability.

