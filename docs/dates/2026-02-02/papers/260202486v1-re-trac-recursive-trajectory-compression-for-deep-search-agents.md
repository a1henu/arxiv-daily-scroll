---
layout: default
title: RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents
---

# RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents
**arXiv**：[2602.02486v1](https://arxiv.org/abs/2602.02486) · [PDF](https://arxiv.org/pdf/2602.02486.pdf)  
**作者**：Jialiang Zhu, Gongrui Zhang, Xiaolong Ma, Lin Xu, Miaosen Zhang, Ruiqi Yang, Song Wang, Kai Qiu, Zhirong Wu, Qi Dai, Ruichun Ma, Bei Liu, Yifan Yang, Chong Luo, Zhengyuan Yang, Linjie Li, Lijuan Wang, Weizhu Chen, Xin Geng, Baining Guo  

**一句话要点**：提出Re-TRAC框架以解决基于ReAct的深度搜索代理在长上下文下难以全局规划和高效探索的问题。

**关键词**：深度搜索代理, 轨迹压缩, 结构化状态表示, 跨轨迹探索, 迭代反思, 监督微调

## 3 点简述
- 核心问题：ReAct框架的线性设计导致代理难以回溯状态、分支探索或保持全局意识，易陷入局部最优和冗余搜索。
- 方法要点：通过生成结构化状态表示来总结证据、不确定性、失败和未来计划，并基于此条件化后续轨迹，实现跨轨迹探索和迭代反思。
- 实验或效果：在BrowseComp上比ReAct提升15-20%，工具调用和令牌使用随轮次单调减少，表明探索更具针对性。

## 摘要（原文）

> LLM-based deep research agents are largely built on the ReAct framework. This linear design makes it difficult to revisit earlier states, branch into alternative search directions, or maintain global awareness under long contexts, often leading to local optima, redundant exploration, and inefficient search. We propose Re-TRAC, an agentic framework that performs cross-trajectory exploration by generating a structured state representation after each trajectory to summarize evidence, uncertainties, failures, and future plans, and conditioning subsequent trajectories on this state representation. This enables iterative reflection and globally informed planning, reframing research as a progressive process. Empirical results show that Re-TRAC consistently outperforms ReAct by 15-20% on BrowseComp with frontier LLMs. For smaller models, we introduce Re-TRAC-aware supervised fine-tuning, achieving state-of-the-art performance at comparable scales. Notably, Re-TRAC shows a monotonic reduction in tool calls and token usage across rounds, indicating progressively targeted exploration driven by cross-trajectory reflection rather than redundant search.

