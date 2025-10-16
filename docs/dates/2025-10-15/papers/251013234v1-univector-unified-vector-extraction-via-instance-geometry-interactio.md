---
layout: default
title: UniVector: Unified Vector Extraction via Instance-Geometry Interaction
---

# UniVector: Unified Vector Extraction via Instance-Geometry Interaction
**arXiv**：[2510.13234v1](https://arxiv.org/abs/2510.13234) · [PDF](https://arxiv.org/pdf/2510.13234.pdf)  
**作者**：Yinglong Yan, Jun Yue, Shaobo Xia, Hanmeng Sun, Tianxu Ying, Chengcheng Wu, Sifan Lan, Min He, Pedram Ghamisi, Leyuan Fang  

**一句话要点**：提出UniVector框架，通过实例-几何交互统一提取多种向量类型

**关键词**：向量提取, 实例-几何交互, 统一框架, 结构化查询, 多结构数据集

## 3 点简述
- 现有方法需为不同向量类型设计独立模型，限制复杂结构捕获能力
- 采用结构化查询编码实例与几何信息，通过交互模块迭代更新
- 在单结构与多结构任务中实现新SOTA，并发布Multi-Vector数据集

## 摘要（原文）

> Vector extraction retrieves structured vector geometry from raster images,
> offering high-fidelity representation and broad applicability. Existing
> methods, however, are usually tailored to a single vector type (e.g., polygons,
> polylines, line segments), requiring separate models for different structures.
> This stems from treating instance attributes (category, structure) and
> geometric attributes (point coordinates, connections) independently, limiting
> the ability to capture complex structures. Inspired by the human brain's
> simultaneous use of semantic and spatial interactions in visual perception, we
> propose UniVector, a unified VE framework that leverages instance-geometry
> interaction to extract multiple vector types within a single model. UniVector
> encodes vectors as structured queries containing both instance- and
> geometry-level information, and iteratively updates them through an interaction
> module for cross-level context exchange. A dynamic shape constraint further
> refines global structures and key points. To benchmark multi-structure
> scenarios, we introduce the Multi-Vector dataset with diverse polygons,
> polylines, and line segments. Experiments show UniVector sets a new state of
> the art on both single- and multi-structure VE tasks. Code and dataset will be
> released at https://github.com/yyyyll0ss/UniVector.

