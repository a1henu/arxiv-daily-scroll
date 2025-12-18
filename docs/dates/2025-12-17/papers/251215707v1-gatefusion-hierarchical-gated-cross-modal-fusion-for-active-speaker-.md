---
layout: default
title: GateFusion: Hierarchical Gated Cross-Modal Fusion for Active Speaker Detection
---

# GateFusion: Hierarchical Gated Cross-Modal Fusion for Active Speaker Detection
**arXiv**：[2512.15707v1](https://arxiv.org/abs/2512.15707) · [PDF](https://arxiv.org/pdf/2512.15707.pdf)  
**作者**：Yu Wang, Juhyung Ha, Frangil M. Ramirez, Yuchen Wang, David J. Crandall  

**一句话要点**：提出GateFusion架构，通过分层门控跨模态融合解决主动说话人检测中细粒度交互不足的问题。

**关键词**：主动说话人检测, 跨模态融合, 分层门控, Transformer架构, 辅助损失, 视频音频分析

## 3 点简述
- 核心问题：主动说话人检测中，现有方法依赖晚期融合，难以捕捉细粒度跨模态交互，影响无约束场景性能。
- 方法要点：结合预训练单模态编码器与分层门控融合解码器，通过可学习门控在Transformer多层级自适应注入跨模态特征。
- 实验或效果：在多个基准测试中达到新最优结果，如Ego4D-ASD上mAP提升9.4%，并通过辅助损失增强泛化能力。

## 摘要（原文）

> Active Speaker Detection (ASD) aims to identify who is currently speaking in each frame of a video. Most state-of-the-art approaches rely on late fusion to combine visual and audio features, but late fusion often fails to capture fine-grained cross-modal interactions, which can be critical for robust performance in unconstrained scenarios. In this paper, we introduce GateFusion, a novel architecture that combines strong pretrained unimodal encoders with a Hierarchical Gated Fusion Decoder (HiGate). HiGate enables progressive, multi-depth fusion by adaptively injecting contextual features from one modality into the other at multiple layers of the Transformer backbone, guided by learnable, bimodally-conditioned gates. To further strengthen multimodal learning, we propose two auxiliary objectives: Masked Alignment Loss (MAL) to align unimodal outputs with multimodal predictions, and Over-Positive Penalty (OPP) to suppress spurious video-only activations. GateFusion establishes new state-of-the-art results on several challenging ASD benchmarks, achieving 77.8% mAP (+9.4%), 86.1% mAP (+2.9%), and 96.1% mAP (+0.5%) on Ego4D-ASD, UniTalk, and WASD benchmarks, respectively, and delivering competitive performance on AVA-ActiveSpeaker. Out-of-domain experiments demonstrate the generalization of our model, while comprehensive ablations show the complementary benefits of each component.

