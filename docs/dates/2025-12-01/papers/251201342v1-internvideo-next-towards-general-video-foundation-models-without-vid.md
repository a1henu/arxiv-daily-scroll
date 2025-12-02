---
layout: default
title: InternVideo-Next: Towards General Video Foundation Models without Video-Text Supervision
---

# InternVideo-Next: Towards General Video Foundation Models without Video-Text Supervision
**arXiv**：[2512.01342v1](https://arxiv.org/abs/2512.01342) · [PDF](https://arxiv.org/pdf/2512.01342.pdf)  
**作者**：Chenting Wang, Yuhan Zhu, Yicheng Xu, Jiange Yang, Ziang Yan, Yali Wang, Yi Wang, Limin Wang  

**一句话要点**：提出InternVideo-Next，通过编码器-预测器-解码器框架和两阶段预训练，解决视频基础模型中像素重建与语义冲突问题。

**关键词**：视频基础模型, 掩码视频建模, 编码器-预测器-解码器框架, 条件扩散解码器, 两阶段预训练, 世界知识学习

## 3 点简述
- 核心问题：视频文本监督依赖噪声字幕，忽略隐式世界知识；掩码视频建模存在像素重建与语义冲突及捷径学习问题。
- 方法要点：引入编码器-预测器-解码器框架，第一阶段使用条件扩散解码器增强语义，第二阶段预测冻结目标学习世界知识。
- 实验或效果：在公开无标签视频上训练，在多个基准测试中达到最先进性能，提供可扩展的视频表示学习路径。

## 摘要（原文）

> Large-scale video-text pretraining achieves strong performance but depends on noisy, synthetic captions with limited semantic coverage, often overlooking implicit world knowledge such as object motion, 3D geometry, and physical cues. In contrast, masked video modeling (MVM) directly exploits spatiotemporal structures but trails text-supervised methods on general tasks. We find this gap arises from overlooked architectural issues: pixel-level reconstruction struggles with convergence and its low-level requirement often conflicts with semantics, while latent prediction often encourages shortcut learning. To address these, we disentangle the traditional encoder-decoder design into an Encoder-Predictor-Decoder (EPD) framework, where the predictor acts as a latent world model, and propose InternVideo-Next, a two-stage pretraining scheme that builds a semantically consistent yet detail-preserving latent space for this world model. First, conventional linear decoder in pixel MVM enforces the predictor output latent to be linearly projected to, thus separable in pixel space, causing the conflict with semantic abstraction. Our Stage 1 proposes a conditional diffusion decoder and injects reliable image-level semantic priors to enhance semantics and convergence, thus bridging pixel-level fidelity with high-level semantic abstraction. Stage 2 further learns world knowledge by predicting frozen Stage 1 targets within this space, mitigating shortcut learning. Trained on public, unlabeled videos, InternVideo-Next achieves state-of-the-art results across benchmarks and provides a scalable path toward general video representation learning.

