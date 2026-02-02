---
layout: default
title: Residual Context Diffusion Language Models
---

# Residual Context Diffusion Language Models
**arXiv**：[2601.22954v1](https://arxiv.org/abs/2601.22954) · [PDF](https://arxiv.org/pdf/2601.22954.pdf)  
**作者**：Yuezhou Hu, Harman Singh, Monishwaran Maheswaran, Haocheng Xi, Coleman Hooper, Jintao Zhang, Aditya Tomar, Michael W. Mahoney, Sewon Min, Mehrdad Farajtabar, Kurt Keutzer, Amir Gholami, Chenfeng Xu  

**一句话要点**：提出残差上下文扩散模块以提升扩散语言模型的解码效率与准确性

**关键词**：扩散语言模型, 并行解码, 残差上下文, 两阶段训练, 推理效率

## 3 点简述
- 现有块状扩散语言模型丢弃低置信度令牌，浪费计算资源与上下文信息
- RCD模块将丢弃令牌转换为残差上下文，注入后续去噪步骤，采用解耦两阶段训练避免内存瓶颈
- 在多种基准测试中提升准确率5-10点，减少去噪步骤达4-5倍，尤其在AIME任务上效果显著

## 摘要（原文）

> Diffusion Large Language Models (dLLMs) have emerged as a promising alternative to purely autoregressive language models because they can decode multiple tokens in parallel. However, state-of-the-art block-wise dLLMs rely on a "remasking" mechanism that decodes only the most confident tokens and discards the rest, effectively wasting computation. We demonstrate that recycling computation from the discarded tokens is beneficial, as these tokens retain contextual information useful for subsequent decoding iterations. In light of this, we propose Residual Context Diffusion (RCD), a module that converts these discarded token representations into contextual residuals and injects them back for the next denoising step. RCD uses a decoupled two-stage training pipeline to bypass the memory bottlenecks associated with backpropagation. We validate our method on both long CoT reasoning (SDAR) and short CoT instruction following (LLaDA) models. We demonstrate that a standard dLLM can be efficiently converted to the RCD paradigm with merely ~1 billion tokens. RCD consistently improves frontier dLLMs by 5-10 points in accuracy with minimal extra computation overhead across a wide range of benchmarks. Notably, on the most challenging AIME tasks, RCD nearly doubles baseline accuracy and attains up to 4-5x fewer denoising steps at equivalent accuracy levels.

