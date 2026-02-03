---
layout: default
title: Learning Topology-Aware Implicit Field for Unified Pulmonary Tree Modeling with Incomplete Topological Supervision
---

# Learning Topology-Aware Implicit Field for Unified Pulmonary Tree Modeling with Incomplete Topological Supervision
**arXiv**：[2602.02186v1](https://arxiv.org/abs/2602.02186) · [PDF](https://arxiv.org/pdf/2602.02186.pdf)  
**作者**：Ziqiao Weng, Jiancheng Yang, Kangxian Xie, Bo Zhou, Weidong Cai  

**一句话要点**：提出TopoField框架，通过拓扑感知隐式场统一建模肺树，解决CT图像中拓扑不完整问题。

**关键词**：肺树建模, 拓扑修复, 隐式场, 医学图像分析, 多任务推理

## 3 点简述
- 核心问题：肺树提取常出现拓扑不完整，如分支缺失，影响解剖分析和现有方法鲁棒性。
- 方法要点：基于稀疏点云学习隐式场，通过合成结构破坏训练，支持拓扑修复和多任务联合推理。
- 实验或效果：在Lung3D+数据集上验证，提升拓扑完整性，实现准确解剖标记和肺段重建，计算高效。

## 摘要（原文）

> Pulmonary trees extracted from CT images frequently exhibit topological incompleteness, such as missing or disconnected branches, which substantially degrades downstream anatomical analysis and limits the applicability of existing pulmonary tree modeling pipelines. Current approaches typically rely on dense volumetric processing or explicit graph reasoning, leading to limited efficiency and reduced robustness under realistic structural corruption. We propose TopoField, a topology-aware implicit modeling framework that treats topology repair as a first-class modeling problem and enables unified multi-task inference for pulmonary tree analysis. TopoField represents pulmonary anatomy using sparse surface and skeleton point clouds and learns a continuous implicit field that supports topology repair without relying on complete or explicit disconnection annotations, by training on synthetically introduced structural disruptions over \textit{already} incomplete trees. Building upon the repaired implicit representation, anatomical labeling and lung segment reconstruction are jointly inferred through task-specific implicit functions within a single forward pass.Extensive experiments on the Lung3D+ dataset demonstrate that TopoField consistently improves topological completeness and achieves accurate anatomical labeling and lung segment reconstruction under challenging incomplete scenarios. Owing to its implicit formulation, TopoField attains high computational efficiency, completing all tasks in just over one second per case, highlighting its practicality for large-scale and time-sensitive clinical applications. Code and data will be available at https://github.com/HINTLab/TopoField.

