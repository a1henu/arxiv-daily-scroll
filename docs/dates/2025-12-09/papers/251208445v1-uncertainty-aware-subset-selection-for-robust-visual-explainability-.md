---
layout: default
title: Uncertainty-Aware Subset Selection for Robust Visual Explainability under Distribution Shifts
---

# Uncertainty-Aware Subset Selection for Robust Visual Explainability under Distribution Shifts
**arXiv**：[2512.08445v1](https://arxiv.org/abs/2512.08445) · [PDF](https://arxiv.org/pdf/2512.08445.pdf)  
**作者**：Madhav Gupta, Vishak Prasad C, Ganesh Ramakrishnan  

**一句话要点**：提出不确定性感知子集选择框架，以提升视觉可解释性在分布偏移下的鲁棒性。

**关键词**：视觉可解释性, 子集选择, 分布偏移, 不确定性估计, 鲁棒性, 梯度方法

## 3 点简述
- 核心问题：现有基于子集选择的可解释方法在分布外场景中可靠性下降，产生冗余、不稳定解释。
- 方法要点：结合子模子集选择与基于梯度的层间不确定性估计，通过自适应权重扰动引导优化。
- 实验或效果：在多个分布内外数据集上验证，框架提升鲁棒性和保真度，且在分布内场景也有改进。

## 摘要（原文）

> Subset selection-based methods are widely used to explain deep vision models: they attribute predictions by highlighting the most influential image regions and support object-level explanations. While these methods perform well in in-distribution (ID) settings, their behavior under out-of-distribution (OOD) conditions remains poorly understood. Through extensive experiments across multiple ID-OOD sets, we find that reliability of the existing subset based methods degrades markedly, yielding redundant, unstable, and uncertainty-sensitive explanations. To address these shortcomings, we introduce a framework that combines submodular subset selection with layer-wise, gradient-based uncertainty estimation to improve robustness and fidelity without requiring additional training or auxiliary models. Our approach estimates uncertainty via adaptive weight perturbations and uses these estimates to guide submodular optimization, ensuring diverse and informative subset selection. Empirical evaluations show that, beyond mitigating the weaknesses of existing methods under OOD scenarios, our framework also yields improvements in ID settings. These findings highlight limitations of current subset-based approaches and demonstrate how uncertainty-driven optimization can enhance attribution and object-level interpretability, paving the way for more transparent and trustworthy AI in real-world vision applications.

