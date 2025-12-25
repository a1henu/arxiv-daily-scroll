---
layout: default
title: Fast SAM2 with Text-Driven Token Pruning
---

# Fast SAM2 with Text-Driven Token Pruning
**arXiv**：[2512.21333v1](https://arxiv.org/abs/2512.21333) · [PDF](https://arxiv.org/pdf/2512.21333.pdf)  
**作者**：Avilasha Mandal, Chaoning Zhang, Fachrina Dewi Puspitasari, Xudong Wang, Jiaquan Zhang, Caiyan Qin, Guoqing Wang, Yang Yang, Heng Tao Shen  

**一句话要点**：提出文本引导的令牌剪枝框架以提升SAM2视频分割效率

**关键词**：视频对象分割, 令牌剪枝, 文本引导, 计算效率, SAM2模型

## 3 点简述
- SAM2视频分割因密集视觉令牌处理导致计算和内存成本高
- 方法在视觉编码后基于文本描述和不确定性剪枝令牌，减少冗余计算
- 实验显示推理速度提升42.50%，GPU内存使用降低37.41%，性能保持

## 摘要（原文）

> Segment Anything Model 2 (SAM2), a vision foundation model has significantly advanced in prompt-driven video object segmentation, yet their practical deployment remains limited by the high computational and memory cost of processing dense visual tokens across time. The SAM2 pipelines typically propagate all visual tokens produced by the image encoder through downstream temporal reasoning modules, regardless of their relevance to the target object, resulting in reduced scalability due to quadratic memory attention overhead. In this work, we introduce a text-guided token pruning framework that improves inference efficiency by selectively reducing token density prior to temporal propagation, without modifying the underlying segmentation architecture. Operating after visual encoding and before memory based propagation, our method ranks tokens using a lightweight routing mechanism that integrates local visual context, semantic relevance derived from object-centric textual descriptions (either user-provided or automatically generated), and uncertainty cues that help preserve ambiguous or boundary critical regions. By retaining only the most informative tokens for downstream processing, the proposed approach reduces redundant computation while maintaining segmentation fidelity. Extensive experiments across multiple challenging video segmentation benchmarks demonstrate that post-encoder token pruning provides a practical and effective pathway to efficient, prompt-aware video segmentation, achieving up to 42.50 percent faster inference and 37.41 percent lower GPU memory usage compared to the unpruned baseline SAM2, while preserving competitive J and F performance. These results highlight the potential of early token selection to improve the scalability of transformer-based video segmentation systems for real-time and resource-constrained applications.

