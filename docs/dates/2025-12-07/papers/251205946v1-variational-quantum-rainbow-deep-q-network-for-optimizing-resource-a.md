---
layout: default
title: Variational Quantum Rainbow Deep Q-Network for Optimizing Resource Allocation Problem
---

# Variational Quantum Rainbow Deep Q-Network for Optimizing Resource Allocation Problem
**arXiv**：[2512.05946v1](https://arxiv.org/abs/2512.05946) · [PDF](https://arxiv.org/pdf/2512.05946.pdf)  
**作者**：Truong Thanh Hung Nguyen, Truong Thinh Nguyen, Hung Cao  

**一句话要点**：提出变分量子彩虹深度Q网络，用于优化人力资源分配问题。

**关键词**：量子强化学习, 资源分配, 变分量子电路, 深度Q网络, 人力资源分配

## 3 点简述
- 资源分配问题因组合复杂性而NP难，经典深度强化学习方法表示能力受限。
- 集成环形拓扑变分量子电路与彩虹DQN，利用量子叠加和纠缠增强表示。
- 在四个HRAP基准上，VQR-DQN相比随机基线减少26.8%归一化完工时间，优于经典方法4.9-13.4%。

## 摘要（原文）

> Resource allocation remains NP-hard due to combinatorial complexity. While deep reinforcement learning (DRL) methods, such as the Rainbow Deep Q-Network (DQN), improve scalability through prioritized replay and distributional heads, classical function approximators limit their representational power. We introduce Variational Quantum Rainbow DQN (VQR-DQN), which integrates ring-topology variational quantum circuits with Rainbow DQN to leverage quantum superposition and entanglement. We frame the human resource allocation problem (HRAP) as a Markov decision process (MDP) with combinatorial action spaces based on officer capabilities, event schedules, and transition times. On four HRAP benchmarks, VQR-DQN achieves 26.8% normalized makespan reduction versus random baselines and outperforms Double DQN and classical Rainbow DQN by 4.9-13.4%. These gains align with theoretical connections between circuit expressibility, entanglement, and policy quality, demonstrating the potential of quantum-enhanced DRL for large-scale resource allocation. Our implementation is available at: https://github.com/Analytics-Everywhere-Lab/qtrl/.

