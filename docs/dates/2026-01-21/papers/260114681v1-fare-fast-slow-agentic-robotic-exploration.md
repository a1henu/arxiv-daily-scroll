---
layout: default
title: FARE: Fast-Slow Agentic Robotic Exploration
---

# FARE: Fast-Slow Agentic Robotic Exploration
**arXiv**：[2601.14681v1](https://arxiv.org/abs/2601.14681) · [PDF](https://arxiv.org/pdf/2601.14681.pdf)  
**作者**：Shuhao Liao, Xuxin Lv, Jeric Lew, Shizhe Zhang, Jingsong Liang, Peizhuo Li, Yuhong Cao, Wenjun Wu, Guillaume Sartoretti  

**一句话要点**：提出FARE框架，通过LLM与RL结合实现机器人高效自主探索

**关键词**：机器人自主探索, 大语言模型, 强化学习, 分层控制, 快慢思维

## 3 点简述
- 核心问题：机器人自主探索中全局语义推理与局部快速控制的整合挑战
- 方法要点：采用快慢思维范式，LLM进行全局策略规划，RL执行局部决策
- 实验或效果：在模拟和真实大尺度环境中，FARE显著提升探索效率

## 摘要（原文）

> This work advances autonomous robot exploration by integrating agent-level semantic reasoning with fast local control. We introduce FARE, a hierarchical autonomous exploration framework that integrates a large language model (LLM) for global reasoning with a reinforcement learning (RL) policy for local decision making. FARE follows a fast-slow thinking paradigm. The slow-thinking LLM module interprets a concise textual description of the unknown environment and synthesizes an agent-level exploration strategy, which is then grounded into a sequence of global waypoints through a topological graph. To further improve reasoning efficiency, this module employs a modularity-based pruning mechanism that reduces redundant graph structures. The fast-thinking RL module executes exploration by reacting to local observations while being guided by the LLM-generated global waypoints. The RL policy is additionally shaped by a reward term that encourages adherence to the global waypoints, enabling coherent and robust closed-loop behavior. This architecture decouples semantic reasoning from geometric decision, allowing each module to operate in its appropriate temporal and spatial scale. In challenging simulated environments, our results show that FARE achieves substantial improvements in exploration efficiency over state-of-the-art baselines. We further deploy FARE on hardware and validate it in complex, large scale $200m\times130m$ building environment.

