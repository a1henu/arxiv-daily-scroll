---
layout: default
title: EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL
---

# EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL
**arXiv**：[2602.04417v1](https://arxiv.org/abs/2602.04417) · [PDF](https://arxiv.org/pdf/2602.04417.pdf)  
**作者**：Lunjun Zhang, Jimmy Ba  

**一句话要点**：提出EMA锚点和Top-k KL估计器以改进大语言模型的策略梯度强化学习

**关键词**：策略梯度, 大语言模型强化学习, 指数移动平均, KL散度估计, 数学推理, 代理任务

## 3 点简述
- 核心问题：策略梯度算法在大语言模型强化学习中存在稳定性与KL散度估计效率问题。
- 方法要点：使用指数移动平均锚点替代固定锚点，并引入Top-k KL估计器实现精确与采样KL的灵活插值。
- 实验效果：结合GRPO，在数学推理和代理任务上显著提升性能，如Qwen-1.5B在OlympiadBench达到53.9%。

## 摘要（原文）

> Reinforcement Learning (RL) has enabled Large Language Models (LLMs) to acquire increasingly complex reasoning and agentic behaviors. In this work, we propose two simple techniques to improve policy gradient algorithms for LLMs. First, we replace the fixed anchor policy during RL with an Exponential Moving Average (EMA), similar to a target network in deep Q-learning. Second, we introduce Top-k KL estimator, which allows for flexible interpolation between exact KL and sampled KL. We derive the stability conditions for using EMA anchor; moreover, we show that our Top-k KL estimator yields both unbiased KL values and unbiased gradients at any k, while bringing the benefits of exact KL. When combined with GRPO, the two techniques (EMA-PG) lead to a significant performance boost. On math reasoning, it allows R1-distilled Qwen-1.5B to reach 53.9% on OlympiadBench compared to 50.8% by GRPO. On agentic RL domains, with Qwen-3B base, EMA-PG improves GRPO by an average of 33.3% across 7 datasets of Q&A with search engines, including 29.7% $\rightarrow$ 44.1% on HotpotQA, 27.4% $\rightarrow$ 40.1% on 2WikiMultiHopQA. Overall, we show that EMA-PG is a simple, principled, and powerful approach to scaling RL for LLMs. Code: https://github.com/LunjunZhang/ema-pg

