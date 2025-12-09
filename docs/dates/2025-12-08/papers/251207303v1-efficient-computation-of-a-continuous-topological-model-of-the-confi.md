---
layout: default
title: Efficient Computation of a Continuous Topological Model of the Configuration Space of Tethered Mobile Robots
---

# Efficient Computation of a Continuous Topological Model of the Configuration Space of Tethered Mobile Robots
**arXiv**：[2512.07303v1](https://arxiv.org/abs/2512.07303) · [PDF](https://arxiv.org/pdf/2512.07303.pdf)  
**作者**：Gianpietro Battocletti, Dimitris Boskos, Bart De Schutter  

**一句话要点**：提出连续拓扑模型以高效计算系绳移动机器人的配置空间

**关键词**：系绳机器人, 配置空间, 拓扑模型, 路径规划, 单纯复形, 通用覆盖空间

## 3 点简述
- 核心问题：现有路径规划方法依赖离散表示，缺乏同时捕获系绳拓扑和机器人连续位置的模型。
- 方法要点：基于工作空间多边形表示，建立配置空间与通用覆盖空间的联系，开发算法计算单纯复形模型。
- 实验或效果：模型计算时间远少于传统同伦增强图，支持多种路径规划算法，提升性能。

## 摘要（原文）

> Despite the attention that the problem of path planning for tethered robots has garnered in the past few decades, the approaches proposed to solve it typically rely on a discrete representation of the configuration space and do not exploit a model that can simultaneously capture the topological information of the tether and the continuous location of the robot. In this work, we explicitly build a topological model of the configuration space of a tethered robot starting from a polygonal representation of the workspace where the robot moves. To do so, we first establish a link between the configuration space of the tethered robot and the universal covering space of the workspace, and then we exploit this link to develop an algorithm to compute a simplicial complex model of the configuration space. We show how this approach improves the performances of existing algorithms that build other types of representations of the configuration space. The proposed model can be computed in a fraction of the time required to build traditional homotopy-augmented graphs, and is continuous, allowing to solve the path planning task for tethered robots using a broad set of path planning algorithms.

