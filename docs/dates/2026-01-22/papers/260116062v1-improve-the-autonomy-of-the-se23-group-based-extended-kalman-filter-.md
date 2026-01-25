---
layout: default
title: Improve the autonomy of the SE2(3) group based Extended Kalman Filter for Integrated Navigation: Theoretical Analysis
---

# Improve the autonomy of the SE2(3) group based Extended Kalman Filter for Integrated Navigation: Theoretical Analysis
**arXiv**：[2601.16062v1](https://arxiv.org/abs/2601.16062) · [PDF](https://arxiv.org/pdf/2601.16062.pdf)  
**作者**：Jiarui Cui, Maosong Wang, Wenqi Wu, Peiqi Li, Xianfei Pan  

**一句话要点**：提出SE2(3)群导航模型构建方法以提升高精度集成导航中的自主性

**关键词**：SE2(3)群, 扩展卡尔曼滤波, 集成导航, 自主性分析, 高精度导航, 科里奥利力

## 3 点简述
- 核心问题：高精度导航中考虑地球旋转和设备偏差时，SE2(3)群误差传播自主性难以维持
- 方法要点：分析惯性、地球和世界坐标系下自主性，提出新模型构建方法减少科里奥利力项影响
- 实验或效果：通过理论分析，使导航模型更接近完全自主，适用于高精度状态估计

## 摘要（原文）

> One of core advantages of the SE2(3) Lie group framework for navigation modeling lies in the autonomy of error propagation. Current research on Lie group based extended Kalman filters has demonstrated that error propagation autonomy holds in low-precision applications, such as in micro electromechanical system (MEMS) based integrated navigation without considering earth rotation and inertial device biases. However, in high-precision navigation state estimation, maintaining autonomy is extremely difficult when considering with earth rotation and inertial device biases. This paper presents the theoretical analysis on the autonomy of SE2(3) group based high-precision navigation models under inertial, earth and world frame respectively. Through theoretical analysis, we find that the limitation of the traditional, trivial SE2(3) group navigation modeling method is that the presence of Coriolis force terms introduced by velocity in non-inertial frame. Therefore, a construction method for SE2(3) group navigation models is proposed, which brings the navigation models closer to full autonomy.

