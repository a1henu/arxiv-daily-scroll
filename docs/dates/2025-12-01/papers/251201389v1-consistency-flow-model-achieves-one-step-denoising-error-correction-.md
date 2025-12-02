---
layout: default
title: Consistency Flow Model Achieves One-step Denoising Error Correction Codes
---

# Consistency Flow Model Achieves One-step Denoising Error Correction Codes
**arXiv**：[2512.01389v1](https://arxiv.org/abs/2512.01389) · [PDF](https://arxiv.org/pdf/2512.01389.pdf)  
**作者**：Haoyu Lei, Chin Wa Lau, Kaiwen Zhou, Nian Guo, Farzan Farnia  

**一句话要点**：提出ECCFM框架实现一步解码，解决纠错码解码中迭代采样导致的低延迟挑战。

**关键词**：纠错码解码, 概率流ODE, 一步推理, 低延迟通信, 神经解码器

## 3 点简述
- 核心问题：神经解码器在准确性与计算效率间存在权衡，迭代采样限制低延迟应用。
- 方法要点：基于概率流ODE，通过微分时间正则化学习从噪声信号到原始码字的一步映射。
- 实验或效果：在多个基准测试中实现更低误码率，推理速度比扩散解码器快30-100倍。

## 摘要（原文）

> Error Correction Codes (ECC) are fundamental to reliable digital communication, yet designing neural decoders that are both accurate and computationally efficient remains challenging. Recent denoising diffusion decoders with transformer backbones achieve state-of-the-art performance, but their iterative sampling limits practicality in low-latency settings. We introduce the Error Correction Consistency Flow Model (ECCFM), an architecture-agnostic training framework for high-fidelity one-step decoding. By casting the reverse denoising process as a Probability Flow Ordinary Differential Equation (PF-ODE) and enforcing smoothness through a differential time regularization, ECCFM learns to map noisy signals along the decoding trajectory directly to the original codeword in a single inference step. Across multiple decoding benchmarks, ECCFM attains lower bit-error rates (BER) than autoregressive and diffusion-based baselines, with notable improvements on longer codes, while delivering inference speeds up from 30x to 100x faster than denoising diffusion decoders.

