---
layout: default
title: A Relative-Budget Theory for Reinforcement Learning with Verifiable Rewards in Large Language Model Reasoning
---

# A Relative-Budget Theory for Reinforcement Learning with Verifiable Rewards in Large Language Model Reasoning
**arXiv**：[2602.01523v1](https://arxiv.org/abs/2602.01523) · [PDF](https://arxiv.org/pdf/2602.01523.pdf)  
**作者**：Akifumi Wachi, Hirota Kinoshita, Shokichi Takakura, Rei Higuchi, Taiji Suzuki  

**一句话要点**：提出相对预算理论以解释大语言模型推理中强化学习效率随计算预算的变化

**关键词**：强化学习, 大语言模型推理, 相对预算理论, 样本效率, 计算预算优化, 在线学习保证

## 3 点简述
- 核心问题：强化学习在大语言模型推理中效率随任务和计算预算变化，缺乏统一理论解释
- 方法要点：引入相对预算ξ=H/𝔼[T]作为单一量，分析其控制奖励方差和信息轨迹概率，划分三种学习机制
- 实验或效果：理论预测在实证中验证，识别ξ∈[1.5,2.0]为最大化学习效率和推理性能的预算范围

## 摘要（原文）

> Reinforcement learning (RL) is a dominant paradigm for improving the reasoning abilities of large language models, yet its effectiveness varies across tasks and compute budgets. We propose a \emph{relative-budget} theory explaining this variation through a single quantity called relative budget $ξ:= H/\mathbb{E}[T]$, where $H$ is the generation horizon (token budget) and $T$ denotes the number of tokens until the first correct solution under a base policy. We show that $ξ$ determines sample efficiency by controlling reward variance and the likelihood of informative trajectories. Our analysis reveals three regimes: in the \emph{deficient} regime ($ξ\to 0$), informative trajectories are rare and the sample complexity explodes; in the \emph{balanced} regime ($ξ=Θ(1)$), informative trajectories occur with non-negligible probability and RL is maximally sample-efficient; and in the \emph{ample} regime ($ξ\to \infty$), learning remains stable but marginal gains per iteration diminish. We further provide finite-sample guarantees for online RL that characterize learning progress across these regimes. Specifically, in a case study under idealized distributional assumptions, we show that the relative budget grows linearly over iterations. Our empirical results confirm these predictions in realistic settings, identifying a budget $ξ\in [1.5, 2.0]$ that maximizes learning efficiency and coincides with peak reasoning performance.

