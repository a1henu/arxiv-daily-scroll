---
layout: default
title: Partial Policy Gradients for RL in LLMs
---

# Partial Policy Gradients for RL in LLMs
**arXiv**：[2603.06138v1](https://arxiv.org/abs/2603.06138) · [PDF](https://arxiv.org/pdf/2603.06138.pdf)  
**作者**：Puneet Mathur, Branislav Kveton, Subhojyoti Mukherjee, Viet Dac Lai  

**一句话要点**：提出部分策略梯度方法以优化大型语言模型中的强化学习策略结构。

**关键词**：强化学习, 策略梯度, 大型语言模型, 策略结构, 对话对齐, 奖励优化

## 3 点简述
- 核心问题：强化学习中策略梯度方法在未知环境下的策略结构建模与优化。
- 方法要点：通过优化未来奖励子集来简化策略，提高梯度估计准确性，支持多种策略类建模。
- 实验或效果：在多人设对齐对话问题上实证评估，不同策略在不同问题中表现优异。

## 摘要（原文）

> Reinforcement learning is a framework for learning to act sequentially in an unknown environment. We propose a natural approach for modeling policy structure in policy gradients. The key idea is to optimize for a subset of future rewards: smaller subsets represent simpler policies, which can be learned more reliably because their empirical gradient estimates are more accurate. Our approach allows for modeling and comparison of different policy classes, including full planning, greedy, K-step lookahead, and segment policies. We evaluate the policies empirically on multiple persona-alignment conversational problems. Different policies excel in different problems, reflecting their different characteristics and highlighting the importance of our studied policy class.

