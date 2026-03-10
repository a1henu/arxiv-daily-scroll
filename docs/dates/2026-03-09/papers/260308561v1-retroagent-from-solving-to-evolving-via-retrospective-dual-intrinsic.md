---
layout: default
title: RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
---

# RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
**arXiv**：[2603.08561v1](https://arxiv.org/abs/2603.08561) · [PDF](https://arxiv.org/pdf/2603.08561.pdf)  
**作者**：Xiaoying Zhang, Zichen Liu, Yipeng Zhang, Xia Hu, Wenqi Shao  

**一句话要点**：提出RetroAgent框架，通过回顾性双内在反馈解决LLM智能体在复杂交互任务中探索不足与经验利用受限的问题。

**关键词**：强化学习智能体, 内在反馈机制, 经验记忆检索, 在线学习框架, 复杂交互任务

## 3 点简述
- 核心问题：标准强化学习范式导致智能体探索不足、知识隐式存储，限制持续适应与经验学习。
- 方法要点：引入回顾性自我反思机制，生成数值和语言双内在反馈，结合SimUtil-UCB策略优化经验检索与利用。
- 实验或效果：在四个挑战性任务上显著超越现有方法，如ALFWorld提升18.3%，并展示强测试时适应与泛化能力。

## 摘要（原文）

> Large language model (LLM)-based agents trained with reinforcement learning (RL) have shown strong potential on complex interactive tasks. However, standard RL paradigms favor static problem-solving over continuous adaptation: agents often converge to suboptimal strategies due to insufficient exploration, while learned knowledge remains implicit within parameters rather than explicitly retrievable, limiting effective experiential learning. To address these limitations, we introduce RetroAgent, an online RL framework that empowers agents to master complex interactive environments not just by solving, but by evolving. Concretely, RetroAgent features a hindsight self-reflection mechanism that produces dual intrinsic feedback: (1) intrinsic numerical feedback that that tracks incremental subtask completion relative to prior attempts, rewarding promising explorations, and (2) intrinsic language feedback that distills reusable lessons into a memory buffer, retrieved via our proposed Similarity & Utility-Aware Upper Confidence Bound (SimUtil-UCB) strategy balancing relevance, utility, and exploration to effectively leverage past experiences. Extensive experiments on two model families across four challenging agentic tasks demonstrate that RetroAgent significantly outperforms existing methods, achieving state-of-the-art results -- e.g., surpassing Group Relative Policy Optimization (GRPO)-trained agents by +18.3% on ALFWorld, +15.4% on WebShop, +27.1% on Sokoban, and +8.9% on MineSweeper -- while exhibiting strong test-time adaptation and generalization to out-of-distribution scenarios.

