---
layout: default
title: Multi-Objective Pareto-Front Optimization for Efficient Adaptive VVC Streaming
---

# Multi-Objective Pareto-Front Optimization for Efficient Adaptive VVC Streaming
**arXiv**：[2601.10607v1](https://arxiv.org/abs/2601.10607) · [PDF](https://arxiv.org/pdf/2601.10607.pdf)  
**作者**：Angeliki Katsenou, Vignesh V. Menon, Guoda Laurinaviciute, Benjamin Bross, Detlev Marpe  

**一句话要点**：提出多目标帕累托前沿优化框架以构建高效自适应VVC流媒体比特率阶梯

**关键词**：自适应视频流媒体, 多目标优化, 帕累托前沿, VVC编码, 解码复杂度, 比特率阶梯

## 3 点简述
- 核心问题：自适应视频流媒体需平衡比特率、视频质量和解码复杂度以实现高效传输。
- 方法要点：引入JRQT-PF和JQT-PF策略，在质量单调性约束下联合优化质量、比特率和解码时间。
- 实验或效果：在UHD数据集上验证，JQT-PF节省比特率11.76%，解码时间减少0.29%，优于现有方法。

## 摘要（原文）

> Adaptive video streaming has facilitated improved video streaming over the past years. A balance among coding performance objectives such as bitrate, video quality, and decoding complexity is required to achieve efficient, content- and codec-dependent, adaptive video streaming. This paper proposes a multi-objective Pareto-front (PF) optimization framework to construct quality-monotonic, content-adaptive bitrate ladders Versatile Video Coding (VVC) streaming that jointly optimize video quality, bitrate, and decoding time, which is used as a practical proxy for decoding energy. Two strategies are introduced: the Joint Rate-Quality-Time Pareto Front (JRQT-PF) and the Joint Quality-Time Pareto Front (JQT-PF), each exploring different tradeoff formulations and objective prioritizations. The ladders are constructed under quality monotonicity constraints during adaptive streaming to ensure a consistent Quality of Experience (QoE). Experiments are conducted on a large-scale UHD dataset (Inter-4K), with quality assessed using PSNR, VMAF, and XPSNR, and complexity measured via decoding time and energy consumption. The JQT-PF method achieves 11.76% average bitrate savings while reducing average decoding time by 0.29% to maintain the same XPSNR, compared to a widely-used fixed ladder. More aggressive configurations yield up to 27.88% bitrate savings at the cost of increased complexity. The JRQT-PF strategy, on the other hand, offers more controlled tradeoffs, achieving 6.38 % bitrate savings and 6.17 % decoding time reduction. This framework outperforms existing methods, including fixed ladders, VMAF- and XPSNR-based dynamic resolution selection, and complexity-aware benchmarks. The results confirm that PF optimization with decoding time constraints enables sustainable, high-quality streaming tailored to network and device capabilities.

