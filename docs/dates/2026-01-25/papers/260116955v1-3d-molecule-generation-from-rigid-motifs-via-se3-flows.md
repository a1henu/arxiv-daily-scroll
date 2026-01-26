---
layout: default
title: 3D Molecule Generation from Rigid Motifs via SE(3) Flows
---

# 3D Molecule Generation from Rigid Motifs via SE(3) Flows
**arXiv**：[2601.16955v1](https://arxiv.org/abs/2601.16955) · [PDF](https://arxiv.org/pdf/2601.16955.pdf)  
**作者**：Roman Poletukhin, Marcel Kollovieh, Eike Eberhard, Stephan Günnemann  

**一句话要点**：提出基于刚性基序的SE(3)流生成方法，用于三维分子结构生成

**关键词**：三维分子生成, 刚性基序, SE(3)等变模型, 生成流, 分子表示压缩

## 3 点简述
- 核心问题：三维分子生成通常基于原子级别，但分子图生成常使用片段作为结构单元。
- 方法要点：将分子表示为刚性基序集合，采用SE(3)等变生成模型进行三维分子生成。
- 实验或效果：在基准测试中性能相当或优于现有方法，生成步骤减少2-10倍，分子表示压缩3.5倍。

## 摘要（原文）

> Three-dimensional molecular structure generation is typically performed at the level of individual atoms, yet molecular graph generation techniques often consider fragments as their structural units. Building on the advances in frame-based protein structure generation, we extend these fragmentation ideas to 3D, treating general molecules as sets of rigid-body motifs. Utilising this representation, we employ SE(3)-equivariant generative modelling for de novo 3D molecule generation from rigid motifs. In our evaluations, we observe comparable or superior results to state-of-the-art across benchmarks, surpassing it in atom stability on GEOM-Drugs, while yielding a 2x to 10x reduction in generation steps and offering 3.5x compression in molecular representations compared to the standard atom-based methods.

