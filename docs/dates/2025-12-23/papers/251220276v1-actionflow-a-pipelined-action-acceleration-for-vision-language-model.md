---
layout: default
title: ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge
---

# ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge
**arXiv**：[2512.20276v1](https://arxiv.org/abs/2512.20276) · [PDF](https://arxiv.org/pdf/2512.20276.pdf)  
**作者**：Yuntao Dai, Hang Gu, Teng Wang, Qianyu Cheng, Yifei Zheng, Zhiyong Qiu, Lei Gong, Wenqi Lou, Xuehai Zhou  

**一句话要点**：提出ActionFlow系统级推理框架，通过跨请求流水线调度解决边缘设备上视觉语言动作模型推理延迟高的问题。

**关键词**：视觉语言动作模型, 边缘计算, 推理加速, 流水线调度, 硬件利用率优化, 系统级框架

## 3 点简述
- 核心问题：VLA模型在边缘设备上因自回归解码内存受限导致推理延迟高，无法满足实时机器人交互需求。
- 方法要点：采用跨请求流水线策略，将推理重构为微请求宏流水线，智能批处理内存受限的解码阶段与计算受限的预填充阶段。
- 实验或效果：在OpenVLA-7B模型上实现2.55倍FPS提升，无需重新训练，支持边缘硬件上的实时动态操作。

## 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hin dered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typi cally operate at only 3-5 Hz on edge devices due to the memory bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge plat forms. At the core of ActionFlow is a Cross-Request Pipelin ing strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dy namic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

