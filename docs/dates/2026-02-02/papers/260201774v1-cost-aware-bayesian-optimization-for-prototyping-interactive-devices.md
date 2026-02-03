---
layout: default
title: Cost-Aware Bayesian Optimization for Prototyping Interactive Devices
---

# Cost-Aware Bayesian Optimization for Prototyping Interactive Devices
**arXiv**：[2602.01774v1](https://arxiv.org/abs/2602.01774) · [PDF](https://arxiv.org/pdf/2602.01774.pdf)  
**作者**：Thomas Langerak, Renate Zhang, Ziyuan Wang, Per Ola Kristensson, Antti Oulasvirta  

**一句话要点**：提出成本感知贝叶斯优化方法，以解决交互设备原型设计中成本不对称问题。

**关键词**：贝叶斯优化, 原型设计, 成本感知, 交互设备, 迭代设计, 采集函数

## 3 点简述
- 核心问题：迭代设计中原型成本差异大，阻碍设计空间探索。
- 方法要点：基于贝叶斯优化，通过设计师估计成本调整采集函数，引导采样至成本效益更高的原型。
- 实验或效果：技术评估中成本降低约30%，预算严格时性能提升三倍；用户研究验证实际设计任务中的有效性。

## 摘要（原文）

> Deciding which idea is worth prototyping is a central concern in iterative design. A prototype should be produced when the expected improvement is high and the cost is low. However, this is hard to decide, because costs can vary drastically: a simple parameter tweak may take seconds, while fabricating hardware consumes material and energy. Such asymmetries, can discourage a designer from exploring the design space. In this paper, we present an extension of cost-aware Bayesian optimization to account for diverse prototyping costs. The method builds on the power of Bayesian optimization and requires only a minimal modification to the acquisition function. The key idea is to use designer-estimated costs to guide sampling toward more cost-effective prototypes. In technical evaluations, the method achieved comparable utility to a cost-agnostic baseline while requiring only ${\approx}70\%$ of the cost; under strict budgets, it outperformed the baseline threefold. A within-subjects study with 12 participants in a realistic joystick design task demonstrated similar benefits. These results show that accounting for prototyping costs can make Bayesian optimization more compatible with real-world design projects.

