---
layout: default
title: Escaping the Verifier: Learning to Reason via Demonstrations
---

# Escaping the Verifier: Learning to Reason via Demonstrations
**arXiv**：[2511.21667v1](https://arxiv.org/abs/2511.21667) · [PDF](https://arxiv.org/pdf/2511.21667.pdf)  
**作者**：Locke Cai, Ivan Provilkov  

**一句话要点**：提出RARO方法，从专家演示中学习推理能力，无需任务特定验证器。

**关键词**：逆强化学习, 对抗训练, 推理优化, 专家演示, 语言模型训练

## 3 点简述
- 核心问题：许多推理任务缺乏验证器，但专家演示未被充分利用。
- 方法要点：通过对抗性交互，策略模仿专家答案，批评者区分策略与专家。
- 实验效果：在Countdown等任务上超越基线，展示稳健扩展趋势。

## 摘要（原文）

> Training Large Language Models (LLMs) to reason often relies on Reinforcement Learning (RL) with task-specific verifiers. However, many real-world reasoning-intensive tasks lack verifiers, despite offering abundant expert demonstrations that remain under-utilized for reasoning-focused training. We introduce RARO (Relativistic Adversarial Reasoning Optimization) that learns strong reasoning capabilities from only expert demonstrations via Inverse Reinforcement Learning. Our method sets up an adversarial interaction between a policy (generator) and a relativistic critic (discriminator): the policy learns to mimic expert answers, while the critic learns to compare and distinguish between policy and expert answers. Our method trains both the policy and the critic jointly and continuously via RL, and we identify the key stabilization techniques required for robust learning. Empirically, RARO significantly outperforms strong verifier-free baselines on all of our evaluation tasks -- Countdown, DeepMath, and Poetry Writing -- and enjoys the same robust scaling trends as RL on verifiable tasks. These results demonstrate that our method effectively elicits strong reasoning performance from expert demonstrations alone, enabling robust reasoning learning even when task-specific verifiers are unavailable.

