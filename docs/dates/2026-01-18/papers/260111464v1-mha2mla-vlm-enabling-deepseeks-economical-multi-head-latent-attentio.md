---
layout: default
title: MHA2MLA-VLM: Enabling DeepSeek's Economical Multi-Head Latent Attention across Vision-Language Models
---

# MHA2MLA-VLM: Enabling DeepSeek's Economical Multi-Head Latent Attention across Vision-Language Models
**arXiv**：[2601.11464v1](https://arxiv.org/abs/2601.11464) · [PDF](https://arxiv.org/pdf/2601.11464.pdf)  
**作者**：Xiaoran Fan, Zhichao Sun, Tao Ji, Lixing Shen, Tao Gui  

**一句话要点**：提出MHA2MLA-VLM框架，将现有多模态模型高效转换为多头潜在注意力架构以降低推理开销

**关键词**：多模态模型, 注意力机制, 推理优化, 参数高效微调, KV缓存压缩, 低秩近似

## 3 点简述
- 核心问题：多模态任务中KV缓存增长导致内存和计算瓶颈，现有模型难以低成本适配MLA架构
- 方法要点：采用模态自适应部分RoPE和模态解耦低秩近似，结合参数高效微调，最小化性能损失
- 实验或效果：在三个代表性多模态模型上验证，恢复原始性能，显著减少KV缓存占用，兼容KV量化

## 摘要（原文）

> As vision-language models (VLMs) tackle increasingly complex and multimodal tasks, the rapid growth of Key-Value (KV) cache imposes significant memory and computational bottlenecks during inference. While Multi-Head Latent Attention (MLA) offers an effective means to compress the KV cache and accelerate inference, adapting existing VLMs to the MLA architecture without costly pretraining remains largely unexplored. In this work, we present MHA2MLA-VLM, a parameter-efficient and multimodal-aware framework for converting off-the-shelf VLMs to MLA. Our approach features two core techniques: (1) a modality-adaptive partial-RoPE strategy that supports both traditional and multimodal settings by selectively masking nonessential dimensions, and (2) a modality-decoupled low-rank approximation method that independently compresses the visual and textual KV spaces. Furthermore, we introduce parameter-efficient fine-tuning to minimize adaptation cost and demonstrate that minimizing output activation error, rather than parameter distance, substantially reduces performance loss. Extensive experiments on three representative VLMs show that MHA2MLA-VLM restores original model performance with minimal supervised data, significantly reduces KV cache footprint, and integrates seamlessly with KV quantization.

