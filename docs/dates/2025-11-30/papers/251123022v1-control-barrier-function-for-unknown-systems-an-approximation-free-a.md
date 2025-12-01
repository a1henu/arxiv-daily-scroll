---
layout: default
title: Control Barrier Function for Unknown Systems: An Approximation-free Approach
---

# Control Barrier Function for Unknown Systems: An Approximation-free Approach
**arXiv**：[2511.23022v1](https://arxiv.org/abs/2511.23022) · [PDF](https://arxiv.org/pdf/2511.23022.pdf)  
**作者**：Shubham Sawarkar, Pushpak Jagtap  

**一句话要点**：提出无近似控制屏障函数方法，解决未知非线性系统在动态障碍环境中的规定时间到达-避障问题。

**关键词**：控制屏障函数, 未知系统控制, 规定时间控制, 动态障碍避障, 无近似方法, 非线性系统

## 3 点简述
- 研究未知非线性系统在动态障碍环境中的规定时间到达-避障控制问题。
- 基于虚拟系统求解CBF-QP生成安全参考，使用无近似反馈律将真实系统限制在虚拟约束区内。
- 仿真验证了无需模型学习或不确定性估计，即可保证实时安全和规定时间目标可达性。

## 摘要（原文）

> We study the prescribed-time reach-avoid (PT-RA) control problem for nonlinear systems with unknown dynamics operating in environments with moving obstacles. Unlike robust or learning based Control Barrier Function (CBF) methods, the proposed framework requires neither online model learning nor uncertainty bound estimation. A CBF-based Quadratic Program (CBF-QP) is solved on a simple virtual system to generate a safe reference satisfying PT-RA conditions with respect to time-varying, tightened obstacle and goal sets. The true system is confined to a Virtual Confinement Zone (VCZ) around this reference using an approximation-free feedback law. This construction guarantees real-time safety and prescribed-time target reachability under unknown dynamics and dynamic constraints without explicit model identification or offline precomputation. Simulation results illustrate reliable dynamic obstacle avoidance and timely convergence to the target set.

