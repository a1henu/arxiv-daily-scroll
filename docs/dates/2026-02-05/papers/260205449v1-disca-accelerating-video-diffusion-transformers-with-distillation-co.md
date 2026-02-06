---
layout: default
title: DisCa: Accelerating Video Diffusion Transformers with Distillation-Compatible Learnable Feature Caching
---

# DisCa: Accelerating Video Diffusion Transformers with Distillation-Compatible Learnable Feature Caching
**arXiv**：[2602.05449v1](https://arxiv.org/abs/2602.05449) · [PDF](https://arxiv.org/pdf/2602.05449.pdf)  
**作者**：Chang Zou, Changlin Li, Yang Li, Patrol Li, Jianbing Wu, Xiao He, Songtao Liu, Zhao Zhong, Kailin Huang, Linfeng Zhang  

**一句话要点**：提出蒸馏兼容的可学习特征缓存机制，以加速视频扩散变换器并保持生成质量。

**关键词**：视频扩散模型, 特征缓存, 模型蒸馏, 加速方法, 可学习预测器, 受限平均流

## 3 点简述
- 核心问题：视频扩散模型计算负担重，现有特征缓存方法在压缩时面临语义和细节丢失，步数蒸馏在视频生成中质量下降严重。
- 方法要点：引入可学习的神经预测器替代传统启发式方法，更准确捕捉特征演化；提出保守的受限平均流方法，实现稳定无损的蒸馏。
- 实验或效果：在保持生成质量的同时，将加速比提升至11.8倍，并通过大量实验验证了方法的有效性。

## 摘要（原文）

> While diffusion models have achieved great success in the field of video generation, this progress is accompanied by a rapidly escalating computational burden. Among the existing acceleration methods, Feature Caching is popular due to its training-free property and considerable speedup performance, but it inevitably faces semantic and detail drop with further compression. Another widely adopted method, training-aware step-distillation, though successful in image generation, also faces drastic degradation in video generation with a few steps. Furthermore, the quality loss becomes more severe when simply applying training-free feature caching to the step-distilled models, due to the sparser sampling steps. This paper novelly introduces a distillation-compatible learnable feature caching mechanism for the first time. We employ a lightweight learnable neural predictor instead of traditional training-free heuristics for diffusion models, enabling a more accurate capture of the high-dimensional feature evolution process. Furthermore, we explore the challenges of highly compressed distillation on large-scale video models and propose a conservative Restricted MeanFlow approach to achieve more stable and lossless distillation. By undertaking these initiatives, we further push the acceleration boundaries to $11.8\times$ while preserving generation quality. Extensive experiments demonstrate the effectiveness of our method. The code is in the supplementary materials and will be publicly available.

