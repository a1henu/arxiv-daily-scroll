---
layout: default
title: Beyond Boundary Frames: Audio-Visual Semantic Guidance for Context-Aware Video Interpolation
---

# Beyond Boundary Frames: Audio-Visual Semantic Guidance for Context-Aware Video Interpolation
**arXiv**：[2512.03590v1](https://arxiv.org/abs/2512.03590) · [PDF](https://arxiv.org/pdf/2512.03590.pdf)  
**作者**：Yuchen Deng, Xiuyang Wu, Hai-Tao Zheng, Jie Wang, Feidiao Yang, Yuxing Han  

**一句话要点**：提出BBF框架，通过音频-视觉语义引导解决视频帧插值中的快速复杂运动问题

**关键词**：视频帧插值, 多模态融合, 扩散模型, 音频-视觉同步, 上下文感知, 渐进训练

## 3 点简述
- 核心问题：传统方法难以处理快速、复杂和非线性运动，尤其在音频-视觉同步插值中效果不佳
- 方法要点：增强输入设计以处理多模态条件，采用解耦融合机制和渐进多阶段训练
- 实验或效果：在通用和音频-视觉同步插值任务上优于现有方法，建立统一框架

## 摘要（原文）

> Handling fast, complex, and highly non-linear motion patterns has long posed challenges for video frame interpolation. Although recent diffusion-based approaches improve upon traditional optical-flow-based methods, they still struggle to cover diverse application scenarios and often fail to produce sharp, temporally consistent frames in fine-grained motion tasks such as audio-visual synchronized interpolation. To address these limitations, we introduce BBF (Beyond Boundary Frames), a context-aware video frame interpolation framework, which could be guided by audio/visual semantics. First, we enhance the input design of the interpolation model so that it can flexibly handle multiple conditional modalities, including text, audio, images, and video. Second, we propose a decoupled multimodal fusion mechanism that sequentially injects different conditional signals into a DiT backbone. Finally, to maintain the generation abilities of the foundation model, we adopt a progressive multi-stage training paradigm, where the start-end frame difference embedding is used to dynamically adjust both the data sampling and the loss weighting. Extensive experimental results demonstrate that BBF outperforms specialized state-of-the-art methods on both generic interpolation and audio-visual synchronized interpolation tasks, establishing a unified framework for video frame interpolation under coordinated multi-channel conditioning.

