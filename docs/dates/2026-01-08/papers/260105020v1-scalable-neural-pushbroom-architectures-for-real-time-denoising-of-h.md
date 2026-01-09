---
layout: default
title: Scalable neural pushbroom architectures for real-time denoising of hyperspectral images onboard satellites
---

# Scalable neural pushbroom architectures for real-time denoising of hyperspectral images onboard satellites
**arXiv**：[2601.05020v1](https://arxiv.org/abs/2601.05020) · [PDF](https://arxiv.org/pdf/2601.05020.pdf)  
**作者**：Ziyao Yi, Davide Piccinini, Diego Valsesia, Tiziano Bianchi, Enrico Magli  

**一句话要点**：提出可扩展神经推扫架构，用于卫星上高光谱图像实时去噪

**关键词**：高光谱图像去噪, 卫星上处理, 神经推扫架构, 功耗可扩展性, 辐射容错, 实时处理

## 3 点简述
- 针对卫星上高光谱图像去噪，需平衡高质量推理、低复杂度、动态功耗可扩展性和容错性。
- 设计混合去噪器，采用因果逐行处理匹配推扫传感器，降低内存需求，支持功耗调整和辐射容错。
- 在低功耗硬件上实现实时处理，去噪质量与更复杂模型竞争，展示功耗与容错间的权衡设计空间。

## 摘要（原文）

> The next generation of Earth observation satellites will seek to deploy intelligent models directly onboard the payload in order to minimize the latency incurred by the transmission and processing chain of the ground segment, for time-critical applications. Designing neural architectures for onboard execution, particularly for satellite-based hyperspectral imagers, poses novel challenges due to the unique constraints of this environment and imaging system that are largely unexplored by the traditional computer vision literature. In this paper, we show that this setting requires addressing three competing objectives, namely high-quality inference with low complexity, dynamic power scalability and fault tolerance. We focus on the problem of hyperspectral image denoising, which is a critical task to enable effective downstream inference, and highlights the constraints of the onboard processing scenario. We propose a neural network design that addresses the three aforementioned objectives with several novel contributions. In particular, we propose a mixture of denoisers that can be resilient to radiation-induced faults as well as allowing for time-varying power scaling. Moreover, each denoiser employs an innovative architecture where an image is processed line-by-line in a causal way, with a memory of past lines, in order to match the acquisition process of pushbroom hyperspectral sensors and greatly limit memory requirements. We show that the proposed architecture can run in real-time, i.e., process one line in the time it takes to acquire the next one, on low-power hardware and provide competitive denoising quality with respect to significantly more complex state-of-the-art models. We also show that the power scalability and fault tolerance objectives provide a design space with multiple tradeoffs between those properties and denoising quality.

