---
layout: default
title: POPE: Learning to Reason on Hard Problems via Privileged On-Policy Exploration
---

# POPE: Learning to Reason on Hard Problems via Privileged On-Policy Exploration
**arXiv**：[2601.18779v1](https://arxiv.org/abs/2601.18779) · [PDF](https://arxiv.org/pdf/2601.18779.pdf)  
**作者**：Yuxiao Qu, Amrith Setlur, Virginia Smith, Ruslan Salakhutdinov, Aviral Kumar  

**一句话要点**：提出POPE方法，利用特权信息引导强化学习在难题上的探索以提升推理能力

**关键词**：强化学习, 大语言模型推理, 特权信息引导, 探索策略, 难题求解

## 3 点简述
- 核心问题：强化学习在难题上探索失败，导致零奖励和无学习信号，传统方法如熵奖励或混合训练无效
- 方法要点：POPE通过添加特权解决方案前缀引导探索，使RL获得非零奖励，并利用指令跟随与推理的协同实现行为迁移
- 实验或效果：POPE扩展了可解问题集，在挑战性推理基准上显著提升性能

## 摘要（原文）

> Reinforcement learning (RL) has improved the reasoning abilities of large language models (LLMs), yet state-of-the-art methods still fail to learn on many training problems. On hard problems, on-policy RL rarely explores even a single correct rollout, yielding zero reward and no learning signal for driving improvement. We find that natural solutions to remedy this exploration problem from classical RL, such as entropy bonuses, more permissive clipping of the importance ratio, or direct optimization of pass@k objectives, do not resolve this issue and often destabilize optimization without improving solvability. A natural alternative is to leverage transfer from easier problems. However, we show that mixing easy and hard problems during RL training is counterproductive due to ray interference, where optimization focuses on already-solvable problems in a way that actively inhibits progress on harder ones. To address this challenge, we introduce Privileged On-Policy Exploration (POPE), an approach that leverages human- or other oracle solutions as privileged information to guide exploration on hard problems, unlike methods that use oracle solutions as training targets (e.g., off-policy RL methods or warmstarting from SFT). POPE augments hard problems with prefixes of oracle solutions, enabling RL to obtain non-zero rewards during guided rollouts. Crucially, the resulting behaviors transfer back to the original, unguided problems through a synergy between instruction-following and reasoning. Empirically, POPE expands the set of solvable problems and substantially improves performance on challenging reasoning benchmarks.

