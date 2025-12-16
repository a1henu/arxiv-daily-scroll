---
layout: default
title: Directional Textual Inversion for Personalized Text-to-Image Generation
---

# Directional Textual Inversion for Personalized Text-to-Image Generation
**arXiv**：[2512.13672v1](https://arxiv.org/abs/2512.13672) · [PDF](https://arxiv.org/pdf/2512.13672.pdf)  
**作者**：Kunhee Kim, NaHyeon Park, Kibeom Hong, Hyunjung Shim  

**一句话要点**：提出方向性文本反转以解决文本到图像个性化中嵌入范数膨胀导致的提示条件退化问题

**关键词**：文本到图像个性化, 方向性文本反转, 嵌入范数膨胀, 黎曼优化, 超球面参数化, 语义插值

## 3 点简述
- 核心问题：文本反转在复杂提示下失败，源于嵌入范数膨胀导致预归一化Transformer中提示条件退化
- 方法要点：固定嵌入范数，通过黎曼SGD在单位超球面上优化方向，采用冯·米塞斯-费舍尔先验简化梯度计算
- 实验或效果：在个性化任务中提升文本保真度，保持主体相似性，并支持概念间平滑语义插值

## 摘要（原文）

> Textual Inversion (TI) is an efficient approach to text-to-image personalization but often fails on complex prompts. We trace these failures to embedding norm inflation: learned tokens drift to out-of-distribution magnitudes, degrading prompt conditioning in pre-norm Transformers. Empirically, we show semantics are primarily encoded by direction in CLIP token space, while inflated norms harm contextualization; theoretically, we analyze how large magnitudes attenuate positional information and hinder residual updates in pre-norm blocks. We propose Directional Textual Inversion (DTI), which fixes the embedding magnitude to an in-distribution scale and optimizes only direction on the unit hypersphere via Riemannian SGD. We cast direction learning as MAP with a von Mises-Fisher prior, yielding a constant-direction prior gradient that is simple and efficient to incorporate. Across personalization tasks, DTI improves text fidelity over TI and TI-variants while maintaining subject similarity. Crucially, DTI's hyperspherical parameterization enables smooth, semantically coherent interpolation between learned concepts (slerp), a capability that is absent in standard TI. Our findings suggest that direction-only optimization is a robust and scalable path for prompt-faithful personalization.

