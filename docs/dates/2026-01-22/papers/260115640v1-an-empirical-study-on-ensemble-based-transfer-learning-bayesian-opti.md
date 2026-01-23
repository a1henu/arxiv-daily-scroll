---
layout: default
title: An Empirical Study on Ensemble-Based Transfer Learning Bayesian Optimisation with Mixed Variable Types
---

# An Empirical Study on Ensemble-Based Transfer Learning Bayesian Optimisation with Mixed Variable Types
**arXiv**：[2601.15640v1](https://arxiv.org/abs/2601.15640) · [PDF](https://arxiv.org/pdf/2601.15640.pdf)  
**作者**：Natasha Trinkle, Huong Ha, Jeffrey Chan  

**一句话要点**：提出基于正则化回归的正权重集成策略，以提升混合变量贝叶斯优化中的迁移学习性能

**关键词**：贝叶斯优化, 迁移学习, 集成方法, 混合变量优化, 正则化回归

## 3 点简述
- 核心问题：如何利用历史数据集改进混合变量贝叶斯优化的样本效率
- 方法要点：引入正权重约束的集成代理模型和暖启动初始化组件
- 实验或效果：通过新基准测试验证，正权重和暖启动能提升迁移学习效果

## 摘要（原文）

> Bayesian optimisation is a sample efficient method for finding a global optimum of expensive black-box objective functions. Historic datasets from related problems can be exploited to help improve performance of Bayesian optimisation by adapting transfer learning methods to various components of the Bayesian optimisation pipeline. In this study we perform an empirical analysis of various ensemble-based transfer learning Bayesian optimisation methods and pipeline components. We expand on previous work in the literature by contributing some specific pipeline components, and three new real-time transfer learning Bayesian optimisation benchmarks. In particular we propose to use a weighting strategy for ensemble surrogate model predictions based on regularised regression with weights constrained to be positive, and a related component for handling the case when transfer learning is not improving Bayesian optimisation performance. We find that in general, two components that help improve transfer learning Bayesian optimisation performance are warm start initialisation and constraining weights used with ensemble surrogate model to be positive.

