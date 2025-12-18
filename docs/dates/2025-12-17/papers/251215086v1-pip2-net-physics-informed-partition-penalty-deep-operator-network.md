---
layout: default
title: PIP$^2$ Net: Physics-informed Partition Penalty Deep Operator Network
---

# PIP$^2$ Net: Physics-informed Partition Penalty Deep Operator Network
**arXiv**：[2512.15086v1](https://arxiv.org/abs/2512.15086) · [PDF](https://arxiv.org/pdf/2512.15086.pdf)  
**作者**：Hongjin Mi, Huiqiang Lun, Changhong Mou, Yeyu Zhang  

**一句话要点**：提出PIP² Net以改进DeepONet，通过分区惩罚正则化提升参数化偏微分方程算子学习的准确性和鲁棒性。

**关键词**：算子学习, 偏微分方程求解, 分区统一正则化, 物理信息神经网络, DeepONet改进, 非线性系统建模

## 3 点简述
- 现有算子学习方法如DeepONet和FNO需要大数据集、缺乏物理结构且特征不稳定。
- 基于分区统一方法，引入简化的分区惩罚正则化，协调分支网络输出以增强表达能力。
- 在非线性偏微分方程上测试，PIP² Net在预测精度和鲁棒性上优于多种基线模型。

## 摘要（原文）

> Operator learning has become a powerful tool for accelerating the solution of parameterized partial differential equations (PDEs), enabling rapid prediction of full spatiotemporal fields for new initial conditions or forcing functions. Existing architectures such as DeepONet and the Fourier Neural Operator (FNO) show strong empirical performance but often require large training datasets, lack explicit physical structure, and may suffer from instability in their trunk-network features, where mode imbalance or collapse can hinder accurate operator approximation. Motivated by the stability and locality of classical partition-of-unity (PoU) methods, we investigate PoU-based regularization techniques for operator learning and develop a revised formulation of the existing POU--PI--DeepONet framework. The resulting \emph{P}hysics-\emph{i}nformed \emph{P}artition \emph{P}enalty Deep Operator Network (PIP$^{2}$ Net) introduces a simplified and more principled partition penalty that improved the coordinated trunk outputs that leads to more expressiveness without sacrificing the flexibility of DeepONet. We evaluate PIP$^{2}$ Net on three nonlinear PDEs: the viscous Burgers equation, the Allen--Cahn equation, and a diffusion--reaction system. The results show that it consistently outperforms DeepONet, PI-DeepONet, and POU-DeepONet in prediction accuracy and robustness.

