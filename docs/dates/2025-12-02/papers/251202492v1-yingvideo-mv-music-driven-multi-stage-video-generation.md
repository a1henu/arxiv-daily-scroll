---
layout: default
title: YingVideo-MV: Music-Driven Multi-Stage Video Generation
---

# YingVideo-MV: Music-Driven Multi-Stage Video Generation
**arXiv**：[2512.02492v1](https://arxiv.org/abs/2512.02492) · [PDF](https://arxiv.org/pdf/2512.02492.pdf)  
**作者**：Jiahui Chen, Weida Wang, Runhua Shi, Huan Yang, Chaofan Ding, Zihao Chen  

**一句话要点**：提出YingVideo-MV框架以解决音乐驱动长视频生成中相机运动控制与连贯性问题

**关键词**：音乐驱动视频生成, 长视频生成, 相机运动控制, 扩散模型, 音频-视觉同步, 多阶段框架

## 3 点简述
- 核心问题：现有长视频生成方法缺乏显式相机运动控制，音乐表演视频生成未充分探索
- 方法要点：集成音频语义分析、可解释镜头规划模块、相机适配器模块和时间感知动态窗口策略
- 实验或效果：在音乐视频生成中实现高质量、连贯且音乐-动作-相机同步的结果

## 摘要（原文）

> While diffusion model for audio-driven avatar video generation have achieved notable process in synthesizing long sequences with natural audio-visual synchronization and identity consistency, the generation of music-performance videos with camera motions remains largely unexplored. We present YingVideo-MV, the first cascaded framework for music-driven long-video generation. Our approach integrates audio semantic analysis, an interpretable shot planning module (MV-Director), temporal-aware diffusion Transformer architectures, and long-sequence consistency modeling to enable automatic synthesis of high-quality music performance videos from audio signals. We construct a large-scale Music-in-the-Wild Dataset by collecting web data to support the achievement of diverse, high-quality results. Observing that existing long-video generation methods lack explicit camera motion control, we introduce a camera adapter module that embeds camera poses into latent noise. To enhance continulity between clips during long-sequence inference, we further propose a time-aware dynamic window range strategy that adaptively adjust denoising ranges based on audio embedding. Comprehensive benchmark tests demonstrate that YingVideo-MV achieves outstanding performance in generating coherent and expressive music videos, and enables precise music-motion-camera synchronization. More videos are available in our project page: https://giantailab.github.io/YingVideo-MV/ .

