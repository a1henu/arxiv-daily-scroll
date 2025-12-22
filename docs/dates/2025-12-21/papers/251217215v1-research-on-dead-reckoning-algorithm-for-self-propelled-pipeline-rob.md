---
layout: default
title: Research on Dead Reckoning Algorithm for Self-Propelled Pipeline Robots in Three-Dimensional Complex Pipelines
---

# Research on Dead Reckoning Algorithm for Self-Propelled Pipeline Robots in Three-Dimensional Complex Pipelines
**arXiv**：[2512.17215v1](https://arxiv.org/abs/2512.17215) · [PDF](https://arxiv.org/pdf/2512.17215.pdf)  
**作者**：Yan Gao, Jiliang Wang, Minghan Wang, Xiaohua Chen, Demin Chen, Zhiyong Ren, Tian-Yun Huang  

**一句话要点**：提出基于扩展卡尔曼滤波的管道机器人航位推算算法，用于三维复杂管道定位。

**关键词**：管道机器人, 航位推算, 扩展卡尔曼滤波, 惯性导航, 轮式里程计, 三维管道定位

## 3 点简述
- 针对复杂弯曲管道中传统定位方法因电缆缠绕和设备灵活性不足而失效的问题。
- 采用惯性导航与轮式里程计融合，通过扩展卡尔曼滤波提高姿态角估计精度。
- 在矩形循环管道实验中验证了自驱动机器人算法的有效性，平衡运动能力与定位精度。

## 摘要（原文）

> In the field of gas pipeline location, existing pipeline location methods mostly rely on pipeline location instruments. However, when faced with complex and curved pipeline scenarios, these methods often fail due to problems such as cable entanglement and insufficient equipment flexibility. To address this pain point, we designed a self-propelled pipeline robot. This robot can autonomously complete the location work of complex and curved pipelines in complex pipe networks without external dragging. In terms of pipeline mapping technology, traditional visual mapping and laser mapping methods are easily affected by lighting conditions and insufficient features in the confined space of pipelines, resulting in mapping drift and divergence problems. In contrast, the pipeline location method that integrates inertial navigation and wheel odometers is less affected by pipeline environmental factors. Based on this, this paper proposes a pipeline robot location method based on extended Kalman filtering (EKF). Firstly, the body attitude angle is initially obtained through an inertial measurement unit (IMU). Then, the extended Kalman filtering algorithm is used to improve the accuracy of attitude angle estimation. Finally, high-precision pipeline location is achieved by combining wheel odometers. During the testing phase, the roll wheels of the pipeline robot needed to fit tightly against the pipe wall to reduce slippage. However, excessive tightness would reduce the flexibility of motion control due to excessive friction. Therefore, a balance needed to be struck between the robot's motion capability and positioning accuracy. Experiments were conducted using the self-propelled pipeline robot in a rectangular loop pipeline, and the results verified the effectiveness of the proposed dead reckoning algorithm.

