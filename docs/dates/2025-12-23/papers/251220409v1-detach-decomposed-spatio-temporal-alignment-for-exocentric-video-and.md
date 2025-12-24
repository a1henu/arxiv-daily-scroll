---
layout: default
title: DETACH : Decomposed Spatio-Temporal Alignment for Exocentric Video and Ambient Sensors with Staged Learning
---

# DETACH : Decomposed Spatio-Temporal Alignment for Exocentric Video and Ambient Sensors with Staged Learning
**arXiv**：[2512.20409v1](https://arxiv.org/abs/2512.20409) · [PDF](https://arxiv.org/pdf/2512.20409.pdf)  
**作者**：Junho Yoon, Jaemo Jung, Hyunju Kim, Dongman Lee  

**一句话要点**：提出DETACH框架，通过分解时空对齐解决外中心视频与环境传感器中的局部细节缺失和误对齐问题。

**关键词**：外中心视频对齐, 环境传感器, 时空分解, 对比学习, 动作识别, 多模态融合

## 3 点简述
- 核心问题：外中心视频与环境传感器对齐中，全局方法无法捕捉局部细节且易因相似时间模式导致误对齐。
- 方法要点：采用分解时空框架，通过在线聚类发现传感器-空间特征，并分阶段进行空间对应和时空加权对比对齐。
- 实验或效果：在Opportunity++和HWU-USP数据集的下游任务中，相比适应基线有显著提升。

## 摘要（原文）

> Aligning egocentric video with wearable sensors have shown promise for human action recognition, but face practical limitations in user discomfort, privacy concerns, and scalability. We explore exocentric video with ambient sensors as a non-intrusive, scalable alternative. While prior egocentric-wearable works predominantly adopt Global Alignment by encoding entire sequences into unified representations, this approach fails in exocentric-ambient settings due to two problems: (P1) inability to capture local details such as subtle motions, and (P2) over-reliance on modality-invariant temporal patterns, causing misalignment between actions sharing similar temporal patterns with different spatio-semantic contexts. To resolve these problems, we propose DETACH, a decomposed spatio-temporal framework. This explicit decomposition preserves local details, while our novel sensor-spatial features discovered via online clustering provide semantic grounding for context-aware alignment. To align the decomposed features, our two-stage approach establishes spatial correspondence through mutual supervision, then performs temporal alignment via a spatial-temporal weighted contrastive loss that adaptively handles easy negatives, hard negatives, and false negatives. Comprehensive experiments with downstream tasks on Opportunity++ and HWU-USP datasets demonstrate substantial improvements over adapted egocentric-wearable baselines.

