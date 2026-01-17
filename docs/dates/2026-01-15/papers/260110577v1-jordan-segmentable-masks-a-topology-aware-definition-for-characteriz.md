---
layout: default
title: Jordan-Segmentable Masks: A Topology-Aware definition for characterizing Binary Image Segmentation
---

# Jordan-Segmentable Masks: A Topology-Aware definition for characterizing Binary Image Segmentation
**arXiv**：[2601.10577v1](https://arxiv.org/abs/2601.10577) · [PDF](https://arxiv.org/pdf/2601.10577.pdf)  
**作者**：Serena Grazia De Benedictis, Amedeo Altavilla, Nicoletta Del Buono  

**一句话要点**：提出Jordan可分割掩码，基于数字拓扑理论评估分割的结构连贯性。

**关键词**：图像分割评估, 数字拓扑, Jordan曲线定理, Betti数, 结构连贯性, 无监督准则

## 3 点简述
- 核心问题：传统分割评估指标难以捕捉结构拓扑连贯性，导致高分数但形状或连通性差。
- 方法要点：基于Jordan曲线定理定义Jordan可分割掩码，利用Betti数验证拓扑分离为两个连通分量。
- 实验或效果：提供无监督数学准则，适用于需保持拓扑正确性的应用如医学影像。

## 摘要（原文）

> Image segmentation plays a central role in computer vision. However, widely used evaluation metrics, whether pixel-wise, region-based, or boundary-focused, often struggle to capture the structural and topological coherence of a segmentation. In many practical scenarios, such as medical imaging or object delineation, small inaccuracies in boundary, holes, or fragmented predictions can result in high metric scores, despite the fact that the resulting masks fail to preserve the object global shape or connectivity. This highlights a limitation of conventional metrics: they are unable to assess whether a predicted segmentation partitions the image into meaningful interior and exterior regions.
>   In this work, we introduce a topology-aware notion of segmentation based on the Jordan Curve Theorem, and adapted for use in digital planes. We define the concept of a \emph{Jordan-segmentatable mask}, which is a binary segmentation whose structure ensures a topological separation of the image domain into two connected components. We analyze segmentation masks through the lens of digital topology and homology theory, extracting a $4$-curve candidate from the mask, verifying its topological validity using Betti numbers. A mask is considered Jordan-segmentatable when this candidate forms a digital 4-curve with $β_0 = β_1 = 1$, or equivalently when its complement splits into exactly two $8$-connected components.
>   This framework provides a mathematically rigorous, unsupervised criterion with which to assess the structural coherence of segmentation masks. By combining digital Jordan theory and homological invariants, our approach provides a valuable alternative to standard evaluation metrics, especially in applications where topological correctness must be preserved.

