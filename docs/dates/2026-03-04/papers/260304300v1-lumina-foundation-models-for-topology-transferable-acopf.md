---
layout: default
title: LUMINA: Foundation Models for Topology Transferable ACOPF
---

# LUMINA: Foundation Models for Topology Transferable ACOPF
**arXiv**：[2603.04300v1](https://arxiv.org/abs/2603.04300) · [PDF](https://arxiv.org/pdf/2603.04300.pdf)  
**作者**：Yijiang Li, Zeeshan Memon, Hongwei Jin, Stefano Fenu, Keunju Song, Sunash B Sharma, Parfait Gasana, Hongseok Kim, Liang Zhao, Kibaek Kim  

**一句话要点**：提出LUMINA框架以解决约束科学基础模型在ACOPF中的设计挑战

**关键词**：基础模型, AC最优潮流, 约束优化, 物理信息学习, 可转移拓扑, 科学计算

## 3 点简述
- 核心问题：约束科学系统如ACOPF需满足物理定律和安全限制，传统训练范式面临挑战
- 方法要点：通过系统实验提取三个设计原则，平衡物理不变表示与系统特定约束
- 实验或效果：开发数据与训练管道，支持可重复研究，确保高影响工况下的可靠性

## 摘要（原文）

> Foundation models in general promise to accelerate scientific computation by learning reusable representations across problem instances, yet constrained scientific systems, where predictions must satisfy physical laws and safety limits, pose unique challenges that stress conventional training paradigms. We derive design principles for constrained scientific foundation models through systematic investigation of AC optimal power flow (ACOPF), a representative optimization problem in power grid operations where power balance equations and operational constraints are non-negotiable. Through controlled experiments spanning architectures, training objectives, and system diversity, we extract three empirically grounded principles governing scientific foundation model design. These principles characterize three design trade-offs: learning physics-invariant representations while respecting system-specific constraints, optimizing accuracy while ensuring constraint satisfaction, and ensuring reliability in high-impact operating regimes. We present the LUMINA framework, including data processing and training pipelines to support reproducible research on physics-informed, feasibility-aware foundation models across scientific applications.

