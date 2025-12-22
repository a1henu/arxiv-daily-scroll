---
layout: default
title: Enabling Disaggregated Multi-Stage MLLM Inference via GPU-Internal Scheduling and Resource Sharing
---

# Enabling Disaggregated Multi-Stage MLLM Inference via GPU-Internal Scheduling and Resource Sharing
**arXiv**：[2512.17574v1](https://arxiv.org/abs/2512.17574) · [PDF](https://arxiv.org/pdf/2512.17574.pdf)  
**作者**：Lingxiao Zhao, Haoran Zhou, Yuezhi Che, Dazhao Cheng  

**一句话要点**：提出FlashCodec与UnifiedServe以优化多模态大语言模型推理的端到端系统性能

**关键词**：多模态大语言模型, 视频解码加速, GPU资源调度, 端到端优化, 系统吞吐量提升

## 3 点简述
- 核心问题：多模态预处理（如视频解码）延迟高，视觉编码与LLM推理异构导致资源利用不足和系统瓶颈
- 方法要点：FlashCodec通过多GPU协作解码加速预处理，UnifiedServe逻辑解耦物理共享GPU资源以消除阶段阻塞
- 实验或效果：相比现有系统，实现高达4.4倍吞吐量提升，支持3.0倍更多请求或1.5倍更严格SLO

## 摘要（原文）

> Multimodal large language models (MLLMs) extend LLMs with visual understanding through a three-stage pipeline: multimodal preprocessing, vision encoding, and LLM inference. While these stages enhance capability, they introduce significant system bottlenecks. First, multimodal preprocessing-especially video decoding-often dominates Time-to-First-Token (TTFT). Most systems rely on CPU-based decoding, which severely limits throughput, while existing GPU-based approaches prioritize throughput-oriented parallelism and fail to meet the latency-sensitive requirements of MLLM inference. Second, the vision encoder is a standalone, compute-intensive stage that produces visual embeddings and cannot be co-batched with LLM prefill or decoding. This heterogeneity forces inter-stage blocking and increases token-generation latency. Even when deployed on separate GPUs, these stages underutilize available compute and memory resources, reducing overall utilization and constraining system throughput.
>   To address these challenges, we present FlashCodec and UnifiedServe, two complementary designs that jointly optimize the end-to-end MLLM pipeline. FlashCodec accelerates the multimodal preprocessing stage through collaborative multi-GPU video decoding, reducing decoding latency while preserving high throughput. UnifiedServe optimizes the vision-to-text and inference stages using a logically decoupled their execution to eliminate inter-stage blocking, yet physically sharing GPU resources to maximize GPU system utilization. By carefully orchestrating execution across stages and minimizing interference, UnifiedServe Together, our proposed framework forms an end-to-end optimized stack that can serve up to 3.0$\times$ more requests or enforce 1.5$\times$ tighter SLOs, while achieving up to 4.4$\times$ higher throughput compared to state-of-the-art systems.

