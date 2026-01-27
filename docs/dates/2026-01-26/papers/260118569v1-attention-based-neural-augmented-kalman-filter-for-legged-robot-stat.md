---
layout: default
title: Attention-Based Neural-Augmented Kalman Filter for Legged Robot State Estimation
---

# Attention-Based Neural-Augmented Kalman Filter for Legged Robot State Estimation
**arXiv**：[2601.18569v1](https://arxiv.org/abs/2601.18569) · [PDF](https://arxiv.org/pdf/2601.18569.pdf)  
**作者**：Seokju Lee, Kyung-Soo Kim  

**一句话要点**：提出基于注意力的神经增强卡尔曼滤波器以解决足式机器人滑移状态估计问题

**关键词**：足式机器人, 状态估计, 卡尔曼滤波, 注意力机制, 神经补偿, 滑移检测

## 3 点简述
- 核心问题：足滑移导致运动学测量违反无滑移假设，引入估计偏差。
- 方法要点：在不变扩展卡尔曼滤波器中添加基于注意力的神经补偿器，推断滑移误差并进行后更新补偿。
- 实验或效果：在易滑移条件下，相比现有方法性能提升。

## 摘要（原文）

> In this letter, we propose an Attention-Based Neural-Augmented Kalman Filter (AttenNKF) for state estimation in legged robots. Foot slip is a major source of estimation error: when slip occurs, kinematic measurements violate the no-slip assumption and inject bias during the update step. Our objective is to estimate this slip-induced error and compensate for it. To this end, we augment an Invariant Extended Kalman Filter (InEKF) with a neural compensator that uses an attention mechanism to infer error conditioned on foot-slip severity and then applies this estimate as a post-update compensation to the InEKF state (i.e., after the filter update). The compensator is trained in a latent space, which aims to reduce sensitivity to raw input scales and encourages structured slip-conditioned compensations, while preserving the InEKF recursion. Experiments demonstrate improved performance compared to existing legged-robot state estimators, particularly under slip-prone conditions.

