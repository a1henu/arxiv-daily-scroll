---
layout: default
title: Magnitude Distance: A Geometric Measure of Dataset Similarity
---

# Magnitude Distance: A Geometric Measure of Dataset Similarity
**arXiv**：[2602.08859v1](https://arxiv.org/abs/2602.08859) · [PDF](https://arxiv.org/pdf/2602.08859.pdf)  
**作者**：Sahel Torkamani, Henry Gouk, Rik Sarkar  

**一句话要点**：提出幅度距离作为数据集相似性的几何度量，用于高维判别和生成模型训练。

**关键词**：数据集相似性度量, 幅度距离, 高维数据分析, 生成模型训练, 几何度量

## 3 点简述
- 量化数据集间距离是数学与机器学习的基础问题，现有方法在高维下可能失效。
- 基于度量空间幅度概念，定义幅度距离，通过可调参数控制对全局结构与细节的敏感性。
- 理论证明其度量性质，实验显示在高维下保持判别性，并作为生成模型的训练目标有效。

## 摘要（原文）

> Quantifying the distance between datasets is a fundamental question in mathematics and machine learning. We propose \textit{magnitude distance}, a novel distance metric defined on finite datasets using the notion of the \emph{magnitude} of a metric space. The proposed distance incorporates a tunable scaling parameter, $t$, that controls the sensitivity to global structure (small $t$) and finer details (large $t$). We prove several theoretical properties of magnitude distance, including its limiting behavior across scales and conditions under which it satisfies key metric properties. In contrast to classical distances, we show that magnitude distance remains discriminative in high-dimensional settings when the scale is appropriately tuned. We further demonstrate how magnitude distance can be used as a training objective for push-forward generative models. Our experimental results support our theoretical analysis and demonstrate that magnitude distance provides meaningful signals, comparable to established distance-based generative approaches.

