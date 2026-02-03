---
layout: default
title: Learning Half-Spaces from Perturbed Contrastive Examples
---

# Learning Half-Spaces from Perturbed Contrastive Examples
**arXiv**：[2602.02080v1](https://arxiv.org/abs/2602.02080) · [PDF](https://arxiv.org/pdf/2602.02080.pdf)  
**作者**：Aryan Alavi Razavi Ravari, Farnam Mansouri, Yuxin Chen, Valentio Iverson, Adish Singla, Sandra Zilles  

**一句话要点**：提出扰动对比示例机制以加速半空间学习，分析噪声函数对样本复杂度的影响。

**关键词**：对比学习, 半空间学习, 样本复杂度, 噪声扰动, 查询复杂度, 主动学习

## 3 点简述
- 研究在两步对比示例oracle下的学习问题，其中对比示例被噪声函数扰动。
- 分析一维阈值和有界域均匀分布下半空间的主动与被动对比样本复杂度。
- 在特定噪声函数条件下，对比示例能降低查询复杂度，加速学习过程。

## 摘要（原文）

> We study learning under a two-step contrastive example oracle, as introduced by Mansouri et. al. (2025), where each queried (or sampled) labeled example is paired with an additional contrastive example of opposite label. While Mansouri et al. assume an idealized setting, where the contrastive example is at minimum distance of the originally queried/sampled point, we introduce and analyze a mechanism, parameterized by a non-decreasing noise function $f$, under which this ideal contrastive example is perturbed. The amount of perturbation is controlled by $f(d)$, where $d$ is the distance of the queried/sampled point to the decision boundary. Intuitively, this results in higher-quality contrastive examples for points closer to the decision boundary. We study this model in two settings: (i) when the maximum perturbation magnitude is fixed, and (ii) when it is stochastic.
>   For one-dimensional thresholds and for half-spaces under the uniform distribution on a bounded domain, we characterize active and passive contrastive sample complexity in dependence on the function $f$. We show that, under certain conditions on $f$, the presence of contrastive examples speeds up learning in terms of asymptotic query complexity and asymptotic expected query complexity.

