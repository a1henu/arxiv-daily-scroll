---
layout: default
title: Clapeyron Neural Networks for Single-Species Vapor-Liquid Equilibria
---

# Clapeyron Neural Networks for Single-Species Vapor-Liquid Equilibria
**arXiv**：[2602.18313v1](https://arxiv.org/abs/2602.18313) · [PDF](https://arxiv.org/pdf/2602.18313.pdf)  
**作者**：Jan Pavšek, Alexander Mitsos, Elvis J. Sim, Jan G. Rittig  

**一句话要点**：提出Clapeyron图神经网络以解决数据稀缺下纯组分气液平衡预测的热力学一致性问题

**关键词**：热力学感知机器学习, 图神经网络, 气液平衡预测, 多任务学习, Clapeyron方程

## 3 点简述
- 核心问题：机器学习预测分子性质常受实验数据稀缺和缺乏热力学一致性限制
- 方法要点：将Clapeyron方程融入损失函数，以多任务方式预测纯组分性质
- 实验或效果：相比单任务学习提升预测精度，在数据稀缺场景下改进最大

## 摘要（原文）

> Machine learning (ML) approaches have shown promising results for predicting molecular properties relevant for chemical process design. However, they are often limited by scarce experimental property data and lack thermodynamic consistency. As such, thermodynamics-informed ML, i.e., incorporating thermodynamic relations into the loss function as regularization term for training, has been proposed. We herein transfer the concept of thermodynamics-informed graph neural networks (GNNs) from the Gibbs-Duhem to the Clapeyron equation, predicting several pure component properties in a multi-task manner, namely: vapor pressure, liquid molar volume, vapor molar volume and enthalpy of vaporization. We find improved prediction accuracy of the Clapeyron-GNN compared to the single-task learning setting, and improved approximation of the Clapeyron equation compared to the purely data-driven multi-task learning setting. In fact, we observe the largest improvement in prediction accuracy for the properties with the lowest availability of data, making our model promising for practical application in data scarce scenarios of chemical engineering practice.

