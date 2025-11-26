---
layout: default
title: PhysChoreo: Physics-Controllable Video Generation with Part-Aware Semantic Grounding
---

# PhysChoreo: Physics-Controllable Video Generation with Part-Aware Semantic Grounding
**arXiv**：[2511.20562v1](https://arxiv.org/abs/2511.20562) · [PDF](https://arxiv.org/pdf/2511.20562.pdf)  
**作者**：Haoze Zhang, Tianyu Huang, Zichen Wan, Xiaowei Jin, Hongzhi Zhang, Hui Li, Wangmeng Zuo  

**一句话要点**：提出PhysChoreo框架，从单图像生成物理可控视频以提升物理真实性和控制性。

**关键词**：物理可控视频生成, 部分感知语义基础, 物理属性重建, 视频合成, 物理模拟

## 3 点简述
- 核心问题：现有视频生成模型缺乏显式物理可控性和物理合理性。
- 方法要点：通过部分感知物理属性重建和物理可编辑模拟实现视频合成。
- 实验或效果：在多个评估指标上优于现有方法，生成视频具有丰富动态行为和物理真实感。

## 摘要（原文）

> While recent video generation models have achieved significant visual fidelity, they often suffer from the lack of explicit physical controllability and plausibility. To address this, some recent studies attempted to guide the video generation with physics-based rendering. However, these methods face inherent challenges in accurately modeling complex physical properties and effectively control ling the resulting physical behavior over extended temporal sequences. In this work, we introduce PhysChoreo, a novel framework that can generate videos with diverse controllability and physical realism from a single image. Our method consists of two stages: first, it estimates the static initial physical properties of all objects in the image through part-aware physical property reconstruction. Then, through temporally instructed and physically editable simulation, it synthesizes high-quality videos with rich dynamic behaviors and physical realism. Experimental results show that PhysChoreo can generate videos with rich behaviors and physical realism, outperforming state-of-the-art methods on multiple evaluation metrics.

