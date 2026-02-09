---
layout: default
title: Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention
---

# Efficient-LVSM: Faster, Cheaper, and Better Large View Synthesis Model via Decoupled Co-Refinement Attention
**arXiv**：[2602.06478v1](https://arxiv.org/abs/2602.06478) · [PDF](https://arxiv.org/pdf/2602.06478.pdf)  
**作者**：Xiaosong Jia, Yihang Sun, Junqi You, Songbur Wong, Zichen Zou, Junchi Yan, Zuxuan Wu, Yu-Gang Jiang  

**一句话要点**：提出Efficient-LVSM，通过解耦协同精炼注意力优化大视图合成模型，提升效率与性能。

**关键词**：视图合成, 注意力机制, Transformer模型, 效率优化, 零样本泛化, 增量推理

## 3 点简述
- 核心问题：LVSM等基于Transformer的视图合成模型存在全自注意力设计，导致输入视图数量的二次复杂度及异构令牌间参数共享不灵活。
- 方法要点：采用双流架构，输入视图使用视图内自注意力，目标视图使用自后交叉注意力，实现解耦协同精炼，减少不必要计算。
- 实验或效果：在RealEstate10K上以2输入视图达到29.86 dB PSNR，超越LVSM 0.2 dB，训练收敛快2倍，推理速度提升4.4倍，支持零样本泛化和增量推理。

## 摘要（原文）

> Feedforward models for novel view synthesis (NVS) have recently advanced by transformer-based methods like LVSM, using attention among all input and target views. In this work, we argue that its full self-attention design is suboptimal, suffering from quadratic complexity with respect to the number of input views and rigid parameter sharing among heterogeneous tokens. We propose Efficient-LVSM, a dual-stream architecture that avoids these issues with a decoupled co-refinement mechanism. It applies intra-view self-attention for input views and self-then-cross attention for target views, eliminating unnecessary computation. Efficient-LVSM achieves 29.86 dB PSNR on RealEstate10K with 2 input views, surpassing LVSM by 0.2 dB, with 2x faster training convergence and 4.4x faster inference speed. Efficient-LVSM achieves state-of-the-art performance on multiple benchmarks, exhibits strong zero-shot generalization to unseen view counts, and enables incremental inference with KV-cache, thanks to its decoupled designs.

