---
layout: default
title: Generalized Bayes for Causal Inference
---

# Generalized Bayes for Causal Inference
**arXiv**：[2603.03035v1](https://arxiv.org/abs/2603.03035) · [PDF](https://arxiv.org/pdf/2603.03035.pdf)  
**作者**：Emil Javurek, Dennis Frauen, Yuxin Wang, Stefan Feuerriegel  

**一句话要点**：提出广义贝叶斯框架以解决因果推断中的不确定性量化挑战

**关键词**：因果推断, 广义贝叶斯, 不确定性量化, 损失函数, Neyman正交性, 机器学习

## 3 点简述
- 核心问题：标准贝叶斯方法需指定数据生成过程模型，易受建模选择影响，难以灵活量化因果效应不确定性。
- 方法要点：避免显式似然建模，直接在因果估计量上设置先验，使用识别驱动的损失函数更新，生成广义后验。
- 实验或效果：框架适用于多种因果估计量，结合先进因果机器学习流程，经验验证提供校准的不确定性估计。

## 摘要（原文）

> Uncertainty quantification is central to many applications of causal machine learning, yet principled Bayesian inference for causal effects remains challenging. Standard Bayesian approaches typically require specifying a probabilistic model for the data-generating process, including high-dimensional nuisance components such as propensity scores and outcome regressions. Standard posteriors are thus vulnerable to strong modeling choices, including complex prior elicitation. In this paper, we propose a generalized Bayesian framework for causal inference. Our framework avoids explicit likelihood modeling; instead, we place priors directly on the causal estimands and update these using an identification-driven loss function, which yields generalized posteriors for causal effects. As a result, our framework turns existing loss-based causal estimators into estimators with full uncertainty quantification. Our framework is flexible and applicable to a broad range of causal estimands (e.g., ATE, CATE). Further, our framework can be applied on top of state-of-the-art causal machine learning pipelines (e.g., Neyman-orthogonal meta-learners). For Neyman-orthogonal losses, we show that the generalized posteriors converge to their oracle counterparts and remain robust to first-stage nuisance estimation error. With calibration, we thus obtain valid frequentist uncertainty even when nuisance estimators converge at slower-than-parametric rates. Empirically, we demonstrate that our proposed framework offers causal effect estimation with calibrated uncertainty across several causal inference settings. To the best of our knowledge, this is the first flexible framework for constructing generalized Bayesian posteriors for causal machine learning.

