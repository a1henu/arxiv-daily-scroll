---
layout: default
title: Scaling Machine Learning Interatomic Potentials with Mixtures of Experts
---

# Scaling Machine Learning Interatomic Potentials with Mixtures of Experts
**arXiv**：[2603.07977v1](https://arxiv.org/abs/2603.07977) · [PDF](https://arxiv.org/pdf/2603.07977.pdf)  
**作者**：Yuzhi Liu, Duo Zhang, Anyang Peng, Weinan E, Linfeng Zhang, Han Wang  

**一句话要点**：提出基于专家混合的机器学习原子间势能模型，以提升表达能力和准确性

**关键词**：机器学习原子间势能, 专家混合架构, 元素级路由, 非线性专家, 原子模拟, 化学特性建模

## 3 点简述
- 核心问题：机器学习原子间势能模型在高效提升表达能力方面面临挑战
- 方法要点：系统开发专家混合和线性专家混合架构，分析路由策略和专家设计的影响
- 实验或效果：元素级路由模型在多个基准测试中达到最先进精度，路由模式显示化学可解释的专家专业化

## 摘要（原文）

> Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

