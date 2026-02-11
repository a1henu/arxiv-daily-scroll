---
layout: default
title: Efficient Special Stain Classification
---

# Efficient Special Stain Classification
**arXiv**：[2602.09989v1](https://arxiv.org/abs/2602.09989) · [PDF](https://arxiv.org/pdf/2602.09989.pdf)  
**作者**：Oskar Thaeter, Christian Grashei, Anette Haas, Elisa Schmoeckel, Han Li, Peter J. Schüffler  

**一句话要点**：提出基于缩略图的轻量级方法，实现数字病理工作流程中特殊染色的高效分类

**关键词**：数字病理学, 特殊染色分类, 多实例学习, 缩略图处理, 质量控制, 计算病理学

## 3 点简述
- 核心问题：病理学中特殊染色分类对临床档案质量控制至关重要，但传统方法效率低
- 方法要点：比较多实例学习与轻量级缩略图方法，后者通过处理缩略图大幅提升效率
- 实验效果：缩略图方法在外部数据泛化性更好，处理速度比多实例学习快两个数量级

## 摘要（原文）

> Stains are essential in histopathology to visualize specific tissue characteristics, with Haematoxylin and Eosin (H&E) serving as the clinical standard. However, pathologists frequently
>   utilize a variety of special stains for the diagnosis of specific morphologies. Maintaining accurate metadata for these slides is critical for quality control in clinical archives and for
>   the integrity of computational pathology datasets. In this work, we compare two approaches for automated classification of stains using whole slide images, covering the 14 most commonly
>   used special stains in our institute alongside standard and frozen-section H&E. We evaluate a Multi-Instance Learning (MIL) pipeline and a proposed lightweight thumbnail-based approach.
>   On internal test data, MIL achieved the highest performance (macro F1: 0.941 for 16 classes; 0.969 for 14 merged classes), while the thumbnail approach remained competitive (0.897 and
>   0.953, respectively). On external TCGA data, the thumbnail model generalized best (weighted F1: 0.843 vs. 0.807 for MIL). The thumbnail approach also increased throughput by two orders of
>   magnitude (5.635 vs. 0.018 slides/s for MIL with all patches). We conclude that thumbnail-based classification provides a scalable and robust solution for routine visual quality control
>   in digital pathology workflows.

