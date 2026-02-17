---
layout: default
title: Learning Structural Hardness for Combinatorial Auctions: Instance-Dependent Algorithm Selection via Graph Neural Networks
---

# Learning Structural Hardness for Combinatorial Auctions: Instance-Dependent Algorithm Selection via Graph Neural Networks
**arXiv**：[2602.14772v1](https://arxiv.org/abs/2602.14772) · [PDF](https://arxiv.org/pdf/2602.14772.pdf)  
**作者**：Sungwoo Kang  

**一句话要点**：提出基于图神经网络的组合拍卖实例硬度预测方法，实现算法选择以提升贪婪启发式性能。

**关键词**：组合拍卖, 算法选择, 图神经网络, 硬度预测, 贪婪启发式, 最优性差距

## 3 点简述
- 核心问题：组合拍卖中的胜者确定问题NP难，现有方法难以预测哪些实例会击败快速贪婪启发式。
- 方法要点：设计20维结构特征向量，训练轻量级MLP硬度分类器预测贪婪最优性差距，准确率达94.7%。
- 实验或效果：在混合分布上，结合硬度分类器、GNN和贪婪求解器的混合分配器实现0.51%总体差距。

## 摘要（原文）

> The Winner Determination Problem (WDP) in combinatorial auctions is NP-hard, and no existing method reliably predicts which instances will defeat fast greedy heuristics. The ML-for-combinatorial-optimization community has focused on learning to \emph{replace} solvers, yet recent evidence shows that graph neural networks (GNNs) rarely outperform well-tuned classical methods on standard benchmarks. We pursue a different objective: learning to predict \emph{when} a given instance is hard for greedy allocation, enabling instance-dependent algorithm selection. We design a 20-dimensional structural feature vector and train a lightweight MLP hardness classifier that predicts the greedy optimality gap with mean absolute error 0.033, Pearson correlation 0.937, and binary classification accuracy 94.7\% across three random seeds. For instances identified as hard -- those exhibiting ``whale-fish'' trap structure where greedy provably fails -- we deploy a heterogeneous GNN specialist that achieves ${\approx}0\%$ optimality gap on all six adversarial configurations tested (vs.\ 3.75--59.24\% for greedy). A hybrid allocator combining the hardness classifier with GNN and greedy solvers achieves 0.51\% overall gap on mixed distributions. Our honest evaluation on CATS benchmarks confirms that GNNs do not outperform Gurobi (0.45--0.71 vs.\ 0.20 gap), motivating the algorithm selection framing. Learning \emph{when} to deploy expensive solvers is more tractable than learning to replace them.

