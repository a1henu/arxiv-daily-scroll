---
layout: default
title: BenchSeg: A Large-Scale Dataset and Benchmark for Multi-View Food Video Segmentation
---

# BenchSeg: A Large-Scale Dataset and Benchmark for Multi-View Food Video Segmentation
**arXiv**：[2601.07581v1](https://arxiv.org/abs/2601.07581) · [PDF](https://arxiv.org/pdf/2601.07581.pdf)  
**作者**：Ahmad AlMughrabi, Guillermo Rivo, Carlos Jiménez-Farfán, Umair Haroon, Farid Al-Areqi, Hyunjun Jung, Benjamin Busam, Ricardo Marques, Petia Radeva  

**一句话要点**：提出BenchSeg多视角食物视频分割数据集与基准，解决现有方法视角泛化不足问题

**关键词**：食物图像分割, 多视角数据集, 视频分割基准, 时序一致性, 记忆增强模型, 饮食分析

## 3 点简述
- 现有食物图像分割方法在多视角数据不足和视角泛化能力弱的问题
- 构建包含55个菜品场景、25,284帧标注的多视角食物视频数据集BenchSeg
- 评估20种分割模型，发现记忆增强方法能保持跨帧时序一致性并提升性能

## 摘要（原文）

> Food image segmentation is a critical task for dietary analysis, enabling accurate estimation of food volume and nutrients. However, current methods suffer from limited multi-view data and poor generalization to new viewpoints. We introduce BenchSeg, a novel multi-view food video segmentation dataset and benchmark. BenchSeg aggregates 55 dish scenes (from Nutrition5k, Vegetables & Fruits, MetaFood3D, and FoodKit) with 25,284 meticulously annotated frames, capturing each dish under free 360° camera motion. We evaluate a diverse set of 20 state-of-the-art segmentation models (e.g., SAM-based, transformer, CNN, and large multimodal) on the existing FoodSeg103 dataset and evaluate them (alone and combined with video-memory modules) on BenchSeg. Quantitative and qualitative results demonstrate that while standard image segmenters degrade sharply under novel viewpoints, memory-augmented methods maintain temporal consistency across frames. Our best model based on a combination of SeTR-MLA+XMem2 outperforms prior work (e.g., improving over FoodMem by ~2.63% mAP), offering new insights into food segmentation and tracking for dietary analysis. We release BenchSeg to foster future research. The project page including the dataset annotations and the food segmentation models can be found at https://amughrabi.github.io/benchseg.

