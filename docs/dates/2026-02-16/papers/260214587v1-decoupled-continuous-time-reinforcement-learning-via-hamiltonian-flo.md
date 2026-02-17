---
layout: default
title: Decoupled Continuous-Time Reinforcement Learning via Hamiltonian Flow
---

# Decoupled Continuous-Time Reinforcement Learning via Hamiltonian Flow
**arXiv**：[2602.14587v1](https://arxiv.org/abs/2602.14587) · [PDF](https://arxiv.org/pdf/2602.14587.pdf)  
**作者**：Minh Nguyen  

**一句话要点**：提出解耦连续时间强化学习算法，通过哈密顿流解决非均匀决策场景中的训练难题。

**关键词**：连续时间强化学习, 哈密顿流, 解耦优化, 演员-评论家算法, 非均匀决策, 扩散生成器

## 3 点简述
- 标准离散时间强化学习在连续时间控制中面临Q函数退化问题，导致动作排序失效。
- 新方法采用交替更新：从V的扩散生成器学习q，并通过哈密顿流更新V，保持信息性。
- 实验在连续控制和真实交易任务中超越基线，实现21%季度利润，近乎翻倍次优方法。

## 摘要（原文）

> Many real-world control problems, ranging from finance to robotics, evolve in continuous time with non-uniform, event-driven decisions. Standard discrete-time reinforcement learning (RL), based on fixed-step Bellman updates, struggles in this setting: as time gaps shrink, the $Q$-function collapses to the value function $V$, eliminating action ranking. Existing continuous-time methods reintroduce action information via an advantage-rate function $q$. However, they enforce optimality through complicated martingale losses or orthogonality constraints, which are sensitive to the choice of test processes. These approaches entangle $V$ and $q$ into a large, complex optimization problem that is difficult to train reliably. To address these limitations, we propose a novel decoupled continuous-time actor-critic algorithm with alternating updates: $q$ is learned from diffusion generators on $V$, and $V$ is updated via a Hamiltonian-based value flow that remains informative under infinitesimal time steps, where standard max/softmax backups fail. Theoretically, we prove rigorous convergence via new probabilistic arguments, sidestepping the challenge that generator-based Hamiltonians lack Bellman-style contraction under the sup-norm. Empirically, our method outperforms prior continuous-time and leading discrete-time baselines across challenging continuous-control benchmarks and a real-world trading task, achieving 21% profit over a single quarter$-$nearly doubling the second-best method.

