---
layout: default
title: PathFormer: A Transformer with 3D Grid Constraints for Digital Twin Robot-Arm Trajectory Generation
---

# PathFormer: A Transformer with 3D Grid Constraints for Digital Twin Robot-Arm Trajectory Generation
**arXiv**：[2510.20161v1](https://arxiv.org/abs/2510.20161) · [PDF](https://arxiv.org/pdf/2510.20161.pdf)  
**作者**：Ahmed Alanazi, Duy Ho, Yugyung Lee  

**一句话要点**：提出PathFormer以解决机器人臂轨迹生成中的无效运动问题

**关键词**：机器人轨迹生成, Transformer模型, 3D网格表示, 数字孪生, 约束解码

## 3 点简述
- 机器人臂轨迹规划常因忽略运动结构而产生无效或低效执行
- 采用基于3D网格的Transformer编码和约束掩码解码，强制相邻移动和边界约束
- 在53,755条轨迹上训练，达到高精度和成功率，支持语言指定任务

## 摘要（原文）

> Robotic arms require precise, task-aware trajectory planning, yet sequence
> models that ignore motion structure often yield invalid or inefficient
> executions. We present a Path-based Transformer that encodes robot motion with
> a 3-grid (where/what/when) representation and constraint-masked decoding,
> enforcing lattice-adjacent moves and workspace bounds while reasoning over task
> graphs and action order. Trained on 53,755 trajectories (80% train / 20%
> validation), the model aligns closely with ground truth -- 89.44% stepwise
> accuracy, 93.32% precision, 89.44% recall, and 90.40% F1 -- with 99.99% of
> paths legal by construction. Compiled to motor primitives on an xArm Lite 6
> with a depth-camera digital twin, it attains up to 97.5% reach and 92.5% pick
> success in controlled tests, and 86.7% end-to-end success across 60
> language-specified tasks in cluttered scenes, absorbing slips and occlusions
> via local re-grounding without global re-planning. These results show that
> path-structured representations enable Transformers to generate accurate,
> reliable, and interpretable robot trajectories, bridging graph-based planning
> and sequence-based learning and providing a practical foundation for
> general-purpose manipulation and sim-to-real transfer.

