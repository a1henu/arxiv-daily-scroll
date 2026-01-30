---
layout: default
title: Explicit Credit Assignment through Local Rewards and Dependence Graphs in Multi-Agent Reinforcement Learning
---

# Explicit Credit Assignment through Local Rewards and Dependence Graphs in Multi-Agent Reinforcement Learning
**arXiv**：[2601.21523v1](https://arxiv.org/abs/2601.21523) · [PDF](https://arxiv.org/pdf/2601.21523.pdf)  
**作者**：Bang Giang Le, Viet Cuong Ta  

**一句话要点**：提出基于交互图与局部奖励的显式信用分配方法以提升多智能体强化学习中的合作效率

**关键词**：多智能体强化学习, 信用分配, 交互图, 局部奖励, 合作优化

## 3 点简述
- 核心问题：全局奖励噪声大，局部奖励易导致次优合作，需平衡信用分配与全局最优性。
- 方法要点：利用智能体交互图精细分配个体贡献，结合局部奖励加速学习，缓解合作问题。
- 实验或效果：实验显示方法灵活，优于传统局部和全局奖励设置，提升学习性能。

## 摘要（原文）

> To promote cooperation in Multi-Agent Reinforcement Learning, the reward signals of all agents can be aggregated together, forming global rewards that are commonly known as the fully cooperative setting. However, global rewards are usually noisy because they contain the contributions of all agents, which have to be resolved in the credit assignment process. On the other hand, using local reward benefits from faster learning due to the separation of agents' contributions, but can be suboptimal as agents myopically optimize their own reward while disregarding the global optimality. In this work, we propose a method that combines the merits of both approaches. By using a graph of interaction between agents, our method discerns the individual agent contribution in a more fine-grained manner than a global reward, while alleviating the cooperation problem with agents' local reward. We also introduce a practical approach for approximating such a graph. Our experiments demonstrate the flexibility of the approach, enabling improvements over the traditional local and global reward settings.

