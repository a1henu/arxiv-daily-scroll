---
layout: default
title: Language and Geometry Grounded Sparse Voxel Representations for Holistic Scene Understanding
---

# Language and Geometry Grounded Sparse Voxel Representations for Holistic Scene Understanding
**arXiv**：[2602.15734v1](https://arxiv.org/abs/2602.15734) · [PDF](https://arxiv.org/pdf/2602.15734.pdf)  
**作者**：Guile Wu, David Huang, Bingbing Liu, Dongfeng Bai  

**一句话要点**：提出基于语言与几何的稀疏体素表示方法，以统一框架实现三维场景的整体理解与重建。

**关键词**：三维场景理解, 稀疏体素表示, 语言特征蒸馏, 几何蒸馏, 统一框架, 整体重建

## 3 点简述
- 现有方法忽视场景外观、语义与几何的协同，导致理解偏离几何结构并与重建过程脱节。
- 采用稀疏体素作为基元，通过外观、密度、特征和置信度场，并引入特征调制模块和语言特征蒸馏。
- 集成几何蒸馏，通过深度相关和模式一致性正则化，在实验中展现优于现有方法的整体性能。

## 摘要（原文）

> Existing 3D open-vocabulary scene understanding methods mostly emphasize distilling language features from 2D foundation models into 3D feature fields, but largely overlook the synergy among scene appearance, semantics, and geometry. As a result, scene understanding often deviates from the underlying geometric structure of scenes and becomes decoupled from the reconstruction process. In this work, we propose a novel approach that leverages language and geometry grounded sparse voxel representations to comprehensively model appearance, semantics, and geometry within a unified framework. Specifically, we use 3D sparse voxels as primitives and employ an appearance field, a density field, a feature field, and a confidence field to holistically represent a 3D scene. To promote synergy among the appearance, density, and feature fields, we construct a feature modulation module and distill language features from a 2D foundation model into our 3D scene model. In addition, we integrate geometric distillation into feature field distillation to transfer geometric knowledge from a geometry foundation model to our 3D scene representations via depth correlation regularization and pattern consistency regularization. These components work together to synergistically model the appearance, semantics, and geometry of the 3D scene within a unified framework. Extensive experiments demonstrate that our approach achieves superior overall performance compared with state-of-the-art methods in holistic scene understanding and reconstruction.

