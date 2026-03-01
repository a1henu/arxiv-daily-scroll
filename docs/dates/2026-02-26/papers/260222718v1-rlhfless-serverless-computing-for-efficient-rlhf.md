---
layout: default
title: RLHFless: Serverless Computing for Efficient RLHF
---

# RLHFless: Serverless Computing for Efficient RLHF
**arXiv**：[2602.22718v1](https://arxiv.org/abs/2602.22718) · [PDF](https://arxiv.org/pdf/2602.22718.pdf)  
**作者**：Rui Wei, Hanfei Yu, Shubham Jain, Yogarajan Sivakumar, Devesh Tiwari, Jian Li, Seung-Jong Park, Hao Wang  

**一句话要点**：提出RLHFless框架，基于无服务器计算优化同步RLHF训练效率

**关键词**：强化学习人类反馈, 无服务器计算, 训练效率优化, 同步训练框架, 资源动态管理

## 3 点简述
- 核心问题：同步RLHF训练中资源需求动态变化，传统服务器基础设施导致空闲时间和资源浪费
- 方法要点：采用无服务器计算适应动态资源需求，预计算共享前缀避免重复计算，成本感知的actor缩放策略优化响应长度变化
- 实验或效果：在物理测试床和大规模模拟集群上，相比最先进基线，实现最高1.35倍加速和44.8%成本降低

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) has been widely applied to Large Language Model (LLM) post-training to align model outputs with human preferences. Recent models, such as DeepSeek-R1, have also shown RLHF's potential to improve LLM reasoning on complex tasks. In RL, inference and training co-exist, creating dynamic resource demands throughout the workflow. Compared to traditional RL, RLHF further challenges training efficiency due to expanding model sizes and resource consumption. Several RLHF frameworks aim to balance flexible abstraction and efficient execution. However, they rely on serverful infrastructures, which struggle with fine-grained resource variability. As a result, during synchronous RLHF training, idle time between or within RL components often causes overhead and resource wastage.
>   To address these issues, we present RLHFless, the first scalable training framework for synchronous RLHF, built on serverless computing environments. RLHFless adapts to dynamic resource demands throughout the RLHF pipeline, pre-computes shared prefixes to avoid repeated computation, and uses a cost-aware actor scaling strategy that accounts for response length variation to find sweet spots with lower cost and higher speed. In addition, RLHFless assigns workloads efficiently to reduce intra-function imbalance and idle time. Experiments on both physical testbeds and a large-scale simulated cluster show that RLHFless achieves up to 1.35x speedup and 44.8% cost reduction compared to the state-of-the-art baseline.

