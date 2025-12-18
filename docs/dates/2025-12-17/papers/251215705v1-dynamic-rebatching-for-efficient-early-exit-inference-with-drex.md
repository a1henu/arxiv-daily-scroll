---
layout: default
title: Dynamic Rebatching for Efficient Early-Exit Inference with DREX
---

# Dynamic Rebatching for Efficient Early-Exit Inference with DREX
**arXiv**：[2512.15705v1](https://arxiv.org/abs/2512.15705) · [PDF](https://arxiv.org/pdf/2512.15705.pdf)  
**作者**：Xuting Liu, Daniel Alexander, Siva Kesava Reddy Kakarla, Behnaz Arzani, Vincent Liu  

**一句话要点**：提出动态重批处理系统DREX以优化早期退出大语言模型推理效率

**关键词**：早期退出推理, 动态批处理, 大语言模型优化, 推理系统, 服务质量感知调度

## 3 点简述
- 传统批处理框架不适用于早期退出LLM，导致推理效率低下或输出质量下降
- DREX通过动态重批处理，在退出点重组请求，结合无拷贝缓冲和调度器优化
- 实验显示DREX提升吞吐量2-12%，完全消除非自愿退出，保持输出质量

## 摘要（原文）

> Early-Exit (EE) is a Large Language Model (LLM) architecture that accelerates inference by allowing easier tokens to be generated using only a subset of the model's layers. However, traditional batching frameworks are ill-suited for EE LLMs, as not all requests in a batch may be ready to exit at the same time. Existing solutions either force a uniform decision on the batch, which overlooks EE opportunities, or degrade output quality by forcing premature exits. We propose Dynamic Rebatching, a solution where we dynamically reorganize the batch at each early-exit point. Requests that meet the exit criteria are immediately processed, while those that continue are held in a buffer, re-grouped into a new batch, and forwarded to deeper layers. We introduce DREX, an early-exit inference system that implements Dynamic Rebatching with two key optimizations: 1) a copy-free rebatching buffer that avoids physical data movement, and 2) an EE and SLA-aware scheduler that analytically predicts whether a given rebatching operation will be profitable. DREX also efficiently handles the missing KV cache from skipped layers using memory-efficient state-copying. Our evaluation shows that DREX improves throughput by 2-12% compared to baseline approaches while maintaining output quality. Crucially, DREX completely eliminates involuntary exits, providing a key guarantee for preserving the output quality intended by the EE model.

