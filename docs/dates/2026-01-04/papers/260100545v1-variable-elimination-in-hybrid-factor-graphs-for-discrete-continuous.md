---
layout: default
title: Variable Elimination in Hybrid Factor Graphs for Discrete-Continuous Inference & Estimation
---

# Variable Elimination in Hybrid Factor Graphs for Discrete-Continuous Inference & Estimation
**arXiv**：[2601.00545v1](https://arxiv.org/abs/2601.00545) · [PDF](https://arxiv.org/pdf/2601.00545.pdf)  
**作者**：Varun Agrawal, Frank Dellaert  

**一句话要点**：提出混合因子图框架与变量消除算法，用于机器人中离散-连续推理与估计问题

**关键词**：混合因子图, 变量消除, 离散-连续推理, 条件线性高斯, SLAM, 最大后验估计

## 3 点简述
- 核心问题：机器人混合问题中离散与连续变量联合建模困难，现有方法依赖近似
- 方法要点：引入混合高斯因子和混合条件表示，基于条件线性高斯方案实现精确变量消除
- 实验或效果：在SLAM数据集上验证框架，处理模糊测量，展示准确性、通用性和简洁性

## 摘要（原文）

> Many hybrid problems in robotics involve both continuous and discrete components, and modeling them together for estimation tasks has been a long standing and difficult problem. Hybrid Factor Graphs give us a mathematical framework to model these types of problems, however existing approaches for solving them are based on approximations. In this work, we propose an efficient Hybrid Factor Graph framework alongwith a variable elimination algorithm to produce a hybrid Bayes network, which can then be used for exact Maximum A Posteriori estimation and marginalization over both sets of variables. Our approach first develops a novel hybrid Gaussian factor which can connect to both discrete and continuous variables, and a hybrid conditional which can represent multiple continuous hypotheses conditioned on the discrete variables. Using these representations, we derive the process of hybrid variable elimination under the Conditional Linear Gaussian scheme, giving us exact posteriors as hybrid Bayes network. To bound the number of discrete hypotheses, we use a tree-structured representation of the factors coupled with a simple pruning and probabilistic assignment scheme, which allows for tractable inference. We demonstrate the applicability of our framework on a SLAM dataset with ambiguous measurements, where discrete choices for the most likely measurement have to be made. Our demonstrated results showcase the accuracy, generality, and simplicity of our hybrid factor graph framework.

