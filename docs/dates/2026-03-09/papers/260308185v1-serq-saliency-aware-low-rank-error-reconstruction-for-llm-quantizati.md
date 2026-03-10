---
layout: default
title: SERQ: Saliency-Aware Low-Rank Error Reconstruction for LLM Quantization
---

# SERQ: Saliency-Aware Low-Rank Error Reconstruction for LLM Quantization
**arXiv**：[2603.08185v1](https://arxiv.org/abs/2603.08185) · [PDF](https://arxiv.org/pdf/2603.08185.pdf)  
**作者**：Yeonsik Park, Hyeonseong Kim, Seungkyu Choi  

**一句话要点**：提出SERQ方法，通过显著性感知低秩误差重构提升低比特LLM量化精度

**关键词**：大语言模型量化, 低秩误差重构, 显著性感知, 后训练量化, 低比特推理

## 3 点简述
- 核心问题：现有低秩误差重构方法在W4A4设置下精度下降严重，且依赖顺序因子导致推理效率受限
- 方法要点：采用单低秩补偿矩阵，通过静态激活展平、显著性感知误差重构和离线权重置换三阶段联合缓解激活与权重量化误差
- 实验或效果：在W4A4和W4A8设置下优于先前方法，精度超越基于旋转的W4A4方法，并显著降低校准复杂度

## 摘要（原文）

> Post-training quantization (PTQ) has emerged as a prevailing technique for deploying large language models (LLMs) efficiently in terms of both memory and computation, across edge devices and server platforms. Existing PTQ methods primarily aim to reduce precision in weights and activations by mitigating quantization errors caused by channel-wise outlier activations (e.g., pre-quantization scaling, online transformations, or low-rank error reconstruction). Among these approaches, error reconstruction with low-rank adaptation (LoRA) has proven particularly effective, as it introduces a lightweight auxiliary computation path without requiring heavy optimization or additional online layers. However, prior studies reveal severe accuracy degradation under W4A4 settings, and conventional low-rank adaptations rely on two sequential factors, necessitating intermediate quantization during inference and thereby limiting low-precision efficiency. In this work, we propose SERQ, a saliency-aware error reconstruction method for low-bit LLM inference that employs a single low-rank compensation matrix. SERQ preserves efficient 4-bit matrix multiplication in linear layers by jointly mitigating quantization errors arising from both activation and weight saliency through three stages: (1) static activation flattening, (2) saliency-aware error reconstruction, and (3) offline weight permutation. The method incurs additional computation only for low-rank error reconstruction via a single decomposition, while all other operations are performed offline, thereby keeping latency overhead minimal. Empirically, SERQ outperforms prior error reconstruction methods under both W4A8 and W4A4 settings, and achieves higher accuracy than state-of-the-art rotation-based W4A4 approaches, while substantially reducing calibration complexity.

