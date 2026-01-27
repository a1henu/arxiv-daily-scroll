---
layout: default
title: Reuse your FLOPs: Scaling RL on Hard Problems by Conditioning on Very Off-Policy Prefixes
---

# Reuse your FLOPs: Scaling RL on Hard Problems by Conditioning on Very Off-Policy Prefixes
**arXiv**：[2601.18795v1](https://arxiv.org/abs/2601.18795) · [PDF](https://arxiv.org/pdf/2601.18795.pdf)  
**作者**：Amrith Setlur, Zijian Wang, Andrew Cohen, Paria Rashidinejad, Sang Michael Xie  

**一句话要点**：提出PrefixRL以解决大语言模型强化学习中硬问题训练效率低下的问题

**关键词**：强化学习, 大语言模型推理, 离策略训练, 样本效率, 自改进循环, 条件化前缀

## 3 点简述
- 核心问题：传统强化学习方法在硬推理问题上因正确轨迹稀少导致梯度消失和训练停滞
- 方法要点：通过条件化成功离策略轨迹的前缀并运行在策略强化学习来避免离策略不稳定性
- 实验或效果：在硬推理任务上训练奖励提升3倍，速度加快2倍，并验证了跨模型泛化能力

## 摘要（原文）

> Typical reinforcement learning (RL) methods for LLM reasoning waste compute on hard problems, where correct on-policy traces are rare, policy gradients vanish, and learning stalls. To bootstrap more efficient RL, we consider reusing old sampling FLOPs (from prior inference or RL training) in the form of off-policy traces. Standard off-policy methods supervise against off-policy data, causing instabilities during RL optimization. We introduce PrefixRL, where we condition on the prefix of successful off-policy traces and run on-policy RL to complete them, side-stepping off-policy instabilities. PrefixRL boosts the learning signal on hard problems by modulating the difficulty of the problem through the off-policy prefix length. We prove that the PrefixRL objective is not only consistent with the standard RL objective but also more sample efficient. Empirically, we discover back-generalization: training only on prefixed problems generalizes to out-of-distribution unprefixed performance, with learned strategies often differing from those in the prefix. In our experiments, we source the off-policy traces by rejection sampling with the base model, creating a self-improvement loop. On hard reasoning problems, PrefixRL reaches the same training reward 2x faster than the strongest baseline (SFT on off-policy data then RL), even after accounting for the compute spent on the initial rejection sampling, and increases the final reward by 3x. The gains transfer to held-out benchmarks, and PrefixRL is still effective when off-policy traces are derived from a different model family, validating its flexibility in practical settings.

