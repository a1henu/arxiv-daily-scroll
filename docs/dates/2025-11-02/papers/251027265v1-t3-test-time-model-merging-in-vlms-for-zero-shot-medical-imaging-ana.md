---
layout: default
title: T3: Test-Time Model Merging in VLMs for Zero-Shot Medical Imaging Analysis
---

# T3: Test-Time Model Merging in VLMs for Zero-Shot Medical Imaging Analysis
**arXiv**：[2510.27265v1](https://arxiv.org/abs/2510.27265) · [PDF](https://arxiv.org/pdf/2510.27265.pdf)  
**作者**：Raza Imam, Hu Wang, Dwarikanath Mahapatra, Mohammad Yaqub  

**一句话要点**：提出T3框架以解决医学影像中视觉语言模型在模态偏移下的性能问题

**关键词**：视觉语言模型, 模型融合, 医学影像分析, 零样本学习, 测试时适应

## 3 点简述
- 核心问题：预训练模型泛化性强但缺乏模态特异性，微调模型在模态偏移下性能下降
- 方法要点：基于Jensen-Shannon散度动态计算样本级或批次级模型融合系数
- 实验或效果：在跨模态评估中实现最高Top-1准确率和错误率降低，保持高效

## 摘要（原文）

> In medical imaging, vision-language models face a critical duality:
> pretrained networks offer broad robustness but lack subtle, modality-specific
> characteristics, while fine-tuned expert models achieve high in-distribution
> accuracy yet falter under modality shift. Existing model-merging techniques,
> designed for natural-image benchmarks, are simple and efficient but fail to
> deliver consistent gains across diverse medical modalities; their static
> interpolation limits reliability in varied clinical tasks. To address this, we
> introduce Test-Time Task adaptive merging (T^3), a backpropagation-free
> framework that computes per-sample interpolation coefficients via the
> Jensen-Shannon divergence between the two models' output distributions. T^3
> dynamically preserves local precision when models agree and defers to
> generalist robustness under drift. To overcome the inference costs of
> sample-wise merging, we further propose a batch-wise extension, T^3_B, that
> computes a merging coefficient across a batch of samples, dramatically reducing
> computational bottleneck. Recognizing the lack of a standardized
> medical-merging benchmark, we present a rigorous cross-evaluation protocol
> spanning in-domain, base-to-novel, and corruptions across four modalities.
> Empirically, T^3 sets new state-of-the-art in Top-1 accuracy and error
> reduction, outperforming strong baselines while maintaining efficiency, paving
> the way for adaptive MVLM deployment in clinical settings. Our code is
> available at https://github.com/Razaimam45/TCube.

