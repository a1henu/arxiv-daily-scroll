---
layout: default
title: Counterfactual Training: Teaching Models Plausible and Actionable Explanations
---

# Counterfactual Training: Teaching Models Plausible and Actionable Explanations
**arXiv**：[2601.16205v1](https://arxiv.org/abs/2601.16205) · [PDF](https://arxiv.org/pdf/2601.16205.pdf)  
**作者**：Patrick Altmeyer, Aleksander Buszydlik, Arie van Deursen, Cynthia C. S. Liem  

**一句话要点**：提出反事实训练方法，通过训练阶段整合反事实解释，提升模型解释能力与对抗鲁棒性。

**关键词**：反事实解释, 模型训练, 可解释人工智能, 对抗鲁棒性, 机器学习

## 3 点简述
- 核心问题：现有反事实解释多为后处理方法，难以确保解释的合理性和可操作性。
- 方法要点：在训练阶段直接优化模型，使其学习生成合理且可操作的反事实解释。
- 实验或效果：实证与理论分析表明，该方法能提升模型解释质量和对抗鲁棒性。

## 摘要（原文）

> We propose a novel training regime termed counterfactual training that leverages counterfactual explanations to increase the explanatory capacity of models. Counterfactual explanations have emerged as a popular post-hoc explanation method for opaque machine learning models: they inform how factual inputs would need to change in order for a model to produce some desired output. To be useful in real-world decision-making systems, counterfactuals should be plausible with respect to the underlying data and actionable with respect to the feature mutability constraints. Much existing research has therefore focused on developing post-hoc methods to generate counterfactuals that meet these desiderata. In this work, we instead hold models directly accountable for the desired end goal: counterfactual training employs counterfactuals during the training phase to minimize the divergence between learned representations and plausible, actionable explanations. We demonstrate empirically and theoretically that our proposed method facilitates training models that deliver inherently desirable counterfactual explanations and additionally exhibit improved adversarial robustness.

