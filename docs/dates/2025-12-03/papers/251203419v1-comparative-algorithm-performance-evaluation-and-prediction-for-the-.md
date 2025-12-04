---
layout: default
title: Comparative algorithm performance evaluation and prediction for the maximum clique problem using instance space analysis
---

# Comparative algorithm performance evaluation and prediction for the maximum clique problem using instance space analysis
**arXiv**：[2512.03419v1](https://arxiv.org/abs/2512.03419) · [PDF](https://arxiv.org/pdf/2512.03419.pdf)  
**作者**：Bharat Sharman, Elkafi Hassini  

**一句话要点**：应用实例空间分析评估与预测最大团问题算法性能

**关键词**：最大团问题, 实例空间分析, 算法性能评估, 图神经网络, 组合优化, 性能预测

## 3 点简述
- 研究最大团问题，缺乏系统实例分析，采用实例空间分析方法。
- 使用图机器学习基准数据集，提取35个图特征，结合解质量和运行时间评估算法。
- MOMC算法在约74.7%实例空间表现最优，预测模型在测试集上准确率达88%和97%。

## 摘要（原文）

> The maximum clique problem, a well-known graph-based combinatorial optimization problem, has been addressed through various algorithmic approaches, though systematic analyses of the problem instances remain sparse. This study employs the instance space analysis (ISA) methodology to systematically analyze the instance space of this problem and assess & predict the performance of state-of-the-art (SOTA) algorithms, including exact, heuristic, and graph neural network (GNN)-based methods. A dataset was compiled using graph instances from TWITTER, COLLAB and IMDB-BINARY benchmarks commonly used in graph machine learning research. A set of 33 generic and 2 problem-specific polynomial-time-computable graph-based features, including several spectral properties, was employed for the ISA. A composite performance mea- sure incorporating both solution quality and algorithm runtime was utilized. The comparative analysis demonstrated that the exact algorithm Mixed Order Maximum Clique (MOMC) exhib- ited superior performance across approximately 74.7% of the instance space constituted by the compiled dataset. Gurobi & CliSAT accounted for superior performance in 13.8% and 11% of the instance space, respectively. The ISA-based algorithm performance prediction model run on 34 challenging test instances compiled from the BHOSLIB and DIMACS datasets yielded top-1 and top-2 best performing algorithm prediction accuracies of 88% and 97%, respectively.

