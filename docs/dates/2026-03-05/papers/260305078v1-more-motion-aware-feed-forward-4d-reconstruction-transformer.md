---
layout: default
title: MoRe: Motion-aware Feed-forward 4D Reconstruction Transformer
---

# MoRe: Motion-aware Feed-forward 4D Reconstruction Transformer
**arXiv**：[2603.05078v1](https://arxiv.org/abs/2603.05078) · [PDF](https://arxiv.org/pdf/2603.05078.pdf)  
**作者**：Juntong Fang, Zequn Chen, Weiqi Zhang, Donglin Di, Xuancheng Zhang, Chengmin Yang, Yu-Shen Liu  

**一句话要点**：提出MoRe前馈网络，从单目视频高效重建动态4D场景

**关键词**：4D场景重建, 动态物体分离, 注意力机制, 单目视频处理, 前馈网络

## 3 点简述
- 核心问题：动态物体运动干扰相机位姿估计，现有优化方法计算成本高
- 方法要点：基于静态重建骨干，采用注意力强制策略分离动态与静态，分组因果注意力捕获时序依赖
- 实验效果：在多个基准测试中实现高质量动态重建，效率优异

## 摘要（原文）

> Reconstructing dynamic 4D scenes remains challenging due to the presence of moving objects that corrupt camera pose estimation. Existing optimization methods alleviate this issue with additional supervision, but they are mostly computationally expensive and impractical in real-time applications. To address these limitations, we propose MoRe, a feedforward 4D reconstruction network that efficiently recovers dynamic 3D scenes from monocular videos. Built upon a strong static reconstruction backbone, MoRe employs an attention-forcing strategy to disentangle dynamic motion from static structure. To further enhance robustness, we fine-tune the model on large-scale, diverse datasets encompassing both dynamic and static scenes. Moreover, our grouped causal attention captures temporal dependencies and adapts to varying token lengths across frames, ensuring temporally coherent geometry reconstruction. Extensive experiments on multiple benchmarks demonstrate that MoRe achieves high-quality dynamic reconstructions with exceptional efficiency.

