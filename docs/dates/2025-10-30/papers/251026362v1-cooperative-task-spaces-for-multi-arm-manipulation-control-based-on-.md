---
layout: default
title: Cooperative Task Spaces for Multi-Arm Manipulation Control based on Similarity Transformations
---

# Cooperative Task Spaces for Multi-Arm Manipulation Control based on Similarity Transformations
**arXiv**：[2510.26362v1](https://arxiv.org/abs/2510.26362) · [PDF](https://arxiv.org/pdf/2510.26362.pdf)  
**作者**：Tobias Löw, Cem Bilaloglu, Sylvain Calinon  

**一句话要点**：提出基于相似变换的多臂机器人协作任务空间框架以简化复杂系统控制

**关键词**：多臂机器人控制, 协作任务空间, 相似变换, 共形几何代数, 操作空间控制

## 3 点简述
- 核心问题：多臂机器人系统自由度多，协调运动建模困难。
- 方法要点：使用共形几何代数定义几何基元，推导协作任务空间和雅可比矩阵。
- 实验或效果：在双手机器人、人形机器人和多指手上验证控制性能。

## 摘要（原文）

> Many tasks in human environments require collaborative behavior between
> multiple kinematic chains, either to provide additional support for carrying
> big and bulky objects or to enable the dexterity that is required for in-hand
> manipulation. Since these complex systems often have a very high number of
> degrees of freedom coordinating their movements is notoriously difficult to
> model. In this article, we present the derivation of the theoretical
> foundations for cooperative task spaces of multi-arm robotic systems based on
> geometric primitives defined using conformal geometric algebra. Based on the
> similarity transformations of these cooperative geometric primitives, we derive
> an abstraction of complex robotic systems that enables representing these
> systems in a way that directly corresponds to single-arm systems. By deriving
> the associated analytic and geometric Jacobian matrices, we then show the
> straightforward integration of our approach into classical control techniques
> rooted in operational space control. We demonstrate this using bimanual
> manipulators, humanoids and multi-fingered hands in optimal control experiments
> for reaching desired geometric primitives and in teleoperation experiments
> using differential kinematics control. We then discuss how the geometric
> primitives naturally embed nullspace structures into the controllers that can
> be exploited for introducing secondary control objectives. This work,
> represents the theoretical foundations of this cooperative manipulation control
> framework, and thus the experiments are presented in an abstract way, while
> giving pointers towards potential future applications.

