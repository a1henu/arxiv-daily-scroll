---
layout: default
title: Extended OpenTT Games Dataset: A table tennis dataset for fine-grained shot type and point outcome
---

# Extended OpenTT Games Dataset: A table tennis dataset for fine-grained shot type and point outcome
**arXiv**：[2512.19327v1](https://arxiv.org/abs/2512.19327) · [PDF](https://arxiv.org/pdf/2512.19327.pdf)  
**作者**：Moamal Fadhil Abdul, Jonas Bruun Hubrechts, Thomas Martini Jørgensen, Emil Hovad  

**一句话要点**：扩展OpenTTGames数据集，提供精细击球类型与回合结果标注，以支持乒乓球视频分析。

**关键词**：乒乓球视频分析, 精细击球分类, 数据集扩展, 战术理解, 标注方案

## 3 点简述
- 核心问题：乒乓球视频中自动检测和分类击球类型缺乏公开、精细标注的数据集。
- 方法要点：在OpenTTGames数据集基础上，添加帧级击球类型、球员姿态和回合结果标签。
- 实验或效果：提供标注方案和基准，促进球拍运动中的战术理解模型开发。

## 摘要（原文）

> Automatically detecting and classifying strokes in table tennis video can streamline training workflows, enrich broadcast overlays, and enable fine-grained performance analytics. For this to be possible, annotated video data of table tennis is needed. We extend the public OpenTTGames dataset with highly detailed, frame-accurate shot type annotations (forehand, backhand with subtypes), player posture labels (body lean and leg stance), and rally outcome tags at point end. OpenTTGames is a set of recordings from the side of the table with official labels for bounces, when the ball is above the net, or hitting the net. The dataset already contains ball coordinates near events, which are either "bounce", "net", or "empty_event" in the original OpenTTGames dataset, and semantic masks (humans, table, scoreboard). Our extension adds the types of stroke to the events and a per-player taxonomy so models can move beyond event spotting toward tactical understanding (e.g., whether a stroke is likely to win the point or set up an advantage). We provide a compact coding scheme and code-assisted labeling procedure to support reproducible annotations and baselines for fine-grained stroke understanding in racket sports. This fills a practical gap in the community, where many prior video resources are either not publicly released or carry restrictive/unclear licenses that hinder reuse and benchmarking. Our annotations are released under the same CC BY-NC-SA 4.0 license as OpenTTGames, allowing free non-commercial use, modification, and redistribution, with appropriate attribution.

