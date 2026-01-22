---
layout: default
title: TIDAL: Temporally Interleaved Diffusion and Action Loop for High-Frequency VLA Control
---

# TIDAL: Temporally Interleaved Diffusion and Action Loop for High-Frequency VLA Control
**arXiv**：[2601.14945v1](https://arxiv.org/abs/2601.14945) · [PDF](https://arxiv.org/pdf/2601.14945.pdf)  
**作者**：Yuteng Sun, Haoran Wang, Ruofei Bai, Zhengguo Li, Jun Li, Meng Yee, Chuah, Wei Yun Yau  

**一句话要点**：提出TIDAL框架以解决视觉语言动作模型在动态环境中的高频控制延迟问题

**关键词**：视觉语言动作模型, 高频控制, 扩散模型, 延迟补偿, 动态环境, 分层架构

## 3 点简述
- 核心问题：大规模VLA模型推理延迟高，在动态环境中执行存在盲区
- 方法要点：采用双频架构分离语义推理与高频执行，引入时间错位训练策略
- 实验效果：在动态拦截任务中性能提升2倍，控制频率提高至约9Hz

## 摘要（原文）

> Large-scale Vision-Language-Action (VLA) models offer semantic generalization but suffer from high inference latency, limiting them to low-frequency batch-and-execute paradigm. This frequency mismatch creates an execution blind spot, causing failures in dynamic environments where targets move during the open-loop execution window. We propose TIDAL (Temporally Interleaved Diffusion and Action Loop), a hierarchical framework that decouples semantic reasoning from high-frequency actuation. TIDAL operates as a backbone-agnostic module for diffusion-based VLAs, using a dual-frequency architecture to redistribute the computational budget. Specifically, a low-frequency macro-intent loop caches semantic embeddings, while a high-frequency micro-control loop interleaves single-step flow integration with execution. This design enables approximately 9 Hz control updates on edge hardware (vs. approximately 2.4 Hz baselines) without increasing marginal overhead. To handle the resulting latency shift, we introduce a temporally misaligned training strategy where the policy learns predictive compensation using stale semantic intent alongside real-time proprioception. Additionally, we address the insensitivity of static vision encoders to velocity by incorporating a differential motion predictor. TIDAL is architectural, making it orthogonal to system-level optimizations. Experiments show a 2x performance gain over open-loop baselines in dynamic interception tasks. Despite a marginal regression in static success rates, our approach yields a 4x increase in feedback frequency and extends the effective horizon of semantic embeddings beyond the native action chunk size. Under non-paused inference protocols, TIDAL remains robust where standard baselines fail due to latency.

