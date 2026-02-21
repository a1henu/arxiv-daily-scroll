---
layout: default
title: PartRAG: Retrieval-Augmented Part-Level 3D Generation and Editing
---

# PartRAG: Retrieval-Augmented Part-Level 3D Generation and Editing
**arXiv**：[2602.17033v1](https://arxiv.org/abs/2602.17033) · [PDF](https://arxiv.org/pdf/2602.17033.pdf)  
**作者**：Peize Li, Zeyu Zhang, Hao Tang  

**一句话要点**：提出PartRAG框架，通过检索增强实现单图像3D生成与部件级编辑

**关键词**：3D生成, 部件级编辑, 检索增强, 扩散变换器, 多视图一致性

## 3 点简述
- 核心问题：单图像3D生成中部件几何多样性不足、多视图一致性差，且编辑支持有限。
- 方法要点：结合外部部件数据库与扩散变换器，通过分层对比检索注入多样部件，并支持掩码部件级编辑。
- 实验或效果：在Objaverse等数据集上提升指标，如Chamfer距离从0.1726降至0.1528，支持快速交互编辑。

## 摘要（原文）

> Single-image 3D generation with part-level structure remains challenging: learned priors struggle to cover the long tail of part geometries and maintain multi-view consistency, and existing systems provide limited support for precise, localized edits. We present PartRAG, a retrieval-augmented framework that integrates an external part database with a diffusion transformer to couple generation with an editable representation. To overcome the first challenge, we introduce a Hierarchical Contrastive Retrieval module that aligns dense image patches with 3D part latents at both part and object granularity, retrieving from a curated bank of 1,236 part-annotated assets to inject diverse, physically plausible exemplars into denoising. To overcome the second challenge, we add a masked, part-level editor that operates in a shared canonical space, enabling swaps, attribute refinements, and compositional updates without regenerating the whole object while preserving non-target parts and multi-view consistency. PartRAG achieves competitive results on Objaverse, ShapeNet, and ABO-reducing Chamfer Distance from 0.1726 to 0.1528 and raising F-Score from 0.7472 to 0.844 on Objaverse-with inference of 38s and interactive edits in 5-8s. Qualitatively, PartRAG produces sharper part boundaries, better thin-structure fidelity, and robust behavior on articulated objects. Code: https://github.com/AIGeeksGroup/PartRAG. Website: https://aigeeksgroup.github.io/PartRAG.

