---
layout: default
title: Beyond URDF: The Universal Robot Description Directory for Shared, Extensible, and Standardized Robot Models
---

# Beyond URDF: The Universal Robot Description Directory for Shared, Extensible, and Standardized Robot Models
**arXiv**：[2512.23135v1](https://arxiv.org/abs/2512.23135) · [PDF](https://arxiv.org/pdf/2512.23135.pdf)  
**作者**：Roshan Klein-Seetharaman, Daniel Rakita  

**一句话要点**：提出通用机器人描述目录以解决机器人模型信息冗余和标准化不足问题

**关键词**：机器人描述, 模块化表示, 标准化, 开源工具包, JSON/YAML, 可视化

## 3 点简述
- 核心问题：现有机器人描述文件仅编码基础信息，导致下游应用重复计算和标准化有限
- 方法要点：引入模块化URDD，将派生信息组织为结构化JSON/YAML模块，并提供开源工具包
- 实验或效果：在多个机器人平台上高效生成URDD，封装更丰富信息，支持核心子程序构建

## 摘要（原文）

> Robots are typically described in software by specification files (e.g., URDF, SDF, MJCF, USD) that encode only basic kinematic, dynamic, and geometric information. As a result, downstream applications such as simulation, planning, and control must repeatedly re-derive richer data, leading to redundant computations, fragmented implementations, and limited standardization. In this work, we introduce the Universal Robot Description Directory (URDD), a modular representation that organizes derived robot information into structured, easy-to-parse JSON and YAML modules. Our open-source toolkit automatically generates URDDs from URDFs, with a Rust implementation supporting Bevy-based visualization. Additionally, we provide a JavaScript/Three.js viewer for web-based inspection of URDDs. Experiments on multiple robot platforms show that URDDs can be generated efficiently, encapsulate substantially richer information than standard specification files, and directly enable the construction of core robotics subroutines. URDD provides a unified, extensible resource for reducing redundancy and establishing shared standards across robotics frameworks. We conclude with a discussion on the limitations and implications of our work.

