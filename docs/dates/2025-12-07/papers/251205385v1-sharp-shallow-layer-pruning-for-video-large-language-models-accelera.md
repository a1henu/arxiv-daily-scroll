---
layout: default
title: ShaRP: SHAllow-LayeR Pruning for Video Large Language Models Acceleration
---

# ShaRP: SHAllow-LayeR Pruning for Video Large Language Models Acceleration
**arXiv**：[2512.05385v1](https://arxiv.org/abs/2512.05385) · [PDF](https://arxiv.org/pdf/2512.05385.pdf)  
**作者**：Yingjie Xia, Tao Liu, Jinglei Shi, Qingsong Xie, Heng Guo, Jian Yang, Xi Wang  

**一句话要点**：提出ShaRP框架，通过改进注意力剪枝加速视频大语言模型推理

**关键词**：视频大语言模型, 注意力剪枝, 浅层加速, 令牌选择, 推理优化, 视频理解

## 3 点简述
- 核心问题：视频大语言模型在预填充阶段因视觉令牌过多导致高计算负载，浅层剪枝易致性能下降
- 方法要点：集成分段感知因果掩码、位置去偏和令牌去重，增强浅层令牌选择能力
- 实验或效果：在多个视频理解基准上保持竞争性能，支持高压缩率无需重训练

## 摘要（原文）

> Video Large Language Models (VLLMs) face the challenge of high computational load during the pre-filling stage due to the processing of an enormous number of visual tokens. Although attention-based pruning methods are widely used to accelerate inference, trials at early decoder layers often result in significant performance degradation, especially under high compression rates. We argue that while attention-based pruning inherently holds the potential to identify the most relevant visual tokens, its effectiveness in shallow decoder layers is limited by factors such as positional encoding bias and insufficient information interaction. In this paper, we propose an improved attention-based pruning framework, termed ShaRP, that integrates segment-aware causal masking, positional debiasing, and token deduplication for enhanced token selection. It enables effective pruning at shallow layers while maintaining stable performance under high compression rates without retraining. Extensive experiments demonstrate that ShaRP achieves competitive performance across multiple video understanding benchmarks, establishing a new paradigm for accelerating VLLM inference.

