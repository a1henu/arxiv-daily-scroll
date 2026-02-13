---
layout: default
title: Exploring Multiple High-Scoring Subspaces in Generative Flow Networks
---

# Exploring Multiple High-Scoring Subspaces in Generative Flow Networks
**arXiv**：[2602.11491v1](https://arxiv.org/abs/2602.11491) · [PDF](https://arxiv.org/pdf/2602.11491.pdf)  
**作者**：Xuan Yu, Xu Wang, Rui Zhu, Yudong Zhang, Yang Wang  

**一句话要点**：提出CMAB-GFN以解决生成流网络在复杂组合对象构建中探索低效的问题

**关键词**：生成流网络, 组合多臂老虎机, 高奖励子空间探索, 概率采样框架, 复杂组合对象构建

## 3 点简述
- 核心问题：生成流网络在广阔状态空间中过度探索，导致低奖励区域过采样和收敛到次优分布
- 方法要点：集成组合多臂老虎机框架，通过剪枝低质量动作生成紧凑高奖励子空间进行探索
- 实验或效果：在多个任务中生成比现有方法更高奖励的候选对象，同时保持多样性

## 摘要（原文）

> As a probabilistic sampling framework, Generative Flow Networks (GFlowNets) show strong potential for constructing complex combinatorial objects through the sequential composition of elementary components. However, existing GFlowNets often suffer from excessive exploration over vast state spaces, leading to over-sampling of low-reward regions and convergence to suboptimal distributions. Effectively biasing GFlowNets toward high-reward solutions remains a non-trivial challenge. In this paper, we propose CMAB-GFN, which integrates a combinatorial multi-armed bandit (CMAB) framework with GFlowNet policies. The CMAB component prunes low-quality actions, yielding compact high-scoring subspaces for exploration. Restricting GFNs to these compact high-scoring subspaces accelerates the discovery of high-value candidates, while the exploration of different subspaces ensures that diversity is not sacrificed. Experimental results on multiple tasks demonstrate that CMAB-GFN generates higher-reward candidates than existing approaches.

