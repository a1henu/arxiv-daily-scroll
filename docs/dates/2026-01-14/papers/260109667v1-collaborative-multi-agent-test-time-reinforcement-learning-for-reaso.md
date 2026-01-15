---
layout: default
title: Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning
---

# Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning
**arXiv**：[2601.09667v1](https://arxiv.org/abs/2601.09667) · [PDF](https://arxiv.org/pdf/2601.09667.pdf)  
**作者**：Zhiyuan Hu, Yunhai Hu, Juncheng Liu, Shuyue Stella Li, Yucheng Wang, Zhen Xu, See-Kiong Ng, Anh Tuan Luu, Xinxing Xu, Bryan Hooi, Cynthia Breazeal, Hae Won Park  

**一句话要点**：提出多智能体测试时强化学习框架，以增强推理任务中的分布偏移鲁棒性。

**关键词**：多智能体系统, 测试时强化学习, 推理任务, 经验检索, 共识决策, 分布偏移鲁棒性

## 3 点简述
- 核心问题：多智能体强化学习训练资源密集且不稳定，奖励稀疏且高方差。
- 方法要点：在推理时注入结构化文本经验，通过多专家团队检索、整合经验并达成共识决策。
- 实验或效果：在医学、数学和教育基准上，平均准确率提升3.67%优于多智能体基线，8.67%优于单智能体基线。

## 摘要（原文）

> Multi-agent systems have evolved into practical LLM-driven collaborators for many applications, gaining robustness from diversity and cross-checking. However, multi-agent RL (MARL) training is resource-intensive and unstable: co-adapting teammates induce non-stationarity, and rewards are often sparse and high-variance. Therefore, we introduce \textbf{Multi-Agent Test-Time Reinforcement Learning (MATTRL)}, a framework that injects structured textual experience into multi-agent deliberation at inference time. MATTRL forms a multi-expert team of specialists for multi-turn discussions, retrieves and integrates test-time experiences, and reaches consensus for final decision-making. We also study credit assignment for constructing a turn-level experience pool, then reinjecting it into the dialogue. Across challenging benchmarks in medicine, math, and education, MATTRL improves accuracy by an average of 3.67\% over a multi-agent baseline, and by 8.67\% over comparable single-agent baselines. Ablation studies examine different credit-assignment schemes and provide a detailed comparison of how they affect training outcomes. MATTRL offers a stable, effective and efficient path to distribution-shift-robust multi-agent reasoning without tuning.

