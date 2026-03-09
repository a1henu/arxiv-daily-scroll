---
layout: default
title: Training-free Latent Inter-Frame Pruning with Attention Recovery
---

# Training-free Latent Inter-Frame Pruning with Attention Recovery
**arXiv**：[2603.05811v1](https://arxiv.org/abs/2603.05811) · [PDF](https://arxiv.org/pdf/2603.05811.pdf)  
**作者**：Dennis Menn, Yuedong Yang, Bokun Wang, Xiwen Wei, Mustafa Munir, Feng Liang, Radu Marculescu, Chenfeng Xu, Diana Marculescu  

**一句话要点**：提出无需训练的潜在帧间剪枝与注意力恢复框架，以提升视频生成效率

**关键词**：视频生成, 潜在剪枝, 注意力恢复, 计算效率, 无需训练

## 3 点简述
- 核心问题：视频生成模型计算延迟高，难以实时应用
- 方法要点：利用潜在补丁的时间冗余性，检测并跳过重复计算，通过注意力恢复机制减少视觉伪影
- 实验或效果：平均提升吞吐量1.45倍，在NVIDIA A6000上达到12.2 FPS，不损害生成质量

## 摘要（原文）

> Current video generation models suffer from high computational latency, making real-time applications prohibitively costly. In this paper, we address this limitation by exploiting the temporal redundancy inherent in video latent patches. To this end, we propose the Latent Inter-frame Pruning with Attention Recovery (LIPAR) framework, which detects and skips recomputing duplicated latent patches. Additionally, we introduce a novel Attention Recovery mechanism that approximates the attention values of pruned tokens, thereby removing visual artifacts arising from naively applying the pruning method. Empirically, our method increases video editing throughput by $1.45\times$, on average achieving 12.2 FPS on an NVIDIA A6000 compared to the baseline 8.4 FPS. The proposed method does not compromise generation quality and can be seamlessly integrated with the model without additional training. Our approach effectively bridges the gap between traditional compression algorithms and modern generative pipelines.

