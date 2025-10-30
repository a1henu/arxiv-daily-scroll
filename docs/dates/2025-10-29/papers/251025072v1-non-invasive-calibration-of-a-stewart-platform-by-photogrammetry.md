---
layout: default
title: Non-Invasive Calibration Of A Stewart Platform By Photogrammetry
---

# Non-Invasive Calibration Of A Stewart Platform By Photogrammetry
**arXiv**：[2510.25072v1](https://arxiv.org/abs/2510.25072) · [PDF](https://arxiv.org/pdf/2510.25072.pdf)  
**作者**：Sourabh Karmakar, Cameron J. Turner  

**一句话要点**：提出基于摄影测量的非侵入式Stewart平台校准方法，以解决正向运动学校准难题。

**关键词**：Stewart平台校准, 摄影测量, 正向运动学, 最小二乘法, 非侵入式方法, 位姿精度

## 3 点简述
- 核心问题：Stewart平台正向运动学校准复杂，易产生多解且难以高效实现。
- 方法要点：使用Denavit-Hartenberg约定和摄影测量，无需硬件改动，通过多角度图像测量平台位姿。
- 实验或效果：采用最小二乘法补偿误差，三种策略均显著提升位姿精度，显示进一步改进空间。

## 摘要（原文）

> Accurate calibration of a Stewart platform is important for their precise and
> efficient operation. However, the calibration of these platforms using forward
> kinematics is a challenge for researchers because forward kinematics normally
> generates multiple feasible and unfeasible solutions for any pose of the moving
> platform. The complex kinematic relations among the six actuator paths
> connecting the fixed base to the moving platform further compound the
> difficulty in establishing a straightforward and efficient calibration method.
> The authors developed a new forward kinematics-based calibration method using
> Denavit-Hartenberg convention and used the Stewart platform Tiger 66.1
> developed in their lab for experimenting with the photogrammetry-based
> calibration strategies described in this paper. This system became operational
> upon completion of construction, marking its inaugural use. The authors used
> their calibration model for estimating the errors in the system and adopted
> three compensation options or strategies as per Least Square method to improve
> the accuracy of the system. These strategies leveraged a high-resolution
> digital camera and off-the-shelf software to capture the poses of the moving
> platform's center. This process is non-invasive and does not need any
> additional equipment to be attached to the hexapod or any alteration of the
> hexapod hardware. This photogrammetry-based calibration process involves
> multiple high-resolution images from different angles to measure the position
> and orientation of the platform center in the three-dimensional space. The
> Target poses and Actual poses are then compared, and the error compensations
> are estimated using the Least-Squared methods to calculate the Predicted poses.
> Results from each of the three compensation approaches demonstrated noticeable
> enhancements in platform pose accuracies, suggesting room for further
> improvements.

