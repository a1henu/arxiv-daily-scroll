---
layout: default
title: HERO: Hierarchical Traversable 3D Scene Graphs for Embodied Navigation Among Movable Obstacles
---

# HERO: Hierarchical Traversable 3D Scene Graphs for Embodied Navigation Among Movable Obstacles
**arXiv**：[2512.15047v1](https://arxiv.org/abs/2512.15047) · [PDF](https://arxiv.org/pdf/2512.15047.pdf)  
**作者**：Yunheng Wang, Yixiao Feng, Yuetong Fang, Shuning Zhang, Tan Jing, Jian Li, Xiangrui Jiang, Renjing Xu  

**一句话要点**：提出HERO框架以解决可移动障碍物下具身导航的静态世界假设限制

**关键词**：3D场景图, 具身导航, 可移动障碍物, 分层表示, 可通行性建模, 交互式环境

## 3 点简述
- 核心问题：现有3D场景图依赖静态世界假设，将可交互障碍物视为不可通行，限制导航效率与可达性。
- 方法要点：构建分层可通行3D场景图，通过建模可操作障碍物的物理交互性、功能语义和关系层次来重新定义可通行性。
- 实验或效果：在部分和完全阻塞环境中，HERO分别减少路径长度35.1%和提高成功率79.4%，显著提升效率与可达性。

## 摘要（原文）

> 3D Scene Graphs (3DSGs) constitute a powerful representation of the physical world, distinguished by their abilities to explicitly model the complex spatial, semantic, and functional relationships between entities, rendering a foundational understanding that enables agents to interact intelligently with their environment and execute versatile behaviors. Embodied navigation, as a crucial component of such capabilities, leverages the compact and expressive nature of 3DSGs to enable long-horizon reasoning and planning in complex, large-scale environments. However, prior works rely on a static-world assumption, defining traversable space solely based on static spatial layouts and thereby treating interactable obstacles as non-traversable. This fundamental limitation severely undermines their effectiveness in real-world scenarios, leading to limited reachability, low efficiency, and inferior extensibility. To address these issues, we propose HERO, a novel framework for constructing Hierarchical Traversable 3DSGs, that redefines traversability by modeling operable obstacles as pathways, capturing their physical interactivity, functional semantics, and the scene's relational hierarchy. The results show that, relative to its baseline, HERO reduces PL by 35.1% in partially obstructed environments and increases SR by 79.4% in fully obstructed ones, demonstrating substantially higher efficiency and reachability.

