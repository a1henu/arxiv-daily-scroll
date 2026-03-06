---
layout: default
title: TAPFormer: Robust Arbitrary Point Tracking via Transient Asynchronous Fusion of Frames and Events
---

# TAPFormer: Robust Arbitrary Point Tracking via Transient Asynchronous Fusion of Frames and Events
**arXiv**：[2603.04989v1](https://arxiv.org/abs/2603.04989) · [PDF](https://arxiv.org/pdf/2603.04989.pdf)  
**作者**：Jiaxiong Liu, Zhen Tan, Jinpu Zhang, Yi Zhou, Hui Shen, Xieyuanli Chen, Dewen Hu  

**一句话要点**：提出TAPFormer框架，通过异步融合帧与事件实现鲁棒任意点跟踪

**关键词**：任意点跟踪, 帧事件融合, 异步融合, Transformer, 鲁棒跟踪, 多模态感知

## 3 点简述
- 核心问题：现有方法融合帧与事件时存在时间错位，导致模态失效时性能下降
- 方法要点：引入TAF机制建模帧间时间演化，CLWF模块自适应调整空间注意力
- 实验或效果：在真实数据集上平均像素误差提升28.2%，标准基准测试中表现最佳

## 摘要（原文）

> Tracking any point (TAP) is a fundamental yet challenging task in computer vision, requiring high precision and long-term motion reasoning. Recent attempts to combine RGB frames and event streams have shown promise, yet they typically rely on synchronous or non-adaptive fusion, leading to temporal misalignment and severe degradation when one modality fails. We introduce TAPFormer, a transformer-based framework that performs asynchronous temporal-consistent fusion of frames and events for robust and high-frequency arbitrary point tracking. Our key innovation is a Transient Asynchronous Fusion (TAF) mechanism, which explicitly models the temporal evolution between discrete frames through continuous event updates, bridging the gap between low-rate frames and high-rate events. In addition, a Cross-modal Locally Weighted Fusion (CLWF) module adaptively adjusts spatial attention according to modality reliability, yielding stable and discriminative features even under blur or low light. To evaluate our approach under realistic conditions, we construct a novel real-world frame-event TAP dataset under diverse illumination and motion conditions. Our method outperforms existing point trackers, achieving a 28.2% improvement in average pixel error within threshold. Moreover, on standard point tracking benchmarks, our tracker consistently achieves the best performance. Project website: tapformer.github.io

