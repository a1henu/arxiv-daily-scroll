---
layout: default
title: Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models
---

# Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models
**arXiv**：[2602.12586v1](https://arxiv.org/abs/2602.12586) · [PDF](https://arxiv.org/pdf/2602.12586.pdf)  
**作者**：Joshua Ong Jun Leang, Yu Zhao, Mihaela Cătălina Stoian, Wenda Li, Shay B. Cohen, Eleonora Giunchiglia  

**一句话要点**：提出McDiffuSE框架，利用蒙特卡洛树搜索优化掩码扩散模型中的槽填充顺序以提升生成质量

**关键词**：掩码扩散模型, 蒙特卡洛树搜索, 槽填充顺序优化, 规划和填充解码, 生成质量提升, 数学代码推理

## 3 点简述
- 核心问题：掩码扩散模型在规划和填充解码中，槽填充顺序敏感导致输出方差大，影响数学和代码推理性能。
- 方法要点：将槽选择建模为决策过程，通过蒙特卡洛树搜索进行前瞻模拟，系统探索生成顺序的组合空间以优化填充顺序。
- 实验效果：在MBPP和MATH500等数据集上平均提升3.2%至8.0%，分析显示非顺序生成和较大探索常数对克服模型置信偏差至关重要。

## 摘要（原文）

> While plan-and-infill decoding in Masked Diffusion Models (MDMs) shows promise for mathematical and code reasoning, performance remains highly sensitive to slot infilling order, often yielding substantial output variance. We introduce McDiffuSE, a framework that formulates slot selection as decision making and optimises infilling orders through Monte Carlo Tree Search (MCTS). McDiffuSE uses look-ahead simulations to evaluate partial completions before commitment, systematically exploring the combinatorial space of generation orders. Experiments show an average improvement of 3.2% over autoregressive baselines and 8.0% over baseline plan-and-infill, with notable gains of 19.5% on MBPP and 4.9% on MATH500. Our analysis reveals that while McDiffuSE predominantly follows sequential ordering, incorporating non-sequential generation is essential for maximising performance. We observe that larger exploration constants, rather than increased simulations, are necessary to overcome model confidence biases and discover effective orderings. These findings establish MCTS-based planning as an effective approach for enhancing generation quality in MDMs.

