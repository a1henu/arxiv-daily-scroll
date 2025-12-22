---
layout: default
title: MMLANDMARKS: a Cross-View Instance-Level Benchmark for Geo-Spatial Understanding
---

# MMLANDMARKS: a Cross-View Instance-Level Benchmark for Geo-Spatial Understanding
**arXiv**：[2512.17492v1](https://arxiv.org/abs/2512.17492) · [PDF](https://arxiv.org/pdf/2512.17492.pdf)  
**作者**：Oskar Kristoffersen, Alba R. Sánchez, Morten R. Hannemose, Anders B. Dahl, Dim P. Papadopoulos  

**一句话要点**：提出MMLANDMARKS多模态基准以解决地理空间理解中模态覆盖不足的问题

**关键词**：多模态地理空间理解, 跨视图检索, 地标数据集, CLIP基线模型, 地理定位

## 3 点简述
- 核心问题：现有地理空间基准模态覆盖有限，阻碍多模态统一框架发展
- 方法要点：构建包含航拍图、地面图、文本和坐标的多模态数据集，支持跨视图检索等任务
- 实验或效果：通过CLIP基线模型展示广泛泛化性和竞争性能，验证多模态数据集必要性

## 摘要（原文）

> Geo-spatial analysis of our world benefits from a multimodal approach, as every single geographic location can be described in numerous ways (images from various viewpoints, textual descriptions, and geographic coordinates). Current geo-spatial benchmarks have limited coverage across modalities, considerably restricting progress in the field, as current approaches cannot integrate all relevant modalities within a unified framework. We introduce the Multi-Modal Landmark dataset (MMLANDMARKS), a benchmark composed of four modalities: 197k highresolution aerial images, 329k ground-view images, textual information, and geographic coordinates for 18,557 distinct landmarks in the United States. The MMLANDMARKS dataset has a one-to-one correspondence across every modality, which enables training and benchmarking models for various geo-spatial tasks, including cross-view Ground-to-Satellite retrieval, ground and satellite geolocalization, Text-to-Image, and Text-to-GPS retrieval. We demonstrate broad generalization and competitive performance against off-the-shelf foundational models and specialized state-of-the-art models across different tasks by employing a simple CLIP-inspired baseline, illustrating the necessity for multimodal datasets to achieve broad geo-spatial understanding.

