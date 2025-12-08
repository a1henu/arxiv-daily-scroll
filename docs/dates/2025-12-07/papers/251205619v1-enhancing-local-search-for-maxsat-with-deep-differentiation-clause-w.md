---
layout: default
title: Enhancing Local Search for MaxSAT with Deep Differentiation Clause Weighting
---

# Enhancing Local Search for MaxSAT with Deep Differentiation Clause Weighting
**arXiv**：[2512.05619v1](https://arxiv.org/abs/2512.05619) · [PDF](https://arxiv.org/pdf/2512.05619.pdf)  
**作者**：Menghua Jiang, Haokai Gao, Shuhao Chen, Yin Chen  

**一句话要点**：提出DeepDist子句加权方案以增强局部搜索求解部分最大可满足性问题

**关键词**：最大可满足性问题, 局部搜索算法, 子句加权方案, 混合求解器, 性能评估

## 3 点简述
- 针对PMS和WPMS问题，现有方法未区分其结构差异，采用统一权重更新策略。
- 提出新颖子句加权方案，首次根据PMS和WPMS不同条件更新权重，并引入新初始化方法。
- 实验表明DeepDist优于先进SLS求解器，混合求解器超越MaxSAT评估2024优胜者。

## 摘要（原文）

> Partial Maximum Satisfiability (PMS) and Weighted Partial Maximum Satisfiability (WPMS) generalize Maximum Satisfiability (MaxSAT), with broad real-world applications. Recent advances in Stochastic Local Search (SLS) algorithms for solving (W)PMS have mainly focused on designing clause weighting schemes. However, existing methods often fail to adequately distinguish between PMS and WPMS, typically employing uniform update strategies for clause weights and overlooking critical structural differences between the two problem types. In this work, we present a novel clause weighting scheme that, for the first time, updates the clause weights of PMS and WPMS instances according to distinct conditions. This scheme also introduces a new initialization method, which better accommodates the unique characteristics of both instance types. Furthermore, we propose a decimation method that prioritizes satisfying unit and hard clauses, effectively complementing our proposed clause weighting scheme. Building on these methods, we develop a new SLS solver for (W)PMS named DeepDist. Experimental results on benchmarks from the anytime tracks of recent MaxSAT Evaluations show that DeepDist outperforms state-of-the-art SLS solvers. Notably, a hybrid solver combining DeepDist with TT-Open-WBO-Inc surpasses the performance of the MaxSAT Evaluation 2024 winners, SPB-MaxSAT-c-Band and SPB-MaxSAT-c-FPS, highlighting the effectiveness of our approach. The code is available at https://github.com/jmhmaxsat/DeepDist

