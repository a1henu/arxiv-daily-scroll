---
layout: default
title: A Hybrid Model-based and Data-based Approach Developed for a Prosthetic Hand Wrist
---

# A Hybrid Model-based and Data-based Approach Developed for a Prosthetic Hand Wrist
**arXiv**：[2601.08711v1](https://arxiv.org/abs/2601.08711) · [PDF](https://arxiv.org/pdf/2601.08711.pdf)  
**作者**：Shifa Sulaiman, Francesco Schetter, Mehul Menon, Fanny Ficuciello  

**一句话要点**：提出结合人工神经网络与滑模控制的混合控制器，用于PRISMA HAND II假手手腕的快速动态响应。

**关键词**：假手控制, 混合控制器, 人工神经网络, 滑模控制, 分段恒定曲率, 肌腱驱动手腕

## 3 点简述
- 核心问题：假手手腕需快速动态响应且计算量小，以模拟人手精细运动。
- 方法要点：使用人工神经网络计算弯曲角度，滑模控制器调节肌腱力，基于分段恒定曲率假设建模。
- 实验或效果：通过仿真和实验验证，与其他控制策略比较，展示性能提升。

## 摘要（原文）

> The incorporation of advanced control algorithms into prosthetic hands significantly enhances their ability to replicate the intricate motions of a human hand. This work introduces a model-based controller that combines an Artificial Neural Network (ANN) approach with a Sliding Mode Controller (SMC) designed for a tendon-driven soft continuum wrist integrated into a prosthetic hand known as "PRISMA HAND II". Our research focuses on developing a controller that provides a fast dynamic response with reduced computational effort during wrist motions. The proposed controller consists of an ANN for computing bending angles together with an SMC to regulate tendon forces. Kinematic and dynamic models of the wrist are formulated using the Piece-wise Constant Curvature (PCC) hypothesis. The performance of the proposed controller is compared with other control strategies developed for the same wrist. Simulation studies and experimental validations of the fabricated wrist using the controller are included in the paper.

