---
layout: default
title: Default Machine Learning Hyperparameters Do Not Provide Informative Initialization for Bayesian Optimization
---

# Default Machine Learning Hyperparameters Do Not Provide Informative Initialization for Bayesian Optimization
**arXiv**：[2602.08774v1](https://arxiv.org/abs/2602.08774) · [PDF](https://arxiv.org/pdf/2602.08774.pdf)  
**作者**：Nicolás Villagrán Prieto, Eduardo C. Garrido-Merchán  

**一句话要点**：验证默认超参数初始化对贝叶斯优化无显著加速效果

**关键词**：贝叶斯优化, 超参数调优, 机器学习库, 初始化策略, 实验评估

## 3 点简述
- 核心问题：默认超参数是否能为贝叶斯优化提供信息性初始化以加速收敛
- 方法要点：使用截断高斯分布围绕库默认值初始化，并与均匀随机基线比较
- 实验或效果：跨多种后端、模型和数据集，默认初始化无统计显著优势，p值0.141-0.908

## 摘要（原文）

> Bayesian Optimization (BO) is a standard tool for hyperparameter tuning thanks to its sample efficiency on expensive black-box functions. While most BO pipelines begin with uniform random initialization, default hyperparameter values shipped with popular ML libraries such as scikit-learn encode implicit expert knowledge and could serve as informative starting points that accelerate convergence. This hypothesis, despite its intuitive appeal, has remained largely unexamined. We formalize the idea by initializing BO with points drawn from truncated Gaussian distributions centered at library defaults and compare the resulting trajectories against a uniform-random baseline. We conduct an extensive empirical evaluation spanning three BO back-ends (BoTorch, Optuna, Scikit-Optimize), three model families (Random Forests, Support Vector Machines, Multilayer Perceptrons), and five benchmark datasets covering classification and regression tasks. Performance is assessed through convergence speed and final predictive quality, and statistical significance is determined via one-sided binomial tests. Across all conditions, default-informed initialization yields no statistically significant advantage over purely random sampling, with p-values ranging from 0.141 to 0.908. A sensitivity analysis on the prior variance confirms that, while tighter concentration around the defaults improves early evaluations, this transient benefit vanishes as optimization progresses, leaving final performance unchanged. Our results provide no evidence that default hyperparameters encode useful directional information for optimization. We therefore recommend that practitioners treat hyperparameter tuning as an integral part of model development and favor principled, data-driven search strategies over heuristic reliance on library defaults.

