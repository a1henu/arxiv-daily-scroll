---
layout: default
title: How Sampling Shapes LLM Alignment: From One-Shot Optima to Iterative Dynamics
---

# How Sampling Shapes LLM Alignment: From One-Shot Optima to Iterative Dynamics
**arXiv**：[2602.12180v1](https://arxiv.org/abs/2602.12180) · [PDF](https://arxiv.org/pdf/2602.12180.pdf)  
**作者**：Yurong Chen, Yu He, Michael I. Jordan, Fan Yao  

**一句话要点**：分析采样与参考策略对LLM对齐的影响，揭示迭代动态中的振荡与稳定性条件

**关键词**：LLM对齐, 采样策略, 偏好优化, 迭代动态, 理论分析

## 3 点简述
- 研究采样和参考策略在LLM对齐中的理论影响，基于Identity Preference Optimization框架
- 证明实例依赖采样可增强排序保证，而偏斜采样可能导致过度集中，并分析迭代动态的振荡或熵崩溃
- 理论扩展到Direct Preference Optimization，实验在真实偏好数据上验证发现

## 摘要（原文）

> Standard methods for aligning large language models with human preferences learn from pairwise comparisons among sampled candidate responses and regularize toward a reference policy. Despite their effectiveness, the effects of sampling and reference choices are poorly understood theoretically. We investigate these effects through Identity Preference Optimization, a widely used preference alignment framework, and show that proper instance-dependent sampling can yield stronger ranking guarantees, while skewed on-policy sampling can induce excessive concentration under structured preferences. We then analyze iterative alignment dynamics in which the learned policy feeds back into future sampling and reference policies, reflecting a common practice of model-generated preference data. We prove that these dynamics can exhibit persistent oscillations or entropy collapse for certain parameter choices, and characterize regimes that guarantee stability. Our theoretical insights extend to Direct Preference Optimization, indicating the phenomena we captured are common to a broader class of preference-alignment methods. Experiments on real-world preference data validate our findings.

