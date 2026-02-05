---
layout: default
title: Depth-Guided Metric-Aware Temporal Consistency for Monocular Video Human Mesh Recovery
---

# Depth-Guided Metric-Aware Temporal Consistency for Monocular Video Human Mesh Recovery
**arXiv**：[2602.04257v1](https://arxiv.org/abs/2602.04257) · [PDF](https://arxiv.org/pdf/2602.04257.pdf)  
**作者**：Jiaxin Cen, Xudong Mao, Guanghui Yue, Wei Zhou, Ruomei Wang, Fan Zhou, Baoquan Zhao  

**一句话要点**：提出深度引导的度量感知时序一致性框架，以解决单目视频人体网格恢复中的深度模糊和尺度漂移问题。

**关键词**：单目视频人体网格恢复, 深度引导, 度量感知时序一致性, 多尺度融合, 运动-深度对齐, 遮挡鲁棒性

## 3 点简述
- 核心问题：单目视频人体网格恢复面临深度模糊、尺度不确定性和时序不稳定性，导致深度排序错误和遮挡引起的抖动。
- 方法要点：通过深度引导多尺度融合、深度引导度量感知姿态形状估计器和运动-深度对齐细化模块，协同整合几何先验与RGB特征，实现尺度一致性和时序连贯性。
- 实验或效果：在三个挑战性基准测试中取得优越结果，显著提升对严重遮挡的鲁棒性和空间准确性，同时保持计算效率。

## 摘要（原文）

> Monocular video human mesh recovery faces fundamental challenges in maintaining metric consistency and temporal stability due to inherent depth ambiguities and scale uncertainties. While existing methods rely primarily on RGB features and temporal smoothing, they struggle with depth ordering, scale drift, and occlusion-induced instabilities. We propose a comprehensive depth-guided framework that achieves metric-aware temporal consistency through three synergistic components: A Depth-Guided Multi-Scale Fusion module that adaptively integrates geometric priors with RGB features via confidence-aware gating; A Depth-guided Metric-Aware Pose and Shape (D-MAPS) estimator that leverages depth-calibrated bone statistics for scale-consistent initialization; A Motion-Depth Aligned Refinement (MoDAR) module that enforces temporal coherence through cross-modal attention between motion dynamics and geometric cues. Our method achieves superior results on three challenging benchmarks, demonstrating significant improvements in robustness against heavy occlusion and spatial accuracy while maintaining computational efficiency.

