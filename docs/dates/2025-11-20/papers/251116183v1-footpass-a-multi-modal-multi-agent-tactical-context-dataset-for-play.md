---
layout: default
title: FOOTPASS: A Multi-Modal Multi-Agent Tactical Context Dataset for Play-by-Play Action Spotting in Soccer Broadcast Videos
---

# FOOTPASS: A Multi-Modal Multi-Agent Tactical Context Dataset for Play-by-Play Action Spotting in Soccer Broadcast Videos
**arXiv**：[2511.16183v1](https://arxiv.org/abs/2511.16183) · [PDF](https://arxiv.org/pdf/2511.16183.pdf)  
**作者**：Jeremie Ochin, Raphael Chekroun, Bogdan Stanciulescu, Sotiris Manitsaris  

**一句话要点**：提出FOOTPASS数据集以支持足球广播视频中多模态多智能体战术背景下的逐场动作识别

**关键词**：足球视频理解, 多模态动作识别, 多智能体跟踪, 战术建模, 逐场数据生成

## 3 点简述
- 核心问题：现有动作识别方法不足以自动生成可靠的逐场数据，需结合战术知识。
- 方法要点：集成计算机视觉任务输出与足球战术先验知识，实现玩家中心动作识别。
- 实验或效果：未知具体实验细节，但作为首个基准，支持数据驱动体育分析。

## 摘要（原文）

> Soccer video understanding has motivated the creation of datasets for tasks such as temporal action localization, spatiotemporal action detection (STAD), or multiobject tracking (MOT). The annotation of structured sequences of events (who does what, when, and where) used for soccer analytics requires a holistic approach that integrates both STAD and MOT. However, current action recognition methods remain insufficient for constructing reliable play-by-play data and are typically used to assist rather than fully automate annotation. Parallel research has advanced tactical modeling, trajectory forecasting, and performance analysis, all grounded in game-state and play-by-play data. This motivates leveraging tactical knowledge as a prior to support computer-vision-based predictions, enabling more automated and reliable extraction of play-by-play data. We introduce Footovision Play-by-Play Action Spotting in Soccer Dataset (FOOTPASS), the first benchmark for play-by-play action spotting over entire soccer matches in a multi-modal, multi-agent tactical context. It enables the development of methods for player-centric action spotting that exploit both outputs from computer-vision tasks (e.g., tracking, identification) and prior knowledge of soccer, including its tactical regularities over long time horizons, to generate reliable play-by-play data streams. These streams form an essential input for data-driven sports analytics.

