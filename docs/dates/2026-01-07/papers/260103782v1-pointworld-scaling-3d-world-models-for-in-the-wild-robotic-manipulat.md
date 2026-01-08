---
layout: default
title: PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation
---

# PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation
**arXiv**：[2601.03782v1](https://arxiv.org/abs/2601.03782) · [PDF](https://arxiv.org/pdf/2601.03782.pdf)  
**作者**：Wenlong Huang, Yu-Wei Chao, Arsalan Mousavian, Ming-Yu Liu, Dieter Fox, Kaichun Mo, Li Fei-Fei  

**一句话要点**：提出PointWorld，一个预训练的3D世界模型，通过3D点流预测机器人动作在开放世界中的响应。

**关键词**：3D世界模型, 机器人操作, 点流预测, 模型预测控制, 开放世界环境, 预训练模型

## 3 点简述
- 核心问题：机器人需要从单张或少图像预测动作对3D世界的响应，以支持野外操作。
- 方法要点：将状态和动作统一表示为3D点流，基于RGB-D图像和动作命令预测像素级3D位移。
- 实验或效果：在真实和模拟数据上训练，实现实时推理，支持多种操作任务，无需演示或后训练。

## 摘要（原文）

> Humans anticipate, from a glance and a contemplated action of their bodies, how the 3D world will respond, a capability that is equally vital for robotic manipulation. We introduce PointWorld, a large pre-trained 3D world model that unifies state and action in a shared 3D space as 3D point flows: given one or few RGB-D images and a sequence of low-level robot action commands, PointWorld forecasts per-pixel displacements in 3D that respond to the given actions. By representing actions as 3D point flows instead of embodiment-specific action spaces (e.g., joint positions), this formulation directly conditions on physical geometries of robots while seamlessly integrating learning across embodiments. To train our 3D world model, we curate a large-scale dataset spanning real and simulated robotic manipulation in open-world environments, enabled by recent advances in 3D vision and simulated environments, totaling about 2M trajectories and 500 hours across a single-arm Franka and a bimanual humanoid. Through rigorous, large-scale empirical studies of backbones, action representations, learning objectives, partial observability, data mixtures, domain transfers, and scaling, we distill design principles for large-scale 3D world modeling. With a real-time (0.1s) inference speed, PointWorld can be efficiently integrated in the model-predictive control (MPC) framework for manipulation. We demonstrate that a single pre-trained checkpoint enables a real-world Franka robot to perform rigid-body pushing, deformable and articulated object manipulation, and tool use, without requiring any demonstrations or post-training and all from a single image captured in-the-wild. Project website at https://point-world.github.io/.

