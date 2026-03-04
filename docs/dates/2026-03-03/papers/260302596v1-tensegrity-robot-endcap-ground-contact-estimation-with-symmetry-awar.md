---
layout: default
title: Tensegrity Robot Endcap-Ground Contact Estimation with Symmetry-aware Heterogeneous Graph Neural Network
---

# Tensegrity Robot Endcap-Ground Contact Estimation with Symmetry-aware Heterogeneous Graph Neural Network
**arXiv**：[2603.02596v1](https://arxiv.org/abs/2603.02596) · [PDF](https://arxiv.org/pdf/2603.02596.pdf)  
**作者**：Wenzhe Tong, Yicheng Jiang, Chi Zhang, Maani Ghaffari, Xiaonan Huang  

**一句话要点**：提出对称感知异构图神经网络以解决张拉整体机器人无专用传感器下的接触状态估计问题

**关键词**：张拉整体机器人, 接触状态估计, 异构图神经网络, 对称感知学习, 本体感知传感, 状态估计

## 3 点简述
- 张拉整体机器人因柔顺分布式地面接触导致状态估计困难
- 方法利用本体感知数据，结合D3对称性提升样本效率和泛化能力
- 仿真显示仅用20%训练数据，精度和F1分数分别提升15%和5%

## 摘要（原文）

> Tensegrity robots possess lightweight and resilient structures but present significant challenges for state estimation due to compliant and distributed ground contacts. This paper introduces a symmetry-aware heterogeneous graph neural network (Sym-HGNN) that infers contact states directly from proprioceptive measurements, including IMU and cable-length histories, without dedicated contact sensors. The network incorporates the robot's dihedral symmetry $D_3$ into the message-passing process to enhance sample efficiency and generalization. The predicted contacts are integrated into a state-of-the-art contact-aided invariant extended Kalman filter (InEKF) for improved pose estimation. Simulation results demonstrate that the proposed method achieves up to 15% higher accuracy and 5% higher F1-score using only 20% of the training data compared to the CNN and MI-HGNN baselines, while maintaining low-drift and physically consistent state estimation results comparable to ground truth contacts. This work highlights the potential of fully proprioceptive sensing for accurate and robust state estimation in tensegrity robots. Code available at: https://github.com/Jonathan-Twz/Tensegrity-Sym-HGNN

