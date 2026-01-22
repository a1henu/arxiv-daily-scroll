---
layout: default
title: POTR: Post-Training 3DGS Compression
---

# POTR: Post-Training 3DGS Compression
**arXiv**：[2601.14821v1](https://arxiv.org/abs/2601.14821) · [PDF](https://arxiv.org/pdf/2601.14821.pdf)  
**作者**：Bert Ramlot, Martijn Courteaux, Peter Lambert, Glenn Van Wallendael  

**一句话要点**：提出POTR以解决3D高斯泼溅的存储与推理效率问题

**关键词**：3D高斯泼溅压缩, 后训练剪枝, 光照系数优化, 实时新视角合成, 存储效率提升

## 3 点简述
- 3D高斯泼溅在实时新视角合成中存储需求高，POTR通过后训练压缩降低存储并加速推理。
- 引入新型剪枝方法，利用改进的3DGS光栅化器同时计算每个泼溅的移除效果，减少泼溅数量2-4倍。
- 提出重新计算光照系数的方法，增加稀疏性至97%，并通过微调方案进一步提升性能。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently emerged as a promising contender to Neural Radiance Fields (NeRF) in 3D scene reconstruction and real-time novel view synthesis. 3DGS outperforms NeRF in training and inference speed but has substantially higher storage requirements. To remedy this downside, we propose POTR, a post-training 3DGS codec built on two novel techniques. First, POTR introduces a novel pruning approach that uses a modified 3DGS rasterizer to efficiently calculate every splat's individual removal effect simultaneously. This technique results in 2-4x fewer splats than other post-training pruning techniques and as a result also significantly accelerates inference with experiments demonstrating 1.5-2x faster inference than other compressed models. Second, we propose a novel method to recompute lighting coefficients, significantly reducing their entropy without using any form of training. Our fast and highly parallel approach especially increases AC lighting coefficient sparsity, with experiments demonstrating increases from 70% to 97%, with minimal loss in quality. Finally, we extend POTR with a simple fine-tuning scheme to further enhance pruning, inference, and rate-distortion performance. Experiments demonstrate that POTR, even without fine-tuning, consistently outperforms all other post-training compression techniques in both rate-distortion performance and inference speed.

