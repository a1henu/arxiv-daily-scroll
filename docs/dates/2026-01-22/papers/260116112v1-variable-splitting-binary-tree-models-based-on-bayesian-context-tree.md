---
layout: default
title: Variable Splitting Binary Tree Models Based on Bayesian Context Tree Models for Time Series Segmentation
---

# Variable Splitting Binary Tree Models Based on Bayesian Context Tree Models for Time Series Segmentation
**arXiv**：[2601.16112v1](https://arxiv.org/abs/2601.16112) · [PDF](https://arxiv.org/pdf/2601.16112.pdf)  
**作者**：Yuta Nakahara, Shota Saito, Kohei Horinouchi, Koshi Shimada, Naoki Ichijo, Manabu Kobayashi, Toshiyasu Matsushima  

**一句话要点**：提出基于贝叶斯上下文树的变分分裂二叉树模型，用于时间序列分割

**关键词**：时间序列分割, 贝叶斯上下文树, 变分分裂二叉树, 递归逻辑回归, 上下文树加权算法

## 3 点简述
- 核心问题：时间序列分割中，传统方法可能无法灵活表示分割位置或树结构。
- 方法要点：结合贝叶斯上下文树与递归逻辑回归，实现任意位置的分割和紧凑树表示。
- 实验或效果：在合成数据上展示模型和算法的有效性，未知具体性能指标。

## 摘要（原文）

> We propose a variable splitting binary tree (VSBT) model based on Bayesian context tree (BCT) models for time series segmentation. Unlike previous applications of BCT models, the tree structure in our model represents interval partitioning on the time domain. Moreover, interval partitioning is represented by recursive logistic regression models. By adjusting logistic regression coefficients, our model can represent split positions at arbitrary locations within each interval. This enables more compact tree representations. For simultaneous estimation of both split positions and tree depth, we develop an effective inference algorithm that combines local variational approximation for logistic regression with the context tree weighting (CTW) algorithm. We present numerical examples on synthetic data demonstrating the effectiveness of our model and algorithm.

