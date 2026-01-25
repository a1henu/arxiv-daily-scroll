---
layout: default
title: A Rolling-Space Branch-and-Price Algorithm for the Multi-Compartment Vehicle Routing Problem with Multiple Time Windows
---

# A Rolling-Space Branch-and-Price Algorithm for the Multi-Compartment Vehicle Routing Problem with Multiple Time Windows
**arXiv**：[2601.16194v1](https://arxiv.org/abs/2601.16194) · [PDF](https://arxiv.org/pdf/2601.16194.pdf)  
**作者**：El Mehdi Er Raqabi, Kevin Dalmeijer, Pascal Van Hentenryck  

**一句话要点**：提出滚动空间分支定价算法以解决带多时间窗的多隔间车辆路径问题

**关键词**：车辆路径问题, 分支定价算法, 多隔间车辆, 时间窗口, 标签算法, 聚类技术

## 3 点简述
- 核心问题：研究带多时间窗的多隔间车辆路径问题，考虑隔间灵活性、物品兼容性和司机休息等实际约束
- 方法要点：开发精确分支定价算法，结合标签算法和加速策略，并集成聚类技术处理大规模实例
- 实验或效果：基于真实工业应用实例进行广泛计算实验，验证算法有效性并提供管理见解

## 摘要（原文）

> This paper investigates the multi-compartment vehicle routing problem with multiple time windows (MCVRPMTW), an extension of the classical vehicle routing problem with time windows that considers vehicles equipped with multiple compartments and customers requiring service across several delivery time windows. The problem incorporates three key compartment-related features: (i) compartment flexibility in the number of compartments, (ii) item-to-compartment compatibility, and (iii) item-to-item compatibility. The problem also accommodates practical operational requirements such as driver breaks. To solve the MCVRPMTW, we develop an exact branch-and-price (B&P) algorithm in which the pricing problem is solved using a labeling algorithm. Several acceleration strategies are introduced to limit symmetry during label extensions, improve the stability of dual solutions in column generation, and enhance the branching process. To handle large-scale instances, we propose a rolling-space B&P algorithm that integrates clustering techniques into the solution framework. Extensive computational experiments on instances inspired by a real-world industrial application demonstrate the effectiveness of the proposed approach and provide useful managerial insights for practical implementation.

