---
layout: default
title: De-paradox Tree: Breaking Down Simpson's Paradox via A Kernel-Based Partition Algorithm
---

# De-paradox Tree: Breaking Down Simpson's Paradox via A Kernel-Based Partition Algorithm
**arXiv**：[2603.02174v1](https://arxiv.org/abs/2603.02174) · [PDF](https://arxiv.org/pdf/2603.02174.pdf)  
**作者**：Xian Teng, Yu-Ru Lin  

**一句话要点**：提出De-paradox Tree算法，通过核基分割解决观测数据中的辛普森悖论问题。

**关键词**：辛普森悖论, 因果推断, 可解释机器学习, 递归分区, 混杂调整, 观测数据分析

## 3 点简述
- 核心问题：辛普森悖论导致聚合与子组关联矛盾，误导数据驱动决策。
- 方法要点：基于因果结构，使用新分割准则和平衡程序递归分区，调整混杂并同质化异质效应。
- 实验或效果：相比现有方法，构建更简单可解释的树，选择相关协变量，识别嵌套相反效应。

## 摘要（原文）

> Real-world observational datasets and machine learning have revolutionized data-driven decision-making, yet many models rely on empirical associations that may be misleading due to confounding and subgroup heterogeneity. Simpson's paradox exemplifies this challenge, where aggregated and subgroup-level associations contradict each other, leading to misleading conclusions. Existing methods provide limited support for detecting and interpreting such paradoxical associations, especially for practitioners without deep causal expertise. We introduce De-paradox Tree, an interpretable algorithm designed to uncover hidden subgroup patterns behind paradoxical associations under assumed causal structures involving confounders and effect heterogeneity. It employs novel split criteria and balancing-based procedures to adjust for confounders and homogenize heterogeneous effects through recursive partitioning. Compared to state-of-the-art methods, De-paradox Tree builds simpler, more interpretable trees, selects relevant covariates, and identifies nested opposite effects while ensuring robust estimation of causal effects when causally admissible variables are provided. Our approach addresses the limitations of traditional causal inference and machine learning methods by introducing an interpretable framework that supports non-expert practitioners while explicitly acknowledging causal assumptions and scope limitations, enabling more reliable and informed decision-making in complex observational data environments.

