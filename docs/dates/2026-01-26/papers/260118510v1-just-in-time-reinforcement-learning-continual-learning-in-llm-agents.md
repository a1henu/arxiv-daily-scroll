---
layout: default
title: Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates
---

# Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates
**arXiv**：[2601.18510v1](https://arxiv.org/abs/2601.18510) · [PDF](https://arxiv.org/pdf/2601.18510.pdf)  
**作者**：Yibo Li, Zijie Lin, Ailin Deng, Xuan Zhang, Yufei He, Shuo Ji, Tri Cao, Bryan Hooi  

**一句话要点**：提出JitRL框架，实现无需梯度更新的LLM智能体持续学习

**关键词**：持续学习, 强化学习, 大语言模型智能体, 训练无关优化, 动态记忆检索, 在线策略优化

## 3 点简述
- LLM智能体部署后权重冻结，难以持续适应新任务
- JitRL通过动态记忆检索轨迹，在线估计优势并调制输出logits
- 在WebArena和Jericho上超越训练无关方法，成本降低30倍以上

## 摘要（原文）

> While Large Language Model (LLM) agents excel at general tasks, they inherently struggle with continual adaptation due to the frozen weights after deployment. Conventional reinforcement learning (RL) offers a solution but incurs prohibitive computational costs and the risk of catastrophic forgetting. We introduce Just-In-Time Reinforcement Learning (JitRL), a training-free framework that enables test-time policy optimization without any gradient updates. JitRL maintains a dynamic, non-parametric memory of experiences and retrieves relevant trajectories to estimate action advantages on-the-fly. These estimates are then used to directly modulate the LLM's output logits. We theoretically prove that this additive update rule is the exact closed-form solution to the KL-constrained policy optimization objective. Extensive experiments on WebArena and Jericho demonstrate that JitRL establishes a new state-of-the-art among training-free methods. Crucially, JitRL outperforms the performance of computationally expensive fine-tuning methods (e.g., WebRL) while reducing monetary costs by over 30 times, offering a scalable path for continual learning agents. The code is available at https://github.com/liushiliushi/JitRL.

