---
layout: default
title: Dynamic Log-Gaussian Process Control Barrier Function for Safe Robotic Navigation in Dynamic Environments
---

# Dynamic Log-Gaussian Process Control Barrier Function for Safe Robotic Navigation in Dynamic Environments
**arXiv**：[2512.01668v1](https://arxiv.org/abs/2512.01668) · [PDF](https://arxiv.org/pdf/2512.01668.pdf)  
**作者**：Xin Yin, Chenyang Liang, Yanning Guo, Jie Mei  

**一句话要点**：提出动态对数高斯过程控制屏障函数以解决动态环境中机器人安全导航问题

**关键词**：控制屏障函数, 高斯过程回归, 机器人导航, 动态环境, 安全控制, 障碍物避让

## 3 点简述
- 核心问题：在线合成信息丰富且感知障碍物运动的控制屏障函数在未知动态场景中具有挑战性
- 方法要点：利用对数变换的高斯过程回归生成平滑屏障值，并建模障碍物位置以整合预测速度
- 实验或效果：仿真显示在安全裕度、轨迹平滑性和响应性方面优于基线方法

## 摘要（原文）

> Control Barrier Functions (CBFs) have emerged as efficient tools to address the safe navigation problem for robot applications. However, synthesizing informative and obstacle motion-aware CBFs online using real-time sensor data remains challenging, particularly in unknown and dynamic scenarios. Motived by this challenge, this paper aims to propose a novel Gaussian Process-based formulation of CBF, termed the Dynamic Log Gaussian Process Control Barrier Function (DLGP-CBF), to enable real-time construction of CBF which are both spatially informative and responsive to obstacle motion. Firstly, the DLGP-CBF leverages a logarithmic transformation of GP regression to generate smooth and informative barrier values and gradients, even in sparse-data regions. Secondly, by explicitly modeling the DLGP-CBF as a function of obstacle positions, the derived safety constraint integrates predicted obstacle velocities, allowing the controller to proactively respond to dynamic obstacles' motion. Simulation results demonstrate significant improvements in obstacle avoidance performance, including increased safety margins, smoother trajectories, and enhanced responsiveness compared to baseline methods.

