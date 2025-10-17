---
layout: default
title: Proprioceptive Image: An Image Representation of Proprioceptive Data from Quadruped Robots for Contact Estimation Learning
---

# Proprioceptive Image: An Image Representation of Proprioceptive Data from Quadruped Robots for Contact Estimation Learning
**arXiv**：[2510.14612v1](https://arxiv.org/abs/2510.14612) · [PDF](https://arxiv.org/pdf/2510.14612.pdf)  
**作者**：Gabriel Fischer Abati, João Carlos Virgolino Soares, Giulio Turrisi, Victor Barasuol, Claudio Semini  

**一句话要点**：提出将四足机器人本体感觉数据编码为图像的方法，以提升接触估计性能。

**关键词**：四足机器人, 本体感觉数据编码, 卷积神经网络, 接触估计, 跨模态学习

## 3 点简述
- 核心问题：四足机器人在多变地形中稳定运动需准确估计接触状态。
- 方法要点：将多源本体感觉数据编码为结构化图像，保留时空动态和形态结构。
- 实验效果：在真实和模拟数据上，接触估计准确率从87.7%提升至94.5%。

## 摘要（原文）

> This paper presents a novel approach for representing proprioceptive
> time-series data from quadruped robots as structured two-dimensional images,
> enabling the use of convolutional neural networks for learning
> locomotion-related tasks. The proposed method encodes temporal dynamics from
> multiple proprioceptive signals, such as joint positions, IMU readings, and
> foot velocities, while preserving the robot's morphological structure in the
> spatial arrangement of the image. This transformation captures inter-signal
> correlations and gait-dependent patterns, providing a richer feature space than
> direct time-series processing. We apply this concept in the problem of contact
> estimation, a key capability for stable and adaptive locomotion on diverse
> terrains. Experimental evaluations on both real-world datasets and simulated
> environments show that our image-based representation consistently enhances
> prediction accuracy and generalization over conventional sequence-based models,
> underscoring the potential of cross-modal encoding strategies for robotic state
> learning. Our method achieves superior performance on the contact dataset,
> improving contact state accuracy from 87.7% to 94.5% over the recently proposed
> MI-HGNN method, using a 15 times shorter window size.

