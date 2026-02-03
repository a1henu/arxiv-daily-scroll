---
layout: default
title: Traffic-Aware Navigation in Road Networks
---

# Traffic-Aware Navigation in Road Networks
**arXiv**：[2602.02158v1](https://arxiv.org/abs/2602.02158) · [PDF](https://arxiv.org/pdf/2602.02158.pdf)  
**作者**：Sarah Nassar  

**一句话要点**：比较三种图搜索方法在金斯顿路网中的交通感知导航性能

**关键词**：交通感知导航, 图搜索算法, 路网规划, 实时路径优化, 预处理权衡

## 3 点简述
- 核心问题：在金斯顿路网中实现交通感知导航，需权衡预处理、实时性和最优性。
- 方法要点：对比单次多查询预处理（Floyd-Warshall-Ingerman）、连续单查询实时搜索（Dijkstra's和A*）及结合两者的Yen's算法。
- 实验或效果：Dijkstra's和A*提供最优交通感知路径，Floyd-Warshall-Ingerman实时最快但无交通感知，Yen's算法平衡速度和最优性。

## 摘要（原文）

> This project compares three graph search approaches for the task of traffic-aware navigation in Kingston's road network. These approaches include a single-run multi-query preprocessing algorithm (Floyd-Warshall-Ingerman), continuous single-query real-time search (Dijkstra's and A*), and an algorithm combining both approaches to balance between their trade-offs by first finding the top K shortest paths then iterating over them in real time (Yen's). Dijkstra's and A* resulted in the most traffic-aware optimal solutions with minimal preprocessing required. Floyd-Warshall-Ingerman was the fastest in real time but provided distance based paths with no traffic awareness. Yen's algorithm required significant preprocessing but balanced between the other two approaches in terms of runtime speed and optimality. Each approach presents advantages and disadvantages that need to be weighed depending on the circumstances of specific deployment contexts to select the best custom solution. *This project was completed as part of ELEC 844 (Search and Planning Algorithms for Robotics) in the Fall 2025 term.

