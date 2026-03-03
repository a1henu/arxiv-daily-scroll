---
layout: default
title: SeaVIS: Sound-Enhanced Association for Online Audio-Visual Instance Segmentation
---

# SeaVIS: Sound-Enhanced Association for Online Audio-Visual Instance Segmentation
**arXiv**：[2603.01431v1](https://arxiv.org/abs/2603.01431) · [PDF](https://arxiv.org/pdf/2603.01431.pdf)  
**作者**：Yingjian Zhu, Ying Wang, Yuyang Hong, Ruohao Guo, Kun Ding, Xin Gu, Bin Fan, Shiming Xiang  

**一句话要点**：提出SeaVIS在线框架，通过声音增强关联解决音频-视觉实例分割中的实时流处理问题

**关键词**：音频-视觉实例分割, 在线处理, 因果注意力, 对比学习, 实时视频流

## 3 点简述
- 现有音频-视觉实例分割方法多为离线处理，无法关联连续视频片段，难以应用于实时场景
- 引入因果交叉注意力融合模块实现在线处理，并采用音频引导对比学习生成编码声音活动的实例原型
- 在AVISeg数据集上超越现有方法，保持实时推理速度，显著提升音频跟随能力

## 摘要（原文）

> Recently, an audio-visual instance segmentation (AVIS) task has been introduced, aiming to identify, segment and track individual sounding instances in videos. However, prevailing methods primarily adopt the offline paradigm, that cannot associate detected instances across consecutive clips, making them unsuitable for real-world scenarios that involve continuous video streams. To address this limitation, we introduce SeaVIS, the first online framework designed for audio-visual instance segmentation. SeaVIS leverages the Causal Cross Attention Fusion (CCAF) module to enable efficient online processing, which integrates visual features from the current frame with the entire audio history under strict causal constraints. A major challenge for conventional VIS methods is that appearance-based instance association fails to distinguish between an object's sounding and silent states, resulting in the incorrect segmentation of silent objects. To tackle this, we employ an Audio-Guided Contrastive Learning (AGCL) strategy to generate instance prototypes that encode not only visual appearance but also sounding activity. In this way, instances preserved during per-frame prediction that do not emit sound can be effectively suppressed during instance association process, thereby significantly enhancing the audio-following capability of SeaVIS. Extensive experiments conducted on the AVISeg dataset demonstrate that SeaVIS surpasses existing state-of-the-art models across multiple evaluation metrics while maintaining a competitive inference speed suitable for real-time processing.

