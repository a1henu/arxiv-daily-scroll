---
layout: default
title: Nonlinear Spectral Modeling and Control of Soft-Robotic Muscles from Data
---

# Nonlinear Spectral Modeling and Control of Soft-Robotic Muscles from Data
**arXiv**：[2601.03247v1](https://arxiv.org/abs/2601.03247) · [PDF](https://arxiv.org/pdf/2601.03247.pdf)  
**作者**：Leonardo Bettini, Amirhossein Kazemipour, Robert K. Katzschmann, George Haller  

**一句话要点**：提出基于谱子流形理论的软机器人肌肉数据驱动建模与控制方法

**关键词**：软机器人肌肉, 谱子流形理论, 数据驱动建模, 非线性控制, HASEL执行器, 实时控制

## 3 点简述
- 软人工肌肉如HASEL执行器存在非线性多物理场动力学和迟滞效应，控制复杂
- 利用谱子流形理论，在绝热状态下学习低维慢流形上的输入-输出映射，避免触发迟滞
- 在拮抗HASEL离合器关节上部署模型，实时控制显著降低跟踪误差，优于基准方法

## 摘要（原文）

> Artificial muscles are essential for compliant musculoskeletal robotics but complicate control due to nonlinear multiphysics dynamics. Hydraulically amplified electrostatic (HASEL) actuators, a class of soft artificial muscles, offer high performance but exhibit memory effects and hysteresis. Here we present a data-driven reduction and control strategy grounded in spectral submanifold (SSM) theory. In the adiabatic regime, where inputs vary slowly relative to intrinsic transients, trajectories rapidly converge to a low-dimensional slow manifold. We learn an explicit input-to-output map on this manifold from forced-response trajectories alone, avoiding decay experiments that can trigger hysteresis. We deploy the SSM-based model for real-time control of an antagonistic HASEL-clutch joint. This approach yields a substantial reduction in tracking error compared to feedback-only and feedforward-only baselines under identical settings. This record-and-control workflow enables rapid characterization and high-performance control of soft muscles and muscle-driven joints without detailed physics-based modeling.

