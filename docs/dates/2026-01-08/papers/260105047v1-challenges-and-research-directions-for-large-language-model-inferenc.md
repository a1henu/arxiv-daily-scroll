---
layout: default
title: Challenges and Research Directions for Large Language Model Inference Hardware
---

# Challenges and Research Directions for Large Language Model Inference Hardware
**arXiv**：[2601.05047v1](https://arxiv.org/abs/2601.05047) · [PDF](https://arxiv.org/pdf/2601.05047.pdf)  
**作者**：Xiaoyu Ma, David Patterson  

**一句话要点**：分析大语言模型推理硬件挑战，提出内存与互连优化架构研究方向

**关键词**：大语言模型推理, 硬件架构, 内存优化, 互连技术, 数据中心AI

## 3 点简述
- 核心问题：自回归解码阶段使推理与训练本质不同，内存和互连成为主要瓶颈
- 方法要点：聚焦高带宽闪存、近内存处理、3D堆叠和低延迟互连等架构机会
- 实验或效果：未知具体实验，但强调数据中心应用，并评估移动设备适用性

## 摘要（原文）

> Large Language Model (LLM) inference is hard. The autoregressive Decode phase of the underlying Transformer model makes LLM inference fundamentally different from training. Exacerbated by recent AI trends, the primary challenges are memory and interconnect rather than compute. To address these challenges, we highlight four architecture research opportunities: High Bandwidth Flash for 10X memory capacity with HBM-like bandwidth; Processing-Near-Memory and 3D memory-logic stacking for high memory bandwidth; and low-latency interconnect to speedup communication. While our focus is datacenter AI, we also review their applicability for mobile devices.

