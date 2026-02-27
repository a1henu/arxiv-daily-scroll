---
layout: default
title: Learning-based Multi-agent Race Strategies in Formula 1
---

# Learning-based Multi-agent Race Strategies in Formula 1
**arXiv**：[2602.23056v1](https://arxiv.org/abs/2602.23056) · [PDF](https://arxiv.org/pdf/2602.23056.pdf)  
**作者**：Giona Fieni, Joschua Wüthrich, Marc-Philippe Neumann, Christopher H. Onder  

**一句话要点**：提出基于强化学习的多智能体赛车策略优化方法，以应对F1比赛中的动态竞争环境。

**关键词**：强化学习, 多智能体系统, 赛车策略优化, 自博弈训练, 交互模块

## 3 点简述
- 核心问题：F1比赛中需根据对手行为和比赛条件动态调整策略，涉及能量管理、轮胎磨损和进站决策。
- 方法要点：基于预训练单智能体策略，引入交互模块模拟对手行为，结合自博弈训练生成竞争性策略。
- 实验或效果：智能体能自适应调整进站时机、轮胎选择和能量分配，实现稳健比赛表现，支持赛前赛中决策。

## 摘要（原文）

> In Formula 1, race strategies are adapted according to evolving race conditions and competitors' actions. This paper proposes a reinforcement learning approach for multi-agent race strategy optimization. Agents learn to balance energy management, tire degradation, aerodynamic interaction, and pit-stop decisions. Building on a pre-trained single-agent policy, we introduce an interaction module that accounts for the behavior of competitors. The combination of the interaction module and a self-play training scheme generates competitive policies, and agents are ranked based on their relative performance. Results show that the agents adapt pit timing, tire selection, and energy allocation in response to opponents, achieving robust and consistent race performance. Because the framework relies only on information available during real races, it can support race strategists' decisions before and during races.

