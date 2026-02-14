---
layout: default
title: Adaptive Milestone Reward for GUI Agents
---

# Adaptive Milestone Reward for GUI Agents
**arXiv**：[2602.11524v1](https://arxiv.org/abs/2602.11524) · [PDF](https://arxiv.org/pdf/2602.11524.pdf)  
**作者**：Congmin Zheng, Xiaoyun Mo, Xinbei Ma, Qiqiang Lin, Yin Zhao, Jiachen Zhu, Xingyu Lou, Jun Wang, Zhaoxiang Wang, Weiwen Liu, Zhuosheng Zhang, Yong Yu, Weinan Zhang  

**一句话要点**：提出自适应里程碑奖励机制，以解决移动GUI智能体中长时程任务的信用分配问题。

**关键词**：移动GUI智能体, 强化学习, 信用分配, 自适应奖励, 里程碑学习, 泛化性能

## 3 点简述
- 核心问题：强化学习在移动GUI智能体训练中面临长时程任务的信用分配难题，奖励保真度与密度之间存在权衡。
- 方法要点：ADMIRE通过锚定轨迹到动态从成功探索中提炼的里程碑，构建可验证的自适应奖励系统，并集成非对称信用分配策略。
- 实验或效果：在AndroidWorld上，ADMIRE在不同基础模型上实现超过10%的绝对成功率提升，并在多种环境和算法中展现强泛化性。

## 摘要（原文）

> Reinforcement Learning (RL) has emerged as a mainstream paradigm for training Mobile GUI Agents, yet it struggles with the temporal credit assignment problem inherent in long-horizon tasks. A primary challenge lies in the trade-off between reward fidelity and density: outcome reward offers high fidelity but suffers from signal sparsity, while process reward provides dense supervision but remains prone to bias and reward hacking. To resolve this conflict, we propose the Adaptive Milestone Reward (ADMIRE) mechanism. ADMIRE constructs a verifiable, adaptive reward system by anchoring trajectory to milestones, which are dynamically distilled from successful explorations. Crucially, ADMIRE integrates an asymmetric credit assignment strategy that denoises successful trajectories and scaffolds failed trajectories. Extensive experiments demonstrate that ADMIRE consistently yields over 10% absolute improvement in success rate across different base models on AndroidWorld. Moreover, the method exhibits robust generalizability, achieving strong performance across diverse RL algorithms and heterogeneous environments such as web navigation and embodied tasks.

