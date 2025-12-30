---
layout: default
title: SoulX-LiveTalk Technical Report
---

# SoulX-LiveTalk Technical Report
**arXiv**：[2512.23379v1](https://arxiv.org/abs/2512.23379) · [PDF](https://arxiv.org/pdf/2512.23379.pdf)  
**作者**：Le Shen, Qiao Qian, Tan Yu, Ke Zhou, Tianhang Yu, Yu Zhan, Zhenjie Wang, Ming Tao, Shunshun Yin, Siyuan Liu  

**一句话要点**：提出SoulX-LiveTalk框架，通过双向蒸馏与自校正机制，实现高保真实时音频驱动虚拟人生成。

**关键词**：实时虚拟人生成, 音频驱动动画, 双向注意力蒸馏, 自校正机制, 推理加速, 扩散模型优化

## 3 点简述
- 核心问题：大规模扩散模型在实时音频驱动虚拟人生成中面临计算负载与延迟约束的冲突，现有方法常牺牲视觉保真度。
- 方法要点：采用自校正双向蒸馏策略，在视频块内保留双向注意力，增强运动连贯性与视觉细节；结合多步回顾自校正机制，防止无限生成中的错误累积与崩溃。
- 实验或效果：系统达到0.87秒启动延迟和32 FPS实时吞吐量，为高保真交互式数字人合成设立新标准。

## 摘要（原文）

> Deploying massive diffusion models for real-time, infinite-duration, audio-driven avatar generation presents a significant engineering challenge, primarily due to the conflict between computational load and strict latency constraints. Existing approaches often compromise visual fidelity by enforcing strictly unidirectional attention mechanisms or reducing model capacity. To address this problem, we introduce \textbf{SoulX-LiveTalk}, a 14B-parameter framework optimized for high-fidelity real-time streaming. Diverging from conventional unidirectional paradigms, we use a \textbf{Self-correcting Bidirectional Distillation} strategy that retains bidirectional attention within video chunks. This design preserves critical spatiotemporal correlations, significantly enhancing motion coherence and visual detail. To ensure stability during infinite generation, we incorporate a \textbf{Multi-step Retrospective Self-Correction Mechanism}, enabling the model to autonomously recover from accumulated errors and preventing collapse. Furthermore, we engineered a full-stack inference acceleration suite incorporating hybrid sequence parallelism, Parallel VAE, and kernel-level optimizations. Extensive evaluations confirm that SoulX-LiveTalk is the first 14B-scale system to achieve a \textbf{sub-second start-up latency (0.87s)} while reaching a real-time throughput of \textbf{32 FPS}, setting a new standard for high-fidelity interactive digital human synthesis.

