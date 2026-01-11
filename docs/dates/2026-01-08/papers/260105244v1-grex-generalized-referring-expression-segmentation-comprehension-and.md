---
layout: default
title: GREx: Generalized Referring Expression Segmentation, Comprehension, and Generation
---

# GREx: Generalized Referring Expression Segmentation, Comprehension, and Generation
**arXiv**：[2601.05244v1](https://arxiv.org/abs/2601.05244) · [PDF](https://arxiv.org/pdf/2601.05244.pdf)  
**作者**：Henghui Ding, Chang Liu, Shuting He, Xudong Jiang, Yu-Gang Jiang  

**一句话要点**：提出GREx基准和ReLA方法，以解决指代表达任务中多目标和无目标表达的限制。

**关键词**：指代表达分割, 指代表达理解, 指代表达生成, 多目标表达, 关系建模, 基准数据集

## 3 点简述
- 核心问题：现有指代表达任务仅支持单目标表达，限制了实际应用。
- 方法要点：构建gRefCOCO数据集，并设计ReLA方法建模区域间和区域-语言依赖关系。
- 实验或效果：ReLA在GRES和GREC任务上达到最优性能，数据集和方法开源。

## 摘要（原文）

> Referring Expression Segmentation (RES) and Comprehension (REC) respectively segment and detect the object described by an expression, while Referring Expression Generation (REG) generates an expression for the selected object. Existing datasets and methods commonly support single-target expressions only, i.e., one expression refers to one object, not considering multi-target and no-target expressions. This greatly limits the real applications of REx (RES/REC/REG). This paper introduces three new benchmarks called Generalized Referring Expression Segmentation (GRES), Comprehension (GREC), and Generation (GREG), collectively denoted as GREx, which extend the classic REx to allow expressions to identify an arbitrary number of objects. We construct the first large-scale GREx dataset gRefCOCO that contains multi-target, no-target, and single-target expressions and their corresponding images with labeled targets. GREx and gRefCOCO are designed to be backward-compatible with REx, facilitating extensive experiments to study the performance gap of the existing REx methods on GREx tasks. One of the challenges of GRES/GREC is complex relationship modeling, for which we propose a baseline ReLA that adaptively divides the image into regions with sub-instance clues and explicitly models the region-region and region-language dependencies. The proposed ReLA achieves the state-of-the-art results on the both GRES and GREC tasks. The proposed gRefCOCO dataset and method are available at https://henghuiding.github.io/GREx.

