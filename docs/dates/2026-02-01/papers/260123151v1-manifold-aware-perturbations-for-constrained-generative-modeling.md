---
layout: default
title: Manifold-Aware Perturbations for Constrained Generative Modeling
---

# Manifold-Aware Perturbations for Constrained Generative Modeling
**arXiv**：[2601.23151v1](https://arxiv.org/abs/2601.23151) · [PDF](https://arxiv.org/pdf/2601.23151.pdf)  
**作者**：Katherine Keegan, Lars Ruthotto  

**一句话要点**：提出流形感知扰动方法，以解决等式约束生成模型中的分布建模难题。

**关键词**：生成模型, 等式约束, 流形扰动, 扩散模型, 归一化流, 分布恢复

## 3 点简述
- 核心问题：生成模型在等式约束分布建模中存在数学限制，常见于科学领域。
- 方法要点：通过约束感知扰动数据分布，使新分布支持匹配环境空间维度，同时隐含流形几何。
- 实验或效果：在多个任务中验证，该方法能稳定恢复数据分布并支持扩散模型和归一化流。

## 摘要（原文）

> Generative models have enjoyed widespread success in a variety of applications. However, they encounter inherent mathematical limitations in modeling distributions where samples are constrained by equalities, as is frequently the setting in scientific domains. In this work, we develop a computationally cheap, mathematically justified, and highly flexible distributional modification for combating known pitfalls in equality-constrained generative models. We propose perturbing the data distribution in a constraint-aware way such that the new distribution has support matching the ambient space dimension while still implicitly incorporating underlying manifold geometry. Through theoretical analyses and empirical evidence on several representative tasks, we illustrate that our approach consistently enables data distribution recovery and stable sampling with both diffusion models and normalizing flows.

