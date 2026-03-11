---
layout: default
title: Exploring Modality-Aware Fusion and Decoupled Temporal Propagation for Multi-Modal Object Tracking
---

# Exploring Modality-Aware Fusion and Decoupled Temporal Propagation for Multi-Modal Object Tracking
**arXiv**：[2603.09287v1](https://arxiv.org/abs/2603.09287) · [PDF](https://arxiv.org/pdf/2603.09287.pdf)  
**作者**：Shilei Wang, Pujian Lai, Dong Gao, Jifeng Ning, Gong Cheng  

**一句话要点**：提出MDTrack框架，通过模态感知融合与解耦时序传播解决多模态目标跟踪中的融合与表示问题。

**关键词**：多模态目标跟踪, 模态感知融合, 解耦时序传播, 状态空间模型, 专家混合

## 3 点简述
- 核心问题：现有多模态跟踪器采用统一融合策略，忽略模态差异，且时序传播导致表示纠缠。
- 方法要点：引入模态感知融合，基于专家混合动态选择模态专家；设计解耦时序传播，用独立状态空间模型分别处理RGB和X模态流。
- 实验或效果：在五个多模态跟踪基准上，MDTrack S和MDTrack U均达到最先进性能。

## 摘要（原文）

> Most existing multimodal trackers adopt uniform fusion strategies, overlooking the inherent differences between modalities. Moreover, they propagate temporal information through mixed tokens, leading to entangled and less discriminative temporal representations. To address these limitations, we propose MDTrack, a novel framework for modality aware fusion and decoupled temporal propagation in multimodal object tracking. Specifically, for modality aware fusion, we allocate dedicated experts to each modality, including infrared, event, depth, and RGB, to process their respective representations. The gating mechanism within the Mixture of Experts dynamically selects the optimal experts based on the input features, enabling adaptive and modality specific fusion. For decoupled temporal propagation, we introduce two separate State Space Model structures to independently store and update the hidden states of the RGB and X modal streams, effectively capturing their distinct temporal information. To ensure synergy between the two temporal representations, we incorporate a set of cross attention modules between the input features of the two SSMs, facilitating implicit information exchange. The resulting temporally enriched features are then integrated into the backbone through another set of cross attention modules, enhancing MDTrack's ability to leverage temporal information. Extensive experiments demonstrate the effectiveness of our proposed method. Both MDTrack S and MDTrack U achieve state of the art performance across five multimodal tracking benchmarks.

