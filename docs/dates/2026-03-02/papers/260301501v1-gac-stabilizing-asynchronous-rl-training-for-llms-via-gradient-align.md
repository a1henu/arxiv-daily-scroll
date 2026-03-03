---
layout: default
title: GAC: Stabilizing Asynchronous RL Training for LLMs via Gradient Alignment Control
---

# GAC: Stabilizing Asynchronous RL Training for LLMs via Gradient Alignment Control
**arXiv**：[2603.01501v1](https://arxiv.org/abs/2603.01501) · [PDF](https://arxiv.org/pdf/2603.01501.pdf)  
**作者**：Haofeng Xu, Junwei Su, Yukun Tian, Lansong Diao, Zhengping Qian, Chuan Wu  

**一句话要点**：提出GAC方法以稳定大语言模型异步强化学习训练

**关键词**：异步强化学习, 梯度对齐控制, 训练稳定性, 大语言模型, 策略梯度

## 3 点简述
- 异步训练导致策略梯度高余弦相似度，引发训练不稳定
- GAC通过梯度投影控制陈旧对齐方向，稳定训练动态
- 理论保证收敛，实验匹配同步基线，支持高陈旧度

## 摘要（原文）

> Asynchronous execution is essential for scaling reinforcement learning (RL) to modern large model workloads, including large language models and AI agents, but it can fundamentally alter RL optimization behavior. While prior work on asynchronous RL focuses on training throughput and distributional correction, we show that naively applying asynchrony to policy-gradient updates can induce qualitatively different training dynamics and lead to severe training instability. Through systematic empirical and theoretical analysis, we identify a key signature of this instability: asynchronous training exhibits persistently high cosine similarity between consecutive policy gradients, in contrast to the near-orthogonal updates observed under synchronized training. This stale-aligned gradient effect amplifies correlated updates and increases the risk of overshooting and divergence. Motivated by this observation, we propose GRADIENT ALIGNMENT CONTROL(GAC), a simple dynamics-aware stabilization method that regulates asynchronous RL progress along stale-aligned directions via gradient projection. We establish convergence guarantees under bounded staleness and demonstrate empirically that GAC recovers stable, on-policy training dynamics and matches synchronized baselines even at high staleness.

