---
layout: default
title: Embedded AI Companion System on Edge Devices
---

# Embedded AI Companion System on Edge Devices
**arXiv**：[2601.08128v1](https://arxiv.org/abs/2601.08128) · [PDF](https://arxiv.org/pdf/2601.08128.pdf)  
**作者**：Rahul Gupta, Stephen D. H. Hsu  

**一句话要点**：提出边缘设备上基于活动-非活动阶段交替的内存范式，以在资源受限下实现低延迟AI伴侣系统。

**关键词**：边缘计算, AI伴侣系统, 内存管理, 低延迟对话, 资源优化, 量化模型

## 3 点简述
- 核心问题：边缘设备计算资源有限，现有AI伴侣系统难以直接部署，影响用户体验和延迟。
- 方法要点：设计交替内存范式，用户活动时进行轻量检索，非活动时执行计算密集型记忆提取与维护。
- 实验或效果：使用弱模型Qwen2.5-7B-Instruct量化版，在AI伴侣基准上超越无记忆LLM，性能接近GPT-3.5。

## 摘要（原文）

> Computational resource constraints on edge devices make it difficult to develop a fully embedded AI companion system with a satisfactory user experience. AI companion and memory systems detailed in existing literature cannot be directly used in such an environment due to lack of compute resources and latency concerns. In this paper, we propose a memory paradigm that alternates between active and inactive phases: during phases of user activity, the system performs low-latency, real-time dialog using lightweight retrieval over existing memories and context; whereas during phases of user inactivity, it conducts more computationally intensive extraction, consolidation, and maintenance of memories across full conversation sessions. This design minimizes latency while maintaining long-term personalization under the tight constraints of embedded hardware. We also introduce an AI Companion benchmark designed to holistically evaluate the AI Companion across both its conversational quality and memory capabilities. In our experiments, we found that our system (using a very weak model: Qwen2.5-7B-Instruct quantized int4) outperforms the equivalent raw LLM without memory across most metrics, and performs comparably to GPT-3.5 with 16k context window.

