---
layout: default
title: Visualizing the loss landscapes of physics-informed neural networks
---

# Visualizing the loss landscapes of physics-informed neural networks
**arXiv**：[2602.05849v1](https://arxiv.org/abs/2602.05849) · [PDF](https://arxiv.org/pdf/2602.05849.pdf)  
**作者**：Conor Rowan, Finn Murphy-Blanchard  

**一句话要点**：可视化物理信息神经网络的损失景观，比较Deep Ritz与强形式损失

**关键词**：损失景观可视化, 物理信息神经网络, Deep Ritz方法, 强形式损失, 科学机器学习, 优化几何

## 3 点简述
- 研究物理信息机器学习中损失景观的可视化，填补图像分类以外领域的空白
- 应用文献技术实证分析Deep Ritz和平方残差形式的物理损失函数景观
- 发现物理信息网络损失景观与数据驱动分类问题相似，呈现平滑、凸性特征

## 摘要（原文）

> Training a neural network requires navigating a high-dimensional, non-convex loss surface to find parameters that minimize this loss. In many ways, it is surprising that optimizers such as stochastic gradient descent and ADAM can reliably locate minima which perform well on both the training and test data. To understand the success of training, a "loss landscape" community has emerged to study the geometry of the loss function and the dynamics of optimization, often using visualization techniques. However, these loss landscape studies have mostly been limited to machine learning for image classification. In the newer field of physics-informed machine learning, little work has been conducted to visualize the landscapes of losses defined not by regression to large data sets, but by differential operators acting on state fields discretized by neural networks. In this work, we provide a comprehensive review of the loss landscape literature, as well as a discussion of the few existing physics-informed works which investigate the loss landscape. We then use a number of the techniques we survey to empirically investigate the landscapes defined by the Deep Ritz and squared residual forms of the physics loss function. We find that the loss landscapes of physics-informed neural networks have many of the same properties as the data-driven classification problems studied in the literature. Unexpectedly, we find that the two formulations of the physics loss often give rise to similar landscapes, which appear smooth, well-conditioned, and convex in the vicinity of the solution. The purpose of this work is to introduce the loss landscape perspective to the scientific machine learning community, compare the Deep Ritz and the strong form losses, and to challenge prevailing intuitions about the complexity of the loss landscapes of physics-informed networks.

