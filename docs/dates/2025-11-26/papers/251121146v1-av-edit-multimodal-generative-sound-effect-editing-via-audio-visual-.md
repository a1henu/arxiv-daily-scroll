---
layout: default
title: AV-Edit: Multimodal Generative Sound Effect Editing via Audio-Visual Semantic Joint Control
---

# AV-Edit: Multimodal Generative Sound Effect Editing via Audio-Visual Semantic Joint Control
**arXiv**：[2511.21146v1](https://arxiv.org/abs/2511.21146) · [PDF](https://arxiv.org/pdf/2511.21146.pdf)  
**作者**：Xinyue Guo, Xiaoran Yang, Lipan Zhang, Jianxuan Yang, Zhao Wang, Jian Luan  

**一句话要点**：提出AV-Edit框架，通过音视频语义联合控制实现视频中音效的细粒度编辑

**关键词**：音效编辑, 多模态生成, 音视频语义对齐, 扩散变换器, 对比学习, 视频音频数据集

## 3 点简述
- 核心问题：现有音效编辑方法依赖低层信号处理或粗粒度文本提示，灵活性差且音频质量不佳
- 方法要点：使用对比音视频掩码自编码器预训练，结合多模态扩散变换器进行音效移除与生成
- 实验或效果：构建专用数据集评估，生成高质量音频，在音效编辑领域达到先进水平

## 摘要（原文）

> Sound effect editing-modifying audio by adding, removing, or replacing elements-remains constrained by existing approaches that rely solely on low-level signal processing or coarse text prompts, often resulting in limited flexibility and suboptimal audio quality. To address this, we propose AV-Edit, a generative sound effect editing framework that enables fine-grained editing of existing audio tracks in videos by jointly leveraging visual, audio, and text semantics. Specifically, the proposed method employs a specially designed contrastive audio-visual masking autoencoder (CAV-MAE-Edit) for multimodal pre-training, learning aligned cross-modal representations. These representations are then used to train an editorial Multimodal Diffusion Transformer (MM-DiT) capable of removing visually irrelevant sounds and generating missing audio elements consistent with video content through a correlation-based feature gating training strategy. Furthermore, we construct a dedicated video-based sound editing dataset as an evaluation benchmark. Experiments demonstrate that the proposed AV-Edit generates high-quality audio with precise modifications based on visual content, achieving state-of-the-art performance in the field of sound effect editing and exhibiting strong competitiveness in the domain of audio generation.

