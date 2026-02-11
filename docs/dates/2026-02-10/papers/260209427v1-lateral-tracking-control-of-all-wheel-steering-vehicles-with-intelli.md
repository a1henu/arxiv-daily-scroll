---
layout: default
title: Lateral tracking control of all-wheel steering vehicles with intelligent tires
---

# Lateral tracking control of all-wheel steering vehicles with intelligent tires
**arXiv**：[2602.09427v1](https://arxiv.org/abs/2602.09427) · [PDF](https://arxiv.org/pdf/2602.09427.pdf)  
**作者**：Luigi Romano, Ole Morten Aamo, Jan Åslund, Erik Frisk  

**一句话要点**：提出基于智能轮胎与分布式轮胎模型的输出反馈横向跟踪控制策略，以抑制低速微摆振并实现路径跟随。

**关键词**：智能轮胎, 分布式轮胎模型, 横向跟踪控制, ODE-PDE系统, 输出反馈控制, 全轮转向车辆

## 3 点简述
- 核心问题：轮胎动力学准确表征对自动驾驶车辆控制至关重要，现有方法依赖经验或机器学习，鲁棒性不足。
- 方法要点：采用ODE-PDE系统建模刚体与分布式轮胎行为，结合智能轮胎技术估计滑移角、车辆运动学和侧向力。
- 实验或效果：实现低速微摆振抑制和基于力控制的路径跟随，首次为配备分布式轮胎表示与智能轮胎的车辆系统提供严格控制策略。

## 摘要（原文）

> The accurate characterization of tire dynamics is critical for advancing control strategies in autonomous road vehicles, as tire behavior significantly influences handling and stability through the generation of forces and moments at the tire-road interface. Smart tire technologies have emerged as a promising tool for sensing key variables such as road friction, tire pressure, and wear states, and for estimating kinematic and dynamic states like vehicle speed and tire forces. However, most existing estimation and control algorithms rely on empirical correlations or machine learning approaches, which require extensive calibration and can be sensitive to variations in operating conditions. In contrast, model-based techniques, which leverage infinite-dimensional representations of tire dynamics using partial differential equations (PDEs), offer a more robust approach. This paper proposes a novel model-based, output-feedback lateral tracking control strategy for all-wheel steering vehicles that integrates distributed tire dynamics with smart tire technologies. The primary contributions include the suppression of micro-shimmy phenomena at low speeds and path-following via force control, achieved through the estimation of tire slip angles, vehicle kinematics, and lateral tire forces. The proposed controller and observer are based on formulations using ODE-PDE systems, representing rigid body dynamics and distributed tire behavior. This work marks the first rigorous control strategy for vehicular systems equipped with distributed tire representations in conjunction with smart tire technologies.

