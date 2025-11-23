---
layout: default
title: Target Refocusing via Attention Redistribution for Open-Vocabulary Semantic Segmentation: An Explainability Perspective
---

# Target Refocusing via Attention Redistribution for Open-Vocabulary Semantic Segmentation: An Explainability Perspective
**arXiv**：[2511.16170v1](https://arxiv.org/abs/2511.16170) · [PDF](https://arxiv.org/pdf/2511.16170.pdf)  
**作者**：Jiahao Li, Yang Lu, Yachao Zhang, Yong Xie, Fangyong Wang, Yuan Xie, Yanyun Qu  

**一句话要点**：提出RF-CLIP以解决开放词汇语义分割中CLIP注意力分散问题

**关键词**：开放词汇语义分割, 注意力机制, CLIP模型, 密集预测, 多模态对齐

## 3 点简述
- 核心问题：CLIP在密集预测中注意力分散，资源浪费于无关token
- 方法要点：训练无关方法，重定向注意力至目标区域，提升对齐粒度
- 实验或效果：在八个基准上实现SOTA性能，保持高效推理

## 摘要（原文）

> Open-vocabulary semantic segmentation (OVSS) employs pixel-level vision-language alignment to associate category-related prompts with corresponding pixels. A key challenge is enhancing the multimodal dense prediction capability, specifically this pixel-level multimodal alignment. Although existing methods achieve promising results by leveraging CLIP's vision-language alignment, they rarely investigate the performance boundaries of CLIP for dense prediction from an interpretability mechanisms perspective. In this work, we systematically investigate CLIP's internal mechanisms and identify a critical phenomenon: analogous to human distraction, CLIP diverts significant attention resources from target regions to irrelevant tokens. Our analysis reveals that these tokens arise from dimension-specific over-activation; filtering them enhances CLIP's dense prediction performance. Consequently, we propose ReFocusing CLIP (RF-CLIP), a training-free approach that emulates human distraction-refocusing behavior to redirect attention from distraction tokens back to target regions, thereby refining CLIP's multimodal alignment granularity. Our method achieves SOTA performance on eight benchmarks while maintaining high inference efficiency.

