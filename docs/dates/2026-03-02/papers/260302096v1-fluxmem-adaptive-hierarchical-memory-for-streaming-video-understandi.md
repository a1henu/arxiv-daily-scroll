---
layout: default
title: FluxMem: Adaptive Hierarchical Memory for Streaming Video Understanding
---

# FluxMem: Adaptive Hierarchical Memory for Streaming Video Understanding
**arXiv**：[2603.02096v1](https://arxiv.org/abs/2603.02096) · [PDF](https://arxiv.org/pdf/2603.02096.pdf)  
**作者**：Yiweng Xie, Bo He, Junke Wang, Xiangyu Zheng, Ziyi Ye, Zuxuan Wu  

**一句话要点**：提出FluxMem自适应分层内存框架，用于高效流式视频理解，无需训练。

**关键词**：流式视频理解, 自适应内存压缩, 分层设计, 训练免费框架, 实时性能优化

## 3 点简述
- 核心问题：流式视频理解中冗余视觉内存导致效率低下，需高效压缩。
- 方法要点：采用两阶段分层设计，包括时间相邻选择模块去除帧间冗余，空间域整合模块合并帧内重复区域。
- 实验或效果：在StreamingBench和OVO-Bench上达到新SOTA，显著降低延迟和GPU内存使用。

## 摘要（原文）

> This paper presents FluxMem, a training-free framework for efficient streaming video understanding. FluxMem adaptively compresses redundant visual memory through a hierarchical, two-stage design: (1) a Temporal Adjacency Selection (TAS) module removes redundant visual tokens across adjacent frames, and (2) a Spatial Domain Consolidation (SDC) module further merges spatially repetitive regions within each frame into compact representations. To adapt effectively to dynamic scenes, we introduce a self-adaptive token compression mechanism in both TAS and SDC, which automatically determines the compression rate based on intrinsic scene statistics rather than manual tuning. Extensive experiments demonstrate that FluxMem achieves new state-of-the-art results on existing online video benchmarks, reaching 76.4 on StreamingBench and 67.2 on OVO-Bench under real-time settings, while reducing latency by 69.9% and peak GPU memory by 34.5% on OVO-Bench. Furthermore, it maintains strong offline performance, achieving 73.1 on MLVU while using 65% fewer visual tokens.

