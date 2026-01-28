---
layout: default
title: Mocap Anywhere: Towards Pairwise-Distance based Motion Capture in the Wild (for the Wild)
---

# Mocap Anywhere: Towards Pairwise-Distance based Motion Capture in the Wild (for the Wild)
**arXiv**：[2601.19519v1](https://arxiv.org/abs/2601.19519) · [PDF](https://arxiv.org/pdf/2601.19519.pdf)  
**作者**：Ofir Abramovich, Ariel Shamir, Andreas Aristidou  

**一句话要点**：提出基于稀疏成对距离测量的运动捕捉系统，用于野外环境下的全身3D运动重建。

**关键词**：运动捕捉, 成对距离测量, Transformer架构, 野外环境, 实时重建, 形状不变性

## 3 点简述
- 核心问题：传统运动捕捉系统依赖外部摄像头或惯性传感器，在野外环境中易受光照、磁场等干扰，难以实现鲁棒操作。
- 方法要点：使用身体佩戴的UWB传感器进行飞行时间测距，获取稀疏成对距离测量；提出Wild-Poser（WiP）架构，基于Transformer实时预测3D关节位置，无需个体身体测量或形状拟合。
- 实验或效果：WiP在实时操作下实现低关节位置误差，适用于不同形态的人类和非人类物种，在野外环境中准确重建3D运动。

## 摘要（原文）

> We introduce a novel motion capture system that reconstructs full-body 3D motion using only sparse pairwise distance (PWD) measurements from body-mounted(UWB) sensors. Using time-of-flight ranging between wireless nodes, our method eliminates the need for external cameras, enabling robust operation in uncontrolled and outdoor environments. Unlike traditional optical or inertial systems, our approach is shape-invariant and resilient to environmental constraints such as lighting and magnetic interference. At the core of our system is Wild-Poser (WiP for short), a compact, real-time Transformer-based architecture that directly predicts 3D joint positions from noisy or corrupted PWD measurements, which can later be used for joint rotation reconstruction via learned methods. WiP generalizes across subjects of varying morphologies, including non-human species, without requiring individual body measurements or shape fitting. Operating in real time, WiP achieves low joint position error and demonstrates accurate 3D motion reconstruction for both human and animal subjects in-the-wild. Our empirical analysis highlights its potential for scalable, low-cost, and general purpose motion capture in real-world settings.

