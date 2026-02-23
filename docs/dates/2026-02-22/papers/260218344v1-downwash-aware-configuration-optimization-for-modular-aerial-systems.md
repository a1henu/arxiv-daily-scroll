---
layout: default
title: Downwash-aware Configuration Optimization for Modular Aerial Systems
---

# Downwash-aware Configuration Optimization for Modular Aerial Systems
**arXiv**：[2602.18344v1](https://arxiv.org/abs/2602.18344) · [PDF](https://arxiv.org/pdf/2602.18344.pdf)  
**作者**：Mengguang Li, Heinz Koeppl  

**一句话要点**：提出模块化空中系统配置优化框架，考虑下洗流约束以最小化控制输入

**关键词**：模块化空中系统, 配置优化, 下洗流约束, 非线性规划, 气动干扰

## 3 点简述
- 核心问题：现有方法多忽略气动干扰，难以优化模块化空中系统的任务特定配置
- 方法要点：枚举非同构连接拓扑，通过非线性规划检查可行性并选择最优配置
- 实验或效果：在物理仿真和真实实验中评估框架，验证其有效性和实用性

## 摘要（原文）

> This work proposes a framework that generates and optimally selects task-specific assembly configurations for a large group of homogeneous modular aerial systems, explicitly enforcing bounds on inter-module downwash. Prior work largely focuses on planar layouts and often ignores aerodynamic interference. In contrast, firstly we enumerate non-isomorphic connection topologies at scale; secondly, we solve a nonlinear program to check feasibility and select the configuration that minimizes control input subject to actuation limits and downwash constraints. We evaluate the framework in physics-based simulation and demonstrate it in real-world experiments.

