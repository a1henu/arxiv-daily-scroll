---
layout: default
title: StarCraft+: Benchmarking Multi-agent Algorithms in Adversary Paradigm
---

# StarCraft+: Benchmarking Multi-agent Algorithms in Adversary Paradigm
**arXiv**：[2512.16444v1](https://arxiv.org/abs/2512.16444) · [PDF](https://arxiv.org/pdf/2512.16444.pdf)  
**作者**：Yadong Li, Tong Zhang, Bo Huang, Zhen Cui  

**一句话要点**：提出StarCraft II战斗竞技场以在对抗范式中刷新多智能体强化学习算法基准测试

**关键词**：多智能体强化学习, 对抗基准测试, 星际争霸II, 算法评估, 开源环境

## 3 点简述
- 问题：现有基准如SMAC使用固定内置AI对手，导致算法评估多样性不足。
- 方法：创建SC2BA环境，支持算法间对抗，并开发APyMARL库提升易用性。
- 实验：在双算法配对和多算法混合对抗模式下基准测试经典算法，揭示效果、敏感性和可扩展性问题。

## 摘要（原文）

> Deep multi-agent reinforcement learning (MARL) algorithms are booming in the field of collaborative intelligence, and StarCraft multi-agent challenge (SMAC) is widely-used as the benchmark therein. However, imaginary opponents of MARL algorithms are practically configured and controlled in a fixed built-in AI mode, which causes less diversity and versatility in algorithm evaluation. To address this issue, in this work, we establish a multi-agent algorithm-vs-algorithm environment, named StarCraft II battle arena (SC2BA), to refresh the benchmarking of MARL algorithms in an adversary paradigm. Taking StarCraft as infrastructure, the SC2BA environment is specifically created for inter-algorithm adversary with the consideration of fairness, usability and customizability, and meantime an adversarial PyMARL (APyMARL) library is developed with easy-to-use interfaces/modules. Grounding in SC2BA, we benchmark those classic MARL algorithms in two types of adversarial modes: dual-algorithm paired adversary and multi-algorithm mixed adversary, where the former conducts the adversary of pairwise algorithms while the latter focuses on the adversary to multiple behaviors from a group of algorithms. The extensive benchmark experiments exhibit some thought-provoking observations/problems in the effectivity, sensibility and scalability of these completed algorithms. The SC2BA environment as well as reproduced experiments are released in \href{https://github.com/dooliu/SC2BA}{Github}, and we believe that this work could mark a new step for the MARL field in the coming years.

