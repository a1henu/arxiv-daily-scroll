---
layout: default
title: The Art of Being Difficult: Combining Human and AI Strengths to Find Adversarial Instances for Heuristics
---

# The Art of Being Difficult: Combining Human and AI Strengths to Find Adversarial Instances for Heuristics
**arXiv**：[2601.16849v1](https://arxiv.org/abs/2601.16849) · [PDF](https://arxiv.org/pdf/2601.16849.pdf)  
**作者**：Henri Nikoleit, Ankit Anand, Anurag Murty Naredla, Heiko Röglin  

**一句话要点**：结合人类与AI优势改进FunSearch输出，为组合优化启发式算法生成对抗实例以提升下界

**关键词**：组合优化, 对抗实例生成, 人类-AI协作, FunSearch算法, 启发式算法下界

## 3 点简述
- 核心问题：针对组合优化中的启发式算法，生成使其性能差的对抗实例，以提升下界。
- 方法要点：通过人类专家迭代改进FunSearch算法的输出，结合LLM的初始模式和人类数学严谨性。
- 实验或效果：在分层k-中值聚类、装箱问题、背包问题等任务中取得多年未有的下界改进。

## 摘要（原文）

> We demonstrate the power of human-LLM collaboration in tackling open problems in theoretical computer science. Focusing on combinatorial optimization, we refine outputs from the FunSearch algorithm [Romera-Paredes et al., Nature 2023] to derive state-of-the-art lower bounds for standard heuristics. Specifically, we target the generation of adversarial instances where these heuristics perform poorly. By iterating on FunSearch's outputs, we identify improved constructions for hierarchical $k$-median clustering, bin packing, the knapsack problem, and a generalization of Lovász's gasoline problem - some of these have not seen much improvement for over a decade, despite intermittent attention. These results illustrate how expert oversight can effectively extrapolate algorithmic insights from LLM-based evolutionary methods to break long-standing barriers.
>   Our findings demonstrate that while LLMs provide critical initial patterns, human expertise is essential for transforming these patterns into mathematically rigorous and insightful constructions. This work highlights that LLMs are a strong collaborative tool in mathematics and computer science research.

