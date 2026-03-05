---
layout: default
title: Bielik-Q2-Sharp: A Comparative Study of Extreme 2-bit Quantization Methods for a Polish 11B Language Model
---

# Bielik-Q2-Sharp: A Comparative Study of Extreme 2-bit Quantization Methods for a Polish 11B Language Model
**arXiv**：[2603.04162v1](https://arxiv.org/abs/2603.04162) · [PDF](https://arxiv.org/pdf/2603.04162.pdf)  
**作者**：Jakub Prejzner  

**一句话要点**：提出Bielik-Q2-Sharp，系统评估波兰语大模型的极端2位量化方法。

**关键词**：极端量化, 波兰语大模型, 后训练量化, Hessian矩阵, 推理性能

## 3 点简述
- 核心问题：极端2位量化在波兰语大模型中的性能与效率评估。
- 方法要点：比较六种后训练量化方法，使用共享Hessian矩阵在波兰语语料库上校准。
- 实验或效果：最佳方法在多项基准测试中接近基线，部分方法在推理任务中表现优异。

## 摘要（原文）

> We present Bielik-Q2-Sharp, the first systematic academic evaluation of extreme 2-bit quantization applied to a Polish large language model. Using Bielik-11B-v2.3-Instruct (11B parameters, Mistral architecture) as our base model, we compare six state-of-the-art post-training quantization methods -- QuIP#, SpinQuant+GPTQ, ButterflyQuant, QTIP, VPTQ, and AQLM -- all calibrated on a Polish-language corpus (CulturaX-PL) with shared Hessian matrices. Our best variant (QuIP# E8P12) achieves 71.92% across 22 Polish benchmarks versus 72.07% for the IQ2_XXS baseline -- within statistical noise, at a modest size premium (3.26 GB vs. ~2.6 GB). On eq_bench, our method scores 47.14 versus 43.53 (+3.6pp), suggesting superior preservation of higher-order reasoning. QTIP achieves the best per-bit efficiency (79.4% MC acc_norm at ~2.4 bpw, 3.27 GB), matching VPTQ's quality at 35% smaller size. We additionally document a MC-generation dissociation phenomenon where rotation-based methods preserve log-likelihood quality but fail catastrophically at autoregressive generation. The entire project was conducted by a single independent researcher on cloud GPUs (vast.ai) within a $285 budget. All models, Hessians, and evaluation logs are publicly available.

