---
layout: default
title: Beyond Static Frames: Temporal Aggregate-and-Restore Vision Transformer for Human Pose Estimation
---

# Beyond Static Frames: Temporal Aggregate-and-Restore Vision Transformer for Human Pose Estimation
**arXiv**：[2603.05929v1](https://arxiv.org/abs/2603.05929) · [PDF](https://arxiv.org/pdf/2603.05929.pdf)  
**作者**：Hongwei Fang, Jiahang Cai, Xun Wang, Wenwu Yang  

**一句话要点**：提出TAR-ViTPose以解决视频中基于静态图像的姿态估计忽略时间一致性的问题

**关键词**：视频姿态估计, 时间聚合, Vision Transformer, 关节中心注意力, 全局恢复, 实时性能

## 3 点简述
- 现有ViT姿态估计器处理静态图像，忽略视频序列的时间连贯性，导致不稳定预测
- TAR-ViTPose通过关节中心时间聚合和全局恢复注意力，以即插即用方式聚合时间线索
- 在PoseTrack2017基准上提升2.3 mAP，优于现有视频方法并提高实时帧率

## 摘要（原文）

> Vision Transformers (ViTs) have recently achieved state-of-the-art performance in 2D human pose estimation due to their strong global modeling capability. However, existing ViT-based pose estimators are designed for static images and process each frame independently, thereby ignoring the temporal coherence that exists in video sequences. This limitation often results in unstable predictions, especially in challenging scenes involving motion blur, occlusion, or defocus. In this paper, we propose TAR-ViTPose, a novel Temporal Aggregate-and-Restore Vision Transformer tailored for video-based 2D human pose estimation. TAR-ViTPose enhances static ViT representations by aggregating temporal cues across frames in a plug-and-play manner, leading to more robust and accurate pose estimation. To effectively aggregate joint-specific features that are temporally aligned across frames, we introduce a joint-centric temporal aggregation (JTA) that assigns each joint a learnable query token to selectively attend to its corresponding regions from neighboring frames. Furthermore, we develop a global restoring attention (GRA) to restore the aggregated temporal features back into the token sequence of the current frame, enriching its pose representation while fully preserving global context for precise keypoint localization. Extensive experiments demonstrate that TAR-ViTPose substantially improves upon the single-frame baseline ViTPose, achieving a +2.3 mAP gain on the PoseTrack2017 benchmark. Moreover, our approach outperforms existing state-of-the-art video-based methods, while also achieving a noticeably higher runtime frame rate in real-world applications. Project page: https://github.com/zgspose/TARViTPose.

