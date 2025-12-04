---
layout: default
title: UniQL: Unified Quantization and Low-rank Compression for Adaptive Edge LLMs
---

# UniQL: Unified Quantization and Low-rank Compression for Adaptive Edge LLMs
**arXiv**：[2512.03383v1](https://arxiv.org/abs/2512.03383) · [PDF](https://arxiv.org/pdf/2512.03383.pdf)  
**作者**：Hung-Yueh Chiang, Chi-Chih Chang, Yu-Chen Lu, Chien-Yu Lin, Kai-Chiang Wu, Mohamed S. Abdelfattah, Diana Marculescu  

**一句话要点**：提出UniQL统一量化与低秩压缩框架，以支持自适应边缘大语言模型部署。

**关键词**：边缘计算, 模型压缩, 量化, 低秩分解, 自适应部署, Transformer模型

## 3 点简述
- 核心问题：边缘设备内存和计算资源有限，模型部署受设备负载影响，存在不确定性。
- 方法要点：集成量化与低秩压缩，引入权重排序、量化感知SVD、状态感知排序和融合RoPE内核，支持云端单流程处理与设备端可配置剪枝。
- 实验或效果：在Transformers、SSMs和混合模型上，内存减少4-5.7倍，吞吐提升2.7-3.4倍，精度损失在5%以内。

## 摘要（原文）

> Deploying large language model (LLM) models on mobile platforms faces significant challenges due to the limited memory and shared computational resources of the device. Resource availability may be an issue as it is directly impacted by the current device workload, adding to the uncertainty of model deployment. We introduce UniQL, a unified post-training quantization and low-rank compression framework with on-device configurable pruning rates for edge LLMs. UniQL is a general framework that integrates quantization and low-rank compression for Transformers, State Space Models (SSMs), and hybrid models to support diverse edge applications. In our proposed joint framework, we introduce an efficient structured weight-sorting method that speeds up computation by 20x, quantization-aware singular value decomposition (SVD) to minimize quantization errors, state-aware weight sorting for SSMs, and a fused rotary positional embedding (RoPE) kernel for pruned models. Our framework performs weight-sorting, fine-tuning, and quantization in the cloud in a single-pass workflow, while enabling on-device configurable pruning rates up to 35%. Our experiments show that quantized and pruned models achieve a memory reduction of 4x-5.7x and a token-throughput improvement of 2.7x-3.4x, maintaining accuracy within 5% of the original models at 15% pruning across Transformers (Llama3 and Qwen2.5), SSMs (Mamba2), and hybrid models (Nemotron-H and Bamba-v2). The code and quantized models are available at: https://github.com/enyac-group/UniQL.

