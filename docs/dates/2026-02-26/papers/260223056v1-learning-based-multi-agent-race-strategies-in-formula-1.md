---
layout: default
title: Learning-based Multi-agent Race Strategies in Formula 1
---

# Learning-based Multi-agent Race Strategies in Formula 1
**arXiv**：[2602.23056v1](https://arxiv.org/abs/2602.23056) · [PDF](https://arxiv.org/pdf/2602.23056.pdf)  
**作者**：Giona Fieni, Joschua Wüthrich, Marc-Philippe Neumann, Christopher H. Onder  

**一句话要点**：提出基于强化学习的多智能体策略优化框架，以解决F1赛车中动态比赛条件下的策略决策问题。

**关键词**：强化学习, 多智能体系统, F1赛车策略, 自博弈训练, 动态决策优化

## 3 点简述
- 核心问题：F1比赛中策略需根据比赛条件和对手行为动态调整，涉及能量管理、轮胎退化等多因素平衡。
- 方法要点：基于预训练单智能体策略，引入交互模块考虑对手行为，结合自博弈训练生成竞争性策略。
- 实验或效果：智能体能适应对手调整进站时机、轮胎选择和能量分配，实现稳健比赛表现，可支持实际比赛决策。

## 摘要（原文）

> In Formula 1, race strategies are adapted according to evolving race conditions and competitors' actions. This paper proposes a reinforcement learning approach for multi-agent race strategy optimization. Agents learn to balance energy management, tire degradation, aerodynamic interaction, and pit-stop decisions. Building on a pre-trained single-agent policy, we introduce an interaction module that accounts for the behavior of competitors. The combination of the interaction module and a self-play training scheme generates competitive policies, and agents are ranked based on their relative performance. Results show that the agents adapt pit timing, tire selection, and energy allocation in response to opponents, achieving robust and consistent race performance. Because the framework relies only on information available during real races, it can support race strategists' decisions before and during races.

