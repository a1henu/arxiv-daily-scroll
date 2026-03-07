---
layout: default
title: DeformTrace: A Deformable State Space Model with Relay Tokens for Temporal Forgery Localization
---

# DeformTrace: A Deformable State Space Model with Relay Tokens for Temporal Forgery Localization
**arXiv**：[2603.04882v1](https://arxiv.org/abs/2603.04882) · [PDF](https://arxiv.org/pdf/2603.04882.pdf)  
**作者**：Xiaodong Zhu, Suting Wang, Yuanming Zheng, Junqi Yang, Yangxu Liao, Yuhong Yang, Weiping Tu, Zhongyuan Wang  

**一句话要点**：提出DeformTrace，一种结合可变形状态空间模型与中继令牌的混合架构，用于视频音频时序伪造定位。

**关键词**：时序伪造定位, 状态空间模型, 可变形机制, 中继令牌, 混合架构, 视频音频安全

## 3 点简述
- 核心问题：时序伪造定位面临模糊边界、稀疏伪造和长程建模限制。
- 方法要点：引入可变形自状态空间模型和可变形交叉状态空间模型，增强精确定位和稀疏伪造敏感性。
- 实验或效果：在减少参数和加速推理的同时，实现最先进性能与强鲁棒性。

## 摘要（原文）

> Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments in video and audio, offering strong interpretability for security and forensics. While recent State Space Models (SSMs) show promise in precise temporal reasoning, their use in TFL is hindered by ambiguous boundaries, sparse forgeries, and limited long-range modeling. We propose DeformTrace, which enhances SSMs with deformable dynamics and relay mechanisms to address these challenges. Specifically, Deformable Self-SSM (DS-SSM) introduces dynamic receptive fields into SSMs for precise temporal localization. To further enhance its capacity for temporal reasoning and mitigate long-range decay, a Relay Token Mechanism is integrated into DS-SSM. Besides, Deformable Cross-SSM (DC-SSM) partitions the global state space into query-specific subspaces, reducing non-forgery information accumulation and boosting sensitivity to sparse forgeries. These components are integrated into a hybrid architecture that combines the global modeling of Transformers with the efficiency of SSMs. Extensive experiments show that DeformTrace achieves state-of-the-art performance with fewer parameters, faster inference, and stronger robustness.

