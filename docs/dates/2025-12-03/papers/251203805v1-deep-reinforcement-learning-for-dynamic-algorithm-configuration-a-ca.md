---
layout: default
title: Deep Reinforcement Learning for Dynamic Algorithm Configuration: A Case Study on Optimizing OneMax with the (1+($λ$,$λ$))-GA
---

# Deep Reinforcement Learning for Dynamic Algorithm Configuration: A Case Study on Optimizing OneMax with the (1+($λ$,$λ$))-GA
**arXiv**：[2512.03805v1](https://arxiv.org/abs/2512.03805) · [PDF](https://arxiv.org/pdf/2512.03805.pdf)  
**作者**：Tai Nguyen, Phong Le, André Biedenkapp, Carola Doerr, Nguyen Dang  

**一句话要点**：提出自适应奖励偏移机制以解决深度强化学习在动态算法配置中的探索不足问题

**关键词**：动态算法配置, 深度强化学习, 自适应奖励偏移, DDQN, PPO, OneMax优化

## 3 点简述
- 研究深度强化学习在动态算法配置中的挑战，包括可扩展性下降和学习不稳定性
- 引入自适应奖励偏移机制，基于奖励分布统计增强DDQN探索，无需实例特定超参数调优
- 在OneMax问题上，DDQN结合该机制实现与理论策略相当的性能，样本效率大幅提升

## 摘要（原文）

> Dynamic Algorithm Configuration (DAC) studies the efficient identification of control policies for parameterized optimization algorithms. Numerous studies have leveraged the robustness of decision-making in Reinforcement Learning (RL) to address the optimization challenges in algorithm configuration. However, applying RL to DAC is challenging and often requires extensive domain expertise. We conduct a comprehensive study of deep-RL algorithms in DAC through a systematic analysis of controlling the population size parameter of the (1+($λ$,$λ$))-GA on OneMax instances. Our investigation of DDQN and PPO reveals two fundamental challenges that limit their effectiveness in DAC: scalability degradation and learning instability. We trace these issues to two primary causes: under-exploration and planning horizon coverage, each of which can be effectively addressed through targeted solutions. To address under-exploration, we introduce an adaptive reward shifting mechanism that leverages reward distribution statistics to enhance DDQN agent exploration, eliminating the need for instance-specific hyperparameter tuning and ensuring consistent effectiveness across different problem scales. In dealing with the planning horizon coverage problem, we demonstrate that undiscounted learning effectively resolves it in DDQN, while PPO faces fundamental variance issues that necessitate alternative algorithmic designs. We further analyze the hyperparameter dependencies of PPO, showing that while hyperparameter optimization enhances learning stability, it consistently falls short in identifying effective policies across various configurations. Finally, we demonstrate that DDQN equipped with our adaptive reward shifting strategy achieves performance comparable to theoretically derived policies with vastly improved sample efficiency, outperforming prior DAC approaches by several orders of magnitude.

