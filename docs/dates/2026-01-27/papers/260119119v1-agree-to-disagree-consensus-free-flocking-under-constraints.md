---
layout: default
title: Agree to Disagree: Consensus-Free Flocking under Constraints
---

# Agree to Disagree: Consensus-Free Flocking under Constraints
**arXiv**：[2601.19119v1](https://arxiv.org/abs/2601.19119) · [PDF](https://arxiv.org/pdf/2601.19119.pdf)  
**作者**：Peter Travis Jardine, Sidney Givigi  

**一句话要点**：提出基于约束集体势函数的无共识群集控制方法，以解决多智能体目标冲突下的协调运动问题。

**关键词**：多智能体系统, 群集控制, 约束优化, 局部观测, 无共识协调

## 3 点简述
- 核心问题：传统群集控制假设智能体间距离一致，但实际应用中存在目标冲突和通信不可靠的挑战。
- 方法要点：通过局部观测和约束集体势函数，允许智能体协商距离参数，无需全局信息或通信。
- 实验或效果：通过仿真验证了方法在半信任场景下的有效性和鲁棒性。

## 摘要（原文）

> Robots sometimes have to work together with a mixture of partially-aligned or conflicting goals. Flocking - coordinated motion through cohesion, alignment, and separation - traditionally assumes uniform desired inter-agent distances. Many practical applications demand greater flexibility, as the diversity of types and configurations grows with the popularity of multi-agent systems in society. Moreover, agents often operate without guarantees of trust or secure communication. Motivated by these challenges we update well-established frameworks by relaxing this assumption of shared inter-agent distances and constraints. Through a new form of constrained collective potential function, we introduce a solution that permits negotiation of these parameters. In the spirit of the traditional flocking control canon, this negotiation is achieved purely through local observations and does not require any global information or inter-agent communication. The approach is robust to semi-trust scenarios, where neighbouring agents pursue conflicting goals. We validate the effectiveness of the approach through a series of simulations.

