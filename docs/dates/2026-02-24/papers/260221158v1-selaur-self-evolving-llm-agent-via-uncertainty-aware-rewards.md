---
layout: default
title: SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards
---

# SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards
**arXiv**：[2602.21158v1](https://arxiv.org/abs/2602.21158) · [PDF](https://arxiv.org/pdf/2602.21158.pdf)  
**作者**：Dengjia Zhang, Xiaoou Liu, Lu Cheng, Yaqing Wang, Kenton Murray, Hua Wei  

**一句话要点**：提出SELAUR框架，通过不确定性感知奖励提升LLM多步决策代理的学习效果。

**关键词**：大语言模型代理, 不确定性估计, 强化学习, 奖励设计, 多步决策, 探索效率

## 3 点简述
- 核心问题：LLM作为多步决策代理时，其内在不确定性信号在奖励设计中常被忽视。
- 方法要点：集成熵、最小置信度和边距指标，构建令牌级不确定性估计，并用于重塑失败感知的奖励。
- 实验或效果：在ALFWorld和WebShop基准测试中，成功率优于基线，不确定性信号增强探索和鲁棒性。

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed as multi-step decision-making agents, where effective reward design is essential for guiding learning. Although recent work explores various forms of reward shaping and step-level credit assignment, a key signal remains largely overlooked: the intrinsic uncertainty of LLMs. Uncertainty reflects model confidence, reveals where exploration is needed, and offers valuable learning cues even in failed trajectories. We introduce SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards, a reinforcement learning framework that incorporates uncertainty directly into the reward design. SELAUR integrates entropy-, least-confidence-, and margin-based metrics into a combined token-level uncertainty estimate, providing dense confidence-aligned supervision, and employs a failure-aware reward reshaping mechanism that injects these uncertainty signals into step- and trajectory-level rewards to improve exploration efficiency and learning stability. Experiments on two benchmarks, ALFWorld and WebShop, show that our method consistently improves success rates over strong baselines. Ablation studies further demonstrate how uncertainty signals enhance exploration and robustness.

