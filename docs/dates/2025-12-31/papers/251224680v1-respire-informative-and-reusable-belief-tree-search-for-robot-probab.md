---
layout: default
title: ReSPIRe: Informative and Reusable Belief Tree Search for Robot Probabilistic Search and Tracking in Unknown Environments
---

# ReSPIRe: Informative and Reusable Belief Tree Search for Robot Probabilistic Search and Tracking in Unknown Environments
**arXiv**：[2512.24680v1](https://arxiv.org/abs/2512.24680) · [PDF](https://arxiv.org/pdf/2512.24680.pdf)  
**作者**：Kangjie Zhou, Zhaoyang Li, Han Gao, Yao Su, Hangxin Liu, Junzhi Yu, Chang Liu  

**一句话要点**：提出ReSPIRe方法，用于未知杂乱环境中目标搜索与跟踪的轨迹规划。

**关键词**：机器人轨迹规划, 目标搜索与跟踪, 互信息近似, 分层粒子结构, 信念树搜索

## 3 点简述
- 核心问题：在未知杂乱环境中，目标搜索与跟踪面临先验信息不准确和感知范围有限的问题。
- 方法要点：采用基于sigma点的互信息奖励近似和分层粒子结构，结合可重用信念树搜索进行在线规划。
- 实验或效果：仿真和真实实验显示，ReSPIRe在互信息近似误差、搜索效率和跟踪稳定性方面优于基准方法。

## 摘要（原文）

> Target search and tracking (SAT) is a fundamental problem for various robotic applications such as search and rescue and environmental exploration. This paper proposes an informative trajectory planning approach, namely ReSPIRe, for SAT in unknown cluttered environments under considerably inaccurate prior target information and limited sensing field of view. We first develop a novel sigma point-based approximation approach to fast and accurately estimate mutual information reward under non-Gaussian belief distributions, utilizing informative sampling in state and observation spaces to mitigate the computational intractability of integral calculation. To tackle significant uncertainty associated with inadequate prior target information, we propose the hierarchical particle structure in ReSPIRe, which not only extracts critical particles for global route guidance, but also adjusts the particle number adaptively for planning efficiency. Building upon the hierarchical structure, we develop the reusable belief tree search approach to build a policy tree for online trajectory planning under uncertainty, which reuses rollout evaluation to improve planning efficiency. Extensive simulations and real-world experiments demonstrate that ReSPIRe outperforms representative benchmark methods with smaller MI approximation error, higher search efficiency, and more stable tracking performance, while maintaining outstanding computational efficiency.

