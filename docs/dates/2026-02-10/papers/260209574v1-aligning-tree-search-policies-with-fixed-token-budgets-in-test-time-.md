---
layout: default
title: Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs
---

# Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs
**arXiv**：[2602.09574v1](https://arxiv.org/abs/2602.09574) · [PDF](https://arxiv.org/pdf/2602.09574.pdf)  
**作者**：Sora Miyamoto, Daisuke Oba, Naoaki Okazaki  

**一句话要点**：提出预算引导MCTS以在固定令牌预算下优化LLM树搜索解码

**关键词**：树搜索解码, 测试时扩展, 令牌预算, 蒙特卡洛树搜索, 大型语言模型

## 3 点简述
- 核心问题：现有树搜索策略忽略固定令牌预算，导致过度分支或提前终止
- 方法要点：BG-MCTS根据剩余预算动态调整搜索策略，从广泛探索转向精炼和答案完成
- 实验或效果：在MATH500和AIME24/25数据集上，BG-MCTS在不同预算下均优于基线

## 摘要（原文）

> Tree-search decoding is an effective form of test-time scaling for large language models (LLMs), but real-world deployment imposes a fixed per-query token budget that varies across settings. Existing tree-search policies are largely budget-agnostic, treating the budget as a termination condition, which can lead to late-stage over-branching or premature termination. We propose {Budget-Guided MCTS} (BG-MCTS), a tree-search decoding algorithm that aligns its search policy with the remaining token budget: it starts with broad exploration, then prioritizes refinement and answer completion as the budget depletes while reducing late-stage branching from shallow nodes. BG-MCTS consistently outperforms budget-agnostic tree-search baselines across different budgets on MATH500 and AIME24/25 with open-weight LLMs.

