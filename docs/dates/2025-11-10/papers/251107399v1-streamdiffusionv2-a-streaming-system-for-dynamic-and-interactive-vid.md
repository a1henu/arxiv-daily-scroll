---
layout: default
title: StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation
---

# StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation
**arXiv**：[2511.07399v1](https://arxiv.org/abs/2511.07399) · [PDF](https://arxiv.org/pdf/2511.07399.pdf)  
**作者**：Tianrui Feng, Zhi Li, Shuo Yang, Haocheng Xi, Muyang Li, Xiuyu Li, Lvmin Zhang, Keting Yang, Kelly Peng, Song Han, Maneesh Agrawala, Kurt Keutzer, Akio Kodaira, Chenfeng Xu  

**一句话要点**：提出StreamDiffusionV2流式系统，实现动态交互视频生成的实时流媒体服务

**关键词**：视频扩散模型, 实时流媒体系统, 低延迟生成, 多GPU并行, 交互式视频生成

## 3 点简述
- 核心问题：在线流媒体需低延迟、低抖动，现有视频扩散模型难以满足实时SLO要求
- 方法要点：集成SLO感知批处理、块调度、滚动KV缓存和运动感知噪声控制等优化
- 实验或效果：在四H100 GPU上，14B模型达58.28 FPS，首帧渲染<0.5秒，支持灵活去噪步数

## 摘要（原文）

> Generative models are reshaping the live-streaming industry by redefining how
> content is created, styled, and delivered. Previous image-based streaming
> diffusion models have powered efficient and creative live streaming products
> but have hit limits on temporal consistency due to the foundation of
> image-based designs. Recent advances in video diffusion have markedly improved
> temporal consistency and sampling efficiency for offline generation. However,
> offline generation systems primarily optimize throughput by batching large
> workloads. In contrast, live online streaming operates under strict
> service-level objectives (SLOs): time-to-first-frame must be minimal, and every
> frame must meet a per-frame deadline with low jitter. Besides, scalable
> multi-GPU serving for real-time streams remains largely unresolved so far. To
> address this, we present StreamDiffusionV2, a training-free pipeline for
> interactive live streaming with video diffusion models. StreamDiffusionV2
> integrates an SLO-aware batching scheduler and a block scheduler, together with
> a sink-token--guided rolling KV cache, a motion-aware noise controller, and
> other system-level optimizations. Moreover, we introduce a scalable pipeline
> orchestration that parallelizes the diffusion process across denoising steps
> and network layers, achieving near-linear FPS scaling without violating latency
> guarantees. The system scales seamlessly across heterogeneous GPU environments
> and supports flexible denoising steps (e.g., 1--4), enabling both
> ultra-low-latency and higher-quality modes. Without TensorRT or quantization,
> StreamDiffusionV2 renders the first frame within 0.5s and attains 58.28 FPS
> with a 14B-parameter model and 64.52 FPS with a 1.3B-parameter model on four
> H100 GPUs, making state-of-the-art generative live streaming practical and
> accessible--from individual creators to enterprise-scale platforms.

