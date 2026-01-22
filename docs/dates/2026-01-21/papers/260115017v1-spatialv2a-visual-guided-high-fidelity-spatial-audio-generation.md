---
layout: default
title: SpatialV2A: Visual-Guided High-fidelity Spatial Audio Generation
---

# SpatialV2A: Visual-Guided High-fidelity Spatial Audio Generation
**arXiv**：[2601.15017v1](https://arxiv.org/abs/2601.15017) · [PDF](https://arxiv.org/pdf/2601.15017.pdf)  
**作者**：Yanan Wang, Linjie Ren, Zihao Li, Junyi Wang, Tian Gan  

**一句话要点**：提出视觉引导的空间音频生成框架以解决视频到音频生成中空间感知不足的问题

**关键词**：视频到音频生成, 空间音频生成, 双耳音频数据集, 视觉引导音频空间化, 沉浸式听觉体验

## 3 点简述
- 核心问题：现有视频到音频生成模型依赖单声道音频数据集，缺乏空间信息，导致合成音频空间感知和沉浸感差。
- 方法要点：构建首个大规模视频-双耳音频数据集BinauralVGGSound，并设计端到端框架，通过视觉引导音频空间化模块显式建模空间特征。
- 实验或效果：实验表明，该方法在空间保真度上显著优于现有模型，提供更沉浸的听觉体验，同时保持语义和时间一致性。

## 摘要（原文）

> While video-to-audio generation has achieved remarkable progress in semantic and temporal alignment, most existing studies focus solely on these aspects, paying limited attention to the spatial perception and immersive quality of the synthesized audio. This limitation stems largely from current models' reliance on mono audio datasets, which lack the binaural spatial information needed to learn visual-to-spatial audio mappings. To address this gap, we introduce two key contributions: we construct BinauralVGGSound, the first large-scale video-binaural audio dataset designed to support spatially aware video-to-audio generation; and we propose a end-to-end spatial audio generation framework guided by visual cues, which explicitly models spatial features. Our framework incorporates a visual-guided audio spatialization module that ensures the generated audio exhibits realistic spatial attributes and layered spatial depth while maintaining semantic and temporal alignment. Experiments show that our approach substantially outperforms state-of-the-art models in spatial fidelity and delivers a more immersive auditory experience, without sacrificing temporal or semantic consistency. All datasets, code, and model checkpoints will be publicly released to facilitate future research.

