---
layout: default
title: DP$^2$O-SR: Direct Perceptual Preference Optimization for Real-World Image Super-Resolution
---

# DP$^2$O-SR: Direct Perceptual Preference Optimization for Real-World Image Super-Resolution
**arXiv**：[2510.18851v1](https://arxiv.org/abs/2510.18851) · [PDF](https://arxiv.org/pdf/2510.18851.pdf)  
**作者**：Rongyuan Wu, Lingchen Sun, Zhengqiang Zhang, Shihao Wang, Tianhe Wu, Qiaosi Yi, Shuai Li, Lei Zhang  

**一句话要点**：提出DP^2O-SR框架，优化真实世界图像超分辨率的感知质量。

**关键词**：图像超分辨率, 感知偏好优化, 扩散模型, 图像质量评估, 无监督学习

## 3 点简述
- 问题：T2I扩散模型随机性导致输出感知质量不稳定，影响真实世界超分辨率。
- 方法：结合全参考和无参考IQA模型构建混合奖励，无需人工标注优化感知偏好。
- 效果：在扩散和流式T2I骨干上实验，显著提升感知质量并泛化至真实基准。

## 摘要（原文）

> Benefiting from pre-trained text-to-image (T2I) diffusion models, real-world
> image super-resolution (Real-ISR) methods can synthesize rich and realistic
> details. However, due to the inherent stochasticity of T2I models, different
> noise inputs often lead to outputs with varying perceptual quality. Although
> this randomness is sometimes seen as a limitation, it also introduces a wider
> perceptual quality range, which can be exploited to improve Real-ISR
> performance. To this end, we introduce Direct Perceptual Preference
> Optimization for Real-ISR (DP$^2$O-SR), a framework that aligns generative
> models with perceptual preferences without requiring costly human annotations.
> We construct a hybrid reward signal by combining full-reference and
> no-reference image quality assessment (IQA) models trained on large-scale human
> preference datasets. This reward encourages both structural fidelity and
> natural appearance. To better utilize perceptual diversity, we move beyond the
> standard best-vs-worst selection and construct multiple preference pairs from
> outputs of the same model. Our analysis reveals that the optimal selection
> ratio depends on model capacity: smaller models benefit from broader coverage,
> while larger models respond better to stronger contrast in supervision.
> Furthermore, we propose hierarchical preference optimization, which adaptively
> weights training pairs based on intra-group reward gaps and inter-group
> diversity, enabling more efficient and stable learning. Extensive experiments
> across both diffusion- and flow-based T2I backbones demonstrate that DP$^2$O-SR
> significantly improves perceptual quality and generalizes well to real-world
> benchmarks.

