---
layout: default
title: FOOTPASS: A Multi-Modal Multi-Agent Tactical Context Dataset for Play-by-Play Action Spotting in Soccer Broadcast Videos
---

# FOOTPASS: A Multi-Modal Multi-Agent Tactical Context Dataset for Play-by-Play Action Spotting in Soccer Broadcast Videos
**arXiv**：[2511.16183v1](https://arxiv.org/abs/2511.16183) · [PDF](https://arxiv.org/pdf/2511.16183.pdf)  
**作者**：Jeremie Ochin, Raphael Chekroun, Bogdan Stanciulescu, Sotiris Manitsaris  

**一句话要点**：提出FOOTPASS数据集以支持足球视频中基于战术上下文的逐场动作识别

**关键词**：足球视频理解, 多模态动作识别, 战术上下文建模, 逐场数据生成, 计算机视觉基准

## 3 点简述
- 核心问题：现有动作识别方法不足以自动生成可靠的足球逐场数据流
- 方法要点：结合计算机视觉输出与足球战术先验知识，实现多模态多代理动作识别
- 实验或效果：未知，但数据集旨在促进可靠逐场数据提取方法的发展

## 摘要（原文）

> Soccer video understanding has motivated the creation of datasets for tasks such as temporal action localization, spatiotemporal action detection (STAD), or multiobject tracking (MOT). The annotation of structured sequences of events (who does what, when, and where) used for soccer analytics requires a holistic approach that integrates both STAD and MOT. However, current action recognition methods remain insufficient for constructing reliable play-by-play data and are typically used to assist rather than fully automate annotation. Parallel research has advanced tactical modeling, trajectory forecasting, and performance analysis, all grounded in game-state and play-by-play data. This motivates leveraging tactical knowledge as a prior to support computer-vision-based predictions, enabling more automated and reliable extraction of play-by-play data. We introduce Footovision Play-by-Play Action Spotting in Soccer Dataset (FOOTPASS), the first benchmark for play-by-play action spotting over entire soccer matches in a multi-modal, multi-agent tactical context. It enables the development of methods for player-centric action spotting that exploit both outputs from computer-vision tasks (e.g., tracking, identification) and prior knowledge of soccer, including its tactical regularities over long time horizons, to generate reliable play-by-play data streams. These streams form an essential input for data-driven sports analytics.

