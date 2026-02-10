---
layout: default
title: iGRPO: Self-Feedback-Driven LLM Reasoning
---

# iGRPO: Self-Feedback-Driven LLM Reasoning
**arXiv**：[2602.09000v1](https://arxiv.org/abs/2602.09000) · [PDF](https://arxiv.org/pdf/2602.09000.pdf)  
**作者**：Ali Hatamizadeh, Shrimai Prabhumoye, Igor Gitman, Ximing Lu, Seungju Han, Wei Ping, Yejin Choi, Jan Kautz  

**一句话要点**：提出iGRPO以通过自反馈迭代优化LLM数学推理性能

**关键词**：大型语言模型, 强化学习, 数学推理, 策略优化, 自反馈机制, 迭代训练

## 3 点简述
- 核心问题：LLM在复杂数学问题中准确性和一致性不足，需强化学习对齐任务奖励。
- 方法要点：扩展GRPO为两阶段迭代优化，首阶段采样探索草稿并选最优，次阶段基于草稿进行GRPO式精炼更新。
- 实验或效果：在匹配预算下优于GRPO，应用于OpenReasoning-Nemotron-7B在AIME24和AIME25达到新SOTA结果。

## 摘要（原文）

> Large Language Models (LLMs) have shown promise in solving complex mathematical problems, yet they still fall short of producing accurate and consistent solutions. Reinforcement Learning (RL) is a framework for aligning these models with task-specific rewards, improving overall quality and reliability. Group Relative Policy Optimization (GRPO) is an efficient, value-function-free alternative to Proximal Policy Optimization (PPO) that leverages group-relative reward normalization. We introduce Iterative Group Relative Policy Optimization (iGRPO), a two-stage extension of GRPO that adds dynamic self-conditioning through model-generated drafts. In Stage 1, iGRPO samples multiple exploratory drafts and selects the highest-reward draft using the same scalar reward signal used for optimization. In Stage 2, it appends this best draft to the original prompt and applies a GRPO-style update on draft-conditioned refinements, training the policy to improve beyond its strongest prior attempt. Under matched rollout budgets, iGRPO consistently outperforms GRPO across base models (e.g., Nemotron-H-8B-Base-8K and DeepSeek-R1 Distilled), validating its effectiveness on diverse reasoning benchmarks. Moreover, applying iGRPO to OpenReasoning-Nemotron-7B trained on AceReason-Math achieves new state-of-the-art results of 85.62\% and 79.64\% on AIME24 and AIME25, respectively. Ablations further show that the refinement wrapper generalizes beyond GRPO variants, benefits from a generative judge, and alters learning dynamics by delaying entropy collapse. These results underscore the potential of iterative, self-feedback-based RL for advancing verifiable mathematical reasoning.

