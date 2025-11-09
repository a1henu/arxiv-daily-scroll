---
layout: default
title: Tracking and Understanding Object Transformations
---

# Tracking and Understanding Object Transformations
**arXiv**：[2511.04678v1](https://arxiv.org/abs/2511.04678) · [PDF](https://arxiv.org/pdf/2511.04678.pdf)  
**作者**：Yihong Sun, Xinyu Yang, Jennifer J. Sun, Bharath Hariharan  

**一句话要点**：提出TubeletGraph系统以解决物体状态变换中的跟踪丢失问题

**关键词**：物体跟踪, 状态变换, 零样本学习, 语义推理, 视频理解, 基准数据集

## 3 点简述
- 核心问题：物体状态变换导致外观剧变，现有方法难以持续跟踪
- 方法要点：零样本系统识别遗漏轨迹，基于语义和邻近性整合并生成状态图
- 实验或效果：在VOST-TAS基准上实现SOTA跟踪，展示语义推理能力

## 摘要（原文）

> Real-world objects frequently undergo state transformations. From an apple
> being cut into pieces to a butterfly emerging from its cocoon, tracking through
> these changes is important for understanding real-world objects and dynamics.
> However, existing methods often lose track of the target object after
> transformation, due to significant changes in object appearance. To address
> this limitation, we introduce the task of Track Any State: tracking objects
> through transformations while detecting and describing state changes,
> accompanied by a new benchmark dataset, VOST-TAS. To tackle this problem, we
> present TubeletGraph, a zero-shot system that recovers missing objects after
> transformation and maps out how object states are evolving over time.
> TubeletGraph first identifies potentially overlooked tracks, and determines
> whether they should be integrated based on semantic and proximity priors. Then,
> it reasons about the added tracks and generates a state graph describing each
> observed transformation. TubeletGraph achieves state-of-the-art tracking
> performance under transformations, while demonstrating deeper understanding of
> object transformations and promising capabilities in temporal grounding and
> semantic reasoning for complex object transformations. Code, additional
> results, and the benchmark dataset are available at
> https://tubelet-graph.github.io.

