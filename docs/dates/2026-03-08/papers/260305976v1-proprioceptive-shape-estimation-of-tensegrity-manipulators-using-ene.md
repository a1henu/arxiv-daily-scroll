---
layout: default
title: Proprioceptive Shape Estimation of Tensegrity Manipulators Using Energy Minimisation
---

# Proprioceptive Shape Estimation of Tensegrity Manipulators Using Energy Minimisation
**arXiv**：[2603.05976v1](https://arxiv.org/abs/2603.05976) · [PDF](https://arxiv.org/pdf/2603.05976.pdf)  
**作者**：Tufail Ahmad Bhat, Shuhei Ikemoto  

**一句话要点**：提出基于能量最小化的本体感知形状估计方法，用于连续弯曲张拉整体机械臂

**关键词**：张拉整体机械臂, 形状估计, 能量最小化, 本体感知, 倾角传感器, 惯性测量单元

## 3 点简述
- 核心问题：连续弯曲张拉整体机械臂的形状估计困难，外感知方法成本高且环境受限。
- 方法要点：仅利用各撑杆相对于重力的倾角信息，通过能量最小化实现全机械臂形状估计。
- 实验或效果：在五层20撑杆机械臂上验证，静态和扰动下估计精度达总长度的2.1%。

## 摘要（原文）

> Shape estimation is fundamental for controlling continuously bending tensegrity manipulators, yet achieving it remains a challenge. Although using exteroceptive sensors makes the implementation straightforward, it is costly and limited to specific environments. Proprioceptive approaches, by contrast, do not suffer from these limitations. So far, several methods have been proposed; however, to our knowledge, there are no proven examples of large-scale tensegrity structures used as manipulators. This paper demonstrates that shape estimation of the entire tensegrity manipulator can be achieved using only the inclination angle information relative to gravity for each strut. Inclination angle information is intrinsic sensory data that can be obtained simply by attaching an inertial measurement unit (IMU) to each strut. Experiments conducted on a five-layer tensegrity manipulator with 20 struts and a total length of 1160 mm demonstrate that the proposed method can estimate the shape with an accuracy of 2.1 \% of the total manipulator length, from arbitrary initial conditions under both static conditions and maintains stable shape estimation under external disturbances.

