---
layout: default
title: Learning functional components of PDEs from data using neural networks
---

# Learning functional components of PDEs from data using neural networks
**arXiv**：[2602.13174v1](https://arxiv.org/abs/2602.13174) · [PDF](https://arxiv.org/pdf/2602.13174.pdf)  
**作者**：Torkel E. Loman, Yurij Salmaniw, Antonio Leon Villares, Jose A. Carrillo, Ruth E. Baker  

**一句话要点**：提出嵌入神经网络的PDE函数恢复方法，从稳态数据中学习未知函数组件。

**关键词**：偏微分方程函数恢复, 神经网络嵌入, 非局部方程, 稳态数据学习, 参数拟合工作流

## 3 点简述
- 核心问题：偏微分方程中的未知函数难以直接测量，阻碍模型预测。
- 方法要点：将神经网络嵌入PDE，通过数据训练近似未知函数，利用标准参数拟合流程。
- 实验或效果：以非局部聚集-扩散方程为例，从稳态数据恢复交互核和外部势，分析数据量、噪声等因素影响。

## 摘要（原文）

> Partial differential equations often contain unknown functions that are difficult or impossible to measure directly, hampering our ability to derive predictions from the model. Workflows for recovering scalar PDE parameters from data are well studied: here we show how similar workflows can be used to recover functions from data. Specifically, we embed neural networks into the PDE and show how, as they are trained on data, they can approximate unknown functions with arbitrary accuracy. Using nonlocal aggregation-diffusion equations as a case study, we recover interaction kernels and external potentials from steady state data. Specifically, we investigate how a wide range of factors, such as the number of available solutions, their properties, sampling density, and measurement noise, affect our ability to successfully recover functions. Our approach is advantageous because it can utilise standard parameter-fitting workflows, and in that the trained PDE can be treated as a normal PDE for purposes such as generating system predictions.

