---
layout: default
title: RaCo: Ranking and Covariance for Practical Learned Keypoints
---

# RaCo: Ranking and Covariance for Practical Learned Keypoints
**arXiv**：[2602.15755v1](https://arxiv.org/abs/2602.15755) · [PDF](https://arxiv.org/pdf/2602.15755.pdf)  
**作者**：Abhiram Shenoi, Philipp Lindenberger, Paul-Edouard Sarlin, Marc Pollefeys  

**一句话要点**：提出RaCo轻量神经网络，通过排名与协方差学习鲁棒关键点，适用于3D视觉任务。

**关键词**：关键点检测, 3D计算机视觉, 可微分排名, 协方差估计, 旋转鲁棒性, 轻量神经网络

## 3 点简述
- 核心问题：学习鲁棒且通用的关键点，无需共视图像对，应对大旋转等挑战。
- 方法要点：集成可重复检测器、可微分排名器和协方差估计器，仅用透视图像裁剪训练。
- 实验或效果：在多个数据集上实现关键点可重复性和两视图匹配的先进性能，尤其在大平面旋转下。

## 摘要（原文）

> This paper introduces RaCo, a lightweight neural network designed to learn robust and versatile keypoints suitable for a variety of 3D computer vision tasks. The model integrates three key components: the repeatable keypoint detector, a differentiable ranker to maximize matches with a limited number of keypoints, and a covariance estimator to quantify spatial uncertainty in metric scale. Trained on perspective image crops only, RaCo operates without the need for covisible image pairs. It achieves strong rotational robustness through extensive data augmentation, even without the use of computationally expensive equivariant network architectures. The method is evaluated on several challenging datasets, where it demonstrates state-of-the-art performance in keypoint repeatability and two-view matching, particularly under large in-plane rotations. Ultimately, RaCo provides an effective and simple strategy to independently estimate keypoint ranking and metric covariance without additional labels, detecting interpretable and repeatable interest points. The code is available at https://github.com/cvg/RaCo.

