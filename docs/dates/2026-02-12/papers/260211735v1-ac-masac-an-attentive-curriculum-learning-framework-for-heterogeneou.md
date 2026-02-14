---
layout: default
title: AC-MASAC: An Attentive Curriculum Learning Framework for Heterogeneous UAV Swarm Coordination
---

# AC-MASAC: An Attentive Curriculum Learning Framework for Heterogeneous UAV Swarm Coordination
**arXiv**：[2602.11735v1](https://arxiv.org/abs/2602.11735) · [PDF](https://arxiv.org/pdf/2602.11735.pdf)  
**作者**：Wanhao Liu, Junhong Dai, Yixuan Zhang, Shengyun Yin, Panshuo Li  

**一句话要点**：提出基于注意力课程学习的异构无人机集群协调框架，以解决多智能体强化学习中的非对称依赖和训练挑战。

**关键词**：异构无人机集群, 多智能体强化学习, 注意力机制, 课程学习, 协同路径规划

## 3 点简述
- 核心问题：异构无人机集群协同路径规划中，多智能体强化学习面临非对称依赖、稀疏奖励和灾难性遗忘等挑战。
- 方法要点：引入角色感知异构注意力机制建模非对称依赖，设计结构化课程策略结合知识迁移和经验回放。
- 实验或效果：在自定义仿真平台验证，方法在成功率、队形保持率和加权任务时间上优于先进方法。

## 摘要（原文）

> Cooperative path planning for heterogeneous UAV swarms poses significant challenges for Multi-Agent Reinforcement Learning (MARL), particularly in handling asymmetric inter-agent dependencies and addressing the risks of sparse rewards and catastrophic forgetting during training. To address these issues, this paper proposes an attentive curriculum learning framework (AC-MASAC). The framework introduces a role-aware heterogeneous attention mechanism to explicitly model asymmetric dependencies. Moreover, a structured curriculum strategy is designed, integrating hierarchical knowledge transfer and stage-proportional experience replay to address the issues of sparse rewards and catastrophic forgetting. The proposed framework is validated on a custom multi-agent simulation platform, and the results show that our method has significant advantages over other advanced methods in terms of Success Rate, Formation Keeping Rate, and Success-weighted Mission Time. The code is available at \textcolor{red}{https://github.com/Wanhao-Liu/AC-MASAC}.

