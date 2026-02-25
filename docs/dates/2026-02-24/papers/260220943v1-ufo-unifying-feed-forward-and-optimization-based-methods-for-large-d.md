---
layout: default
title: UFO: Unifying Feed-Forward and Optimization-based Methods for Large Driving Scene Modeling
---

# UFO: Unifying Feed-Forward and Optimization-based Methods for Large Driving Scene Modeling
**arXiv**：[2602.20943v1](https://arxiv.org/abs/2602.20943) · [PDF](https://arxiv.org/pdf/2602.20943.pdf)  
**作者**：Kaiyuan Tan, Yingying Shen, Mingfei Tu, Haohui Zhu, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun  

**一句话要点**：提出UFO统一前馈与优化方法，实现高效长程驾驶场景4D重建

**关键词**：4D场景重建, 长序列处理, 动态对象建模, 循环神经网络, 驾驶场景模拟

## 3 点简述
- 核心问题：前馈方法处理长序列时复杂度高且动态对象建模困难
- 方法要点：采用循环范式结合优化与前馈，基于可见性过滤选择场景令牌
- 实验或效果：在Waymo数据集上优于现有方法，0.5秒内重建16秒日志

## 摘要（原文）

> Dynamic driving scene reconstruction is critical for autonomous driving simulation and closed-loop learning. While recent feed-forward methods have shown promise for 3D reconstruction, they struggle with long-range driving sequences due to quadratic complexity in sequence length and challenges in modeling dynamic objects over extended durations. We propose UFO, a novel recurrent paradigm that combines the benefits of optimization-based and feed-forward methods for efficient long-range 4D reconstruction. Our approach maintains a 4D scene representation that is iteratively refined as new observations arrive, using a visibility-based filtering mechanism to select informative scene tokens and enable efficient processing of long sequences. For dynamic objects, we introduce an object pose-guided modeling approach that supports accurate long-range motion capture. Experiments on the Waymo Open Dataset demonstrate that our method significantly outperforms both per-scene optimization and existing feed-forward methods across various sequence lengths. Notably, our approach can reconstruct 16-second driving logs within 0.5 second while maintaining superior visual quality and geometric accuracy.

