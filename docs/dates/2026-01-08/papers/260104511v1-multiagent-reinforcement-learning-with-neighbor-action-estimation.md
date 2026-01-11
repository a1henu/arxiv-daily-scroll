---
layout: default
title: Multiagent Reinforcement Learning with Neighbor Action Estimation
---

# Multiagent Reinforcement Learning with Neighbor Action Estimation
**arXiv**：[2601.04511v1](https://arxiv.org/abs/2601.04511) · [PDF](https://arxiv.org/pdf/2601.04511.pdf)  
**作者**：Zhenglong Luo, Zhiyong Chen, Aoxiang Liu  

**一句话要点**：提出基于邻居动作估计的多智能体强化学习框架，以解决通信受限环境下的协作决策问题。

**关键词**：多智能体强化学习, 动作估计, 通信受限, 机器人协作, TD3算法, 去中心化系统

## 3 点简述
- 核心问题：现有方法依赖显式动作交换，在通信受限的实际工程环境中不实用。
- 方法要点：集成轻量级动作估计模块，仅用局部可观测信息推断邻居行为，无需显式动作共享。
- 实验或效果：在双臂机器人协作任务中验证，提升系统鲁棒性和部署可行性，减少对信息基础设施依赖。

## 摘要（原文）

> Multiagent reinforcement learning, as a prominent intelligent paradigm, enables collaborative decision-making within complex systems. However, existing approaches often rely on explicit action exchange between agents to evaluate action value functions, which is frequently impractical in real-world engineering environments due to communication constraints, latency, energy consumption, and reliability requirements. From an artificial intelligence perspective, this paper proposes an enhanced multiagent reinforcement learning framework that employs action estimation neural networks to infer agent behaviors. By integrating a lightweight action estimation module, each agent infers neighboring agents' behaviors using only locally observable information, enabling collaborative policy learning without explicit action sharing. This approach is fully compatible with standard TD3 algorithms and scalable to larger multiagent systems. At the engineering application level, this framework has been implemented and validated in dual-arm robotic manipulation tasks: two robotic arms collaboratively lift objects. Experimental results demonstrate that this approach significantly enhances the robustness and deployment feasibility of real-world robotic systems while reducing dependence on information infrastructure. Overall, this research advances the development of decentralized multiagent artificial intelligence systems while enabling AI to operate effectively in dynamic, information-constrained real-world environments.

