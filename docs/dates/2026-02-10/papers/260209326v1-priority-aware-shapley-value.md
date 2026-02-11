---
layout: default
title: Priority-Aware Shapley Value
---

# Priority-Aware Shapley Value
**arXiv**：[2602.09326v1](https://arxiv.org/abs/2602.09326) · [PDF](https://arxiv.org/pdf/2602.09326.pdf)  
**作者**：Kiljae Lee, Ziqi Liu, Weijing Tang, Yuan Zhang  

**一句话要点**：提出优先级感知Shapley值以解决贡献者依赖或优先级调整问题

**关键词**：Shapley值, 数据估值, 特征归因, 优先级约束, 蒙特卡洛采样, 敏感性分析

## 3 点简述
- 核心问题：Shapley值假设贡献者可互换，不适用于依赖或优先级场景
- 方法要点：引入硬优先级约束和软优先级权重，扩展Shapley值框架
- 实验或效果：在数据估值和特征归因实验中验证结构忠实分配和敏感性分析

## 摘要（原文）

> Shapley values are widely used for model-agnostic data valuation and feature attribution, yet they implicitly assume contributors are interchangeable. This can be problematic when contributors are dependent (e.g., reused/augmented data or causal feature orderings) or when contributions should be adjusted by factors such as trust or risk. We propose Priority-Aware Shapley Value (PASV), which incorporates both hard precedence constraints and soft, contributor-specific priority weights. PASV is applicable to general precedence structures, recovers precedence-only and weight-only Shapley variants as special cases, and is uniquely characterized by natural axioms. We develop an efficient adjacent-swap Metropolis-Hastings sampler for scalable Monte Carlo estimation and analyze limiting regimes induced by extreme priority weights. Experiments on data valuation (MNIST/CIFAR10) and feature attribution (Census Income) demonstrate more structure-faithful allocations and a practical sensitivity analysis via our proposed "priority sweeping".

