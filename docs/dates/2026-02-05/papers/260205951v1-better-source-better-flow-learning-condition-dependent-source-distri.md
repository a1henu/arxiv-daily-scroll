---
layout: default
title: Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching
---

# Better Source, Better Flow: Learning Condition-Dependent Source Distribution for Flow Matching
**arXiv**：[2602.05951v1](https://arxiv.org/abs/2602.05951) · [PDF](https://arxiv.org/pdf/2602.05951.pdf)  
**作者**：Junwan Kim, Jiho Park, Seonghu Jeon, Seungryong Kim  

**一句话要点**：提出学习条件依赖源分布以提升流匹配在文本到图像生成中的性能

**关键词**：流匹配, 文本到图像生成, 条件依赖源分布, 方差正则化, 方向对齐, 生成模型

## 3 点简述
- 核心问题：流匹配中源分布通常固定为高斯分布，未充分利用条件信号，导致性能受限。
- 方法要点：学习条件依赖源分布，通过方差正则化和方向对齐避免分布崩溃和不稳定性。
- 实验或效果：在多个文本到图像基准测试中，实现FID收敛速度提升高达3倍，显示稳健改进。

## 摘要（原文）

> Flow matching has recently emerged as a promising alternative to diffusion-based generative models, particularly for text-to-image generation. Despite its flexibility in allowing arbitrary source distributions, most existing approaches rely on a standard Gaussian distribution, a choice inherited from diffusion models, and rarely consider the source distribution itself as an optimization target in such settings. In this work, we show that principled design of the source distribution is not only feasible but also beneficial at the scale of modern text-to-image systems. Specifically, we propose learning a condition-dependent source distribution under flow matching objective that better exploit rich conditioning signals. We identify key failure modes that arise when directly incorporating conditioning into the source, including distributional collapse and instability, and show that appropriate variance regularization and directional alignment between source and target are critical for stable and effective learning. We further analyze how the choice of target representation space impacts flow matching with structured sources, revealing regimes in which such designs are most effective. Extensive experiments across multiple text-to-image benchmarks demonstrate consistent and robust improvements, including up to a 3x faster convergence in FID, highlighting the practical benefits of a principled source distribution design for conditional flow matching.

