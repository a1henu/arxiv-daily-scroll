---
layout: default
title: StreamWise: Serving Multi-Modal Generation in Real-Time at Scale
---

# StreamWise: Serving Multi-Modal Generation in Real-Time at Scale
**arXiv**：[2603.05800v1](https://arxiv.org/abs/2603.05800) · [PDF](https://arxiv.org/pdf/2603.05800.pdf)  
**作者**：Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  

**一句话要点**：提出StreamWise系统以解决实时多模态生成服务中的延迟与资源协调挑战

**关键词**：多模态生成, 实时服务, 资源调度, 异构硬件, 播客视频生成

## 3 点简述
- 核心问题：实时多模态生成服务面临高延迟、资源协调复杂和成本高昂的挑战
- 方法要点：设计自适应模块化系统，动态管理质量、并行性和资源调度，利用异构硬件
- 实验或效果：在A100 GPU上，低成本设置生成10分钟播客视频需1.4小时，实时流媒体启动延迟低于1秒

## 摘要（原文）

> Advances in multi-modal generative models are enabling new applications, from storytelling to automated media synthesis. Most current workloads generate simple outputs (e.g., image generation from a prompt) in batch mode, often requiring several seconds even for basic results. Serving real-time multi-modal workflows at scale is costly and complex, requiring efficient coordination of diverse models (each with unique resource needs) across language, audio, image, and video, all under strict latency and resource constraints.
>   We tackle these challenges through the lens of real-time podcast video generation, integrating LLMs, text-to-speech, and video-audio generation. To meet tight SLOs, we design an adaptive, modular serving system, StreamWise, that dynamically manages quality (e.g., resolution, sharpness), model/content parallelism, and resource-aware scheduling. We leverage heterogeneous hardware to maximize responsiveness and efficiency. For example, the system can lower video resolution and allocate more resources to early scenes.
>   We quantify the trade-offs between latency, cost, and quality. The cheapest setup generates a 10-minute podcast video on A100 GPUs in 1.4 hours (8.4x slower than the real-time) for less than \$25. StreamWise enables high-quality real-time streaming with a sub-second startup delay under $45.

