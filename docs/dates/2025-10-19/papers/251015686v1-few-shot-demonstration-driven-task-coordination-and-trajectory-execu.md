---
layout: default
title: Few-Shot Demonstration-Driven Task Coordination and Trajectory Execution for Multi-Robot Systems
---

# Few-Shot Demonstration-Driven Task Coordination and Trajectory Execution for Multi-Robot Systems
**arXiv**：[2510.15686v1](https://arxiv.org/abs/2510.15686) · [PDF](https://arxiv.org/pdf/2510.15686.pdf)  
**作者**：Taehyeon Kim, Vishnunandan L. N. Venkatesh, Byung-Cheol Min  

**一句话要点**：提出DDACE框架以解决多机器人系统在少样本学习下的任务协调与轨迹执行问题

**关键词**：多机器人系统, 少样本学习, 任务协调, 轨迹执行, 时间图网络, 高斯过程

## 3 点简述
- 核心问题：多机器人系统需高效协调任务与轨迹，但传统方法数据需求高
- 方法要点：使用时间图网络学习时序序列，高斯过程建模空间轨迹，实现模块化
- 实验或效果：在多样化环境中验证，少样本条件下成功执行任务并泛化

## 摘要（原文）

> In this paper, we propose a novel few-shot learning framework for multi-robot
> systems that integrate both spatial and temporal elements: Few-Shot
> Demonstration-Driven Task Coordination and Trajectory Execution (DDACE). Our
> approach leverages temporal graph networks for learning task-agnostic temporal
> sequencing and Gaussian Processes for spatial trajectory modeling, ensuring
> modularity and generalization across various tasks. By decoupling temporal and
> spatial aspects, DDACE requires only a small number of demonstrations,
> significantly reducing data requirements compared to traditional learning from
> demonstration approaches. To validate our proposed framework, we conducted
> extensive experiments in task environments designed to assess various aspects
> of multi-robot coordination-such as multi-sequence execution, multi-action
> dynamics, complex trajectory generation, and heterogeneous configurations. The
> experimental results demonstrate that our approach successfully achieves task
> execution under few-shot learning conditions and generalizes effectively across
> dynamic and diverse settings. This work underscores the potential of modular
> architectures in enhancing the practicality and scalability of multi-robot
> systems in real-world applications. Additional materials are available at
> https://sites.google.com/view/ddace.

