---
layout: default
title: LongStream: Long-Sequence Streaming Autoregressive Visual Geometry
---

# LongStream: Long-Sequence Streaming Autoregressive Visual Geometry
**arXiv**：[2602.13172v1](https://arxiv.org/abs/2602.13172) · [PDF](https://arxiv.org/pdf/2602.13172.pdf)  
**作者**：Chong Cheng, Xianda Chen, Tao Xie, Wei Yin, Weiqiang Ren, Qian Zhang, Xiaoyuang Guo, Hao Wang  

**一句话要点**：提出LongStream以解决长序列流式三维重建中的姿态锚定和注意力衰减问题

**关键词**：长序列三维重建, 流式视觉几何, 自回归模型, 姿态估计, Transformer缓存优化, 度量尺度重建

## 3 点简述
- 核心问题：现有自回归模型在长序列处理中因首帧锚定导致注意力衰减、尺度漂移和外推错误
- 方法要点：采用关键帧相对姿态预测、正交尺度学习和缓存一致性训练，解耦几何与尺度，抑制漂移
- 实验或效果：在千米级序列上实现稳定度量尺度重建，达到18 FPS，性能领先

## 摘要（原文）

> Long-sequence streaming 3D reconstruction remains a significant open challenge. Existing autoregressive models often fail when processing long sequences. They typically anchor poses to the first frame, which leads to attention decay, scale drift, and extrapolation errors. We introduce LongStream, a novel gauge-decoupled streaming visual geometry model for metric-scale scene reconstruction across thousands of frames. Our approach is threefold. First, we discard the first-frame anchor and predict keyframe-relative poses. This reformulates long-range extrapolation into a constant-difficulty local task. Second, we introduce orthogonal scale learning. This method fully disentangles geometry from scale estimation to suppress drift. Finally, we solve Transformer cache issues such as attention-sink reliance and long-term KV-cache contamination. We propose cache-consistent training combined with periodic cache refresh. This approach suppresses attention degradation over ultra-long sequences and reduces the gap between training and inference. Experiments show LongStream achieves state-of-the-art performance. It delivers stable, metric-scale reconstruction over kilometer-scale sequences at 18 FPS. Project Page: https://3dagentworld.github.io/longstream/

