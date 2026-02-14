---
layout: default
title: Egocentric Gaze Estimation via Neck-Mounted Camera
---

# Egocentric Gaze Estimation via Neck-Mounted Camera
**arXiv**：[2602.11669v1](https://arxiv.org/abs/2602.11669) · [PDF](https://arxiv.org/pdf/2602.11669.pdf)  
**作者**：Haoyu Huang, Yoichi Sato  

**一句话要点**：提出基于颈戴相机的自我中心视线估计新任务，通过Transformer模型与辅助任务提升性能

**关键词**：自我中心视线估计, 颈戴相机, Transformer模型, 视线越界分类, 多视角学习, 数据集收集

## 3 点简述
- 核心问题：现有自我中心视线估计主要关注头戴相机，颈戴相机视角下的任务未被充分探索，缺乏数据集。
- 方法要点：收集首个颈戴相机视线估计数据集，评估Transformer模型GLC，并引入视线越界分类和多视角协同学习扩展。
- 实验或效果：视线越界分类任务提升性能，但多视角协同学习未带来增益，分析结果并讨论颈戴视线估计的潜在应用。

## 摘要（原文）

> This paper introduces neck-mounted view gaze estimation, a new task that estimates user gaze from the neck-mounted camera perspective. Prior work on egocentric gaze estimation, which predicts device wearer's gaze location within the camera's field of view, mainly focuses on head-mounted cameras while alternative viewpoints remain underexplored. To bridge this gap, we collect the first dataset for this task, consisting of approximately 4 hours of video collected from 8 participants during everyday activities. We evaluate a transformer-based gaze estimation model, GLC, on the new dataset and propose two extensions: an auxiliary gaze out-of-bound classification task and a multi-view co-learning approach that jointly trains head-view and neck-view models using a geometry-aware auxiliary loss. Experimental results show that incorporating gaze out-of-bound classification improves performance over standard fine-tuning, while the co-learning approach does not yield gains. We further analyze these results and discuss implications for neck-mounted gaze estimation.

