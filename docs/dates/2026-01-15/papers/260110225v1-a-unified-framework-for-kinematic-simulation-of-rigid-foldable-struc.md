---
layout: default
title: A Unified Framework for Kinematic Simulation of Rigid Foldable Structures
---

# A Unified Framework for Kinematic Simulation of Rigid Foldable Structures
**arXiv**：[2601.10225v1](https://arxiv.org/abs/2601.10225) · [PDF](https://arxiv.org/pdf/2601.10225.pdf)  
**作者**：Dongwook Kwak, Geonhee Cho, Jiook Chung, Jinkyu Yang  

**一句话要点**：提出统一框架以自动生成刚性可折叠结构的Pfaffian约束矩阵，解决运动学分析难题。

**关键词**：刚性可折叠结构, 运动学分析, Pfaffian约束矩阵, 螺旋理论, 最小环基, 自动化工具

## 3 点简述
- 核心问题：刚性可折叠结构（如折纸、厚板、多片）缺乏统一运动学分析方法，约束计算繁琐易错。
- 方法要点：基于最小扩展数据模式，构建面-铰链图，提取最小环基，通过螺旋理论组装速度级约束矩阵。
- 实验或效果：框架能计算和可视化多种结构的展开与折叠运动，消除手动约束计算。

## 摘要（原文）

> Origami-inspired structures with rigid panels now span thick, kirigami, and multi-sheet realizations, making unified kinematic analysis essential. Yet a general method that consolidates their loop constraints has been lacking. We present an automated approach that generates the Pfaffian constraint matrix for arbitrary rigid foldable structures (RFS). From a minimally extended data schema, the tool constructs the facet-hinge graph, extracts a minimum cycle basis that captures all constraints, and assembles a velocity-level constraint matrix via screw theory that encodes coupled rotation and translation loop closure. The framework computes and visualizes deploy and fold motions across diverse RFS while eliminating tedious and error-prone constraint calculations.

