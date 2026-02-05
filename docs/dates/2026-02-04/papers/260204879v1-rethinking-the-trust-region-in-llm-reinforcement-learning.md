---
layout: default
title: Rethinking the Trust Region in LLM Reinforcement Learning
---

# Rethinking the Trust Region in LLM Reinforcement Learning
**arXiv**：[2602.04879v1](https://arxiv.org/abs/2602.04879) · [PDF](https://arxiv.org/pdf/2602.04879.pdf)  
**作者**：Penghui Qi, Xiangxin Zhou, Zichen Liu, Tianyu Pang, Chao Du, Min Lin, Wee Sun Lee  

**一句话要点**：提出DPPO以解决PPO在大语言模型强化学习中因概率比裁剪导致的训练不稳定问题

**关键词**：强化学习, 大语言模型微调, 策略优化, 训练稳定性, 散度约束

## 3 点简述
- 核心问题：PPO的概率比裁剪机制在大词汇量下对低概率令牌过度惩罚，高概率令牌约束不足，导致训练低效和不稳定
- 方法要点：DPPO用基于策略散度（如总变差或KL散度）的直接估计替代启发式裁剪，并引入高效Binary和Top-K近似降低内存开销
- 实验或效果：实证评估显示DPPO在训练稳定性和效率上优于现有方法，为基于RL的LLM微调提供更稳健基础

## 摘要（原文）

> Reinforcement learning (RL) has become a cornerstone for fine-tuning Large Language Models (LLMs), with Proximal Policy Optimization (PPO) serving as the de facto standard algorithm. Despite its ubiquity, we argue that the core ratio clipping mechanism in PPO is structurally ill-suited for the large vocabularies inherent to LLMs. PPO constrains policy updates based on the probability ratio of sampled tokens, which serves as a noisy single-sample Monte Carlo estimate of the true policy divergence. This creates a sub-optimal learning dynamic: updates to low-probability tokens are aggressively over-penalized, while potentially catastrophic shifts in high-probability tokens are under-constrained, leading to training inefficiency and instability. To address this, we propose Divergence Proximal Policy Optimization (DPPO), which substitutes heuristic clipping with a more principled constraint based on a direct estimate of policy divergence (e.g., Total Variation or KL). To avoid huge memory footprint, we introduce the efficient Binary and Top-K approximations to capture the essential divergence with negligible overhead. Extensive empirical evaluations demonstrate that DPPO achieves superior training stability and efficiency compared to existing methods, offering a more robust foundation for RL-based LLM fine-tuning.

