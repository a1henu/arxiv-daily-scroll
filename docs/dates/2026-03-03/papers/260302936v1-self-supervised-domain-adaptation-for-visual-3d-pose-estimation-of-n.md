---
layout: default
title: Self-supervised Domain Adaptation for Visual 3D Pose Estimation of Nano-drone Racing Gates by Enforcing Geometric Consistency
---

# Self-supervised Domain Adaptation for Visual 3D Pose Estimation of Nano-drone Racing Gates by Enforcing Geometric Consistency
**arXiv**：[2603.02936v1](https://arxiv.org/abs/2603.02936) · [PDF](https://arxiv.org/pdf/2603.02936.pdf)  
**作者**：Nicholas Carlotti, Michele Antonazzi, Elia Cereda, Mirko Nava, Nicola Basilico, Daniele Palossi, Alessandro Giusti  

**一句话要点**：提出基于几何一致性的自监督域适应方法，以提升纳米无人机视觉3D姿态估计的精度。

**关键词**：视觉3D姿态估计, 无监督域适应, 自监督学习, 几何一致性, 纳米无人机, 模拟到真实迁移

## 3 点简述
- 核心问题：模拟到真实域差距导致预训练模型在真实场景中性能下降。
- 方法要点：利用无人机飞行轨迹中的图像序列，通过状态一致性损失强制几何一致性进行无监督域适应。
- 实验或效果：在真实数据上位置误差降低40%，方向误差降低37%，推理时间达30.4ms。

## 摘要（原文）

> We consider the task of visually estimating the relative pose of a drone racing gate in front of a nano-quadrotor, using a convolutional neural network pre-trained on simulated data to regress the gate's pose. Due to the sim-to-real gap, the pre-trained model underperforms in the real world and must be adapted to the target domain. We propose an unsupervised domain adaptation (UDA) approach using only real image sequences collected by the drone flying an arbitrary trajectory in front of a gate; sequences are annotated in a self-supervised fashion with the drone's odometry as measured by its onboard sensors. On this dataset, a state consistency loss enforces that two images acquired at different times yield pose predictions that are consistent with the drone's odometry. Results indicate that our approach outperforms other SoA UDA approaches, has a low mean absolute error in position (x=26, y=28, z=10 cm) and orientation ($ψ$=13${^{\circ}}$), an improvement of 40% in position and 37% in orientation over a baseline. The approach's effectiveness is appreciable with as few as 10 minutes of real-world flight data and yields models with an inference time of 30.4ms (33 fps) when deployed aboard the Crazyflie 2.1 Brushless nano-drone.

