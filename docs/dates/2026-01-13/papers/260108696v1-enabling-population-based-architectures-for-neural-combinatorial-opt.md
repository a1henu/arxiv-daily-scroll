---
layout: default
title: Enabling Population-Based Architectures for Neural Combinatorial Optimization
---

# Enabling Population-Based Architectures for Neural Combinatorial Optimization
**arXiv**：[2601.08696v1](https://arxiv.org/abs/2601.08696) · [PDF](https://arxiv.org/pdf/2601.08696.pdf)  
**作者**：Andoni Irazusta Garmendia, Josu Ceberio, Alexander Mendiburu  

**一句话要点**：提出基于种群的神经组合优化架构，以增强学习方法的鲁棒性和探索能力。

**关键词**：神经组合优化, 种群架构, 元启发式, 强化学习, 多样化策略

## 3 点简述
- 核心问题：神经组合优化通常单解操作，缺乏种群结构，限制了性能提升。
- 方法要点：定义种群意识级别，设计神经网络表示种群并平衡强化与多样化。
- 实验或效果：在最大割和最大独立集问题上验证种群结构对学习优化方法的优势。

## 摘要（原文）

> Neural Combinatorial Optimization (NCO) has mostly focused on learning policies, typically neural networks, that operate on a single candidate solution at a time, either by constructing one from scratch or iteratively improving it. In contrast, decades of work in metaheuristics have shown that maintaining and evolving populations of solutions improves robustness and exploration, and often leads to stronger performance. To close this gap, we study how to make NCO explicitly population-based by learning policies that act on sets of candidate solutions. We first propose a simple taxonomy of population awareness levels and use it to highlight two key design challenges: (i) how to represent a whole population inside a neural network, and (ii) how to learn population dynamics that balance intensification (generating good solutions) and diversification (maintaining variety). We make these ideas concrete with two complementary tools: one that improves existing solutions using information shared across the whole population, and the other generates new candidate solutions that explicitly balance being high-quality with diversity. Experimental results on Maximum Cut and Maximum Independent Set indicate that incorporating population structure is advantageous for learned optimization methods and opens new connections between NCO and classical population-based search.

