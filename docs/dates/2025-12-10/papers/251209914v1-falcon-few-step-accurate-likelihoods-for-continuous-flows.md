---
layout: default
title: FALCON: Few-step Accurate Likelihoods for Continuous Flows
---

# FALCON: Few-step Accurate Likelihoods for Continuous Flows
**arXiv**：[2512.09914v1](https://arxiv.org/abs/2512.09914) · [PDF](https://arxiv.org/pdf/2512.09914.pdf)  
**作者**：Danyal Rehman, Tara Akhound-Sadegh, Artem Gazizov, Yoshua Bengio, Alexander Tong  

**一句话要点**：提出FALCON方法以解决连续流模型在分子玻尔兹曼采样中似然计算成本高的问题

**关键词**：分子玻尔兹曼采样, 连续归一化流, 重要性采样, 可逆性训练, 少步采样

## 3 点简述
- 核心问题：连续归一化流模型在分子热力学平衡态采样中，似然计算需数千次函数评估，成本极高。
- 方法要点：引入混合训练目标，促进模型可逆性，实现少步采样且似然足够精确用于重要性采样。
- 实验或效果：FALCON在分子玻尔兹曼采样中优于当前最优归一化流模型，比等效CNF模型快两个数量级。

## 摘要（原文）

> Scalable sampling of molecular states in thermodynamic equilibrium is a long-standing challenge in statistical physics. Boltzmann Generators tackle this problem by pairing a generative model, capable of exact likelihood computation, with importance sampling to obtain consistent samples under the target distribution. Current Boltzmann Generators primarily use continuous normalizing flows (CNFs) trained with flow matching for efficient training of powerful models. However, likelihood calculation for these models is extremely costly, requiring thousands of function evaluations per sample, severely limiting their adoption. In this work, we propose Few-step Accurate Likelihoods for Continuous Flows (FALCON), a method which allows for few-step sampling with a likelihood accurate enough for importance sampling applications by introducing a hybrid training objective that encourages invertibility. We show FALCON outperforms state-of-the-art normalizing flow models for molecular Boltzmann sampling and is two orders of magnitude faster than the equivalently performing CNF model.

