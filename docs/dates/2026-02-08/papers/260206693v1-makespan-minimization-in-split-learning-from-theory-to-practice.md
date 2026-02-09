---
layout: default
title: Makespan Minimization in Split Learning: From Theory to Practice
---

# Makespan Minimization in Split Learning: From Theory to Practice
**arXiv**：[2602.06693v1](https://arxiv.org/abs/2602.06693) · [PDF](https://arxiv.org/pdf/2602.06693.pdf)  
**作者**：Robert Ganian, Fionn Mc Inerney, Dimitra Tsigkari  

**一句话要点**：提出5-近似算法与启发式方法以最小化分裂学习的训练时间

**关键词**：分裂学习, 训练时间优化, 近似算法, 异构物联网, 任务调度, 内存约束

## 3 点简述
- 研究分裂学习中客户端-助手分配与任务调度的核心优化问题
- 针对同质任务提出多项式时间5-近似算法，并证明其理论界限
- 针对异质任务开发新启发式方法，实验显示优于现有方法

## 摘要（原文）

> Split learning recently emerged as a solution for distributed machine learning with heterogeneous IoT devices, where clients can offload part of their training to computationally-powerful helpers. The core challenge in split learning is to minimize the training time by jointly devising the client-helper assignment and the schedule of tasks at the helpers. We first study the model where each helper has a memory cardinality constraint on how many clients it may be assigned, which represents the case of homogeneous tasks. Through complexity theory, we rule out exact polynomial-time algorithms and approximation schemes even for highly restricted instances of this problem. We complement these negative results with a non-trivial polynomial-time 5-approximation algorithm. Building on this, we then focus on the more general heterogeneous task setting considered by Tirana et al. [INFOCOM 2024], where helpers have memory capacity constraints and clients have variable memory costs. In this case, we prove that, unless P=NP, the problem cannot admit a polynomial-time approximation algorithm for any approximation factor. However, by adapting our aforementioned 5-approximation algorithm, we develop a novel heuristic for the heterogeneous task setting and show that it outperforms heuristics from prior works through extensive experiments.

