---
layout: default
title: Game-Theoretic Risk-Shaped Reinforcement Learning for Safe Autonomous Driving
---

# Game-Theoretic Risk-Shaped Reinforcement Learning for Safe Autonomous Driving
**arXiv**：[2510.10960v1](https://arxiv.org/abs/2510.10960) · [PDF](https://arxiv.org/pdf/2510.10960.pdf)  
**作者**：Dong Hu, Fenqing Hu, Lidong Yang, Chao Huang  

**一句话要点**：提出博弈论风险塑造强化学习框架以解决自动驾驶安全挑战

**关键词**：自动驾驶安全, 强化学习, 博弈论, 风险建模, 不确定性感知, 策略优化

## 3 点简述
- 传统强化学习在动态交通中难以平衡安全与效率，缺乏风险建模
- 结合多级博弈论模型预测交互行为与风险，自适应调整决策视野
- 实验显示在多种场景下显著提升成功率、减少碰撞和违规

## 摘要（原文）

> Ensuring safety in autonomous driving (AD) remains a significant challenge,
> especially in highly dynamic and complex traffic environments where diverse
> agents interact and unexpected hazards frequently emerge. Traditional
> reinforcement learning (RL) methods often struggle to balance safety,
> efficiency, and adaptability, as they primarily focus on reward maximization
> without explicitly modeling risk or safety constraints. To address these
> limitations, this study proposes a novel game-theoretic risk-shaped RL (GTR2L)
> framework for safe AD. GTR2L incorporates a multi-level game-theoretic world
> model that jointly predicts the interactive behaviors of surrounding vehicles
> and their associated risks, along with an adaptive rollout horizon that adjusts
> dynamically based on predictive uncertainty. Furthermore, an uncertainty-aware
> barrier mechanism enables flexible modulation of safety boundaries. A dedicated
> risk modeling approach is also proposed, explicitly capturing both epistemic
> and aleatoric uncertainty to guide constrained policy optimization and enhance
> decision-making in complex environments. Extensive evaluations across diverse
> and safety-critical traffic scenarios show that GTR2L significantly outperforms
> state-of-the-art baselines, including human drivers, in terms of success rate,
> collision and violation reduction, and driving efficiency. The code is
> available at https://github.com/DanielHu197/GTR2L.

