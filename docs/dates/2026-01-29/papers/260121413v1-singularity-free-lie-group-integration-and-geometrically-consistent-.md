---
layout: default
title: Singularity-Free Lie Group Integration and Geometrically Consistent Evaluation of Multibody System Models Described in Terms of Standard Absolute Coordinates
---

# Singularity-Free Lie Group Integration and Geometrically Consistent Evaluation of Multibody System Models Described in Terms of Standard Absolute Coordinates
**arXiv**：[2601.21413v1](https://arxiv.org/abs/2601.21413) · [PDF](https://arxiv.org/pdf/2601.21413.pdf)  
**作者**：Andreas Mueller  

**一句话要点**：提出框架与方法，实现李群积分与标准绝对坐标多体系统模型的几何一致集成

**关键词**：多体系统建模, 李群积分, 绝对坐标, 几何一致性, 局部-全局转换

## 3 点简述
- 核心问题：标准绝对坐标多体系统模型在时间积分中缺乏无奇点参数化，且李群积分与现有公式不兼容
- 方法要点：引入局部-全局转换映射，连接李群积分器与标准运动方程，支持多种绝对坐标描述
- 实验或效果：未知

## 摘要（原文）

> A classical approach to the multibody systems (MBS) modeling is to use absolute coordinates, i.e., a set of (possibly redundant) coordinates that describe the absolute position and orientation of the individual bodies with respect to an inertial frame (IFR). A well-known problem for the time integration of the equations of motion (EOM) is the lack of a singularity-free parameterization of spatial motions, which is usually tackled by using unit quaternions. Lie group integration methods were proposed as an alternative approach to the singularity-free time integration. At the same time, Lie group formulations of EOM naturally respect the geometry of spatial motions during integration. Lie group integration methods, operating directly on the configuration space Lie group, are incompatible with standard formulations of the EOM, and cannot be implemented in existing MBS simulation codes without a major restructuring. The contribution of this paper is twofold: (1) A framework for interfacing Lie group integrators to standard EOM formulations is presented. It allows describing MBS in terms of various absolute coordinates and at the same using Lie group integration schemes. (2) A method for consistently incorporating the geometry of rigid body motions into the evaluation of EOM in absolute coordinates integrated with standard vector space integration schemes. The direct product group and the semidirect product group SO(3)xR3 and the semidirect product group SE(3) are used for representing rigid body motions. The key element is the local-global transitions (LGT) transition map, which facilitates the update of (global) absolute coordinates in terms of the (local) coordinates on the Lie group. This LGT map is specific to the absolute coordinates, the local coordinates on the Lie group, and the Lie group used to represent rigid body configurations.

