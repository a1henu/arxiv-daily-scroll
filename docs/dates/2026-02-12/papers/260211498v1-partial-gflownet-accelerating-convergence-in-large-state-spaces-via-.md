---
layout: default
title: Partial GFlowNet: Accelerating Convergence in Large State Spaces via Strategic Partitioning
---

# Partial GFlowNet: Accelerating Convergence in Large State Spaces via Strategic Partitioning
**arXiv**：[2602.11498v1](https://arxiv.org/abs/2602.11498) · [PDF](https://arxiv.org/pdf/2602.11498.pdf)  
**作者**：Xuan Yu, Xu Wang, Rui Zhu, Yudong Zhang, Yang Wang  

**一句话要点**：提出Partial GFlowNet，通过策略性分区加速大状态空间中的收敛

**关键词**：生成流网络, 状态空间分区, 加速收敛, 大状态空间, 策略探索

## 3 点简述
- 核心问题：现有GFlowNets在大状态空间中自由探索，面临收敛缓慢的挑战。
- 方法要点：引入规划器将状态空间划分为重叠的部分空间，限制探索范围以提高效率。
- 实验或效果：在多个数据集上验证，收敛更快，生成候选者奖励更高且多样性显著提升。

## 摘要（原文）

> Generative Flow Networks (GFlowNets) have shown promising potential to generate high-scoring candidates with probability proportional to their rewards. As existing GFlowNets freely explore in state space, they encounter significant convergence challenges when scaling to large state spaces. Addressing this issue, this paper proposes to restrict the exploration of actor. A planner is introduced to partition the entire state space into overlapping partial state spaces. Given their limited size, these partial state spaces allow the actor to efficiently identify subregions with higher rewards. A heuristic strategy is introduced to switch partial regions thus preventing the actor from wasting time exploring fully explored or low-reward partial regions. By iteratively exploring these partial state spaces, the actor learns to converge towards the high-reward subregions within the entire state space. Experiments on several widely used datasets demonstrate that \modelname converges faster than existing works on large state spaces. Furthermore, \modelname not only generates candidates with higher rewards but also significantly improves their diversity.

