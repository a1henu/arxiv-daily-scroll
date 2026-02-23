---
layout: default
title: Benchmarking Graph Neural Networks in Solving Hard Constraint Satisfaction Problems
---

# Benchmarking Graph Neural Networks in Solving Hard Constraint Satisfaction Problems
**arXiv**：[2602.18419v1](https://arxiv.org/abs/2602.18419) · [PDF](https://arxiv.org/pdf/2602.18419.pdf)  
**作者**：Geri Skenderi, Lorenzo Buffoni, Francesco D'Amico, David Machado, Raffaele Marino, Matteo Negri, Federico Ricci-Tersenghi, Carlo Lucibello, Maria Chiara Angelini  

**一句话要点**：提出基于随机问题的硬基准以评估图神经网络在约束满足问题中的性能

**关键词**：图神经网络, 约束满足问题, 基准测试, 统计物理, 优化算法, 随机问题

## 3 点简述
- 核心问题：现有图神经网络在硬优化问题上的优越性声称缺乏标准基准验证
- 方法要点：从统计物理角度设计基于随机问题的硬基准，提供公平比较框架
- 实验或效果：公平比较显示经典启发式算法仍优于图神经网络，讨论神经网络挑战

## 摘要（原文）

> Graph neural networks (GNNs) are increasingly applied to hard optimization problems, often claiming superiority over classical heuristics. However, such claims risk being unsolid due to a lack of standard benchmarks on truly hard instances. From a statistical physics perspective, we propose new hard benchmarks based on random problems. We provide these benchmarks, along with performance results from both classical heuristics and GNNs. Our fair comparison shows that classical algorithms still outperform GNNs. We discuss the challenges for neural networks in this domain. Future claims of superiority can be made more robust using our benchmarks, available at https://github.com/ArtLabBocconi/RandCSPBench.

