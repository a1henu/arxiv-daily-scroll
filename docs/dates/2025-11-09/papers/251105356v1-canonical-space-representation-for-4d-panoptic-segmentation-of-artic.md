---
layout: default
title: Canonical Space Representation for 4D Panoptic Segmentation of Articulated Objects
---

# Canonical Space Representation for 4D Panoptic Segmentation of Articulated Objects
**arXiv**：[2511.05356v1](https://arxiv.org/abs/2511.05356) · [PDF](https://arxiv.org/pdf/2511.05356.pdf)  
**作者**：Manuel Gomes, Bogdan Raducanu, Miguel Oliveira  

**一句话要点**：提出CanonSeg4D框架以解决铰接物体4D全景分割中的动态对齐问题

**关键词**：4D全景分割, 铰接物体感知, 规范空间表示, 时间动态建模, 数据集构建

## 3 点简述
- 核心问题：铰接物体感知忽略时间动态，缺乏4D全景分割基准数据集。
- 方法要点：通过估计偏移映射到规范空间，实现跨帧一致的部分对齐。
- 实验或效果：在Artic4D数据集上优于现有方法，提升复杂场景分割精度。

## 摘要（原文）

> Articulated object perception presents significant challenges in computer
> vision, particularly because most existing methods ignore temporal dynamics
> despite the inherently dynamic nature of such objects. The use of 4D temporal
> data has not been thoroughly explored in articulated object perception and
> remains unexamined for panoptic segmentation. The lack of a benchmark dataset
> further hurt this field. To this end, we introduce Artic4D as a new dataset
> derived from PartNet Mobility and augmented with synthetic sensor data,
> featuring 4D panoptic annotations and articulation parameters. Building on this
> dataset, we propose CanonSeg4D, a novel 4D panoptic segmentation framework.
> This approach explicitly estimates per-frame offsets mapping observed object
> parts to a learned canonical space, thereby enhancing part-level segmentation.
> The framework employs this canonical representation to achieve consistent
> alignment of object parts across sequential frames. Comprehensive experiments
> on Artic4D demonstrate that the proposed CanonSeg4D outperforms state of the
> art approaches in panoptic segmentation accuracy in more complex scenarios.
> These findings highlight the effectiveness of temporal modeling and canonical
> alignment in dynamic object understanding, and pave the way for future advances
> in 4D articulated object perception.

