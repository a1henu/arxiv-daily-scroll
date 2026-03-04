---
layout: default
title: LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory
---

# LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory
**arXiv**：[2603.03269v1](https://arxiv.org/abs/2603.03269) · [PDF](https://arxiv.org/pdf/2603.03269.pdf)  
**作者**：Junyi Zhang, Charles Herrmann, Junhwa Hur, Chen Sun, Ming-Hsuan Yang, Forrester Cole, Trevor Darrell, Deqing Sun  

**一句话要点**：提出LoGeR架构以解决长视频密集三维重建中的跨块一致性问题

**关键词**：长视频三维重建, 混合记忆模块, 分块处理, 全局一致性, 前馈模型

## 3 点简述
- 核心问题：前馈几何基础模型在长视频重建中面临注意力复杂度高或循环设计内存有限的问题
- 方法要点：采用分块处理视频流，结合基于学习的混合记忆模块确保跨块对齐和全局一致性
- 实验或效果：在标准基准和新VBR数据集上显著优于现有方法，推理可泛化至数千帧

## 摘要（原文）

> Feedforward geometric foundation models achieve strong short-window reconstruction, yet scaling them to minutes-long videos is bottlenecked by quadratic attention complexity or limited effective memory in recurrent designs. We present LoGeR (Long-context Geometric Reconstruction), a novel architecture that scales dense 3D reconstruction to extremely long sequences without post-optimization. LoGeR processes video streams in chunks, leveraging strong bidirectional priors for high-fidelity intra-chunk reasoning. To manage the critical challenge of coherence across chunk boundaries, we propose a learning-based hybrid memory module. This dual-component system combines a parametric Test-Time Training (TTT) memory to anchor the global coordinate frame and prevent scale drift, alongside a non-parametric Sliding Window Attention (SWA) mechanism to preserve uncompressed context for high-precision adjacent alignment. Remarkably, this memory architecture enables LoGeR to be trained on sequences of 128 frames, and generalize up to thousands of frames during inference. Evaluated across standard benchmarks and a newly repurposed VBR dataset with sequences of up to 19k frames, LoGeR substantially outperforms prior state-of-the-art feedforward methods--reducing ATE on KITTI by over 74%--and achieves robust, globally consistent reconstruction over unprecedented horizons.

