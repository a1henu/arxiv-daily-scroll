---
layout: default
title: Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction
---

# Safe Planning in Interactive Environments via Iterative Policy Updates and Adversarially Robust Conformal Prediction
**arXiv**：[2511.10586v1](https://arxiv.org/abs/2511.10586) · [PDF](https://arxiv.org/pdf/2511.10586.pdf)  
**作者**：Omid Mirzaeedodangeh, Eliot Shekhtman, Nikolai Matni, Lars Lindemann  

**一句话要点**：提出迭代策略更新与对抗鲁棒共形预测框架，以在交互环境中实现安全规划。

**关键词**：安全规划, 交互环境, 共形预测, 策略更新, 分布偏移, 收敛分析

## 3 点简述
- 核心问题：交互环境中策略更新导致数据分布偏移，违反共形预测的交换性假设。
- 方法要点：通过策略-轨迹敏感性分析调整共形预测结果，跨策略更新转移安全保证。
- 实验或效果：在二维车-行人案例中实证安全与收敛保证，未知是否优于其他方法。

## 摘要（原文）

> Safe planning of an autonomous agent in interactive environments -- such as the control of a self-driving vehicle among pedestrians and human-controlled vehicles -- poses a major challenge as the behavior of the environment is unknown and reactive to the behavior of the autonomous agent. This coupling gives rise to interaction-driven distribution shifts where the autonomous agent's control policy may change the environment's behavior, thereby invalidating safety guarantees in existing work. Indeed, recent works have used conformal prediction (CP) to generate distribution-free safety guarantees using observed data of the environment. However, CP's assumption on data exchangeability is violated in interactive settings due to a circular dependency where a control policy update changes the environment's behavior, and vice versa. To address this gap, we propose an iterative framework that robustly maintains safety guarantees across policy updates by quantifying the potential impact of a planned policy update on the environment's behavior. We realize this via adversarially robust CP where we perform a regular CP step in each episode using observed data under the current policy, but then transfer safety guarantees across policy updates by analytically adjusting the CP result to account for distribution shifts. This adjustment is performed based on a policy-to-trajectory sensitivity analysis, resulting in a safe, episodic open-loop planner. We further conduct a contraction analysis of the system providing conditions under which both the CP results and the policy updates are guaranteed to converge. We empirically demonstrate these safety and convergence guarantees on a two-dimensional car-pedestrian case study. To the best of our knowledge, these are the first results that provide valid safety guarantees in such interactive settings.

