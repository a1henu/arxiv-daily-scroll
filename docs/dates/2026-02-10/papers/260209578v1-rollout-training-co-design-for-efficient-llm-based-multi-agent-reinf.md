---
layout: default
title: Rollout-Training Co-Design for Efficient LLM-Based Multi-Agent Reinforcement Learning
---

# Rollout-Training Co-Design for Efficient LLM-Based Multi-Agent Reinforcement Learning
**arXiv**：[2602.09578v1](https://arxiv.org/abs/2602.09578) · [PDF](https://arxiv.org/pdf/2602.09578.pdf)  
**作者**：Zhida Jiang, Zhaolong Xing, Jiawei Lu, Yipei Niu, Qingyuan Sang, Liangxu Zhang, Wenquan Dai, Junhua Shu, Jiaxing Wang, Qiangyu Pei, Qiong Chen, Xinyu Liu, Fangming Liu, Ai Han, Zhen Chen, Ke Zhang  

**一句话要点**：提出FlexMARL框架以优化基于LLM的大规模多智能体强化学习训练效率

**关键词**：多智能体强化学习, 训练框架优化, 异步流水线, 负载平衡, 资源分配, LLM应用

## 3 点简述
- 核心问题：现有训练框架未解决MARL的系统级挑战，如同步障碍和资源利用不足
- 方法要点：采用解耦架构和微批次异步流水线，结合分层负载平衡与按需资源分配
- 实验或效果：在大型生产集群上实现最高7.3倍加速和5.6倍硬件利用率提升

## 摘要（原文）

> Despite algorithm-level innovations for multi-agent reinforcement learning (MARL), the underlying networked infrastructure for large-scale MARL training remains underexplored. Existing training frameworks primarily optimize for single-agent scenarios and fail to address the unique system-level challenges of MARL, including rollout-training synchronization barriers, rollout load imbalance, and training resource underutilization. To bridge this gap, we propose FlexMARL, the first end-to-end training framework that holistically optimizes rollout, training, and their orchestration for large-scale LLM-based MARL. Specifically, FlexMARL introduces the joint orchestrator to manage data flow under the rollout-training disaggregated architecture. Building upon the experience store, a novel micro-batch driven asynchronous pipeline eliminates the synchronization barriers while providing strong consistency guarantees. Rollout engine adopts a parallel sampling scheme combined with hierarchical load balancing, which adapts to skewed inter/intra-agent request patterns. Training engine achieves on-demand hardware binding through agent-centric resource allocation. The training states of different agents are swapped via unified and location-agnostic communication. Empirical results on a large-scale production cluster demonstrate that FlexMARL achieves up to 7.3x speedup and improves hardware utilization by up to 5.6x compared to existing frameworks.

