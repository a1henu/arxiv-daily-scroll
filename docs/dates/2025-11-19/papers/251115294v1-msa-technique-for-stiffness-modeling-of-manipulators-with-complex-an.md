---
layout: default
title: MSA - Technique for Stiffness Modeling of Manipulators with Complex and Hybrid Structures
---

# MSA - Technique for Stiffness Modeling of Manipulators with Complex and Hybrid Structures
**arXiv**：[2511.15294v1](https://arxiv.org/abs/2511.15294) · [PDF](https://arxiv.org/pdf/2511.15294.pdf)  
**作者**：Alexandr Klimchik, Anatol Pashkevich, Damien Chablat  

**一句话要点**：提出基于矩阵结构分析的刚度建模方法，用于复杂混合结构机械臂。

**关键词**：刚度建模, 矩阵结构分析, 机械臂, 混合结构, 笛卡尔刚度矩阵

## 3 点简述
- 核心问题：复杂混合结构机械臂的刚度建模，涉及闭环、柔性连杆和弹性关节。
- 方法要点：使用半解析法生成笛卡尔刚度矩阵，避免传统矩阵合并过程。
- 实验或效果：以NaVaRo机械臂为例验证方法优势，实现高效刚度分析。

## 摘要（原文）

> The paper presents a systematic approach for stiffness modeling of manipulators with complex and hybrid structures using matrix structural analysis. In contrast to previous results, it is suitable for mixed architectures containing closed-loops, flexible links, rigid connections, passive and elastic joints with external loadings and preloadings. The proposed approach produces the Cartesian stiffness matrices in a semi-analytical manner. It presents the manipulator stiffness model as a set of conventional equations describing the link elasticities that are supplemented by a set of constraints describing connections between links. Its allows user straightforward aggregation of stiffness model equations avoiding traditional column/row merging procedures in the extended stiffness matrix. Advantages of this approach are illustrated by stiffness analysis of NaVaRo manipulator.

