---
layout: default
title: Decomposing Epistemic Uncertainty for Causal Decision Making
---

# Decomposing Epistemic Uncertainty for Causal Decision Making
**arXiv**：[2601.22736v1](https://arxiv.org/abs/2601.22736) · [PDF](https://arxiv.org/pdf/2601.22736.pdf)  
**作者**：Md Musfiqur Rahman, Ziwei Jiang, Hilaf Hasson, Murat Kocaoglu  

**一句话要点**：提出分解因果效应边界不确定性的框架，以指导决策中数据收集策略。

**关键词**：因果推断, 不确定性分解, 神经网络因果模型, 决策指导, 非可识别性

## 3 点简述
- 核心问题：因果效应估计在未观测混杂下存在不确定性，现有方法难以区分非可识别性与有限样本影响。
- 方法要点：通过置信集与因果效应边界交集，分解样本不确定性与非可识别不确定性。
- 实验或效果：在合成与真实数据集上验证，能判断何时收集更多样本无效，指导变量收集或随机化研究。

## 摘要（原文）

> Causal inference from observational data provides strong evidence for the best action in decision-making without performing expensive randomized trials. The effect of an action is usually not identifiable under unobserved confounding, even with an infinite amount of data. Recent work uses neural networks to obtain practical bounds to such causal effects, which is often an intractable problem. However, these approaches may overfit to the dataset and be overconfident in their causal effect estimates. Moreover, there is currently no systematic approach to disentangle how much of the width of causal effect bounds is due to fundamental non-identifiability versus how much is due to finite-sample limitations. We propose a novel framework to address this problem by considering a confidence set around the empirical observational distribution and obtaining the intersection of causal effect bounds for all distributions in this confidence set. This allows us to distinguish the part of the interval that can be reduced by collecting more samples, which we call sample uncertainty, from the part that can only be reduced by observing more variables, such as latent confounders or instrumental variables, but not with more data, which we call non-ID uncertainty. The upper and lower bounds to this intersection are obtained by solving min-max and max-min problems with neural causal models by searching over all distributions that the dataset might have been sampled from, and all SCMs that entail the corresponding distribution. We demonstrate via extensive experiments on synthetic and real-world datasets that our algorithm can determine when collecting more samples will not help determine the best action. This can guide practitioners to collect more variables or lean towards a randomized study for best action identification.

