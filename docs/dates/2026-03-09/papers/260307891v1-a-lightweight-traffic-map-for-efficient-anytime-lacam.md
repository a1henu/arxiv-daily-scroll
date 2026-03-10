---
layout: default
title: A Lightweight Traffic Map for Efficient Anytime LaCAM*
---

# A Lightweight Traffic Map for Efficient Anytime LaCAM*
**arXiv**：[2603.07891v1](https://arxiv.org/abs/2603.07891) · [PDF](https://arxiv.org/pdf/2603.07891.pdf)  
**作者**：Bojie Shen, Yue Zhang, Zhe Chen, Daniel Harabor  

**一句话要点**：提出动态轻量交通图以提升LaCAM*求解器在MAPF中的解质量

**关键词**：多智能体路径规划, LaCAM*求解器, 交通图优化, 动态搜索, 解质量提升

## 3 点简述
- 核心问题：现有基于引导路径的方法依赖静态优化，计算开销大且仅对首次求解有效。
- 方法要点：利用LaCAM*搜索中构建动态轻量交通图，避免重复单智能体搜索，降低开销。
- 实验或效果：在两种MAPF变体上，相比现有引导路径方法，实现更高解质量。

## 摘要（原文）

> Multi-Agent Path Finding (MAPF) aims to compute collision-free paths for multiple agents and has a wide range of practical applications. LaCAM*, an anytime configuration-based solver, currently represents the state of the art. Recent work has explored the use of guidance paths to steer LaCAM* toward configurations that avoid traffic congestion, thereby improving solution quality. However, existing approaches rely on Frank-Wolfe-style optimization that repeatedly invokes single-agent search before executing LaCAM*, resulting in substantial computational overhead for large-scale problems. Moreover, the guidance path is static and primarily beneficial for finding the first solution in LaCAM*. To address these limitations, we propose a new approach that leverages LaCAM*'s ability to construct a dynamic, lightweight traffic map during its search. Experimental results demonstrate that our method achieves higher solution quality than state-of-the-art guidance-path approaches across two MAPF variants.

