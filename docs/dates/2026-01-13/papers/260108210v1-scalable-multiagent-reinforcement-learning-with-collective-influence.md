---
layout: default
title: Scalable Multiagent Reinforcement Learning with Collective Influence Estimation
---

# Scalable Multiagent Reinforcement Learning with Collective Influence Estimation
**arXiv**：[2601.08210v1](https://arxiv.org/abs/2601.08210) · [PDF](https://arxiv.org/pdf/2601.08210.pdf)  
**作者**：Zhenglong Luo, Zhiyong Chen, Aoxiang Liu, Ke Pan  

**一句话要点**：提出集体影响力估计网络以解决多智能体强化学习在通信受限环境下的可扩展性问题。

**关键词**：多智能体强化学习, 集体影响力估计, 可扩展性, 通信受限环境, 机器人协作

## 3 点简述
- 核心问题：现有方法依赖频繁信息交换，导致网络规模和计算成本随智能体数量快速增长，限制可扩展性。
- 方法要点：通过集体影响力估计网络，智能体仅从局部观察和任务对象状态推断交互信息，无需显式动作交换。
- 实验或效果：在SAC算法上验证，实现稳定高效协作，并在真实机器人平台展示提升的鲁棒性和部署可行性。

## 摘要（原文）

> Multiagent reinforcement learning (MARL) has attracted considerable attention due to its potential in addressing complex cooperative tasks. However, existing MARL approaches often rely on frequent exchanges of action or state information among agents to achieve effective coordination, which is difficult to satisfy in practical robotic systems. A common solution is to introduce estimator networks to model the behaviors of other agents and predict their actions; nevertheless, such designs cause the size and computational cost of the estimator networks to grow rapidly with the number of agents, thereby limiting scalability in large-scale systems.
>   To address these challenges, this paper proposes a multiagent learning framework augmented with a Collective Influence Estimation Network (CIEN). By explicitly modeling the collective influence of other agents on the task object, each agent can infer critical interaction information solely from its local observations and the task object's states, enabling efficient collaboration without explicit action information exchange. The proposed framework effectively avoids network expansion as the team size increases; moreover, new agents can be incorporated without modifying the network structures of existing agents, demonstrating strong scalability. Experimental results on multiagent cooperative tasks based on the Soft Actor-Critic (SAC) algorithm show that the proposed method achieves stable and efficient coordination under communication-limited environments. Furthermore, policies trained with collective influence modeling are deployed on a real robotic platform, where experimental results indicate significantly improved robustness and deployment feasibility, along with reduced dependence on communication infrastructure.

