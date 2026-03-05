---
layout: default
title: Helios: Real Real-Time Long Video Generation Model
---

# Helios: Real Real-Time Long Video Generation Model
**arXiv**：[2603.04379v1](https://arxiv.org/abs/2603.04379) · [PDF](https://arxiv.org/pdf/2603.04379.pdf)  
**作者**：Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  

**一句话要点**：提出Helios模型，实现实时长视频生成，无需抗漂移启发式或标准加速技术。

**关键词**：长视频生成, 实时生成, 自回归扩散模型, 漂移缓解, 训练优化, 基础设施加速

## 3 点简述
- 核心问题：长视频生成中的漂移问题，现有方法依赖启发式技术如自强制或关键帧采样。
- 方法要点：通过训练策略模拟漂移并压缩历史上下文，减少采样步骤，提升效率。
- 实验或效果：在短和长视频生成中优于先前方法，支持T2V、I2V、V2V任务，运行速度达19.5 FPS。

## 摘要（原文）

> We introduce Helios, the first 14B video generation model that runs at 19.5 FPS on a single NVIDIA H100 GPU and supports minute-scale generation while matching the quality of a strong baseline. We make breakthroughs along three key dimensions: (1) robustness to long-video drifting without commonly used anti-drifting heuristics such as self-forcing, error-banks, or keyframe sampling; (2) real-time generation without standard acceleration techniques such as KV-cache, sparse/linear attention, or quantization; and (3) training without parallelism or sharding frameworks, enabling image-diffusion-scale batch sizes while fitting up to four 14B models within 80 GB of GPU memory. Specifically, Helios is a 14B autoregressive diffusion model with a unified input representation that natively supports T2V, I2V, and V2V tasks. To mitigate drifting in long-video generation, we characterize typical failure modes and propose simple yet effective training strategies that explicitly simulate drifting during training, while eliminating repetitive motion at its source. For efficiency, we heavily compress the historical and noisy context and reduce the number of sampling steps, yielding computational costs comparable to -- or lower than -- those of 1.3B video generative models. Moreover, we introduce infrastructure-level optimizations that accelerate both inference and training while reducing memory consumption. Extensive experiments demonstrate that Helios consistently outperforms prior methods on both short- and long-video generation. We plan to release the code, base model, and distilled model to support further development by the community.

