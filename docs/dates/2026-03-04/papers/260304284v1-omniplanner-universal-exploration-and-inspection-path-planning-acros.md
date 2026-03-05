---
layout: default
title: OmniPlanner: Universal Exploration and Inspection Path Planning across Robot Morphologies
---

# OmniPlanner: Universal Exploration and Inspection Path Planning across Robot Morphologies
**arXiv**：[2603.04284v1](https://arxiv.org/abs/2603.04284) · [PDF](https://arxiv.org/pdf/2603.04284.pdf)  
**作者**：Angelos Zacharia, Mihir Dharmadhikari, Mohit Singh, Kostas Alexis  

**一句话要点**：提出OmniPlanner统一规划框架，实现跨空中、地面和水下机器人的通用探索与巡检路径规划。

**关键词**：跨域路径规划, 机器人形态抽象, 探索与巡检一体化

## 3 点简述
- 核心问题：现有路径规划方法多为领域特定，限制了跨平台可扩展性和应用范围。
- 方法要点：集成体积探索、基于视点的巡检和目标到达行为，通过平台抽象层处理形态特定约束。
- 实验或效果：在模拟和实地部署中验证了跨域泛化能力，提升了探索与巡检效率。

## 摘要（原文）

> Autonomous robotic systems are increasingly deployed for mapping, monitoring, and inspection in complex and unstructured environments. However, most existing path planning approaches remain domain-specific (i.e., either on air, land, or sea), limiting their scalability and cross-platform applicability. This article presents OmniPlanner, a unified planning framework for autonomous exploration and inspection across aerial, ground, and underwater robots. The method integrates volumetric exploration and viewpoint-based inspection, alongside target reach behaviors within a single modular architecture, complemented by a platform abstraction layer that captures morphology-specific sensing, traversability and motion constraints. This enables the same planning strategy to generalize across distinct mobility domains with minimal retuning. The framework is validated through extensive simulation studies and field deployments in underground mines, industrial facilities, forests, submarine bunkers, and structured outdoor environments. Across these diverse scenarios, OmniPlanner demonstrates robust performance, consistent cross-domain generalization, and improved exploration and inspection efficiency compared to representative state-of-the-art baselines.

