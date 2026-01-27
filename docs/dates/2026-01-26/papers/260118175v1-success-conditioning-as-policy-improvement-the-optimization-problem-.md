---
layout: default
title: Success Conditioning as Policy Improvement: The Optimization Problem Solved by Imitating Success
---

# Success Conditioning as Policy Improvement: The Optimization Problem Solved by Imitating Success
**arXiv**：[2601.18175v1](https://arxiv.org/abs/2601.18175) · [PDF](https://arxiv.org/pdf/2601.18175.pdf)  
**作者**：Daniel Russo  

**一句话要点**：证明成功条件化作为策略改进，解决带自动约束的信任区域优化问题。

**关键词**：策略改进, 成功条件化, 信任区域优化, χ²散度, 目标条件强化学习, 决策变换器

## 3 点简述
- 核心问题：成功条件化（如拒绝采样、目标条件RL）的优化基础未知。
- 方法要点：证明其精确求解带χ²散度约束的信任区域优化，约束半径由数据自动确定。
- 实验或效果：理论应用于回报阈值化，显示可放大改进但可能偏离真实目标。

## 摘要（原文）

> A widely used technique for improving policies is success conditioning, in which one collects trajectories, identifies those that achieve a desired outcome, and updates the policy to imitate the actions taken along successful trajectories. This principle appears under many names -- rejection sampling with SFT, goal-conditioned RL, Decision Transformers -- yet what optimization problem it solves, if any, has remained unclear. We prove that success conditioning exactly solves a trust-region optimization problem, maximizing policy improvement subject to a $χ^2$ divergence constraint whose radius is determined automatically by the data. This yields an identity: relative policy improvement, the magnitude of policy change, and a quantity we call action-influence -- measuring how random variation in action choices affects success rates -- are exactly equal at every state. Success conditioning thus emerges as a conservative improvement operator. Exact success conditioning cannot degrade performance or induce dangerous distribution shift, but when it fails, it does so observably, by hardly changing the policy at all. We apply our theory to the common practice of return thresholding, showing this can amplify improvement, but at the cost of potential misalignment with the true objective.

