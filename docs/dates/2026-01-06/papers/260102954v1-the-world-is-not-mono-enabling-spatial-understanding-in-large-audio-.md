---
layout: default
title: The World is Not Mono: Enabling Spatial Understanding in Large Audio-Language Models
---

# The World is Not Mono: Enabling Spatial Understanding in Large Audio-Language Models
**arXiv**：[2601.02954v1](https://arxiv.org/abs/2601.02954) · [PDF](https://arxiv.org/pdf/2601.02954.pdf)  
**作者**：Yuhuan You, Lai Wei, Xihong Wu, Tianshu Qu  

**一句话要点**：提出分层听觉场景分析框架，通过双耳音频数据集和混合特征投影器，增强大型音频语言模型的空间理解能力。

**关键词**：听觉场景分析, 空间音频理解, 双耳音频数据集, 混合特征投影器, 渐进训练, 大型音频语言模型

## 3 点简述
- 现有大型音频语言模型忽略空间维度，无法进行全面的声学场景分析。
- 构建大规模合成双耳音频数据集，设计混合特征投影器分离语义和空间表示，并通过渐进训练提升推理能力。
- 在综合基准测试中，模型展现出较强的空间理解能力，从单声道语义识别推进到空间智能。

## 摘要（原文）

> Existing large audio-language models perceive the world as "mono" -- a single stream of audio that ignores the critical spatial dimension ("where") required for universal acoustic scene analysis. To bridge this gap, we first introduce a hierarchical framework for Auditory Scene Analysis (ASA). Guided by this framework, we introduce a system that enables models like Qwen2-Audio to understand and reason about the complex acoustic world. Our framework achieves this through three core contributions: First, we build a large-scale, synthesized binaural audio dataset to provide the rich spatial cues. Second, we design a hybrid feature projector, which leverages parallel semantic and spatial encoders to extract decoupled representations. These distinct streams are integrated via a dense fusion mechanism, ensuring the model receives a holistic view of the acoustic scene. Finally, we employ a progressive training curriculum, advancing from supervised fine-tuning (SFT) to reinforcement learning via Group Relative Policy Optimization (GRPO), to explicitly evolve the model's capabilities towards reasoning. On our comprehensive benchmark, the model demonstrates comparatively strong capability for spatial understanding. By enabling this spatial perception, our work provides a clear pathway for leveraging the powerful reasoning abilities of large models towards holistic acoustic scene analysis, advancing from "mono" semantic recognition to spatial intelligence.

