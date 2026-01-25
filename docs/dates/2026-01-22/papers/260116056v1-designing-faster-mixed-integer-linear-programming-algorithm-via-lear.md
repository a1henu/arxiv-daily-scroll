---
layout: default
title: Designing faster mixed integer linear programming algorithm via learning the optimal path
---

# Designing faster mixed integer linear programming algorithm via learning the optimal path
**arXiv**：[2601.16056v1](https://arxiv.org/abs/2601.16056) · [PDF](https://arxiv.org/pdf/2601.16056.pdf)  
**作者**：Ruizhi Liu, Liming Xu, Xulin Huang, Jingyan Sui, Shizhe Ding, Boyang Xia, Chungong Yu, Dongbo Bu  

**一句话要点**：提出DeepBound学习最优路径以加速混合整数线性规划求解

**关键词**：混合整数线性规划, 分支定界算法, 深度学习, 节点选择, 特征融合, 成对训练

## 3 点简述
- 核心问题：传统分支定界算法依赖人工启发式策略，性能不稳定且不可预测。
- 方法要点：采用深度学习自动学习节点优先级，通过多级特征融合和成对训练处理节点不平衡。
- 实验或效果：在三个NP难基准测试中，DeepBound显著减少计算时间，展现强泛化能力。

## 摘要（原文）

> Designing faster algorithms for solving Mixed-Integer Linear Programming (MILP) problems is highly desired across numerous practical domains, as a vast array of complex real-world challenges can be effectively modeled as MILP formulations. Solving these problems typically employs the branch-and-bound algorithm, the core of which can be conceived as searching for a path of nodes (or sub-problems) that contains the optimal solution to the original MILP problem. Traditional approaches to finding this path rely heavily on hand-crafted, intuition-based heuristic strategies, which often suffer from unstable and unpredictable performance across different MILP problem instances. To address this limitation, we introduce DeepBound, a deep learning-based node selection algorithm that automates the learning of such human intuition from data. The core of DeepBound lies in learning to prioritize nodes containing the optimal solution, thereby improving solving efficiency. DeepBound introduces a multi-level feature fusion network to capture the node representations. To tackle the inherent node imbalance in branch-and-bound trees, DeepBound employs a pairwise training paradigm that enhances the model's ability to discriminate between nodes. Extensive experiments on three NP-hard MILP benchmarks demonstrate that DeepBound achieves superior solving efficiency over conventional heuristic rules and existing learning-based approaches, obtaining optimal feasible solutions with significantly reduced computation time. Moreover, DeepBound demonstrates strong generalization capability on large and complex instances. The analysis of its learned features reveals that the method can automatically discover more flexible and robust feature selection, which may effectively improve and potentially replace human-designed heuristic rules.

