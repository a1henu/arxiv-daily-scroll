---
layout: default
title: Learning Optimal Individualized Decision Rules with Conditional Demographic Parity
---

# Learning Optimal Individualized Decision Rules with Conditional Demographic Parity
**arXiv**：[2603.05226v1](https://arxiv.org/abs/2603.05226) · [PDF](https://arxiv.org/pdf/2603.05226.pdf)  
**作者**：Wenhai Cui, Wen Su, Donglin Zeng, Xingqiu Zhao  

**一句话要点**：提出结合条件人口均等约束的个性化决策规则框架，以解决数据偏见导致的歧视问题。

**关键词**：个性化决策规则, 条件人口均等, 公平机器学习, 算法歧视, 最优策略估计, 收敛率分析

## 3 点简述
- 核心问题：个性化决策规则在训练数据存在偏见时，可能对敏感属性定义的少数群体产生歧视性影响。
- 方法要点：通过将人口均等和条件人口均等约束纳入最优个性化决策规则估计，理论证明可通过扰动无约束最优规则高效求解。
- 实验或效果：理论推导了策略值和公平约束项的收敛率，并通过模拟研究和俄勒冈健康保险实验验证方法有效性。

## 摘要（原文）

> Individualized decision rules (IDRs) have become increasingly prevalent in societal applications such as personalized marketing, healthcare, and public policy design. However, a critical ethical concern arises from the potential discriminatory effects of IDRs trained on biased data. These algorithms may disproportionately harm individuals from minority subgroups defined by sensitive attributes like gender, race, or language. To address this issue, we propose a novel framework that incorporates demographic parity (DP) and conditional demographic parity (CDP) constraints into the estimation of optimal IDRs. We show that the theoretically optimal IDRs under DP and CDP constraints can be obtained by applying perturbations to the unconstrained optimal IDRs, enabling a computationally efficient solution. Theoretically, we derive convergence rates for both policy value and the fairness constraint term. The effectiveness of our methods is illustrated through comprehensive simulation studies and an empirical application to the Oregon Health Insurance Experiment.

