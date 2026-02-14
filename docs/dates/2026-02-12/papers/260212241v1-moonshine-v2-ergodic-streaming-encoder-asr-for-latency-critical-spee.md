---
layout: default
title: Moonshine v2: Ergodic Streaming Encoder ASR for Latency-Critical Speech Applications
---

# Moonshine v2: Ergodic Streaming Encoder ASR for Latency-Critical Speech Applications
**arXiv**：[2602.12241v1](https://arxiv.org/abs/2602.12241) · [PDF](https://arxiv.org/pdf/2602.12241.pdf)  
**作者**：Manjunath Kudlur, Evan King, James Wang, Pete Warden  

**一句话要点**：提出Moonshine v2流式编码器ASR模型，以滑动窗口自注意力解决边缘设备低延迟语音应用需求。

**关键词**：流式自动语音识别, 低延迟推理, 滑动窗口自注意力, 边缘设备ASR, 时间到首令牌优化

## 3 点简述
- 核心问题：全注意力Transformer编码器在流式ASR中导致延迟随话语长度线性增长，不适用于低延迟场景。
- 方法要点：采用滑动窗口自注意力，实现有界低延迟推理，同时保持强局部上下文，以替代全注意力。
- 实验或效果：在标准基准测试中达到最先进词错误率，精度与6倍大小模型相当，运行速度显著更快。

## 摘要（原文）

> Latency-critical speech applications (e.g., live transcription, voice commands, and real-time translation) demand low time-to-first-token (TTFT) and high transcription accuracy, particularly on resource-constrained edge devices. Full-attention Transformer encoders remain a strong accuracy baseline for automatic speech recognition (ASR) because every frame can directly attend to every other frame, which resolves otherwise locally ambiguous acoustics using distant lexical context. However, this global dependency incurs quadratic complexity in sequence length, inducing an inherent "encode-the-whole-utterance" latency profile. For streaming use cases, this causes TTFT to grow linearly with utterance length as the encoder must process the entire prefix before any decoder token can be emitted. To better meet the needs of on-device, streaming ASR use cases we introduce Moonshine v2, an ergodic streaming-encoder ASR model that employs sliding-window self-attention to achieve bounded, low-latency inference while preserving strong local context. Our models achieve state of the art word error rates across standard benchmarks, attaining accuracy on-par with models 6x their size while running significantly faster. These results demonstrate that carefully designed local attention is competitive with the accuracy of full attention at a fraction of the size and latency cost, opening new possibilities for interactive speech interfaces on edge devices.

