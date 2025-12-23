---
layout: default
title: Real-Time Streamable Generative Speech Restoration with Flow Matching
---

# Real-Time Streamable Generative Speech Restoration with Flow Matching
**arXiv**：[2512.19442v1](https://arxiv.org/abs/2512.19442) · [PDF](https://arxiv.org/pdf/2512.19442.pdf)  
**作者**：Simon Welker, Bunlong Lay, Maris Hillemann, Tal Peer, Timo Gerkmann  

**一句话要点**：提出Stream.FM流式生成语音恢复模型，实现低延迟实时通信应用

**关键词**：流式生成模型, 语音恢复, 低延迟处理, 流匹配, 实时通信, 模型压缩

## 3 点简述
- 核心问题：扩散模型计算量大，难以应用于实时语音处理场景
- 方法要点：基于流匹配的帧因果模型，结合缓冲流式推理和优化架构
- 实验或效果：在多种任务中实现高质量流式处理，总延迟低至24-48毫秒

## 摘要（原文）

> Diffusion-based generative models have greatly impacted the speech processing field in recent years, exhibiting high speech naturalness and spawning a new research direction. Their application in real-time communication is, however, still lagging behind due to their computation-heavy nature involving multiple calls of large DNNs.
>   Here, we present Stream.FM, a frame-causal flow-based generative model with an algorithmic latency of 32 milliseconds (ms) and a total latency of 48 ms, paving the way for generative speech processing in real-time communication. We propose a buffered streaming inference scheme and an optimized DNN architecture, show how learned few-step numerical solvers can boost output quality at a fixed compute budget, explore model weight compression to find favorable points along a compute/quality tradeoff, and contribute a model variant with 24 ms total latency for the speech enhancement task.
>   Our work looks beyond theoretical latencies, showing that high-quality streaming generative speech processing can be realized on consumer GPUs available today. Stream.FM can solve a variety of speech processing tasks in a streaming fashion: speech enhancement, dereverberation, codec post-filtering, bandwidth extension, STFT phase retrieval, and Mel vocoding. As we verify through comprehensive evaluations and a MUSHRA listening test, Stream.FM establishes a state-of-the-art for generative streaming speech restoration, exhibits only a reasonable reduction in quality compared to a non-streaming variant, and outperforms our recent work (Diffusion Buffer) on generative streaming speech enhancement while operating at a lower latency.

