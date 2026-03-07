---
layout: default
title: Generalizable Multiscale Segmentation of Heterogeneous Map Collections
---

# Generalizable Multiscale Segmentation of Heterogeneous Map Collections
**arXiv**：[2603.05037v1](https://arxiv.org/abs/2603.05037) · [PDF](https://arxiv.org/pdf/2603.05037.pdf)  
**作者**：Remi Petitpierre  

**一句话要点**：提出通用多尺度分割框架与数据集，以处理异构历史地图集合的语义分割问题。

**关键词**：历史地图分割, 多尺度集成, 程序化数据合成, 语义分割, 通用模型, 地图识别

## 3 点简述
- 核心问题：历史地图集合风格、尺度和地理焦点多样，现有模型多针对同质地图系列，缺乏通用性。
- 方法要点：结合程序化数据合成与多尺度集成，提升分割模型的鲁棒性和可迁移性。
- 实验或效果：在HCMSSD和Semap数据集上达到最先进性能，分割表现跨集合、尺度、区域和出版背景稳定。

## 摘要（原文）

> Historical map collections are highly diverse in style, scale, and geographic focus, often consisting of many single-sheet documents. Yet most work in map recognition focuses on specialist models tailored to homogeneous map series. In contrast, this article aims to develop generalizable semantic segmentation models and ontology. First, we introduce Semap, a new open benchmark dataset comprising 1,439 manually annotated patches designed to reflect the variety of historical map documents. Second, we present a segmentation framework that combines procedural data synthesis with multiscale integration to improve robustness and transferability. This framework achieves state-of-the-art performance on both the HCMSSD and Semap datasets, showing that a diversity-driven approach to map recognition is not only viable but also beneficial. The results indicate that segmentation performance remains largely stable across map collections, scales, geographic regions, and publication contexts. By proposing benchmark datasets and methods for the generic segmentation of historical maps, this work opens the way to integrating the long tail of cartographic archives to historical geographic studies.

