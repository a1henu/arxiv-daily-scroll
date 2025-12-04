---
layout: default
title: A Theoretical Framework for Auxiliary-Loss-Free Load Balancing of Sparse Mixture-of-Experts in Large-Scale AI Models
---

# A Theoretical Framework for Auxiliary-Loss-Free Load Balancing of Sparse Mixture-of-Experts in Large-Scale AI Models
**arXiv**：[2512.03915v1](https://arxiv.org/abs/2512.03915) · [PDF](https://arxiv.org/pdf/2512.03915.pdf)  
**作者**：X. Y. Han, Yuan Zhong  

**一句话要点**：提出理论框架分析无辅助损失负载均衡，用于大规模AI模型中稀疏专家混合的负载平衡。

**关键词**：稀疏专家混合, 负载均衡, 原始-对偶方法, 在线优化, 理论分析, 大规模AI训练

## 3 点简述
- 核心问题：稀疏专家混合层中负载不均衡导致GPU利用率低，需优化令牌路由。
- 方法要点：将无辅助损失负载均衡建模为原始-对偶方法，分析单调改进、偏好规则和近似平衡保证。
- 实验或效果：在1B参数DeepSeekMoE模型上进行实验，验证理论框架的有效性。

## 摘要（原文）

> In large-scale AI training, Sparse Mixture-of-Experts (s-MoE) layers enable scaling by activating only a small subset of experts per token. An operational challenge in this design is load balancing: routing tokens to minimize the number of idle experts, which is important for the efficient utilization of (costly) GPUs. We provide a theoretical framework for analyzing the Auxiliary-Loss-Free Load Balancing (ALF-LB) procedure -- proposed by DeepSeek's Wang et al. (2024) -- by casting it as a one-step-per-iteration primal-dual method for an assignment problem. First, in a stylized deterministic setting, our framework yields several insightful structural properties: (i) a monotonic improvement of a Lagrangian objective, (ii) a preference rule that moves tokens from overloaded to underloaded experts, and (iii) an approximate-balancing guarantee. Then, we incorporate the stochastic and dynamic nature of AI training using a generalized online optimization formulation. In the online setting, we derive a strong convexity property of the objective that leads to a logarithmic expected regret bound under certain step-size choices. Additionally, we present real experiments on 1B-parameter DeepSeekMoE models to complement our theoretical findings. Together, these results build a principled framework for analyzing the Auxiliary-Loss-Free Load Balancing of s-MoE in AI models.

