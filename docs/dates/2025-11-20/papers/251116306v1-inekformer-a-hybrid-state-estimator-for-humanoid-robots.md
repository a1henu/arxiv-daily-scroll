---
layout: default
title: InEKFormer: A Hybrid State Estimator for Humanoid Robots
---

# InEKFormer: A Hybrid State Estimator for Humanoid Robots
**arXiv**：[2511.16306v1](https://arxiv.org/abs/2511.16306) · [PDF](https://arxiv.org/pdf/2511.16306.pdf)  
**作者**：Lasse Hohmeyer, Mihaela Popescu, Ivan Bergonzani, Dennis Mronga, Frank Kirchner  

**一句话要点**：提出InEKFormer混合状态估计方法以提升人形机器人动态运动稳定性

**关键词**：人形机器人, 状态估计, 混合方法, Transformer网络, 不变扩展卡尔曼滤波

## 3 点简述
- 核心问题：人形机器人在不同环境中双足运动难以保持稳定和动态平衡
- 方法要点：结合不变扩展卡尔曼滤波和Transformer网络进行状态估计
- 实验或效果：在RH5机器人数据集上优于InEKF和KalmanNet方法

## 摘要（原文）

> Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

