---
layout: default
title: Oh That Looks Familiar: A Novel Similarity Measure for Spreadsheet Template Discovery
---

# Oh That Looks Familiar: A Novel Similarity Measure for Spreadsheet Template Discovery
**arXiv**：[2511.06973v1](https://arxiv.org/abs/2511.06973) · [PDF](https://arxiv.org/pdf/2511.06973.pdf)  
**作者**：Ananad Krishnakumar, Vengadesh Ravikumaran  

**一句话要点**：提出混合距离度量以解决电子表格模板发现中的结构相似性量化问题

**关键词**：电子表格相似性, 混合距离度量, 模板发现, 无监督聚类, 语义嵌入

## 3 点简述
- 传统方法难以捕捉电子表格的空间布局和类型模式，导致模板识别不准确
- 方法结合语义嵌入、数据类型和空间位置，使用Chamfer和Hausdorff距离聚合
- 在FUSTE数据集上实现完美模板重建，ARI达1.00，优于Mondrian基线

## 摘要（原文）

> Traditional methods for identifying structurally similar spreadsheets fail to
> capture the spatial layouts and type patterns defining templates. To quantify
> spreadsheet similarity, we introduce a hybrid distance metric that combines
> semantic embeddings, data type information, and spatial positioning. In order
> to calculate spreadsheet similarity, our method converts spreadsheets into
> cell-level embeddings and then uses aggregation techniques like Chamfer and
> Hausdorff distances. Experiments across template families demonstrate superior
> unsupervised clustering performance compared to the graph-based Mondrian
> baseline, achieving perfect template reconstruction (Adjusted Rand Index of
> 1.00 versus 0.90) on the FUSTE dataset. Our approach facilitates large-scale
> automated template discovery, which in turn enables downstream applications
> such as retrieval-augmented generation over tabular collections, model
> training, and bulk data cleaning.

