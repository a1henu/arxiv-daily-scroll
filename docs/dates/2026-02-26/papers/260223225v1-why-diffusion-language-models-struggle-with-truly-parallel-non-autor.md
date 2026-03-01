---
layout: default
title: Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?
---

# Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?
**arXiv**：[2602.23225v1](https://arxiv.org/abs/2602.23225) · [PDF](https://arxiv.org/pdf/2602.23225.pdf)  
**作者**：Pengxiang Li, Dilxat Muhtar, Lu Yin, Tianlong Chen, Shiwei Liu  

**一句话要点**：提出NAP方法，通过数据对齐解决扩散语言模型在非自回归并行解码中的自回归倾向问题

**关键词**：扩散语言模型, 非自回归解码, 并行生成, 数据对齐, 数学推理, 监督学习

## 3 点简述
- 核心问题：扩散语言模型在并行解码时易收敛为自回归模式，源于训练数据与目标不匹配
- 方法要点：NAP通过多独立推理轨迹数据与并行强制解码策略，对齐监督与非自回归并行生成
- 实验或效果：在数学推理基准上，NAP在并行解码下性能优于标准长链监督模型，并行性增益随并行度增加

## 摘要（原文）

> Diffusion Language Models (DLMs) are often advertised as enabling parallel token generation, yet practical fast DLMs frequently converge to left-to-right, autoregressive (AR)-like decoding dynamics. In contrast, genuinely non-AR generation is promising because it removes AR's sequential bottleneck, better exploiting parallel hardware to reduce synchronization/communication overhead and improve latency scaling with output length. We argue that a primary driver of AR-like decoding is a mismatch between DLM objectives and the highly sequential structure of widely used training data, including standard pretraining corpora and long chain-of-thought (CoT) supervision. Motivated by this diagnosis, we propose NAP (Non-Autoregressive Parallel DLMs), a proof-of-concept, data-centric approach that better aligns supervision with non-AR parallel decoding. NAP curates examples as multiple independent reasoning trajectories and couples them with a parallel-forced decoding strategy that encourages multi-token parallel updates. Across math reasoning benchmarks, NAP yields stronger performance under parallel decoding than DLMs trained on standard long CoT data, with gains growing as parallelism increases. Our results suggest that revisiting data and supervision is a principled direction for mitigating AR-like behavior and moving toward genuinely non-autoregressive parallel generation in DLMs. Our code is available at https://github.com/pixeli99/NAP.

