---
layout: default
title: From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning
---

# From Absolute to Relative: Rethinking Reward Shaping in Group-Based Reinforcement Learning
**arXiv**：[2601.23058v1](https://arxiv.org/abs/2601.23058) · [PDF](https://arxiv.org/pdf/2601.23058.pdf)  
**作者**：Wenzhe Niu, Wei He, Zongxia Xie, Jinpeng Ou, Huichuan Fan, Yuchen Ge, Yanru Sun, Ziyin Wang, Yizhao Sun, Chengshun Shi, Jiuchong Gao, Jinghua Hao, Renqing He  

**一句话要点**：提出RLRR框架，通过相对奖励解决基于群体的强化学习中的奖励稀疏与不稳定问题。

**关键词**：强化学习, 奖励塑造, 相对排名, 群体优化, 推理增强, 开放生成

## 3 点简述
- 核心问题：基于群体的强化学习依赖绝对奖励，导致监督稀疏和奖励模型分数范围不稳定。
- 方法要点：引入RLRR框架，将奖励塑造从绝对评分转向相对排名，并设计Ranking Reward Model生成相对信号。
- 实验或效果：在推理基准和开放生成任务中，RLRR相比基线方法带来一致性能提升。

## 摘要（原文）

> Reinforcement learning has become a cornerstone for enhancing the reasoning capabilities of Large Language Models, where group-based approaches such as GRPO have emerged as efficient paradigms that optimize policies by leveraging intra-group performance differences. However, these methods typically rely on absolute numerical rewards, introducing intrinsic limitations. In verifiable tasks, identical group evaluations often result in sparse supervision, while in open-ended scenarios, the score range instability of reward models undermines advantage estimation based on group means. To address these limitations, we propose Reinforcement Learning with Relative Rewards (RLRR), a framework that shifts reward shaping from absolute scoring to relative ranking. Complementing this framework, we introduce the Ranking Reward Model, a listwise preference model tailored for group-based optimization to directly generate relative rankings. By transforming raw evaluations into robust relative signals, RLRR effectively mitigates signal sparsity and reward instability. Experimental results demonstrate that RLRR yields consistent performance improvements over standard group-based baselines across reasoning benchmarks and open-ended generation tasks.

