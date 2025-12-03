---
layout: default
title: Representation of Inorganic Synthesis Reactions and Prediction: Graphical Framework and Datasets
---

# Representation of Inorganic Synthesis Reactions and Prediction: Graphical Framework and Datasets
**arXiv**：[2512.02947v1](https://arxiv.org/abs/2512.02947) · [PDF](https://arxiv.org/pdf/2512.02947.pdf)  
**作者**：Samuel Andrello, Daniel Alabi, Simon J. L. Billinge  

**一句话要点**：提出ActionGraph框架以预测无机合成反应路径，提升操作序列准确性。

**关键词**：无机合成预测, 图表示学习, 材料科学机器学习, 合成路径规划, 文本挖掘

## 3 点简述
- 核心问题：机器学习预测无机材料性质后，合成路径确定仍具挑战。
- 方法要点：引入ActionGraph有向无环图，编码化学与过程结构。
- 实验或效果：基于13,017个反应，PCA降维后k近邻模型显著改善预测，操作长度匹配准确率提升3.4倍。

## 摘要（原文）

> While machine learning has enabled the rapid prediction of inorganic materials with novel properties, the challenge of determining how to synthesize these materials remains largely unsolved. Previous work has largely focused on predicting precursors or reaction conditions, but only rarely on full synthesis pathways. We introduce the ActionGraph, a directed acyclic graph framework that encodes both the chemical and procedural structure, in terms of synthesis operations, of inorganic synthesis reactions. Using 13,017 text-mined solid-state synthesis reactions from the Materials Project, we show that incorporating PCA-reduced ActionGraph adjacency matrices into a $k$-nearest neighbors retrieval model significantly improves synthesis pathway prediction. While the ActionGraph framework only results in a 1.34% and 2.76% increase in precursor and operation F1 scores (average over varying numbers of PCA components) respectively, the operation length matching accuracy rises 3.4 times (from 15.8% to 53.3%). We observe an interesting trade-off where precursor prediction performance peaks at 10-11 PCA components while operation prediction continues improving up to 30 components. This suggests composition information dominates precursor selection while structural information is critical for operation sequencing. Overall, the ActionGraph framework demonstrates strong potential, and with further adoption, its full range of benefits can be effectively realized.

