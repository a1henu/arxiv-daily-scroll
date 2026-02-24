---
layout: default
title: TactiVerse: Generalizing Multi-Point Tactile Sensing in Soft Robotics Using Single-Point Data
---

# TactiVerse: Generalizing Multi-Point Tactile Sensing in Soft Robotics Using Single-Point Data
**arXiv**：[2602.19850v1](https://arxiv.org/abs/2602.19850) · [PDF](https://arxiv.org/pdf/2602.19850.pdf)  
**作者**：Junhui Lee, Hyosung Kim, Saekwang Nam  

**一句话要点**：提出TactiVerse框架，基于单点数据实现软体机器人多点触觉感知泛化

**关键词**：软体机器人, 触觉感知, U-Net, 空间热图预测, 多点接触估计, 数据增强

## 3 点简述
- 核心问题：软体材料变形实时预测困难，现有模型泛化能力有限，尤其在多点感知场景。
- 方法要点：采用U-Net架构，将接触几何估计建模为空间热图预测任务，利用单点压痕数据训练。
- 实验或效果：单点感知误差优于基线，多点感知通过数据增强显著提升，MAE从1.214毫米降至0.383毫米。

## 摘要（原文）

> Real-time prediction of deformation in highly compliant soft materials remains a significant challenge in soft robotics. While vision-based soft tactile sensors can track internal marker displacements, learning-based models for 3D contact estimation heavily depend on their training datasets, inherently limiting their ability to generalize to complex scenarios such as multi-point sensing. To address this limitation, we introduce TactiVerse, a U-Net-based framework that formulates contact geometry estimation as a spatial heatmap prediction task. Even when trained exclusively on a limited dataset of single-point indentations, our architecture achieves highly accurate single-point sensing, yielding a superior mean absolute error of 0.0589 mm compared to the 0.0612 mm of a conventional regression-based CNN baseline. Furthermore, we demonstrate that augmenting the training dataset with multi-point contact data substantially enhances the sensor's multi-point sensing capabilities, significantly improving the overall mean MAE for two-point discrimination from 1.214 mm to 0.383 mm. By successfully extrapolating complex contact geometries from fundamental interactions, this methodology unlocks advanced multi-point and large-area shape sensing. Ultimately, it significantly streamlines the development of marker-based soft sensors, offering a highly scalable solution for real-world tactile perception.

