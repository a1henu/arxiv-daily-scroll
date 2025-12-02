---
layout: default
title: Structured Spectral Reasoning for Frequency-Adaptive Multimodal Recommendation
---

# Structured Spectral Reasoning for Frequency-Adaptive Multimodal Recommendation
**arXiv**：[2512.01372v1](https://arxiv.org/abs/2512.01372) · [PDF](https://arxiv.org/pdf/2512.01372.pdf)  
**作者**：Wei Yang, Rui Zhong, Yiqun Chen, Chi Lu, Peng Jiang  

**一句话要点**：提出结构化谱推理框架以解决多模态推荐中的噪声与不一致问题

**关键词**：多模态推荐, 谱域分析, 图神经网络, 频率自适应, 对比学习, 鲁棒性提升

## 3 点简述
- 核心问题：多模态推荐面临模态噪声、语义不一致和图传播不稳定，导致泛化差。
- 方法要点：通过谱分解、谱带掩码、超谱推理和对齐正则化，实现频率自适应建模。
- 实验或效果：在真实基准上优于基线，尤其在稀疏和冷启动场景中提升鲁棒性。

## 摘要（原文）

> Multimodal recommendation aims to integrate collaborative signals with heterogeneous content such as visual and textual information, but remains challenged by modality-specific noise, semantic inconsistency, and unstable propagation over user-item graphs. These issues are often exacerbated by naive fusion or shallow modeling strategies, leading to degraded generalization and poor robustness. While recent work has explored the frequency domain as a lens to separate stable from noisy signals, most methods rely on static filtering or reweighting, lacking the ability to reason over spectral structure or adapt to modality-specific reliability. To address these challenges, we propose a Structured Spectral Reasoning (SSR) framework for frequency-aware multimodal recommendation. Our method follows a four-stage pipeline: (i) Decompose graph-based multimodal signals into spectral bands via graph-guided transformations to isolate semantic granularity; (ii) Modulate band-level reliability with spectral band masking, a training-time masking with a prediction-consistency objective that suppresses brittle frequency components; (iii) Fuse complementary frequency cues using hyperspectral reasoning with low-rank cross-band interaction; and (iv) Align modality-specific spectral features via contrastive regularization to promote semantic and structural consistency. Experiments on three real-world benchmarks show consistent gains over strong baselines, particularly under sparse and cold-start settings. Additional analyses indicate that structured spectral modeling improves robustness and provides clearer diagnostics of how different bands contribute to performance.

