---
layout: default
title: MOVE: A Simple Motion-Based Data Collection Paradigm for Spatial Generalization in Robotic Manipulation
---

# MOVE: A Simple Motion-Based Data Collection Paradigm for Spatial Generalization in Robotic Manipulation
**arXiv**：[2512.04813v1](https://arxiv.org/abs/2512.04813) · [PDF](https://arxiv.org/pdf/2512.04813.pdf)  
**作者**：Huanqian Wang, Chi Bene Chen, Yang Yue, Danhua Tao, Tong Guo, Shaoxuan Xie, Denghang Huang, Shiji Song, Guocai Yao, Gao Huang  

**一句话要点**：提出MOVE数据收集范式，通过动态演示增强空间信息以提升机器人操作的空间泛化能力

**关键词**：机器人操作, 模仿学习, 数据收集, 空间泛化, 动态演示, 数据增强

## 3 点简述
- 核心问题：模仿学习数据稀缺，静态环境配置限制空间信息多样性，影响泛化
- 方法要点：在演示中为可移动物体注入运动，单轨迹生成密集多样的空间配置
- 实验或效果：在仿真和真实环境中验证，空间泛化任务成功率提升76.1%，数据效率提高2-5倍

## 摘要（原文）

> Imitation learning method has shown immense promise for robotic manipulation, yet its practical deployment is fundamentally constrained by the data scarcity. Despite prior work on collecting large-scale datasets, there still remains a significant gap to robust spatial generalization. We identify a key limitation: individual trajectories, regardless of their length, are typically collected from a \emph{single, static spatial configuration} of the environment. This includes fixed object and target spatial positions as well as unchanging camera viewpoints, which significantly restricts the diversity of spatial information available for learning. To address this critical bottleneck in data efficiency, we propose \textbf{MOtion-Based Variability Enhancement} (\emph{MOVE}), a simple yet effective data collection paradigm that enables the acquisition of richer spatial information from dynamic demonstrations. Our core contribution is an augmentation strategy that injects motion into any movable objects within the environment for each demonstration. This process implicitly generates a dense and diverse set of spatial configurations within a single trajectory. We conduct extensive experiments in both simulation and real-world environments to validate our approach. For example, in simulation tasks requiring strong spatial generalization, \emph{MOVE} achieves an average success rate of 39.1\%, a 76.1\% relative improvement over the static data collection paradigm (22.2\%), and yields up to 2--5$\times$ gains in data efficiency on certain tasks. Our code is available at https://github.com/lucywang720/MOVE.

