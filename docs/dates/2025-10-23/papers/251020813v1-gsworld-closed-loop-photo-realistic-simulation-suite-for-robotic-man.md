---
layout: default
title: GSWorld: Closed-Loop Photo-Realistic Simulation Suite for Robotic Manipulation
---

# GSWorld: Closed-Loop Photo-Realistic Simulation Suite for Robotic Manipulation
**arXiv**：[2510.20813v1](https://arxiv.org/abs/2510.20813) · [PDF](https://arxiv.org/pdf/2510.20813.pdf)  
**作者**：Guangqi Jiang, Haoran Chang, Ri-Zhao Qiu, Yutong Liang, Mazeyu Ji, Jiyue Zhu, Zhao Dong, Xueyan Zou, Xiaolong Wang  

**一句话要点**：提出GSWorld仿真套件，结合3D高斯溅射与物理引擎，实现机器人操作的闭环开发。

**关键词**：机器人操作仿真, 3D高斯溅射, sim2real策略, 物理引擎集成, GSDF资产格式, 闭环开发

## 3 点简述
- 核心问题：机器人操作策略开发依赖真实机器人，成本高且难以复现评估。
- 方法要点：使用GSDF资产格式，融合高斯-网格表示与URDF，支持逼真渲染。
- 实验或效果：展示零样本sim2real策略学习、自动化数据收集等应用。

## 摘要（原文）

> This paper presents GSWorld, a robust, photo-realistic simulator for robotics
> manipulation that combines 3D Gaussian Splatting with physics engines. Our
> framework advocates "closing the loop" of developing manipulation policies with
> reproducible evaluation of policies learned from real-robot data and sim2real
> policy training without using real robots. To enable photo-realistic rendering
> of diverse scenes, we propose a new asset format, which we term GSDF (Gaussian
> Scene Description File), that infuses Gaussian-on-Mesh representation with
> robot URDF and other objects. With a streamlined reconstruction pipeline, we
> curate a database of GSDF that contains 3 robot embodiments for single-arm and
> bimanual manipulation, as well as more than 40 objects. Combining GSDF with
> physics engines, we demonstrate several immediate interesting applications: (1)
> learning zero-shot sim2real pixel-to-action manipulation policy with
> photo-realistic rendering, (2) automated high-quality DAgger data collection
> for adapting policies to deployment environments, (3) reproducible benchmarking
> of real-robot manipulation policies in simulation, (4) simulation data
> collection by virtual teleoperation, and (5) zero-shot sim2real visual
> reinforcement learning. Website: https://3dgsworld.github.io/.

