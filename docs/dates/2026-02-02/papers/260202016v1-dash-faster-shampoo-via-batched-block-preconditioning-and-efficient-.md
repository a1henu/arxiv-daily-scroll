---
layout: default
title: DASH: Faster Shampoo via Batched Block Preconditioning and Efficient Inverse-Root Solvers
---

# DASH: Faster Shampoo via Batched Block Preconditioning and Efficient Inverse-Root Solvers
**arXiv**：[2602.02016v1](https://arxiv.org/abs/2602.02016) · [PDF](https://arxiv.org/pdf/2602.02016.pdf)  
**作者**：Ionut-Vlad Modoranu, Philip Zmushko, Erik Schultheis, Mher Safaryan, Dan Alistarh  

**一句话要点**：提出DASH以加速分布式Shampoo优化器，通过批处理块预条件与高效逆矩阵根求解器

**关键词**：二阶优化器, 分布式训练, GPU加速, 矩阵根计算, 预条件技术, 机器学习优化

## 3 点简述
- Shampoo优化器计算成本高，导致应用时显著减速
- 引入批处理块预条件提升GPU利用率，并开发Newton-DB迭代与Chebyshev多项式近似加速逆矩阵根计算
- 实验显示DASH优化器步骤快4.83倍，Newton-DB在每次迭代中验证困惑度最低

## 摘要（原文）

> Shampoo is one of the leading approximate second-order optimizers: a variant of it has won the MLCommons AlgoPerf competition, and it has been shown to produce models with lower activation outliers that are easier to compress. Yet, applying Shampoo currently comes at the cost of significant computational slowdown, due to its expensive internal operations. In this paper, we take a significant step to address this shortcoming by proposing \method (for \textbf{D}istributed \textbf{A}ccelerated \textbf{SH}ampoo), a faster implementation of Distributed Shampoo based on two main new techniques: First, we show that preconditioner blocks can be stacked into 3D tensors to significantly improve GPU utilization; second, we introduce the Newton-DB iteration and the Chebyshev polynomial approximations as novel and faster approaches for computing the inverse matrix roots required by Shampoo. Along with these algorithmic contributions, we provide a first in-depth analysis of how matrix scaling critically affects Shampoo convergence. On the practical side, our GPU-aware implementation achieves up to $4.83\times$ faster optimizer steps compared to the well-optimized Distributed Shampoo, while Newton-DB attains the lowest validation perplexity per iteration among all tested methods. Our code is available at https://github.com/IST-DASLab/DASH.

