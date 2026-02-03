---
layout: default
title: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
---

# A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
**arXiv**：[2602.01632v1](https://arxiv.org/abs/2602.01632) · [PDF](https://arxiv.org/pdf/2602.01632.pdf)  
**作者**：Chuizheng Kong, Yunho Cho, Wonsuhk Jung, Idris Wibowo, Parth Shinde, Sundhar Vinodh-Sangeetha, Long Kiu Chung, Zhenyang Chen, Andrew Mattei, Advaith Nidumukkala, Alexander Elias, Danfei Xu, Taylor Higgins, Shreyas Kousik  

**一句话要点**：提出SEW-Mimic方法，通过姿态对齐实现人形机器人上身运动重定向的闭式几何求解

**关键词**：运动重定向, 人形机器人, 遥操作, 姿态对齐, 闭式求解, 双手机器人

## 3 点简述
- 现有方法基于末端位置优化，导致运动不自然、延迟和机器人工作空间受限
- 将重定向重构为姿态对齐问题，利用肩、肘、腕关键点实现闭式几何求解，保证最优性
- 实验显示SEW-Mimic在计算时间和精度上优于其他方法，提升遥操作任务成功率

## 摘要（原文）

> Retargeting human motion to robot poses is a practical approach for teleoperating bimanual humanoid robot arms, but existing methods can be suboptimal and slow, often causing undesirable motion or latency. This is due to optimizing to match robot end-effector to human hand position and orientation, which can also limit the robot's workspace to that of the human. Instead, this paper reframes retargeting as an orientation alignment problem, enabling a closed-form, geometric solution algorithm with an optimality guarantee. The key idea is to align a robot arm to a human's upper and lower arm orientations, as identified from shoulder, elbow, and wrist (SEW) keypoints; hence, the method is called SEW-Mimic. The method has fast inference (3 kHz) on standard commercial CPUs, leaving computational overhead for downstream applications; an example in this paper is a safety filter to avoid bimanual self-collision. The method suits most 7-degree-of-freedom robot arms and humanoids, and is agnostic to input keypoint source. Experiments show that SEW-Mimic outperforms other retargeting methods in computation time and accuracy. A pilot user study suggests that the method improves teleoperation task success. Preliminary analysis indicates that data collected with SEW-Mimic improves policy learning due to being smoother. SEW-Mimic is also shown to be a drop-in way to accelerate full-body humanoid retargeting. Finally, hardware demonstrations illustrate SEW-Mimic's practicality. The results emphasize the utility of SEW-Mimic as a fundamental building block for bimanual robot manipulation and humanoid robot teleoperation.

