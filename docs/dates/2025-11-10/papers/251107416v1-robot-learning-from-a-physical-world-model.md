---
layout: default
title: Robot Learning from a Physical World Model
---

# Robot Learning from a Physical World Model
**arXiv**：[2511.07416v1](https://arxiv.org/abs/2511.07416) · [PDF](https://arxiv.org/pdf/2511.07416.pdf)  
**作者**：Jiageng Mao, Sicheng He, Hao-Ning Wu, Yang You, Shuyang Sun, Zhicheng Wang, Yanan Bao, Huizhong Chen, Leonidas Guibas, Vitor Guizilini, Howard Zhou, Yue Wang  

**一句话要点**：提出PhysWorld框架，通过物理世界建模从生成视频中学习机器人操作。

**关键词**：机器人学习, 物理世界建模, 视频生成, 强化学习, 零样本泛化

## 3 点简述
- 核心问题：视频生成模型直接用于机器人学习忽略物理约束，导致操作不准确。
- 方法要点：结合视频生成与物理世界重建，使用对象中心残差强化学习将视频运动转化为物理准确动作。
- 实验或效果：在多样真实任务中显著提升操作精度，实现零样本泛化。

## 摘要（原文）

> We introduce PhysWorld, a framework that enables robot learning from video
> generation through physical world modeling. Recent video generation models can
> synthesize photorealistic visual demonstrations from language commands and
> images, offering a powerful yet underexplored source of training signals for
> robotics. However, directly retargeting pixel motions from generated videos to
> robots neglects physics, often resulting in inaccurate manipulations. PhysWorld
> addresses this limitation by coupling video generation with physical world
> reconstruction. Given a single image and a task command, our method generates
> task-conditioned videos and reconstructs the underlying physical world from the
> videos, and the generated video motions are grounded into physically accurate
> actions through object-centric residual reinforcement learning with the
> physical world model. This synergy transforms implicit visual guidance into
> physically executable robotic trajectories, eliminating the need for real robot
> data collection and enabling zero-shot generalizable robotic manipulation.
> Experiments on diverse real-world tasks demonstrate that PhysWorld
> substantially improves manipulation accuracy compared to previous approaches.
> Visit \href{https://pointscoder.github.io/PhysWorld_Web/}{the project webpage}
> for details.

