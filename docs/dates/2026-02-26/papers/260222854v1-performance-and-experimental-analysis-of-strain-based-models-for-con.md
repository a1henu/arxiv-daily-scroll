---
layout: default
title: Performance and Experimental Analysis of Strain-based Models for Continuum Robots
---

# Performance and Experimental Analysis of Strain-based Models for Continuum Robots
**arXiv**：[2602.22854v1](https://arxiv.org/abs/2602.22854) · [PDF](https://arxiv.org/pdf/2602.22854.pdf)  
**作者**：Annika Delucchi, Vincenzo Di Paola, Andreas Müller, and Matteo Zoppi  

**一句话要点**：提出应变插值模型评估方法，通过实验验证连续体机器人形状重建性能

**关键词**：连续体机器人, 应变模型, 形状重建, 性能评估, 实验验证

## 3 点简述
- 核心问题：应变模型缺乏统一性能评估标准，需验证其在连续体机器人中的适用性
- 方法要点：比较三阶应变插值法与几何变量应变法，分析单独和组合变形效应
- 实验或效果：实验显示模型预测与观测形状吻合良好，平均误差0.58%长度，计算时间0.32s

## 摘要（原文）

> Although strain-based models have been widely adopted in robotics, no comparison beyond the uniform bending test is commonly recognized to assess their performance. In addition, the increasing effort in prototyping continuum robots highlights the need to assess the applicability of these models and the necessity of comprehensive performance evaluation. To address this gap, this work investigates the shape reconstruction abilities of a third-order strain interpolation method, examining its ability to capture both individual and combined deformation effects. These results are compared and discussed against the Geometric-Variable Strain approach. Subsequently, simulation results are experimentally verified by reshaping a slender rod while recording the resulting configurations using cameras. The rod configuration is imposed using a manipulator displacing one of its tips and extracted through reflective markers, without the aid of any other external sensor -- i.e. strain gauges or wrench sensors placed along the rod. The experiments demonstrate good agreement between the model predictions and observed shapes, with average error of 0.58% of the rod length and average computational time of 0.32s per configuration, outperforming existing models.

