---
layout: default
title: TVTSyn: Content-Synchronous Time-Varying Timbre for Streaming Voice Conversion and Anonymization
---

# TVTSyn: Content-Synchronous Time-Varying Timbre for Streaming Voice Conversion and Anonymization
**arXiv**：[2602.09389v1](https://arxiv.org/abs/2602.09389) · [PDF](https://arxiv.org/pdf/2602.09389.pdf)  
**作者**：Waris Quamer, Mu-Ruei Tseng, Ghady Nasrallah, Ricardo Gutierrez-Osuna  

**一句话要点**：提出TVTSyn以解决实时语音转换和匿名化中身份与内容时间粒度不匹配的问题。

**关键词**：语音转换, 说话人匿名化, 实时合成, 时间变化音色, 低延迟系统, 隐私保护

## 3 点简述
- 核心问题：现有系统使用静态全局嵌入表示说话人身份，与时间变化的内容不匹配。
- 方法要点：通过内容同步的时间变化音色表示，结合全局音色记忆和门控机制，实现身份与内容对齐。
- 实验或效果：系统在GPU延迟<80毫秒下，相比SOTA基线在自然度、说话人转换和匿名化方面有提升。

## 摘要（原文）

> Real-time voice conversion and speaker anonymization require causal, low-latency synthesis without sacrificing intelligibility or naturalness. Current systems have a core representational mismatch: content is time-varying, while speaker identity is injected as a static global embedding. We introduce a streamable speech synthesizer that aligns the temporal granularity of identity and content via a content-synchronous, time-varying timbre (TVT) representation. A Global Timbre Memory expands a global timbre instance into multiple compact facets; frame-level content attends to this memory, a gate regulates variation, and spherical interpolation preserves identity geometry while enabling smooth local changes. In addition, a factorized vector-quantized bottleneck regularizes content to reduce residual speaker leakage. The resulting system is streamable end-to-end, with <80 ms GPU latency. Experiments show improvements in naturalness, speaker transfer, and anonymization compared to SOTA streaming baselines, establishing TVT as a scalable approach for privacy-preserving and expressive speech synthesis under strict latency budgets.

