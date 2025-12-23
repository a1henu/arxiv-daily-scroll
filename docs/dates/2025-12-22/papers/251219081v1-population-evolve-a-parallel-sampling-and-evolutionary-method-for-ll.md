---
layout: default
title: Population-Evolve: a Parallel Sampling and Evolutionary Method for LLM Math Reasoning
---

# Population-Evolve: a Parallel Sampling and Evolutionary Method for LLM Math Reasoning
**arXiv**：[2512.19081v1](https://arxiv.org/abs/2512.19081) · [PDF](https://arxiv.org/pdf/2512.19081.pdf)  
**作者**：Yanzhi Zhang, Yitong Duan, Zhaoxi Zhang, Jiyan He, Shuxin Zheng  

**一句话要点**：提出Population-Evolve方法，基于遗传算法优化大语言模型的数学推理能力。

**关键词**：大语言模型推理, 遗传算法, 测试时扩展, 并行采样, 进化策略, 数学推理

## 3 点简述
- 核心问题：测试时扩展方法用于提升大语言模型的推理能力，但需高效优化。
- 方法要点：通过并行采样维持候选解种群，利用进化提示自我迭代，收敛后多数投票得出答案。
- 实验或效果：实证显示该方法在准确性、低方差和计算效率方面表现优越。

## 摘要（原文）

> Test-time scaling has emerged as a promising direction for enhancing the reasoning capabilities of Large Language Models in last few years. In this work, we propose Population-Evolve, a training-free method inspired by Genetic Algorithms to optimize LLM reasoning. Our approach maintains a dynamic population of candidate solutions for each problem via parallel reasoning. By incorporating an evolve prompt, the LLM self-evolves its population in all iterations. Upon convergence, the final answer is derived via majority voting. Furthermore, we establish a unification framework that interprets existing test-time scaling strategies through the lens of genetic algorithms. Empirical results demonstrate that Population-Evolve achieves superior accuracy with low performance variance and computational efficiency. Our findings highlight the potential of evolutionary strategies to unlock the reasoning power of LLMs during inference.

