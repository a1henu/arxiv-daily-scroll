---
layout: default
title: Peer-to-Peer Energy Trading in Dairy Farms using Multi-Agent Reinforcement Learning
---

# Peer-to-Peer Energy Trading in Dairy Farms using Multi-Agent Reinforcement Learning
**arXiv**：[2511.23148v1](https://arxiv.org/abs/2511.23148) · [PDF](https://arxiv.org/pdf/2511.23148.pdf)  
**作者**：Mian Ibad Ali Shah, Marcos Eduardo Cruz Victorio, Maeve Duffy, Enda Barrett, Karl Mason  

**一句话要点**：提出基于多智能体强化学习的点对点能源交易方法，优化乳牛场能源管理。

**关键词**：多智能体强化学习, 点对点能源交易, 可再生能源管理, 乳牛场优化, 拍卖市场机制

## 3 点简述
- 核心问题：传统规则方法在动态环境中能源分配效率低，需提升乳牛场可再生能源利用。
- 方法要点：结合PPO和DQN多智能体强化学习，集成拍卖市场清算、价格顾问及负载电池管理。
- 实验或效果：在爱尔兰和芬兰实验中，DQN降低电费14.2%和5.16%，PPO减少峰值需求55.5%。

## 摘要（原文）

> The integration of renewable energy resources in rural areas, such as dairy farming communities, enables decentralized energy management through Peer-to-Peer (P2P) energy trading. This research highlights the role of P2P trading in efficient energy distribution and its synergy with advanced optimization techniques. While traditional rule-based methods perform well under stable conditions, they struggle in dynamic environments. To address this, Multi-Agent Reinforcement Learning (MARL), specifically Proximal Policy Optimization (PPO) and Deep Q-Networks (DQN), is combined with community/distributed P2P trading mechanisms. By incorporating auction-based market clearing, a price advisor agent, and load and battery management, the approach achieves significant improvements. Results show that, compared to baseline models, DQN reduces electricity costs by 14.2% in Ireland and 5.16% in Finland, while increasing electricity revenue by 7.24% and 12.73%, respectively. PPO achieves the lowest peak hour demand, reducing it by 55.5% in Ireland, while DQN reduces peak hour demand by 50.0% in Ireland and 27.02% in Finland. These improvements are attributed to both MARL algorithms and P2P energy trading, which together results in electricity cost and peak hour demand reduction, and increase electricity selling revenue. This study highlights the complementary strengths of DQN, PPO, and P2P trading in achieving efficient, adaptable, and sustainable energy management in rural communities.

