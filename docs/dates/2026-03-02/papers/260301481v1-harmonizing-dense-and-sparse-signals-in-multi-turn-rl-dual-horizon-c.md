---
layout: default
title: Harmonizing Dense and Sparse Signals in Multi-turn RL: Dual-Horizon Credit Assignment for Industrial Sales Agents
---

# Harmonizing Dense and Sparse Signals in Multi-turn RL: Dual-Horizon Credit Assignment for Industrial Sales Agents
**arXiv**：[2603.01481v1](https://arxiv.org/abs/2603.01481) · [PDF](https://arxiv.org/pdf/2603.01481.pdf)  
**作者**：Haojin Yang, Ai Jian, Xinyue Huang, Yiwei Wang, Weipeng Zhang, Ke Zeng, Xunliang Cai, Jingqing Ruan  

**一句话要点**：提出双视野信用分配框架以解决工业销售代理中密集与稀疏信号不平衡问题

**关键词**：强化学习, 信用分配, 多轮对话, 工业销售代理, 语言模型优化, 奖励设计

## 3 点简述
- 核心问题：传统强化学习将长期商业目标与即时语言约束合并为单一奖励，导致会话级奖励压倒轮次级信号，引发训练不稳定或奖励黑客行为。
- 方法要点：引入双视野信用分配框架，通过视野无关优势归一化技术，分别归一化轮次级和会话级奖励的优势，确保策略更新中即时与长期目标的梯度贡献平衡。
- 实验或效果：在高保真用户模拟器上的实验显示，该框架优于GRPO基线，转化率相对提升6.82%，句子间重复率降低82.28%，身份检测率降低27.35%。

## 摘要（原文）

> Optimizing large language models for industrial sales requires balancing long-term commercial objectives (e.g., conversion rate) with immediate linguistic constraints such as fluency and compliance. Conventional reinforcement learning often merges these heterogeneous goals into a single reward, causing high-magnitude session-level rewards to overwhelm subtler turn-level signals, which leads to unstable training or reward hacking. To address this issue, we propose Dual-Horizon Credit Assignment (DuCA), a framework that disentangles optimization across time scales. Its core, Horizon-Independent Advantage Normalization (HIAN), separately normalizes advantages from turn-level and session-level rewards before fusion, ensuring balanced gradient contributions from both immediate and long-term objectives to the policy update. Extensive experiments with a high-fidelity user simulator show DuCA outperforms the state-of-the-art GRPO baseline, achieving a 6.82% relative improvement in conversion rate, reducing inter-sentence repetition by 82.28%, and lowering identity detection rate by 27.35%, indicating a substantial improvement for an industrial sales scenario that effectively balances the dual demands of strategic performance and naturalistic language generation.

