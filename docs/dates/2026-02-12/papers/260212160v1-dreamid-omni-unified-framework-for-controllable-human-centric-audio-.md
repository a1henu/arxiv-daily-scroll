---
layout: default
title: DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation
---

# DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation
**arXiv**：[2602.12160v1](https://arxiv.org/abs/2602.12160) · [PDF](https://arxiv.org/pdf/2602.12160.pdf)  
**作者**：Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  

**一句话要点**：提出DreamID-Omni统一框架，解决人中心音视频生成中多任务隔离与身份音色控制难题。

**关键词**：人中心音视频生成, 条件扩散模型, 身份音色解耦, 多任务学习, 对称条件注入, 音频驱动动画

## 3 点简述
- 核心问题：现有方法将人中心音视频生成任务孤立处理，且难以在多人场景中精确控制身份与音色。
- 方法要点：设计对称条件扩散Transformer，采用双级解耦策略和渐进训练方案，实现统一控制。
- 实验或效果：在视频、音频及音视频一致性上达到SOTA，超越领先商业模型，将开源代码。

## 摘要（原文）

> Recent advancements in foundation models have revolutionized joint audio-video generation. However, existing approaches typically treat human-centric tasks including reference-based audio-video generation (R2AV), video editing (RV2AV) and audio-driven video animation (RA2V) as isolated objectives. Furthermore, achieving precise, disentangled control over multiple character identities and voice timbres within a single framework remains an open challenge. In this paper, we propose DreamID-Omni, a unified framework for controllable human-centric audio-video generation. Specifically, we design a Symmetric Conditional Diffusion Transformer that integrates heterogeneous conditioning signals via a symmetric conditional injection scheme. To resolve the pervasive identity-timbre binding failures and speaker confusion in multi-person scenarios, we introduce a Dual-Level Disentanglement strategy: Synchronized RoPE at the signal level to ensure rigid attention-space binding, and Structured Captions at the semantic level to establish explicit attribute-subject mappings. Furthermore, we devise a Multi-Task Progressive Training scheme that leverages weakly-constrained generative priors to regularize strongly-constrained tasks, preventing overfitting and harmonizing disparate objectives. Extensive experiments demonstrate that DreamID-Omni achieves comprehensive state-of-the-art performance across video, audio, and audio-visual consistency, even outperforming leading proprietary commercial models. We will release our code to bridge the gap between academic research and commercial-grade applications.

