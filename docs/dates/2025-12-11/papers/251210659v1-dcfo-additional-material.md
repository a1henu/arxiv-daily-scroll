---
layout: default
title: DCFO Additional Material
---

# DCFO Additional Material
**arXiv**：[2512.10659v1](https://arxiv.org/abs/2512.10659) · [PDF](https://arxiv.org/pdf/2512.10659.pdf)  
**作者**：Tommaso Amico, Pernille Matthews, Lena Krieger, Arthur Zimek, Ira Assent  

**一句话要点**：提出DCFO方法，为LOF算法生成反事实解释以提升异常检测可解释性。

**关键词**：异常检测, 反事实解释, LOF算法, 可解释性, 梯度优化

## 3 点简述
- 核心问题：LOF等经典异常检测算法缺乏可解释性，现有反事实解释方法未针对其独特挑战。
- 方法要点：DCFO将数据空间分区，基于梯度优化生成最小改变的反事实解释。
- 实验或效果：在50个OpenML数据集上验证，DCFO在邻近性和有效性上优于基准方法。

## 摘要（原文）

> Outlier detection identifies data points that significantly deviate from the majority of the data distribution. Explaining outliers is crucial for understanding the underlying factors that contribute to their detection, validating their significance, and identifying potential biases or errors. Effective explanations provide actionable insights, facilitating preventive measures to avoid similar outliers in the future. Counterfactual explanations clarify why specific data points are classified as outliers by identifying minimal changes required to alter their prediction. Although valuable, most existing counterfactual explanation methods overlook the unique challenges posed by outlier detection, and fail to target classical, widely adopted outlier detection algorithms. Local Outlier Factor (LOF) is one the most popular unsupervised outlier detection methods, quantifying outlierness through relative local density. Despite LOF's widespread use across diverse applications, it lacks interpretability. To address this limitation, we introduce Density-based Counterfactuals for Outliers (DCFO), a novel method specifically designed to generate counterfactual explanations for LOF. DCFO partitions the data space into regions where LOF behaves smoothly, enabling efficient gradient-based optimisation. Extensive experimental validation on 50 OpenML datasets demonstrates that DCFO consistently outperforms benchmarked competitors, offering superior proximity and validity of generated counterfactuals.

