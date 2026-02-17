---
layout: default
title: Socially-Weighted Alignment: A Game-Theoretic Framework for Multi-Agent LLM Systems
---

# Socially-Weighted Alignment: A Game-Theoretic Framework for Multi-Agent LLM Systems
**arXiv**：[2602.14471v1](https://arxiv.org/abs/2602.14471) · [PDF](https://arxiv.org/pdf/2602.14471.pdf)  
**作者**：Furkan Mumcu, Yasin Yilmaz  

**一句话要点**：提出社会加权对齐框架，以解决多智能体LLM系统中个体对齐与集体稳定性的冲突。

**关键词**：多智能体系统, 大语言模型对齐, 博弈论框架, 推理时决策, 社会加权对齐, 拥堵游戏

## 3 点简述
- 核心问题：多智能体LLM在共享环境中，个体理性决策可能导致负外部性，损害系统性能。
- 方法要点：通过社会权重λ在私有目标与群体福利估计间插值，修改推理时决策，无需参数更新或多智能体强化学习。
- 实验或效果：在拥堵游戏中，理论推导临界阈值λ*，模拟验证从持续拥堵到稳定运行的相变行为。

## 摘要（原文）

> Deploying large language model (LLM) agents in shared environments introduces a fundamental tension between individual alignment and collective stability: locally rational decisions can impose negative externalities that degrade system-level performance. We propose Socially-Weighted Alignment (SWA), a game-theoretic framework that modifies inference-time decision making by interpolating between an agent's private objective and an estimate of group welfare via a social weight $λ\in[0,1]$. In a shared-resource congestion game with $n$ agents and congestion severity $β$, we show that SWA induces a critical threshold $λ^*=(n-β)/(n-1)$ above which agents no longer have marginal incentive to increase demand under overload, yielding a phase transition from persistent congestion to stable operation near capacity. We further provide an inference-time algorithmic instantiation of SWA that does not require parameter updates or multi-agent reinforcement learning, and use a multi-agent simulation to empirically validate the predicted threshold behavior.

