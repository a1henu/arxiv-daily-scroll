---
layout: default
title: MMP-A*: Multimodal Perception Enhanced Incremental Heuristic Search on Path Planning
---

# MMP-A*: Multimodal Perception Enhanced Incremental Heuristic Search on Path Planning
**arXiv**：[2601.01910v1](https://arxiv.org/abs/2601.01910) · [PDF](https://arxiv.org/pdf/2601.01910.pdf)  
**作者**：Minh Hieu Ha, Khanh Ly Ta, Hung Phan, Tung Doan, Tung Dao, Dao Tran, Huynh Thi Thanh Binh  

**一句话要点**：提出MMP-A*框架，通过多模态感知增强路径规划，解决复杂环境中计算效率与几何一致性问题。

**关键词**：路径规划, 多模态感知, 启发式搜索, 自适应衰减机制, 视觉语言模型, 自主导航

## 3 点简述
- 核心问题：传统A*在大规模复杂环境中计算和内存成本高，仅基于文本的规划方法缺乏空间基础，导致路径错误和效率低下。
- 方法要点：集成视觉语言模型的空间基础能力，引入自适应衰减机制，动态调节启发式函数中不确定路径点的影响，确保几何有效性。
- 实验或效果：在严重杂乱和拓扑复杂环境中测试，MMP-A*实现近最优轨迹，显著降低操作成本，提升计算效率。

## 摘要（原文）

> Autonomous path planning requires a synergy between global reasoning and geometric precision, especially in complex or cluttered environments. While classical A* is valued for its optimality, it incurs prohibitive computational and memory costs in large-scale scenarios. Recent attempts to mitigate these limitations by using Large Language Models for waypoint guidance remain insufficient, as they rely only on text-based reasoning without spatial grounding. As a result, such models often produce incorrect waypoints in topologically complex environments with dead ends, and lack the perceptual capacity to interpret ambiguous physical boundaries. These inconsistencies lead to costly corrective expansions and undermine the intended computational efficiency.
>   We introduce MMP-A*, a multimodal framework that integrates the spatial grounding capabilities of vision-language models with a novel adaptive decay mechanism. By anchoring high-level reasoning in physical geometry, the framework produces coherent waypoint guidance that addresses the limitations of text-only planners. The adaptive decay mechanism dynamically regulates the influence of uncertain waypoints within the heuristic, ensuring geometric validity while substantially reducing memory overhead. To evaluate robustness, we test the framework in challenging environments characterized by severe clutter and topological complexity. Experimental results show that MMP-A* achieves near-optimal trajectories with significantly reduced operational costs, demonstrating its potential as a perception-grounded and computationally efficient paradigm for autonomous navigation.

