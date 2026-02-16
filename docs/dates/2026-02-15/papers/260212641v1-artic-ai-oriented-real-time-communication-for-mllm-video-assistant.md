---
layout: default
title: Artic: AI-oriented Real-time Communication for MLLM Video Assistant
---

# Artic: AI-oriented Real-time Communication for MLLM Video Assistant
**arXiv**：[2602.12641v1](https://arxiv.org/abs/2602.12641) · [PDF](https://arxiv.org/pdf/2602.12641.pdf)  
**作者**：Jiangkai Wu, Zhiyuan Ren, Junquan Zhong, Liming Liu, Xinggong Zhang  

**一句话要点**：提出Artic框架以解决MLLM视频助手中实时通信的延迟与准确性问题

**关键词**：实时通信, 多模态大语言模型, 视频助手, 自适应比特率, 视频理解基准

## 3 点简述
- 核心问题：现有RTC框架与AI视频助手不匹配，导致延迟激增和准确率下降
- 方法要点：引入响应能力感知自适应比特率、零开销上下文感知流媒体和退化视频理解基准
- 实验或效果：原型实验显示，相比现有方法，准确率提升15.12%，延迟降低135.31毫秒

## 摘要（原文）

> AI Video Assistant emerges as a new paradigm for Real-time Communication (RTC), where one peer is a Multimodal Large Language Model (MLLM) deployed in the cloud. This makes interaction between humans and AI more intuitive, akin to chatting with a real person. However, a fundamental mismatch exists between current RTC frameworks and AI Video Assistants, stemming from the drastic shift in Quality of Experience (QoE) and more challenging networks. Measurements on our production prototype also confirm that current RTC fails, causing latency spikes and accuracy drops.
>   To address these challenges, we propose Artic, an AI-oriented RTC framework for MLLM Video Assistants, exploring the shift from "humans watching video" to "AI understanding video." Specifically, Artic proposes: (1) Response Capability-aware Adaptive Bitrate, which utilizes MLLM accuracy saturation to proactively cap bitrate, reserving bandwidth headroom to absorb future fluctuations for latency reduction; (2) Zero-overhead Context-aware Streaming, which allocates limited bitrate to regions most important for the response, maintaining accuracy even under ultra-low bitrates; and (3) Degraded Video Understanding Benchmark, the first benchmark evaluating how RTC-induced video degradation affects MLLM accuracy. Prototype experiments using real-world uplink traces show that compared with existing methods, Artic significantly improves accuracy by 15.12% and reduces latency by 135.31 ms. We will release the benchmark and codes at https://github.com/pku-netvideo/DeViBench.

