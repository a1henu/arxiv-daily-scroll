---
layout: default
title: Bridging Hidden States in Vision-Language Models
---

# Bridging Hidden States in Vision-Language Models
**arXiv**：[2511.11526v1](https://arxiv.org/abs/2511.11526) · [PDF](https://arxiv.org/pdf/2511.11526.pdf)  
**作者**：Benjamin Fein-Ashley, Jacob Fein-Ashley  

**一句话要点**：提出BRIDGE模块以在视觉语言模型中高效对齐隐藏状态

**关键词**：视觉语言模型, 跨模态对齐, 隐藏状态融合, 双向注意力, 轻量级模块, 检索基准

## 3 点简述
- 现有方法融合视觉与语言模态时，常采用早期或晚期融合，但未充分利用隐藏状态的结构信息。
- 在编码器顶部添加轻量级双向注意力层，跨模态对齐隐藏状态，并保留编码器非因果特性。
- 在检索、VQA和视觉推理基准测试中，BRIDGE优于可比模型，同时保持双编码器效率。

## 摘要（原文）

> Vision-Language Models (VLMs) are a new family of models that align image content with natural language. Existing approaches typically fuse either (a) early: by mixing tokens/features inside the encoders, or (b) late: by comparing pooled embeddings. Many methods also tie fusion to an autoregressive decoder. However, the hidden states of both modalities already carry rich, modality-specific structure (spatial layout in vision; syntax and semantics in text), so directly aligning these states is a natural way to match what the two modalities "think". We propose a lightweight fusion module: a few cross-only, bidirectional attention layers placed near the top of both encoders. Each layer projects the vision and text encoder hidden-state sequences into a shared space, attends across modalities, and sends gated residual updates back, with simple stabilizers to improve alignment. The encoders remain non-causal and strong for understanding, while generation stays cleanly decoupled via an optional decoder. Across standard retrieval, VQA, and visual reasoning benchmarks, BRIDGE outperforms comparable VLMs while preserving the bi-encoder efficiency of contrastive models. We make our code publicly available at https://github.com/jfeinashley/BRIDGE.

