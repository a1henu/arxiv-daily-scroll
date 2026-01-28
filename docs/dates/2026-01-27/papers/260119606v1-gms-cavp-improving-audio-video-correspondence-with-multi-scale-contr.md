---
layout: default
title: GMS-CAVP: Improving Audio-Video Correspondence with Multi-Scale Contrastive and Generative Pretraining
---

# GMS-CAVP: Improving Audio-Video Correspondence with Multi-Scale Contrastive and Generative Pretraining
**arXiv**：[2601.19606v1](https://arxiv.org/abs/2601.19606) · [PDF](https://arxiv.org/pdf/2601.19606.pdf)  
**作者**：Shentong Mo, Zehua Chen, Jun Zhu  

**一句话要点**：提出GMS-CAVP框架，通过多尺度对比与生成预训练提升音视频对应建模，用于跨模态检索与生成任务。

**关键词**：音视频对应建模, 多尺度对比学习, 扩散生成模型, 跨模态检索, 音视频生成

## 3 点简述
- 核心问题：现有方法对音视频信号的多尺度密集特性建模不足，影响对应关系捕捉。
- 方法要点：结合多尺度对比学习和扩散生成目标，增强语义与时间对应及模态转换能力。
- 实验或效果：在VGGSound等数据集上，GMS-CAVP在生成和检索任务中优于先前方法。

## 摘要（原文）

> Recent advances in video-audio (V-A) understanding and generation have increasingly relied on joint V-A embeddings, which serve as the foundation for tasks such as cross-modal retrieval and generation. While prior methods like CAVP effectively model semantic and temporal correspondences between modalities using contrastive objectives, their performance remains suboptimal. A key limitation is the insufficient modeling of the dense, multi-scale nature of both video and audio signals, correspondences often span fine- to coarse-grained spatial-temporal structures, which are underutilized in existing frameworks. To this end, we propose GMS-CAVP, a novel framework that combines Multi-Scale Video-Audio Alignment and Multi-Scale Spatial-Temporal Diffusion-based pretraining objectives to enhance V-A correspondence modeling. First, GMS-CAVP introduces a multi-scale contrastive learning strategy that captures semantic and temporal relations across varying granularities. Second, we go beyond traditional contrastive learning by incorporating a diffusion-based generative objective, enabling modality translation and synthesis between video and audio. This unified discriminative-generative formulation facilitates deeper cross-modal understanding and paves the way for high-fidelity generation. Extensive experiments on VGGSound, AudioSet, and Panda70M demonstrate that GMS-CAVP outperforms previous methods in generation and retrieval.

