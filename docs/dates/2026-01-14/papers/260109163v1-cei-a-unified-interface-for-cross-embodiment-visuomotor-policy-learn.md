---
layout: default
title: CEI: A Unified Interface for Cross-Embodiment Visuomotor Policy Learning in 3D Space
---

# CEI: A Unified Interface for Cross-Embodiment Visuomotor Policy Learning in 3D Space
**arXiv**：[2601.09163v1](https://arxiv.org/abs/2601.09163) · [PDF](https://arxiv.org/pdf/2601.09163.pdf)  
**作者**：Tong Wu, Shoujie Li, Junhao Gong, Changqing Guo, Xingting Li, Shilong Mu, Wenbo Ding  

**一句话要点**：提出跨具身接口CEI，通过功能相似性量化与轨迹对齐，实现不同机器人形态间的策略迁移。

**关键词**：跨具身学习, 功能相似性, 轨迹对齐, 机器人策略迁移, 3D视觉运动控制

## 3 点简述
- 问题：机器人基础模型因数据集偏差，常过拟合于特定视角、机械臂和平行夹爪。
- 方法：引入功能相似性概念，使用方向性Chamfer距离量化，并通过梯度优化对齐轨迹。
- 效果：在仿真和真实任务中，实现多机器人间数据与策略迁移，平均迁移率达82.4%。

## 摘要（原文）

> Robotic foundation models trained on large-scale manipulation datasets have shown promise in learning generalist policies, but they often overfit to specific viewpoints, robot arms, and especially parallel-jaw grippers due to dataset biases. To address this limitation, we propose Cross-Embodiment Interface (\CEI), a framework for cross-embodiment learning that enables the transfer of demonstrations across different robot arm and end-effector morphologies. \CEI introduces the concept of \textit{functional similarity}, which is quantified using Directional Chamfer Distance. Then it aligns robot trajectories through gradient-based optimization, followed by synthesizing observations and actions for unseen robot arms and end-effectors. In experiments, \CEI transfers data and policies from a Franka Panda robot to \textbf{16} different embodiments across \textbf{3} tasks in simulation, and supports bidirectional transfer between a UR5+AG95 gripper robot and a UR5+Xhand robot across \textbf{6} real-world tasks, achieving an average transfer ratio of 82.4\%. Finally, we demonstrate that \CEI can also be extended with spatial generalization and multimodal motion generation capabilities using our proposed techniques. Project website: https://cross-embodiment-interface.github.io/

