---
layout: default
title: VideoLoom: A Video Large Language Model for Joint Spatial-Temporal Understanding
---

# VideoLoom: A Video Large Language Model for Joint Spatial-Temporal Understanding
**arXiv**：[2601.07290v1](https://arxiv.org/abs/2601.07290) · [PDF](https://arxiv.org/pdf/2601.07290.pdf)  
**作者**：Jiapeng Shi, Junke Wang, Zuyao You, Bo He, Zuxuan Wu  

**一句话要点**：提出VideoLoom视频大语言模型，用于联合时空理解，并引入数据集和基准测试。

**关键词**：视频大语言模型, 时空联合理解, 视频数据集, 基准测试, 视频对象分割, 时间定位

## 3 点简述
- 核心问题：视频理解需同时处理空间和时间信息，现有模型能力有限。
- 方法要点：构建LoomData-8.7k数据集，训练VideoLoom实现联合时空定位。
- 实验或效果：在多个基准测试中达到先进性能，如ReVOS和Charades-STA。

## 摘要（原文）

> This paper presents VideoLoom, a unified Video Large Language Model (Video LLM) for joint spatial-temporal understanding. To facilitate the development of fine-grained spatial and temporal localization capabilities, we curate LoomData-8.7k, a human-centric video dataset with temporally grounded and spatially localized captions. With this, VideoLoom achieves state-of-the-art or highly competitive performance across a variety of spatial and temporal benchmarks (e.g., 63.1 J&F on ReVOS for referring video object segmentation, and 48.3 R1@0.7 on Charades-STA for temporal grounding). In addition, we introduce LoomBench, a novel benchmark consisting of temporal, spatial, and compositional video-question pairs, enabling a comprehensive evaluation of Video LLMs from diverse aspects. Collectively, these contributions offer a universal and effective suite for joint spatial-temporal video understanding, setting a new standard in multimodal intelligence.

