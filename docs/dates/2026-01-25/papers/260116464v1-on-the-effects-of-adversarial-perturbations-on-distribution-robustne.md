---
layout: default
title: On the Effects of Adversarial Perturbations on Distribution Robustness
---

# On the Effects of Adversarial Perturbations on Distribution Robustness
**arXiv**：[2601.16464v1](https://arxiv.org/abs/2601.16464) · [PDF](https://arxiv.org/pdf/2601.16464.pdf)  
**作者**：Yipei Wang, Zhaoying Pan, Xiaoqian Wang  

**一句话要点**：分析对抗扰动对分布鲁棒性的影响，揭示特征可分性的调节作用

**关键词**：对抗鲁棒性, 分布鲁棒性, 特征可分性, 对抗训练, 理论分析, 数据偏移

## 3 点简述
- 研究对抗鲁棒性与分布鲁棒性之间的权衡，对抗训练可能依赖虚假特征损害分布鲁棒性
- 理论分析表明，适度偏置数据上的ℓ∞扰动可提升分布鲁棒性，特征可分性增强时增益更显著
- 扩展对权衡的理解，强调特征可分性在鲁棒性分析中的关键作用，避免误导性结论

## 摘要（原文）

> Adversarial robustness refers to a model's ability to resist perturbation of inputs, while distribution robustness evaluates the performance of the model under data shifts. Although both aim to ensure reliable performance, prior work has revealed a tradeoff in distribution and adversarial robustness. Specifically, adversarial training might increase reliance on spurious features, which can harm distribution robustness, especially the performance on some underrepresented subgroups. We present a theoretical analysis of adversarial and distribution robustness that provides a tractable surrogate for per-step adversarial training by studying models trained on perturbed data. In addition to the tradeoff, our work further identified a nuanced phenomenon that $\ell_\infty$ perturbations on data with moderate bias can yield an increase in distribution robustness. Moreover, the gain in distribution robustness remains on highly skewed data when simplicity bias induces reliance on the core feature, characterized as greater feature separability. Our theoretical analysis extends the understanding of the tradeoff by highlighting the interplay of the tradeoff and the feature separability. Despite the tradeoff that persists in many cases, overlooking the role of feature separability may lead to misleading conclusions about robustness.

