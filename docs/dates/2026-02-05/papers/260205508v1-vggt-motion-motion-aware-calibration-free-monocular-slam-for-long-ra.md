---
layout: default
title: VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency
---

# VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency
**arXiv**：[2602.05508v1](https://arxiv.org/abs/2602.05508) · [PDF](https://arxiv.org/pdf/2602.05508.pdf)  
**作者**：Zhuang Xiong, Chen Zhang, Qingshan Xu, Wenbing Tao  

**一句话要点**：提出VGGT-Motion以解决长序列单目SLAM中的尺度漂移问题

**关键词**：单目SLAM, 尺度漂移, 运动感知分割, 直接配准, 长序列一致性, 校准无关视觉定位

## 3 点简述
- 核心问题：校准无关单目SLAM在长序列中尺度漂移严重，运动无关分割破坏上下文连贯性。
- 方法要点：设计运动感知子图构建和锚点驱动直接Sim(3)配准，实现高效全局一致性。
- 实验或效果：在零样本长距离校准无关单目SLAM中达到先进性能，提升轨迹精度和效率。

## 摘要（原文）

> Despite recent progress in calibration-free monocular SLAM via 3D vision foundation models, scale drift remains severe on long sequences. Motion-agnostic partitioning breaks contextual coherence and causes zero-motion drift, while conventional geometric alignment is computationally expensive. To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories. Specifically, we first propose a motion-aware submap construction mechanism that uses optical flow to guide adaptive partitioning, prune static redundancy, and encapsulate turns for stable local geometry. We then design an anchor-driven direct Sim(3) registration strategy. By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching. Finally, a lightweight submap-level pose graph optimization enforces global consistency with linear complexity, enabling scalable long-range operation. Experiments show that VGGT-Motion markedly improves trajectory accuracy and efficiency, achieving state-of-the-art performance in zero-shot, long-range calibration-free monocular SLAM.

