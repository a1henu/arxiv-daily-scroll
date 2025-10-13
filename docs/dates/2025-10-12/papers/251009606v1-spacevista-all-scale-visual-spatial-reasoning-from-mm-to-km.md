---
layout: default
title: SpaceVista: All-Scale Visual Spatial Reasoning from mm to km
---

# SpaceVista: All-Scale Visual Spatial Reasoning from mm to km
**arXiv**：[2510.09606v1](https://arxiv.org/abs/2510.09606) · [PDF](https://arxiv.org/pdf/2510.09606.pdf)  
**作者**：Peiwen Sun, Shiqiang Lang, Dongming Wu, Yi Ding, Kaituo Feng, Huadai Liu, Zhen Ye, Rui Liu, Yun-Hui Liu, Jianan Wang, Xiangyu Yue  

**一句话要点**：提出SpaceVista以解决全尺度视觉空间推理问题，涵盖毫米到千米场景。

**关键词**：全尺度空间推理, 尺度感知建模, 渐进训练, 空间问答数据集, 多模态大语言模型, 视觉基准测试

## 3 点简述
- 核心问题：依赖室内3D扫描和手动标注，缺乏有效全尺度场景建模。
- 方法要点：集成结构化知识系统、尺度感知建模和渐进训练范式。
- 实验或效果：在5个基准测试中表现竞争性，展示全尺度和场景泛化能力。

## 摘要（原文）

> With the current surge in spatial reasoning explorations, researchers have
> made significant progress in understanding indoor scenes, but still struggle
> with diverse applications such as robotics and autonomous driving. This paper
> aims to advance all-scale spatial reasoning across diverse scenarios by
> tackling two key challenges: 1) the heavy reliance on indoor 3D scans and
> labor-intensive manual annotations for dataset curation; 2) the absence of
> effective all-scale scene modeling, which often leads to overfitting to
> individual scenes. In this paper, we introduce a holistic solution that
> integrates a structured spatial reasoning knowledge system, scale-aware
> modeling, and a progressive training paradigm, as the first attempt to broaden
> the all-scale spatial intelligence of MLLMs to the best of our knowledge. Using
> a task-specific, specialist-driven automated pipeline, we curate over 38K video
> scenes across 5 spatial scales to create SpaceVista-1M, a dataset comprising
> approximately 1M spatial QA pairs spanning 19 diverse task types. While
> specialist models can inject useful domain knowledge, they are not reliable for
> evaluation. We then build an all-scale benchmark with precise annotations by
> manually recording, retrieving, and assembling video-based data. However, naive
> training with SpaceVista-1M often yields suboptimal results due to the
> potential knowledge conflict. Accordingly, we introduce SpaceVista-7B, a
> spatial reasoning model that accepts dense inputs beyond semantics and uses
> scale as an anchor for scale-aware experts and progressive rewards. Finally,
> extensive evaluations across 5 benchmarks, including our SpaceVista-Bench,
> demonstrate competitive performance, showcasing strong generalization across
> all scales and scenarios. Our dataset, model, and benchmark will be released on
> https://peiwensun2000.github.io/mm2km .

