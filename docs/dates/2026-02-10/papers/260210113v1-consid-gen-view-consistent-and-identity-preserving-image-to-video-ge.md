---
layout: default
title: ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation
---

# ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation
**arXiv**：[2602.10113v1](https://arxiv.org/abs/2602.10113) · [PDF](https://arxiv.org/pdf/2602.10113.pdf)  
**作者**：Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  

**一句话要点**：提出ConsID-Gen框架以解决图像到视频生成中的视角一致性和身份保持问题

**关键词**：图像到视频生成, 视角一致性, 身份保持, 扩散Transformer, 数据集构建, 多视图基准

## 3 点简述
- 核心问题：现有I2V方法在视角变化下易出现外观漂移和几何失真，源于单视图稀疏性和跨模态对齐弱。
- 方法要点：构建ConsIDVid数据集和基准，提出双流视觉-几何编码器与文本-视觉连接器增强条件，结合扩散Transformer生成视频。
- 实验或效果：在ConsIDVid-Bench上评估，ConsID-Gen在多项指标上优于Wan2.1和HunyuanVideo，实现更好的身份保真度和时间一致性。

## 摘要（原文）

> Image-to-Video generation (I2V) animates a static image into a temporally coherent video sequence following textual instructions, yet preserving fine-grained object identity under changing viewpoints remains a persistent challenge. Unlike text-to-video models, existing I2V pipelines often suffer from appearance drift and geometric distortion, artifacts we attribute to the sparsity of single-view 2D observations and weak cross-modal alignment. Here we address this problem from both data and model perspectives. First, we curate ConsIDVid, a large-scale object-centric dataset built with a scalable pipeline for high-quality, temporally aligned videos, and establish ConsIDVid-Bench, where we present a novel benchmarking and evaluation framework for multi-view consistency using metrics sensitive to subtle geometric and appearance deviations. We further propose ConsID-Gen, a view-assisted I2V generation framework that augments the first frame with unposed auxiliary views and fuses semantic and structural cues via a dual-stream visual-geometric encoder as well as a text-visual connector, yielding unified conditioning for a Diffusion Transformer backbone. Experiments across ConsIDVid-Bench demonstrate that ConsID-Gen consistently outperforms in multiple metrics, with the best overall performance surpassing leading video generation models like Wan2.1 and HunyuanVideo, delivering superior identity fidelity and temporal coherence under challenging real-world scenarios. We will release our model and dataset at https://myangwu.github.io/ConsID-Gen.

