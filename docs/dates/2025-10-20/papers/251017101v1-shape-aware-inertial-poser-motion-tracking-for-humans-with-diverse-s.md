---
layout: default
title: Shape-aware Inertial Poser: Motion Tracking for Humans with Diverse Shapes Using Sparse Inertial Sensors
---

# Shape-aware Inertial Poser: Motion Tracking for Humans with Diverse Shapes Using Sparse Inertial Sensors
**arXiv**：[2510.17101v1](https://arxiv.org/abs/2510.17101) · [PDF](https://arxiv.org/pdf/2510.17101.pdf)  
**作者**：Lu Yin, Ziying Shi, Yinghao Wu, Xinyu Yi, Feng Xu, Shihui Guo  

**一句话要点**：提出Shape-aware Inertial Poser以解决稀疏惯性传感器在多样化人体形状下的运动捕捉问题

**关键词**：惯性运动捕捉, 身体形状估计, 传感器测量分解, 回归模型, 物理优化, 多样化体型数据集

## 3 点简述
- 现有方法依赖模板成人身体形状，难以泛化到不同体型如儿童，因身体形状变化影响IMU加速度测量
- 方法分解传感器测量为形状和姿态相关部分，通过回归模型补偿形状差异并估计全局运动
- 实验基于首个包含不同体型个体的IMU数据集，验证SAIP能有效处理多样化身体形状的运动捕捉

## 摘要（原文）

> Human motion capture with sparse inertial sensors has gained significant
> attention recently. However, existing methods almost exclusively rely on a
> template adult body shape to model the training data, which poses challenges
> when generalizing to individuals with largely different body shapes (such as a
> child). This is primarily due to the variation in IMU-measured acceleration
> caused by changes in body shape. To fill this gap, we propose Shape-aware
> Inertial Poser (SAIP), the first solution considering body shape differences in
> sparse inertial-based motion capture. Specifically, we decompose the sensor
> measurements related to shape and pose in order to effectively model their
> joint correlations. Firstly, we train a regression model to transfer the
> IMU-measured accelerations of a real body to match the template adult body
> model, compensating for the shape-related sensor measurements. Then, we can
> easily follow the state-of-the-art methods to estimate the full body motions of
> the template-shaped body. Finally, we utilize a second regression model to map
> the joint velocities back to the real body, combined with a shape-aware
> physical optimization strategy to calculate global motions on the subject.
> Furthermore, our method relies on body shape awareness, introducing the first
> inertial shape estimation scheme. This is accomplished by modeling the
> shape-conditioned IMU-pose correlation using an MLP-based network. To validate
> the effectiveness of SAIP, we also present the first IMU motion capture dataset
> containing individuals of different body sizes. This dataset features 10
> children and 10 adults, with heights ranging from 110 cm to 190 cm, and a total
> of 400 minutes of paired IMU-Motion samples. Extensive experimental results
> demonstrate that SAIP can effectively handle motion capture tasks for diverse
> body shapes. The code and dataset are available at
> https://github.com/yinlu5942/SAIP.

