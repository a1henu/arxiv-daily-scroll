---
layout: default
title: D-Optimality-Guided Reinforcement Learning for Efficient Open-Loop Calibration of a 3-DOF Ankle Rehabilitation Robot
---

# D-Optimality-Guided Reinforcement Learning for Efficient Open-Loop Calibration of a 3-DOF Ankle Rehabilitation Robot
**arXiv**：[2601.15707v1](https://arxiv.org/abs/2601.15707) · [PDF](https://arxiv.org/pdf/2601.15707.pdf)  
**作者**：Qifan Hu, Branko Celler, Weidong Mu, Steven W. Su  

**一句话要点**：提出基于D最优性引导强化学习的开环校准框架，用于高效校准3自由度踝关节康复机器人。

**关键词**：康复机器人校准, D最优性, 强化学习, 开环校准, 姿态选择, 参数估计

## 3 点简述
- 核心问题：多自由度康复机器人精确对齐对安全有效训练至关重要，需高效校准方法。
- 方法要点：开发基于Kronecker积的开环校准，将校准姿态选择建模为D最优性引导的组合实验设计问题，使用PPO代理选择信息性姿态。
- 实验或效果：在仿真和真实机器人评估中，PPO选择的姿态组合信息矩阵行列式均值比随机选择高两个数量级以上，且参数估计更稳健。

## 摘要（原文）

> Accurate alignment of multi-degree-of-freedom rehabilitation robots is essential for safe and effective patient training. This paper proposes a two-stage calibration framework for a self-designed three-degree-of-freedom (3-DOF) ankle rehabilitation robot. First, a Kronecker-product-based open-loop calibration method is developed to cast the input-output alignment into a linear parameter identification problem, which in turn defines the associated experimental design objective through the resulting information matrix. Building on this formulation, calibration posture selection is posed as a combinatorial design-of-experiments problem guided by a D-optimality criterion, i.e., selecting a small subset of postures that maximises the determinant of the information matrix. To enable practical selection under constraints, a Proximal Policy Optimization (PPO) agent is trained in simulation to choose 4 informative postures from a candidate set of 50. Across simulation and real-robot evaluations, the learned policy consistently yields substantially more informative posture combinations than random selection: the mean determinant of the information matrix achieved by PPO is reported to be more than two orders of magnitude higher with reduced variance. In addition, real-world results indicate that a parameter vector identified from only four D-optimality-guided postures provides stronger cross-episode prediction consistency than estimates obtained from a larger but unstructured set of 50 postures. The proposed framework therefore improves calibration efficiency while maintaining robust parameter estimation, offering practical guidance for high-precision alignment of multi-DOF rehabilitation robots.

