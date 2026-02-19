---
layout: default
title: Functional Decomposition and Shapley Interactions for Interpreting Survival Models
---

# Functional Decomposition and Shapley Interactions for Interpreting Survival Models
**arXiv**：[2602.16505v1](https://arxiv.org/abs/2602.16505) · [PDF](https://arxiv.org/pdf/2602.16505.pdf)  
**作者**：Sophie Hanna Langbein, Hubert Baniecki, Fabian Fumagalli, Niklas Koenen, Marvin N. Wright, Julia Herbinger  

**一句话要点**：提出SurvFD和SurvSHAP-IQ以解释生存模型中的特征交互作用

**关键词**：生存分析, 特征交互, 可解释性, Shapley值, 时间依赖效应, 机器学习

## 3 点简述
- 核心问题：生存函数非加性限制标准可解释方法，需分析特征交互
- 方法要点：SurvFD分解高阶效应，SurvSHAP-IQ扩展Shapley交互到时间函数
- 实验或效果：提供时间依赖交互估计，增强生存模型可解释性

## 摘要（原文）

> Hazard and survival functions are natural, interpretable targets in time-to-event prediction, but their inherent non-additivity fundamentally limits standard additive explanation methods. We introduce Survival Functional Decomposition (SurvFD), a principled approach for analyzing feature interactions in machine learning survival models. By decomposing higher-order effects into time-dependent and time-independent components, SurvFD offers a previously unrecognized perspective on survival explanations, explicitly characterizing when and why additive explanations fail. Building on this theoretical decomposition, we propose SurvSHAP-IQ, which extends Shapley interactions to time-indexed functions, providing a practical estimator for higher-order, time-dependent interactions. Together, SurvFD and SurvSHAP-IQ establish an interaction- and time-aware interpretability approach for survival modeling, with broad applicability across time-to-event prediction tasks.

