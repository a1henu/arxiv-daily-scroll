---
layout: default
title: Multifingered force-aware control for humanoid robots
---

# Multifingered force-aware control for humanoid robots
**arXiv**：[2603.08142v1](https://arxiv.org/abs/2603.08142) · [PDF](https://arxiv.org/pdf/2603.08142.pdf)  
**作者**：Pasquale Marra, Gabriele M. Caddeo, Ugo Pattacini, Lorenzo Natale  

**一句话要点**：提出基于力估计的多指力感知控制方法，用于人形机器人稳定抓取与平衡任务。

**关键词**：力感知控制, 多指机器人手, 力分布, 人形机器人, 触觉传感器, 平衡任务

## 3 点简述
- 核心问题：解决多指机器人手在抓取变质量或不稳定物体时的力感知与力分布控制问题。
- 方法要点：设计控制器，利用力估计调整躯干、手臂、手腕和手指运动，最小化压力中心与指尖接触多边形质心距离。
- 实验或效果：在平衡任务中验证，对五个物体达到82.7%成功率，多物体场景达到80%准确率。

## 摘要（原文）

> In this paper, we address force-aware control and force distribution in robotic platforms with multi-fingered hands. Given a target goal and force estimates from tactile sensors, we design a controller that adapts the motion of the torso, arm, wrist, and fingers, redistributing forces to maintain stable contact with objects of varying mass distribution or unstable contacts. To estimate forces, we collect a dataset of tactile signals and ground-truth force measurements using five Xela magnetic sensors interacting with indenters, and train force estimators. We then introduce a model-based control scheme that minimizes the distance between the Center of Pressure (CoP) and the centroid of the fingertips contact polygon. Since our method relies on estimated forces rather than raw tactile signals, it has the potential to be applied to any sensor capable of force estimation. We validate our framework on a balancing task with five objects, achieving a $82.7\%$ success rate, and further evaluate it in multi-object scenarios, achieving $80\%$ accuracy. Code and data can be found here https://github.com/hsp-iit/multifingered-force-aware-control.

