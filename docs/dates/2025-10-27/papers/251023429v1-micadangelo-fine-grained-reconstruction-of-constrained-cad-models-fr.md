---
layout: default
title: MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans
---

# MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans
**arXiv**：[2510.23429v1](https://arxiv.org/abs/2510.23429) · [PDF](https://arxiv.org/pdf/2510.23429.pdf)  
**作者**：Ahmet Serdar Karadeniz, Dimitrios Mallis, Danila Rukhovich, Kseniya Cherenkova, Anis Kacem, Djamila Aouada  

**一句话要点**：提出多平面截面方法以解决3D扫描重建参数化CAD模型的精细细节和约束问题

**关键词**：CAD逆向工程, 3D扫描重建, 参数化建模, 草图约束, 多平面截面

## 3 点简述
- 核心问题：现有方法难以从3D扫描重建高精度、参数化CAD模型，忽略草图级约束。
- 方法要点：利用多平面截面提取2D模式，捕捉精细参数细节，并集成草图约束。
- 实验或效果：优于现有方法，首次实现约束重建，生成可编辑CAD模型。

## 摘要（原文）

> Computer-Aided Design (CAD) plays a foundational role in modern manufacturing
> and product development, often requiring designers to modify or build upon
> existing models. Converting 3D scans into parametric CAD representations--a
> process known as CAD reverse engineering--remains a significant challenge due
> to the high precision and structural complexity of CAD models. Existing deep
> learning-based approaches typically fall into two categories: bottom-up,
> geometry-driven methods, which often fail to produce fully parametric outputs,
> and top-down strategies, which tend to overlook fine-grained geometric details.
> Moreover, current methods neglect an essential aspect of CAD modeling:
> sketch-level constraints. In this work, we introduce a novel approach to CAD
> reverse engineering inspired by how human designers manually perform the task.
> Our method leverages multi-plane cross-sections to extract 2D patterns and
> capture fine parametric details more effectively. It enables the reconstruction
> of detailed and editable CAD models, outperforming state-of-the-art methods
> and, for the first time, incorporating sketch constraints directly into the
> reconstruction process.

