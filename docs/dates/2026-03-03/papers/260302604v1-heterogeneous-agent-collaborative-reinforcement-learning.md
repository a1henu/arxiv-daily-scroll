---
layout: default
title: Heterogeneous Agent Collaborative Reinforcement Learning
---

# Heterogeneous Agent Collaborative Reinforcement Learning
**arXiv**：[2603.02604v1](https://arxiv.org/abs/2603.02604) · [PDF](https://arxiv.org/pdf/2603.02604.pdf)  
**作者**：Zhixia Zhang, Zixuan Huang, Xin Xia, Deqing Wang, Fuzhen Zhuang, Shuai Ma, Ning Ding, Yaodong Yang, Jianxin Li, Yikun Ban  

**一句话要点**：提出异构智能体协同强化学习以解决孤立策略优化的低效问题

**关键词**：异构智能体强化学习, 协同优化, 轨迹共享, 知识转移, 策略分布偏移, 样本效率

## 3 点简述
- 核心问题：异构智能体在训练中孤立优化导致样本利用率低和知识转移不足
- 方法要点：通过验证的轨迹共享实现双向协同学习，无需推理时协调部署
- 实验或效果：在多样异构模型组合上，HACPO平均性能提升3.3%，且仅需一半轨迹成本

## 摘要（原文）

> We introduce Heterogeneous Agent Collaborative Reinforcement Learning (HACRL), a new learning paradigm that addresses the inefficiencies of isolated on-policy optimization. HACRL enables collaborative optimization with independent execution: heterogeneous agents share verified rollouts during training to mutually improve, while operating independently at inference time. Unlike LLM-based multi-agent reinforcement learning (MARL), HACRL does not require coordinated deployment, and unlike on-/off-policy distillation, it enables bidirectional mutual learning among heterogeneous agents rather than one-directional teacher-to-student transfer. Building on this paradigm, we propose HACPO, a collaborative RL algorithm that enables principled rollout sharing to maximize sample utilization and cross-agent knowledge transfer. To mitigate capability discrepancies and policy distribution shifts, HACPO introduces four tailored mechanisms with theoretical guarantees on unbiased advantage estimation and optimization correctness. Extensive experiments across diverse heterogeneous model combinations and reasoning benchmarks show that HACPO consistently improves all participating agents, outperforming GSPO by an average of 3.3\% while using only half the rollout cost.

