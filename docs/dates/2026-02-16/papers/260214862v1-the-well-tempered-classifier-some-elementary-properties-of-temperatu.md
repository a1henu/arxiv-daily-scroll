---
layout: default
title: The Well-Tempered Classifier: Some Elementary Properties of Temperature Scaling
---

# The Well-Tempered Classifier: Some Elementary Properties of Temperature Scaling
**arXiv**：[2602.14862v1](https://arxiv.org/abs/2602.14862) · [PDF](https://arxiv.org/pdf/2602.14862.pdf)  
**作者**：Pierre-Alexandre Mattei, Bruno Loureiro  

**一句话要点**：分析温度缩放的理论性质，澄清其在分类与语言模型中的不同影响

**关键词**：温度缩放, 分类校准, 语言模型, 不确定性, 信息投影, 线性缩放

## 3 点简述
- 核心问题：温度缩放缺乏严格理论分析，尤其在分类校准和语言模型多样性中的作用
- 方法要点：通过几何和信息投影证明温度缩放是唯一不改变硬预测的线性缩放方法
- 实验或效果：显示温度增加提升分类不确定性，但挑战了其在语言模型中增加多样性的常见说法

## 摘要（原文）

> Temperature scaling is a simple method that allows to control the uncertainty of probabilistic models. It is mostly used in two contexts: improving the calibration of classifiers and tuning the stochasticity of large language models (LLMs). In both cases, temperature scaling is the most popular method for the job. Despite its popularity, a rigorous theoretical analysis of the properties of temperature scaling has remained elusive. We investigate here some of these properties. For classification, we show that increasing the temperature increases the uncertainty in the model in a very general sense (and in particular increases its entropy). However, for LLMs, we challenge the common claim that increasing temperature increases diversity. Furthermore, we introduce two new characterisations of temperature scaling. The first one is geometric: the tempered model is shown to be the information projection of the original model onto the set of models with a given entropy. The second characterisation clarifies the role of temperature scaling as a submodel of more general linear scalers such as matrix scaling and Dirichlet calibration: we show that temperature scaling is the only linear scaler that does not change the hard predictions of the model.

