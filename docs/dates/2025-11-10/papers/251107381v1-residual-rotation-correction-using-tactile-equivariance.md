---
layout: default
title: Residual Rotation Correction using Tactile Equivariance
---

# Residual Rotation Correction using Tactile Equivariance
**arXiv**：[2511.07381v1](https://arxiv.org/abs/2511.07381) · [PDF](https://arxiv.org/pdf/2511.07381.pdf)  
**作者**：Yizhe Zhu, Zhang Ye, Boce Hu, Haibo Zhao, Yu Qi, Dian Wang, Robert Platt  

**一句话要点**：提出EquiTac框架，利用触觉等变性改进触觉视觉策略学习中的样本效率与泛化能力。

**关键词**：触觉视觉策略学习, SO(2)等变性, 样本效率, 残差旋转校正, 零样本泛化

## 3 点简述
- 触觉数据收集成本高，样本效率是触觉视觉策略学习的关键问题。
- 方法利用SO(2)对称性，通过等变网络预测残差旋转动作，增强基础策略。
- 实验显示，在真实机器人上实现零样本泛化，仅需少量训练样本。

## 摘要（原文）

> Visuotactile policy learning augments vision-only policies with tactile
> input, facilitating contact-rich manipulation. However, the high cost of
> tactile data collection makes sample efficiency the key requirement for
> developing visuotactile policies. We present EquiTac, a framework that exploits
> the inherent SO(2) symmetry of in-hand object rotation to improve sample
> efficiency and generalization for visuotactile policy learning. EquiTac first
> reconstructs surface normals from raw RGB inputs of vision-based tactile
> sensors, so rotations of the normal vector field correspond to in-hand object
> rotations. An SO(2)-equivariant network then predicts a residual rotation
> action that augments a base visuomotor policy at test time, enabling real-time
> rotation correction without additional reorientation demonstrations. On a real
> robot, EquiTac accurately achieves robust zero-shot generalization to unseen
> in-hand orientations with very few training samples, where baselines fail even
> with more training data. To our knowledge, this is the first tactile learning
> method to explicitly encode tactile equivariance for policy learning, yielding
> a lightweight, symmetry-aware module that improves reliability in contact-rich
> tasks.

