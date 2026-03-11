---
layout: default
title: ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare
---

# ReCoSplat: Autoregressive Feed-Forward Gaussian Splatting Using Render-and-Compare
**arXiv**：[2603.09968v1](https://arxiv.org/abs/2603.09968) · [PDF](https://arxiv.org/pdf/2603.09968.pdf)  
**作者**：Freeman Cheng, Botao Ye, Xueting Li, Junqi You, Fangneng Zhan, Ming-Hsuan Yang  

**一句话要点**：提出ReCoSplat以解决在线新视角合成中姿态预测误差导致的分布不匹配问题

**关键词**：在线新视角合成, 高斯泼溅, 姿态预测, 序列重建, 缓存压缩

## 3 点简述
- 核心问题：在线新视角合成需从序列观测中重建场景，但训练时使用真实姿态与推理时使用预测姿态存在分布不匹配
- 方法要点：引入Render-and-Compare模块，通过渲染比较补偿姿态误差，并采用混合KV缓存压缩策略支持长序列
- 实验或效果：在分布内外基准测试中实现最先进性能，KV缓存大小减少超过90%

## 摘要（原文）

> Online novel view synthesis remains challenging, requiring robust scene reconstruction from sequential, often unposed, observations. We present ReCoSplat, an autoregressive feed-forward Gaussian Splatting model supporting posed or unposed inputs, with or without camera intrinsics. While assembling local Gaussians using camera poses scales better than canonical-space prediction, it creates a dilemma during training: using ground-truth poses ensures stability but causes a distribution mismatch when predicted poses are used at inference. To address this, we introduce a Render-and-Compare (ReCo) module. ReCo renders the current reconstruction from the predicted viewpoint and compares it with the incoming observation, providing a stable conditioning signal that compensates for pose errors. To support long sequences, we propose a hybrid KV cache compression strategy combining early-layer truncation with chunk-level selective retention, reducing the KV cache size by over 90% for 100+ frames. ReCoSplat achieves state-of-the-art performance across different input settings on both in- and out-of-distribution benchmarks. Code and pretrained models will be released. Our project page is at https://freemancheng.com/ReCoSplat .

