---
layout: default
title: Alpha Discovery via Grammar-Guided Learning and Search
---

# Alpha Discovery via Grammar-Guided Learning and Search
**arXiv**：[2601.22119v1](https://arxiv.org/abs/2601.22119) · [PDF](https://arxiv.org/pdf/2601.22119.pdf)  
**作者**：Han Yang, Dong Hao, Zhuohan Wang, Qi Shi, Xingtong Li  

**一句话要点**：提出AlphaCFG框架，通过语法引导学习和搜索自动发现量化金融中的公式化alpha因子。

**关键词**：量化金融, alpha因子发现, 语法引导学习, 蒙特卡洛树搜索, 符号因子发现

## 3 点简述
- 核心问题：现有方法在无结构空间中搜索alpha因子，忽略语法和语义约束。
- 方法要点：基于上下文无关语法定义树状搜索空间，采用语法感知的蒙特卡洛树搜索求解。
- 实验效果：在中美股市数据集上，AlphaCFG在搜索效率和交易盈利性上优于基线方法。

## 摘要（原文）

> Automatically discovering formulaic alpha factors is a central problem in quantitative finance. Existing methods often ignore syntactic and semantic constraints, relying on exhaustive search over unstructured and unbounded spaces. We present AlphaCFG, a grammar-based framework for defining and discovering alpha factors that are syntactically valid, financially interpretable, and computationally efficient. AlphaCFG uses an alpha-oriented context-free grammar to define a tree-structured, size-controlled search space, and formulates alpha discovery as a tree-structured linguistic Markov decision process, which is then solved using a grammar-aware Monte Carlo Tree Search guided by syntax-sensitive value and policy networks. Experiments on Chinese and U.S. stock market datasets show that AlphaCFG outperforms state-of-the-art baselines in both search efficiency and trading profitability. Beyond trading strategies, AlphaCFG serves as a general framework for symbolic factor discovery and refinement across quantitative finance, including asset pricing and portfolio construction.

