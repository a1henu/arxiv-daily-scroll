---
layout: default
title: No Labels, No Look-Ahead: Unsupervised Online Video Stabilization with Classical Priors
---

# No Labels, No Look-Ahead: Unsupervised Online Video Stabilization with Classical Priors
**arXiv**：[2602.23141v1](https://arxiv.org/abs/2602.23141) · [PDF](https://arxiv.org/pdf/2602.23141.pdf)  
**作者**：Tao Liu, Gang Wan, Kan Ren, Shibo Wen  

**一句话要点**：提出无监督在线视频稳定框架，结合经典先验与多线程缓冲，解决数据限制与硬件效率问题。

**关键词**：无监督学习, 在线视频稳定, 经典先验, 多线程缓冲, 无人机视频, 硬件效率

## 3 点简述
- 核心问题：现有方法依赖配对数据集，在数据有限、可控性差和资源受限硬件上效率低下。
- 方法要点：采用三阶段经典稳定流程，集成多线程缓冲机制，实现无监督在线处理。
- 实验或效果：在定量指标和视觉质量上优于现有在线方法，性能接近离线方法，并引入多模态无人机数据集。

## 摘要（原文）

> We propose a new unsupervised framework for online video stabilization. Unlike methods based on deep learning that require paired stable and unstable datasets, our approach instantiates the classical stabilization pipeline with three stages and incorporates a multithreaded buffering mechanism. This design addresses three longstanding challenges in end-to-end learning: limited data, poor controllability, and inefficiency on hardware with constrained resources. Existing benchmarks focus mainly on handheld videos with a forward view in visible light, which restricts the applicability of stabilization to domains such as UAV nighttime remote sensing. To fill this gap, we introduce a new multimodal UAV aerial video dataset (UAV-Test). Experiments show that our method consistently outperforms state-of-the-art online stabilizers in both quantitative metrics and visual quality, while achieving performance comparable to offline methods.

