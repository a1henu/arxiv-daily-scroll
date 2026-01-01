---
layout: default
title: Hierarchical Deformation Planning and Neural Tracking for DLOs in Constrained Environments
---

# Hierarchical Deformation Planning and Neural Tracking for DLOs in Constrained Environments
**arXiv**：[2512.24974v1](https://arxiv.org/abs/2512.24974) · [PDF](https://arxiv.org/pdf/2512.24974.pdf)  
**作者**：Yunxi Tang, Tianqi Yang, Jing Huang, Xiangyu Chu, Kwok Wai Samuel Au  

**一句话要点**：提出分层变形规划与神经跟踪框架，以解决受限环境中可变形线性物体的操控挑战。

**关键词**：可变形线性物体操控, 分层变形规划, 神经模型预测控制, 受限环境, 数据驱动变形模型, 同伦约束

## 3 点简述
- 核心问题：可变形线性物体在受限环境中操控困难，因高维状态空间、复杂变形动力学和障碍物干扰。
- 方法要点：结合分层变形规划生成满足同伦约束的路径集，并优化时间变形序列；采用神经模型预测控制进行数据驱动跟踪。
- 实验或效果：在广泛受限操控任务中验证了框架的有效性，确保全局变形合成和局部跟踪的可靠性能。

## 摘要（原文）

> Deformable linear objects (DLOs) manipulation presents significant challenges due to DLOs' inherent high-dimensional state space and complex deformation dynamics. The wide-populated obstacles in realistic workspaces further complicate DLO manipulation, necessitating efficient deformation planning and robust deformation tracking. In this work, we propose a novel framework for DLO manipulation in constrained environments. This framework combines hierarchical deformation planning with neural tracking, ensuring reliable performance in both global deformation synthesis and local deformation tracking. Specifically, the deformation planner begins by generating a spatial path set that inherently satisfies the homotopic constraints associated with DLO keypoint paths. Next, a path-set-guided optimization method is applied to synthesize an optimal temporal deformation sequence for the DLO. In manipulation execution, a neural model predictive control approach, leveraging a data-driven deformation model, is designed to accurately track the planned DLO deformation sequence. The effectiveness of the proposed framework is validated in extensive constrained DLO manipulation tasks.

