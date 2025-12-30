---
layout: default
title: A New Software Tool for Generating and Visualizing Robot Self-Collision Matrices
---

# A New Software Tool for Generating and Visualizing Robot Self-Collision Matrices
**arXiv**：[2512.23140v1](https://arxiv.org/abs/2512.23140) · [PDF](https://arxiv.org/pdf/2512.23140.pdf)  
**作者**：Roshan Klein-Seetharama, Daniel Rakita  

**一句话要点**：提出交互式工具以生成和可视化机器人自碰撞矩阵，支持多形状表示和动态检查。

**关键词**：机器人自碰撞矩阵, 交互式可视化, 多形状表示, 自碰撞查询, 自接近度查询, Rust实现

## 3 点简述
- 核心问题：现有工具在自碰撞矩阵生成中存在静态可视化、缺乏接近度支持、单一几何假设和繁琐工作流等限制。
- 方法要点：开发基于Rust和Bevy引擎的交互工具，支持多形状表示，提供动态检查、过滤和细化功能，输出JSON和YAML格式。
- 实验或效果：在多个机器人平台上验证，使用多样形状类型生成的矩阵能实现更快更准确的自碰撞和自接近度查询。

## 摘要（原文）

> In robotics, it is common to check whether a given robot state results in self-intersection (i.e., a self-collision query) or to assess its distance from such an intersection (i.e., a self-proximity query). These checks are typically performed between pairs of shapes attached to different robot links. However, many of these shape pairs can be excluded in advance, as their configurations are known to always or never result in contact. This information is typically encoded in a self-collision matrix, where each entry (i, j) indicates whether a check should be performed between shape i and shape j. While the MoveIt Setup Assistant is widely used to generate such matrices, current tools are limited by static visualization, lack of proximity support, rigid single-geometry assumptions, and tedious refinement workflows, hindering flexibility and reuse in downstream robotics applications. In this work, we introduce an interactive tool that overcomes these limitations by generating and visualizing self-collision matrices across multiple shape representations, enabling dynamic inspection, filtering, and refinement of shape pairs. Outputs are provided in both JSON and YAML for easy integration. The system is implemented in Rust and uses the Bevy game engine to deliver high-quality visualizations. We demonstrate its effectiveness on multiple robot platforms, showing that matrices generated using diverse shape types yield faster and more accurate self-collision and self-proximity queries.

