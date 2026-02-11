---
layout: default
title: Time2General: Learning Spatiotemporal Invariant Representations for Domain-Generalization Video Semantic Segmentation
---

# Time2General: Learning Spatiotemporal Invariant Representations for Domain-Generalization Video Semantic Segmentation
**arXiv**：[2602.09648v1](https://arxiv.org/abs/2602.09648) · [PDF](https://arxiv.org/pdf/2602.09648.pdf)  
**作者**：Siyu Chen, Ting Han, Haoling Huang, Chaolei Wang, Chengzheng Fu, Duxin Zhu, Guorong Cai, Jinhe Su  

**一句话要点**：提出Time2General框架，基于稳定性查询解决领域泛化视频语义分割中的时空一致性问题。

**关键词**：领域泛化视频语义分割, 时空一致性, 驾驶场景, 时序采样偏移, 稳定性查询

## 3 点简述
- 核心问题：领域偏移和时序采样偏移导致视频语义分割预测闪烁，影响跨域部署的稳定性。
- 方法要点：引入时空记忆解码器聚合多帧上下文，并使用掩码时序一致性损失正则化不同步幅的预测差异。
- 实验或效果：在多个驾驶基准测试中显著提升跨域准确性和时序稳定性，运行速度达18 FPS。

## 摘要（原文）

> Domain Generalized Video Semantic Segmentation (DGVSS) is trained on a single labeled driving domain and is directly deployed on unseen domains without target labels and test-time adaptation while maintaining temporally consistent predictions over video streams. In practice, both domain shift and temporal-sampling shift break correspondence-based propagation and fixed-stride temporal aggregation, causing severe frame-to-frame flicker even in label-stable regions. We propose Time2General, a DGVSS framework built on Stability Queries. Time2General introduces a Spatio-Temporal Memory Decoder that aggregates multi-frame context into a clip-level spatio-temporal memory and decodes temporally consistent per-frame masks without explicit correspondence propagation. To further suppress flicker and improve robustness to varying sampling rates, the Masked Temporal Consistency Loss is proposed to regularize temporal prediction discrepancies across different strides, and randomize training strides to expose the model to diverse temporal gaps. Extensive experiments on multiple driving benchmarks show that Time2General achieves a substantial improvement in cross-domain accuracy and temporal stability over prior DGSS and VSS baselines while running at up to 18 FPS. Code will be released after the review process.

