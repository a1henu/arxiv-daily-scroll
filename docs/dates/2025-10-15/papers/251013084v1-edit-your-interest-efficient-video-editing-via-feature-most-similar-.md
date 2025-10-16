---
layout: default
title: Edit-Your-Interest: Efficient Video Editing via Feature Most-Similar Propagation
---

# Edit-Your-Interest: Efficient Video Editing via Feature Most-Similar Propagation
**arXiv**：[2510.13084v1](https://arxiv.org/abs/2510.13084) · [PDF](https://arxiv.org/pdf/2510.13084.pdf)  
**作者**：Yi Zuo, Zitao Wang, Lingling Li, Xu Liu, Fang Liu, Licheng Jiao  

**一句话要点**：提出Edit-Your-Interest方法以高效实现零样本视频编辑

**关键词**：视频编辑, 扩散模型, 特征传播, 时空一致性, 零样本学习, 计算效率

## 3 点简述
- 现有视频编辑方法计算开销高、内存消耗大，且易产生时间不一致性和伪影
- 引入时空特征记忆库和特征最相似传播，缓存并传播关键特征以提升效率与一致性
- 实验表明该方法在效率和视觉保真度上优于现有先进方法，验证其有效性

## 摘要（原文）

> Text-to-image (T2I) diffusion models have recently demonstrated significant
> progress in video editing.
>   However, existing video editing methods are severely limited by their high
> computational overhead and memory consumption.
>   Furthermore, these approaches often sacrifice visual fidelity, leading to
> undesirable temporal inconsistencies and artifacts such as blurring and
> pronounced mosaic-like patterns.
>   We propose Edit-Your-Interest, a lightweight, text-driven, zero-shot video
> editing method.
>   Edit-Your-Interest introduces a spatio-temporal feature memory to cache
> features from previous frames, significantly reducing computational overhead
> compared to full-sequence spatio-temporal modeling approaches.
>   Specifically, we first introduce a Spatio-Temporal Feature Memory bank (SFM),
> which is designed to efficiently cache and retain the crucial image tokens
> processed by spatial attention.
>   Second, we propose the Feature Most-Similar Propagation (FMP) method. FMP
> propagates the most relevant tokens from previous frames to subsequent ones,
> preserving temporal consistency.
>   Finally, we introduce an SFM update algorithm that continuously refreshes the
> cached features, ensuring their long-term relevance and effectiveness
> throughout the video sequence.
>   Furthermore, we leverage cross-attention maps to automatically extract masks
> for the instances of interest.
>   These masks are seamlessly integrated into the diffusion denoising process,
> enabling fine-grained control over target objects and allowing
> Edit-Your-Interest to perform highly accurate edits while robustly preserving
> the background integrity.
>   Extensive experiments decisively demonstrate that the proposed
> Edit-Your-Interest outperforms state-of-the-art methods in both efficiency and
> visual fidelity, validating its superior effectiveness and practicality.

