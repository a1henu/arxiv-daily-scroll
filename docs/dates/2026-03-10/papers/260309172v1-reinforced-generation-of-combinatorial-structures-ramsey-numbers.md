---
layout: default
title: Reinforced Generation of Combinatorial Structures: Ramsey Numbers
---

# Reinforced Generation of Combinatorial Structures: Ramsey Numbers
**arXiv**：[2603.09172v1](https://arxiv.org/abs/2603.09172) · [PDF](https://arxiv.org/pdf/2603.09172.pdf)  
**作者**：Ansh Nagda, Prabhakar Raghavan, Abhradeep Thakurta  

**一句话要点**：提出AlphaEvolve基于LLM的代码突变代理，改进五个经典拉姆齐数的下界。

**关键词**：拉姆齐数, 组合结构生成, 代码突变, 大语言模型应用, 下界改进, 元算法

## 3 点简述
- 核心问题：计算拉姆齐数的下界，这是组合数学中的经典难题。
- 方法要点：使用AlphaEvolve，一个基于大语言模型的代码突变代理，作为单一元算法生成搜索算法。
- 实验或效果：成功提高五个拉姆齐数的下界，并恢复所有已知精确下界，匹配许多其他最佳已知下界。

## 摘要（原文）

> We present improved lower bounds for five classical Ramsey numbers: $\mathbf{R}(3, 13)$ is increased from $60$ to $61$, $\mathbf{R}(3, 18)$ from $99$ to $100$, $\mathbf{R}(4, 13)$ from $138$ to $139$, $\mathbf{R}(4, 14)$ from $147$ to $148$, and $\mathbf{R}(4, 15)$ from $158$ to $159$. These results were achieved using~\emph{AlphaEvolve}, an LLM-based code mutation agent. Beyond these new results, we successfully recovered lower bounds for all Ramsey numbers known to be exact, and matched the best known lower bounds across many other cases. These include bounds for which previous work does not detail the algorithms used. Virtually all known Ramsey lower bounds are derived computationally, with bespoke search algorithms each delivering a handful of results. AlphaEvolve is a single meta-algorithm yielding search algorithms for all of our results.

