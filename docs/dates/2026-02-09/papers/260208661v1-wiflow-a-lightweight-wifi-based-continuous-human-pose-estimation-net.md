---
layout: default
title: WiFlow: A Lightweight WiFi-based Continuous Human Pose Estimation Network with Spatio-Temporal Feature Decoupling
---

# WiFlow: A Lightweight WiFi-based Continuous Human Pose Estimation Network with Spatio-Temporal Feature Decoupling
**arXiv**：[2602.08661v1](https://arxiv.org/abs/2602.08661) · [PDF](https://arxiv.org/pdf/2602.08661.pdf)  
**作者**：Yi Dao, Lankai Zhang, Hao Liu, Haiwei Zhang, Wenbo Wang  

**一句话要点**：提出WiFlow框架，通过时空特征解耦实现基于WiFi的连续人体姿态估计，降低计算开销。

**关键词**：WiFi姿态估计, 时空特征解耦, 编码器-解码器架构, 轴向注意力, 轻量化网络, 连续运动估计

## 3 点简述
- 核心问题：现有WiFi方法在连续运动估计中面临计算复杂度和性能挑战。
- 方法要点：采用编码器-解码器架构，结合时空卷积和轴向注意力捕获CSI特征。
- 实验或效果：在自建数据集上PCK@20达97.00%，参数仅4.82M，显著提升效率。

## 摘要（原文）

> Human pose estimation is fundamental to intelligent perception in the Internet of Things (IoT), enabling applications ranging from smart healthcare to human-computer interaction. While WiFi-based methods have gained traction, they often struggle with continuous motion and high computational overhead. This work presents WiFlow, a novel framework for continuous human pose estimation using WiFi signals. Unlike vision-based approaches such as two-dimensional deep residual networks that treat Channel State Information (CSI) as images, WiFlow employs an encoder-decoder architecture. The encoder captures spatio-temporal features of CSI using temporal and asymmetric convolutions, preserving the original sequential structure of signals. It then refines keypoint features of human bodies to be tracked and capture their structural dependencies via axial attention. The decoder subsequently maps the encoded high-dimensional features into keypoint coordinates. Trained on a self-collected dataset of 360,000 synchronized CSI-pose samples from 5 subjects performing continuous sequences of 8 daily activities, WiFlow achieves a Percentage of Correct Keypoints (PCK) of 97.00% at a threshold of 20% (PCK@20) and 99.48% at PCK@50, with a mean per-joint position error of 0.008m. With only 4.82M parameters, WiFlow significantly reduces model complexity and computational cost, establishing a new performance baseline for practical WiFi-based human pose estimation. Our code and datasets are available at https://github.com/DY2434/WiFlow-WiFi-Pose-Estimation-with-Spatio-Temporal-Decoupling.git.

