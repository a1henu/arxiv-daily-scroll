---
layout: default
title: EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal Robots Driven by Linear Elastic Actuators
---

# EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal Robots Driven by Linear Elastic Actuators
**arXiv**：[2511.07887v1](https://arxiv.org/abs/2511.07887) · [PDF](https://arxiv.org/pdf/2511.07887.pdf)  
**作者**：Yinglei Zhu, Xuguang Dong, Qiyao Wang, Qi Shao, Fugui Xie, Xinjun Liu, Huichan Zhao  

**一句话要点**：提出EquiMus框架以解决肌肉骨骼机器人动态建模与仿真的挑战

**关键词**：肌肉骨骼机器人, 动态建模, 能量等效, 刚柔混合系统, 线性弹性驱动器, MuJoCo仿真

## 3 点简述
- 核心问题：软机器人动态建模因复杂本构行为和现实条件而困难
- 方法要点：基于能量等效原理和MuJoCo仿真，处理刚柔混合机器人
- 实验或效果：通过仿生腿实验验证等效性和有效性，支持控制器设计

## 摘要（原文）

> Dynamic modeling and control are critical for unleashing soft robots' potential, yet remain challenging due to their complex constitutive behaviors and real-world operating conditions. Bio-inspired musculoskeletal robots, which integrate rigid skeletons with soft actuators, combine high load-bearing capacity with inherent flexibility. Although actuation dynamics have been studied through experimental methods and surrogate models, accurate and effective modeling and simulation remain a significant challenge, especially for large-scale hybrid rigid--soft robots with continuously distributed mass, kinematic loops, and diverse motion modes. To address these challenges, we propose EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulation for musculoskeletal rigid--soft hybrid robots with linear elastic actuators. The equivalence and effectiveness of the proposed approach are validated and examined through both simulations and real-world experiments on a bionic robotic leg. EquiMus further demonstrates its utility for downstream tasks, including controller design and learning-based control strategies.

