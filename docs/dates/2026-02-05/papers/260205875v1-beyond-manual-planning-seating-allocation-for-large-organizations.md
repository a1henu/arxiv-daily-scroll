---
layout: default
title: Beyond Manual Planning: Seating Allocation for Large Organizations
---

# Beyond Manual Planning: Seating Allocation for Large Organizations
**arXiv**：[2602.05875v1](https://arxiv.org/abs/2602.05875) · [PDF](https://arxiv.org/pdf/2602.05875.pdf)  
**作者**：Anton Ipsen, Michael Cashmore, Kirsty Fielding, Nicolas Marchesotti, Parisa Zehtabi, Daniele Magazzeni, Manuela Veloso  

**一句话要点**：提出分层座位分配问题框架，以自动优化大型组织团队在平面图中的座位安排。

**关键词**：座位分配优化, 分层组织规划, 概率路线图, 整数规划, 启发式搜索

## 3 点简述
- 核心问题：大型组织需手动分配团队座位，导致规划效率低且不优。
- 方法要点：结合概率路线图和启发式搜索，通过整数规划求解分层座位分配问题。
- 实验或效果：在不同规模实例上评估框架，进行定量和定性分析。

## 摘要（原文）

> We introduce the Hierarchical Seating Allocation Problem (HSAP) which addresses the optimal assignment of hierarchically structured organizational teams to physical seating arrangements on a floor plan. This problem is driven by the necessity for large organizations with large hierarchies to ensure that teams with close hierarchical relationships are seated in proximity to one another, such as ensuring a research group occupies a contiguous area. Currently, this problem is managed manually leading to infrequent and suboptimal replanning efforts. To alleviate this manual process, we propose an end-to-end framework to solve the HSAP. A scalable approach to calculate the distance between any pair of seats using a probabilistic road map (PRM) and rapidly-exploring random trees (RRT) which is combined with heuristic search and dynamic programming approach to solve the HSAP using integer programming. We demonstrate our approach under different sized instances by evaluating the PRM framework and subsequent allocations both quantitatively and qualitatively.

