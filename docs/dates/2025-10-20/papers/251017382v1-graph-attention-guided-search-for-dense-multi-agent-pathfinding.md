---
layout: default
title: Graph Attention-Guided Search for Dense Multi-Agent Pathfinding
---

# Graph Attention-Guided Search for Dense Multi-Agent Pathfinding
**arXiv**：[2510.17382v1](https://arxiv.org/abs/2510.17382) · [PDF](https://arxiv.org/pdf/2510.17382.pdf)  
**作者**：Rishabh Jain, Keisuke Okumura, Michael Amir, Amanda Prorok  

**一句话要点**：提出LaGAT框架以解决密集多智能体路径规划问题

**关键词**：多智能体路径规划, 图注意力机制, 混合搜索算法, 死锁检测, 学习引导搜索

## 3 点简述
- 密集多智能体路径规划在实时求解中面临挑战，现有方法性能不足
- 集成学习启发式与搜索算法，采用图注意力机制和死锁检测
- 在密集场景中优于纯搜索和纯学习方法，验证混合方法的有效性

## 摘要（原文）

> Finding near-optimal solutions for dense multi-agent pathfinding (MAPF)
> problems in real-time remains challenging even for state-of-the-art planners.
> To this end, we develop a hybrid framework that integrates a learned heuristic
> derived from MAGAT, a neural MAPF policy with a graph attention scheme, into a
> leading search-based algorithm, LaCAM. While prior work has explored
> learning-guided search in MAPF, such methods have historically underperformed.
> In contrast, our approach, termed LaGAT, outperforms both purely search-based
> and purely learning-based methods in dense scenarios. This is achieved through
> an enhanced MAGAT architecture, a pre-train-then-fine-tune strategy on maps of
> interest, and a deadlock detection scheme to account for imperfect neural
> guidance. Our results demonstrate that, when carefully designed, hybrid search
> offers a powerful solution for tightly coupled, challenging multi-agent
> coordination problems.

