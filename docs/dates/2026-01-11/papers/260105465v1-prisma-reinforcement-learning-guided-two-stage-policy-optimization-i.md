---
layout: default
title: PRISMA: Reinforcement Learning Guided Two-Stage Policy Optimization in Multi-Agent Architecture for Open-Domain Multi-Hop Question Answering
---

# PRISMA: Reinforcement Learning Guided Two-Stage Policy Optimization in Multi-Agent Architecture for Open-Domain Multi-Hop Question Answering
**arXiv**：[2601.05465v1](https://arxiv.org/abs/2601.05465) · [PDF](https://arxiv.org/pdf/2601.05465.pdf)  
**作者**：Yu Liu, Wenxiao Zhang, Cong Cao, Wenxuan Lu, Fangfang Yuan, Diandian Guo, Kun Peng, Qiang Sun, Kaiyan Zhang, Yanbing Liu, Jin B. Hong, Bowen Zhou, Zhiyuan Ma  

**一句话要点**：提出PRISMA框架以解决开放域多跳问答中的检索崩溃和学习不稳定问题

**关键词**：多智能体架构, 强化学习优化, 开放域问答, 检索增强生成, 多跳推理, 策略优化

## 3 点简述
- 核心问题：大规模语料库迭代检索易崩溃，端到端训练存在学习不稳定和迁移性差
- 方法要点：采用解耦的Plan-Retrieve-Inspect-Solve-Memoize架构，通过两阶段GRPO优化智能体协作
- 实验效果：在十个基准测试中达到最优性能，并能高效部署于实际场景

## 摘要（原文）

> Answering real-world open-domain multi-hop questions over massive corpora is a critical challenge in Retrieval-Augmented Generation (RAG) systems. Recent research employs reinforcement learning (RL) to end-to-end optimize the retrieval-augmented reasoning process, directly enhancing its capacity to resolve complex queries. However, reliable deployment is hindered by two obstacles. 1) Retrieval Collapse: iterative retrieval over large corpora fails to locate intermediate evidence containing bridge answers without reasoning-guided planning, causing downstream reasoning to collapse. 2) Learning Instability: end-to-end trajectory training suffers from weak credit assignment across reasoning chains and poor error localization across modules, causing overfitting to benchmark-specific heuristics that limit transferability and stability. To address these problems, we propose PRISMA, a decoupled RL-guided framework featuring a Plan-Retrieve-Inspect-Solve-Memoize architecture. PRISMA's strength lies in reasoning-guided collaboration: the Inspector provides reasoning-based feedback to refine the Planner's decomposition and fine-grained retrieval, while enforcing evidence-grounded reasoning in the Solver. We optimize individual agent capabilities via Two-Stage Group Relative Policy Optimization (GRPO). Stage I calibrates the Planner and Solver as specialized experts in planning and reasoning, while Stage II utilizes Observation-Aware Residual Policy Optimization (OARPO) to enhance the Inspector's ability to verify context and trigger targeted recovery. Experiments show that PRISMA achieves state-of-the-art performance on ten benchmarks and can be deployed efficiently in real-world scenarios.

