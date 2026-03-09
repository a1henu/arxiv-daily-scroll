---
layout: default
title: KISS-IMU: Self-supervised Inertial Odometry with Motion-balanced Learning and Uncertainty-aware Inference
---

# KISS-IMU: Self-supervised Inertial Odometry with Motion-balanced Learning and Uncertainty-aware Inference
**arXiv**：[2603.06205v1](https://arxiv.org/abs/2603.06205) · [PDF](https://arxiv.org/pdf/2603.06205.pdf)  
**作者**：Jiwon Choi, Hogyun Kim, Geonmo Yang, Juhui Lee, Younggun Cho  

**一句话要点**：提出KISS-IMU自监督惯性里程计框架，通过运动平衡学习和不确定性推理消除地面真值依赖。

**关键词**：惯性里程计, 自监督学习, 运动平衡训练, 不确定性推理, LiDAR监督, 机器人导航

## 3 点简述
- 核心问题：惯性里程计训练严重依赖地面真值，限制在未知和多样化环境中的可扩展性和泛化能力。
- 方法要点：利用LiDAR ICP配准和位姿图优化作为监督信号，结合运动感知平衡训练和不确定性驱动自适应加权。
- 实验或效果：在包括四足机器人的多种真实平台进行实验，验证了框架的鲁棒性和性能。

## 摘要（原文）

> Inertial measurement units (IMUs), which provide high-frequency linear acceleration and angular velocity measurements, serve as fundamental sensing modalities in robotic systems. Recent advances in deep neural networks have led to remarkable progress in inertial odometry. However, the heavy reliance on ground truth data during training fundamentally limits scalability and generalization to unseen and diverse environments. We propose KISS-IMU, a novel self-supervised inertial odometry framework that eliminates ground truth dependency by leveraging simple LiDAR-based ICP registration and pose graph optimization as a supervisory signal. Our approach embodies two key principles: keeping the IMU stable through motion-aware balanced training and keeping the IMU strong through uncertainty-driven adaptive weighting during inference. To evaluate performance across diverse motion patterns and scenarios, we conducted comprehensive experiments on various real-world platforms, including quadruped robots. Importantly, we train only the IMU network in a self-supervised manner, with LiDAR serving solely as a lightweight supervisory signal rather than requiring additional learnable processes. This design enables the framework to ensure robustness without relying on joint multi-modal learning or ground truth supervision. The supplementary materials are available at https://sparolab.github.io/research/kiss_imu.

