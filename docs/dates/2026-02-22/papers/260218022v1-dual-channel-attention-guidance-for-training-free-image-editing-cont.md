---
layout: default
title: Dual-Channel Attention Guidance for Training-Free Image Editing Control in Diffusion Transformers
---

# Dual-Channel Attention Guidance for Training-Free Image Editing Control in Diffusion Transformers
**arXiv**：[2602.18022v1](https://arxiv.org/abs/2602.18022) · [PDF](https://arxiv.org/pdf/2602.18022.pdf)  
**作者**：Guandong Li, Mengxia Ye  

**一句话要点**：提出双通道注意力引导框架，以在扩散Transformer中实现无需训练的图像编辑强度控制。

**关键词**：扩散Transformer, 图像编辑, 注意力机制, 无需训练控制, 双通道引导, 编辑保真度

## 3 点简述
- 核心问题：现有注意力操纵方法仅关注Key空间，未利用Value空间进行特征聚合控制。
- 方法要点：基于Key和Value投影的偏置-增量结构，同时操纵Key和Value通道，实现粗粒度与细粒度编辑控制。
- 实验或效果：在PIE-Bench基准测试中，DCAG在所有保真度指标上优于仅Key引导方法，尤其在局部编辑任务中提升显著。

## 摘要（原文）

> Training-free control over editing intensity is a critical requirement for diffusion-based image editing models built on the Diffusion Transformer (DiT) architecture. Existing attention manipulation methods focus exclusively on the Key space to modulate attention routing, leaving the Value space -- which governs feature aggregation -- entirely unexploited. In this paper, we first reveal that both Key and Value projections in DiT's multi-modal attention layers exhibit a pronounced bias-delta structure, where token embeddings cluster tightly around a layer-specific bias vector. Building on this observation, we propose Dual-Channel Attention Guidance (DCAG), a training-free framework that simultaneously manipulates both the Key channel (controlling where to attend) and the Value channel (controlling what to aggregate). We provide a theoretical analysis showing that the Key channel operates through the nonlinear softmax function, acting as a coarse control knob, while the Value channel operates through linear weighted summation, serving as a fine-grained complement. Together, the two-dimensional parameter space $(δ_k, δ_v)$ enables more precise editing-fidelity trade-offs than any single-channel method. Extensive experiments on the PIE-Bench benchmark (700 images, 10 editing categories) demonstrate that DCAG consistently outperforms Key-only guidance across all fidelity metrics, with the most significant improvements observed in localized editing tasks such as object deletion (4.9% LPIPS reduction) and object addition (3.2% LPIPS reduction).

