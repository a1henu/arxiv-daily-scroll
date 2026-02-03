---
layout: default
title: A Practical Tensor-Network Compression Pipeline for Production-Scale Large Language Models
---

# A Practical Tensor-Network Compression Pipeline for Production-Scale Large Language Models
**arXiv**：[2602.01613v1](https://arxiv.org/abs/2602.01613) · [PDF](https://arxiv.org/pdf/2602.01613.pdf)  
**作者**：Sergii Kozyrev, Davyd Maiboroda  

**一句话要点**：提出Minima压缩管道，通过张量网络分解降低大语言模型内存占用并提升推理吞吐量。

**关键词**：大语言模型压缩, 张量网络分解, 推理优化, 生产部署, 推测解码

## 3 点简述
- 核心问题：大语言模型部署受限于GPU内存和推理延迟，影响生产环境应用。
- 方法要点：训练轻量卷积预测器评估敏感度，结合Tucker、张量链和张量环分解压缩低敏感区域，并进行微调和定制内核执行。
- 实验效果：在Qwen3-32B上，峰值VRAM从64 GiB降至40 GiB，单请求吞吐量从40 tokens/s提升至75 tokens/s，高并发下仍保持优势。

## 摘要（原文）

> Large language models are limited in deployment by GPU memory and inference latency. We present Minima, a production compression pipeline that learns where and how to structurally compress a Transformer and turns that compression into real serving gains. Minima trains a lightweight convolutional predictor to estimate layer- and patch-level sensitivity, applies a mixture of Tucker, tensor-train, and tensor-ring decompositions to low-sensitivity regions, performs a short healing fine-tune, and executes the resulting operators with custom Triton and CUDA kernels. The reduced memory footprint enables speculative decoding with a small draft model and a larger verifier. On Qwen3-32B at an 8k-token context window, Minima reduces peak VRAM from 64 GiB to 40 GiB. For a single active request, throughput increases from 40 tokens per second (baseline) to 50 tokens per second (Minima) and 75 tokens per second (Minima with speculative decoding). Under 50 parallel requests, throughput is 34, 44, and 53 tokens per second respectively, showing that Minima remains effective under high concurrency even when speculative decoding gains compress. We position Minima relative to recent tensor-network, low-rank plus quantization, and cross-layer sharing methods, and argue that it is a practical step toward more aggressive structural compression via shared tensor backbones with tiny per-layer adapters.

