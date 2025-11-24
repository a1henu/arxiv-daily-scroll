---
layout: default
title: Single-Pixel Tactile Skin via Compressive Sampling
---

# Single-Pixel Tactile Skin via Compressive Sampling
**arXiv**：[2511.16898v1](https://arxiv.org/abs/2511.16898) · [PDF](https://arxiv.org/pdf/2511.16898.pdf)  
**作者**：Ariel Slepyan, Laura Xing, Rudy Zhang, Nitish Thakor  

**一句话要点**：提出单像素触觉皮肤以解决电子皮肤布线复杂和数据瓶颈问题

**关键词**：触觉皮肤, 压缩采样, 分布式压缩感知, 机器人接口, 自适应重建

## 3 点简述
- 核心问题：大范围高速电子皮肤受限于布线复杂性和数据瓶颈
- 方法要点：采用压缩采样通过单输出通道重构触觉信息，硬件实现分布式压缩感知
- 实验或效果：实现3500 FPS物体分类，捕获8 ms瞬态动态，支持自适应重建

## 摘要（原文）

> Development of large-area, high-speed electronic skins is a grand challenge for robotics, prosthetics, and human-machine interfaces, but is fundamentally limited by wiring complexity and data bottlenecks. Here, we introduce Single-Pixel Tactile Skin (SPTS), a paradigm that uses compressive sampling to reconstruct rich tactile information from an entire sensor array via a single output channel. This is achieved through a direct circuit-level implementation where each sensing element, equipped with a miniature microcontroller, contributes a dynamically weighted analog signal to a global sum, performing distributed compressed sensing in hardware. Our flexible, daisy-chainable design simplifies wiring to a few input lines and one output, and significantly reduces measurement requirements compared to raster scanning methods. We demonstrate the system's performance by achieving object classification at an effective 3500 FPS and by capturing transient dynamics, resolving an 8 ms projectile impact into 23 frames. A key feature is the support for adaptive reconstruction, where sensing fidelity scales with measurement time. This allows for rapid contact localization using as little as 7% of total data, followed by progressive refinement to a high-fidelity image - a capability critical for responsive robotic systems. This work offers an efficient pathway towards large-scale tactile intelligence for robotics and human-machine interfaces.

