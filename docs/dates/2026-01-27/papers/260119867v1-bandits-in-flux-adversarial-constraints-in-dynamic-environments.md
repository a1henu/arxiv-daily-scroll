---
layout: default
title: Bandits in Flux: Adversarial Constraints in Dynamic Environments
---

# Bandits in Flux: Adversarial Constraints in Dynamic Environments
**arXiv**：[2601.19867v1](https://arxiv.org/abs/2601.19867) · [PDF](https://arxiv.org/pdf/2601.19867.pdf)  
**作者**：Tareq Si Salem  

**一句话要点**：提出一种原对偶算法以解决动态环境中带有时变约束的对抗性多臂老虎机问题。

**关键词**：对抗性多臂老虎机, 时变约束, 原对偶算法, 动态遗憾, 在线镜像下降, 约束违反

## 3 点简述
- 研究动态环境中带有时变约束的对抗性多臂老虎机问题，适用于现实应用场景。
- 提出基于在线镜像下降的原对偶算法，结合梯度估计器和约束处理机制。
- 理论保证动态遗憾和约束违反均为次线性，实验验证算法性能优越。

## 摘要（原文）

> We investigate the challenging problem of adversarial multi-armed bandits operating under time-varying constraints, a scenario motivated by numerous real-world applications. To address this complex setting, we propose a novel primal-dual algorithm that extends online mirror descent through the incorporation of suitable gradient estimators and effective constraint handling. We provide theoretical guarantees establishing sublinear dynamic regret and sublinear constraint violation for our proposed policy. Our algorithm achieves state-of-the-art performance in terms of both regret and constraint violation. Empirical evaluations demonstrate the superiority of our approach.

