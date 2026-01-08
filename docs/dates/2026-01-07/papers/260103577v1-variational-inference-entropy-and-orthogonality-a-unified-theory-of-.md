---
layout: default
title: Variational Inference, Entropy, and Orthogonality: A Unified Theory of Mixture-of-Experts
---

# Variational Inference, Entropy, and Orthogonality: A Unified Theory of Mixture-of-Experts
**arXiv**：[2601.03577v1](https://arxiv.org/abs/2601.03577) · [PDF](https://arxiv.org/pdf/2601.03577.pdf)  
**作者**：Ye Su, Yong Liu  

**一句话要点**：提出统一理论框架，从贝叶斯和信息论角度推导MoE路由机制，并证明正交性正则化的最优性。

**关键词**：混合专家模型, 变分推断, 信息论, 正交性正则化, NP-hard问题, 路由机制

## 3 点简述
- 核心问题：MoE的Top-k路由和负载均衡缺乏理论支撑，路由问题本质上是NP-hard稀疏子集选择。
- 方法要点：构建贝叶斯和信息论统一框架，将路由机制推导为最优稀疏后验近似和先验正则化，并证明正交性可缩小NP-hard最优解与贪婪近似差距。
- 实验或效果：比较分析确认正交性正则化是大规模模型的最优工程松弛，提供理论支持和技术保障。

## 摘要（原文）

> Mixture-of-Experts models enable large language models to scale efficiently, as they only activate a subset of experts for each input. Their core mechanisms, Top-k routing and auxiliary load balancing, remain heuristic, however, lacking a cohesive theoretical underpinning to support them. To this end, we build the first unified theoretical framework that rigorously derives these practices as optimal sparse posterior approximation and prior regularization from a Bayesian perspective, while simultaneously framing them as mechanisms to minimize routing ambiguity and maximize channel capacity from an information-theoretic perspective. We also pinpoint the inherent combinatorial hardness of routing, defining it as the NP-hard sparse subset selection problem. We rigorously prove the existence of a "Coherence Barrier"; when expert representations exhibit high mutual coherence, greedy routing strategies theoretically fail to recover the optimal expert subset. Importantly, we formally verify that imposing geometric orthogonality in the expert feature space is sufficient to narrow the divide between the NP-hard global optimum and polynomial-time greedy approximation. Our comparative analyses confirm orthogonality regularization as the optimal engineering relaxation for large-scale models. Our work offers essential theoretical support and technical assurance for a deeper understanding and novel designs of MoE.

