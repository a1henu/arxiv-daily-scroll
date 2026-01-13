---
layout: default
title: Active Evaluation of General Agents: Problem Definition and Comparison of Baseline Algorithms
---

# Active Evaluation of General Agents: Problem Definition and Comparison of Baseline Algorithms
**arXiv**：[2601.07651v1](https://arxiv.org/abs/2601.07651) · [PDF](https://arxiv.org/pdf/2601.07651.pdf)  
**作者**：Marc Lanctot, Kate Larson, Ian Gemp, Michael Kaisers  

**一句话要点**：提出主动评估通用智能体的框架，以高效比较多任务性能

**关键词**：智能体评估, 主动学习, 排名算法, 多任务学习, Atari游戏

## 3 点简述
- 核心问题：通用智能体评估成本高，任务相关且随机，需大量样本
- 方法要点：在线主动评估框架，迭代选择任务和智能体采样，评估排名算法性能
- 实验或效果：比较基线算法，Elo在合成数据中可靠，Soft Condorcet在Atari数据中更优

## 摘要（原文）

> As intelligent agents become more generally-capable, i.e. able to master a wide variety of tasks, the complexity and cost of properly evaluating them rises significantly. Tasks that assess specific capabilities of the agents can be correlated and stochastic, requiring many samples for accurate comparisons, leading to added costs. In this paper, we propose a formal definition and a conceptual framework for active evaluation of agents across multiple tasks, which assesses the performance of ranking algorithms as a function of number of evaluation data samples. Rather than curating, filtering, or compressing existing data sets as a preprocessing step, we propose an online framing: on every iteration, the ranking algorithm chooses the task and agents to sample scores from. Then, evaluation algorithms report a ranking of agents on each iteration and their performance is assessed with respect to the ground truth ranking over time. Several baselines are compared under different experimental contexts, with synthetic generated data and simulated online access to real evaluation data from Atari game-playing agents. We find that the classical Elo rating system -- while it suffers from well-known failure modes, in theory -- is a consistently reliable choice for efficient reduction of ranking error in practice. A recently-proposed method, Soft Condorcet Optimization, shows comparable performance to Elo on synthetic data and significantly outperforms Elo on real Atari agent evaluation. When task variation from the ground truth is high, selecting tasks based on proportional representation leads to higher rate of ranking error reduction.

