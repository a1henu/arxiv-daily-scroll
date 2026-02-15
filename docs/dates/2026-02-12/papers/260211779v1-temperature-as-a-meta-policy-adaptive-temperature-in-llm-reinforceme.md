---
layout: default
title: Temperature as a Meta-Policy: Adaptive Temperature in LLM Reinforcement Learning
---

# Temperature as a Meta-Policy: Adaptive Temperature in LLM Reinforcement Learning
**arXiv**：[2602.11779v1](https://arxiv.org/abs/2602.11779) · [PDF](https://arxiv.org/pdf/2602.11779.pdf)  
**作者**：Haoran Dang, Cuiling Lan, Hai Wan, Xibin Zhao, Yan Lu  

**一句话要点**：提出温度自适应元策略优化框架，将温度控制作为可学习的元策略，以解决大语言模型强化学习中探索与利用的动态平衡问题。

**关键词**：大语言模型强化学习, 温度控制, 元策略优化, 自适应探索, 数学推理基准

## 3 点简述
- 核心问题：静态或启发式温度调度在大语言模型强化学习中无法适应训练动态，限制策略改进。
- 方法要点：通过分层双循环框架，内环更新语言模型策略，外环基于高优势轨迹奖励更新温度分布，实现在线自适应。
- 实验或效果：在五个数学推理基准上优于固定或启发式温度基线，验证了温度作为可学习元策略的有效性。

## 摘要（原文）

> Temperature is a crucial hyperparameter in large language models (LLMs), controlling the trade-off between exploration and exploitation during text generation. High temperatures encourage diverse but noisy outputs, while low temperatures produce focused outputs but may cause premature convergence. Yet static or heuristic temperature schedules fail to adapt to the dynamic demands of reinforcement learning (RL) throughout training, often limiting policy improvement. We propose Temperature Adaptive Meta Policy Optimization (TAMPO), a new framework that recasts temperature control as a learnable meta-policy. TAMPO operates through a hierarchical two-loop process. In the inner loop, the LLM policy is updated (e.g., using GRPO) with trajectories sampled at the temperature selected by the meta-policy. In the outer loop, meta-policy updates the distribution over candidate temperatures by rewarding those that maximize the likelihood of high-advantage trajectories. This trajectory-guided, reward-driven mechanism enables online adaptation without additional rollouts, directly aligning exploration with policy improvement. On five mathematical reasoning benchmarks, TAMPO outperforms baselines using fixed or heuristic temperatures, establishing temperature as an effective learnable meta-policy for adaptive exploration in LLM reinforcement learning. Accepted at ICLR 2026.

