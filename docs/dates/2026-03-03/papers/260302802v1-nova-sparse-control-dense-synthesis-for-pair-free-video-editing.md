---
layout: default
title: NOVA: Sparse Control, Dense Synthesis for Pair-Free Video Editing
---

# NOVA: Sparse Control, Dense Synthesis for Pair-Free Video Editing
**arXiv**：[2603.02802v1](https://arxiv.org/abs/2603.02802) · [PDF](https://arxiv.org/pdf/2603.02802.pdf)  
**作者**：Tianlin Pan, Jiayi Dai, Chenpu Yuan, Zhengyao Lv, Binxin Yang, Hubery Yin, Chen Li, Jing Lyu, Caifeng Shan, Chenyang Si  

**一句话要点**：提出NOVA框架，通过稀疏控制和密集合成实现无需配对数据的视频编辑

**关键词**：无配对视频编辑, 稀疏控制, 密集合成, 退化模拟训练, 时间一致性, 运动重建

## 3 点简述
- 核心问题：现有视频编辑模型依赖大规模配对数据，收集困难，且全局运动控制方法难以保持背景和时间一致性。
- 方法要点：采用稀疏分支提供语义指导，密集分支整合原始视频的运动和纹理信息，结合退化模拟训练策略学习运动重建和时间一致性。
- 实验或效果：在编辑保真度、运动保持和时间连贯性方面优于现有方法，无需配对数据。

## 摘要（原文）

> Recent video editing models have achieved impressive results, but most still require large-scale paired datasets. Collecting such naturally aligned pairs at scale remains highly challenging and constitutes a critical bottleneck, especially for local video editing data. Existing workarounds transfer image editing to video through global motion control for pair-free video editing, but such designs struggle with background and temporal consistency. In this paper, we propose NOVA: Sparse Control \& Dense Synthesis, a new framework for unpaired video editing. Specifically, the sparse branch provides semantic guidance through user-edited keyframes distributed across the video, and the dense branch continuously incorporates motion and texture information from the original video to maintain high fidelity and coherence. Moreover, we introduce a degradation-simulation training strategy that enables the model to learn motion reconstruction and temporal consistency by training on artificially degraded videos, thus eliminating the need for paired data. Our extensive experiments demonstrate that NOVA outperforms existing approaches in edit fidelity, motion preservation, and temporal coherence.

