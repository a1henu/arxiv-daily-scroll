---
layout: default
title: VideoAR: Autoregressive Video Generation via Next-Frame & Scale Prediction
---

# VideoAR: Autoregressive Video Generation via Next-Frame & Scale Prediction
**arXiv**：[2601.05966v1](https://arxiv.org/abs/2601.05966) · [PDF](https://arxiv.org/pdf/2601.05966.pdf)  
**作者**：Longbin Ji, Xiaoxiong Liu, Junyuan Shang, Shuohuan Wang, Yu Sun, Hua Wu, Haifeng Wang  

**一句话要点**：提出VideoAR框架，通过多尺度下一帧预测与自回归建模实现高效视频生成。

**关键词**：视频生成, 自回归模型, 多尺度预测, 时空一致性, 高效推理

## 3 点简述
- 核心问题：扩散和流匹配模型计算密集且难以扩展，视频生成效率低。
- 方法要点：结合帧内自回归建模与因果下一帧预测，使用3D多尺度分词器编码时空动态。
- 实验或效果：在UCF-101上FVD从99.5降至88.6，推理步骤减少超10倍，VBench得分81.74。

## 摘要（原文）

> Recent advances in video generation have been dominated by diffusion and flow-matching models, which produce high-quality results but remain computationally intensive and difficult to scale. In this work, we introduce VideoAR, the first large-scale Visual Autoregressive (VAR) framework for video generation that combines multi-scale next-frame prediction with autoregressive modeling. VideoAR disentangles spatial and temporal dependencies by integrating intra-frame VAR modeling with causal next-frame prediction, supported by a 3D multi-scale tokenizer that efficiently encodes spatio-temporal dynamics. To improve long-term consistency, we propose Multi-scale Temporal RoPE, Cross-Frame Error Correction, and Random Frame Mask, which collectively mitigate error propagation and stabilize temporal coherence. Our multi-stage pretraining pipeline progressively aligns spatial and temporal learning across increasing resolutions and durations. Empirically, VideoAR achieves new state-of-the-art results among autoregressive models, improving FVD on UCF-101 from 99.5 to 88.6 while reducing inference steps by over 10x, and reaching a VBench score of 81.74-competitive with diffusion-based models an order of magnitude larger. These results demonstrate that VideoAR narrows the performance gap between autoregressive and diffusion paradigms, offering a scalable, efficient, and temporally consistent foundation for future video generation research.

