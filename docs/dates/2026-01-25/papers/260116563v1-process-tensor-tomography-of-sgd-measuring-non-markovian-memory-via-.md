---
layout: default
title: Process-Tensor Tomography of SGD: Measuring Non-Markovian Memory via Back-Flow of Distinguishability
---

# Process-Tensor Tomography of SGD: Measuring Non-Markovian Memory via Back-Flow of Distinguishability
**arXiv**：[2601.16563v1](https://arxiv.org/abs/2601.16563) · [PDF](https://arxiv.org/pdf/2601.16563.pdf)  
**作者**：Vasileios Sevetlidis, George Pavlidis  

**一句话要点**：提出基于可区分性回流的训练记忆测量方法，以诊断SGD的非马尔可夫性

**关键词**：过程张量, 非马尔可夫性, 可区分性回流, SGD优化器, 训练记忆测量, 课程学习

## 3 点简述
- 核心问题：将神经训练建模为过程张量，量化训练过程中的非马尔可夫记忆效应
- 方法要点：通过两步骤协议测量可区分性回流，使用TV/JS/Hellinger距离作为见证指标
- 实验或效果：观察到正回流现象，验证了动量、批次重叠和微步数的影响，并应用于课程排序案例

## 摘要（原文）

> This work proposes neural training as a \emph{process tensor}: a multi-time map that takes a sequence of controllable instruments (batch choices, augmentations, optimizer micro-steps) and returns an observable of the trained model. Building on this operational lens, we introduce a simple, model-agnostic witness of training memory based on \emph{back-flow of distinguishability}. In a controlled two-step protocol, we compare outcome distributions after one intervention versus two; the increase $Δ_{\mathrm{BF}} = D_2 - D_1>0$ (with $D\in\{\mathrm{TV}, \mathrm{JS}, \mathrm{H}\}$ measured on softmax predictions over a fixed probe set) certifies non-Markovianity. We observe consistent positive back-flow with tight bootstrap confidence intervals, amplification under higher momentum, larger batch overlap, and more micro-steps, and collapse under a \emph{causal break} (resetting optimizer state), directly attributing the effect to optimizer/data-state memory. The witness is robust across TV/JS/Hellinger, inexpensive to compute, and requires no architectural changes. We position this as a \emph{measurement} contribution: a principled diagnostic and empirical evidence that practical SGD deviates from the Markov idealization. An exploratory case study illustrates how the micro-level signal can inform curriculum orderings. "Data order matters" turns into a testable operator with confidence bounds, our framework offers a common stage to compare optimizers, curricula, and schedules through their induced training memory.

