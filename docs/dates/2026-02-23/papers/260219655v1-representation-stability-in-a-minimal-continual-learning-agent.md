---
layout: default
title: Representation Stability in a Minimal Continual Learning Agent
---

# Representation Stability in a Minimal Continual Learning Agent
**arXiv**：[2602.19655v1](https://arxiv.org/abs/2602.19655) · [PDF](https://arxiv.org/pdf/2602.19655.pdf)  
**作者**：Vishnu Subramanian  

**一句话要点**：提出最小持续学习代理以研究内部表示稳定性，揭示无显式正则化下的稳定性-可塑性权衡。

**关键词**：持续学习, 表示稳定性, 最小代理, 状态向量, 稳定性-可塑性权衡, 语义扰动

## 3 点简述
- 核心问题：持续学习系统在不可重置环境中，内部表示随时间演化的稳定性常被忽视。
- 方法要点：设计最小代理，通过持久状态向量增量更新，量化表示变化以定义稳定性指标。
- 实验或效果：纵向实验显示表示从初始可塑过渡到稳定，语义扰动后能恢复并再稳定。

## 摘要（原文）

> Continual learning systems are increasingly deployed in environments where retraining or reset is infeasible, yet many approaches emphasize task performance rather than the evolution of internal representations over time. In this work, we study a minimal continual learning agent designed to isolate representational dynamics from architectural complexity and optimization objectives. The agent maintains a persistent state vector across executions and incrementally updates it as new textual data is introduced. We quantify representational change using cosine similarity between successive normalized state vectors and define a stability metric over time intervals. Longitudinal experiments across eight executions reveal a transition from an initial plastic regime to a stable representational regime under consistent input. A deliberately introduced semantic perturbation produces a bounded decrease in similarity, followed by recovery and restabilization under subsequent coherent input. These results demonstrate that meaningful stability plasticity tradeoffs can emerge in a minimal, stateful learning system without explicit regularization, replay, or architectural complexity. The work establishes a transparent empirical baseline for studying representational accumulation and adaptation in continual learning systems.

