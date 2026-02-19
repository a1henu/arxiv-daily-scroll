---
layout: default
title: Predicting The Cop Number Using Machine Learning
---

# Predicting The Cop Number Using Machine Learning
**arXiv**：[2602.16600v1](https://arxiv.org/abs/2602.16600) · [PDF](https://arxiv.org/pdf/2602.16600.pdf)  
**作者**：Meagan Mann, Christian Muise, Erin Meger  

**一句话要点**：应用机器学习预测图的警察数，以补充传统算法在计算不可行时的可扩展近似。

**关键词**：警察与强盗游戏, 图神经网络, 机器学习预测, 图结构分析, 可解释性分析

## 3 点简述
- 核心问题：图的警察数计算困难，传统算法限于小图族，需可扩展预测方法。
- 方法要点：使用经典机器学习（如树模型）和图神经网络，从结构属性预测警察数，无需显式特征工程。
- 实验或效果：树模型在类别不平衡下实现高准确率，图神经网络结果相当，可解释性分析显示节点连通性等特征最预测。

## 摘要（原文）

> Cops and Robbers is a pursuit evasion game played on a graph, first introduced independently by Quilliot \cite{quilliot1978jeux} and Nowakowski and Winkler \cite{NOWAKOWSKI1983235} over four decades ago. A main interest in recent the literature is identifying the cop number of graph families. The cop number of a graph, $c(G)$, is defined as the minimum number of cops required to guarantee capture of the robber. Determining the cop number is computationally difficult and exact algorithms for this are typically restricted to small graph families. This paper investigates whether classical machine learning methods and graph neural networks can accurately predict a graph's cop number from its structural properties and identify which properties most strongly influence this prediction. Of the classical machine learning models, tree-based models achieve high accuracy in prediction despite class imbalance, whereas graph neural networks achieve comparable results without explicit feature engineering. The interpretability analysis shows that the most predictive features are related to node connectivity, clustering, clique structure, and width parameters, which aligns with known theoretical results. Our findings suggest that machine learning approaches can be used in complement with existing cop number algorithms by offering scalable approximations where computation is infeasible.

