---
layout: default
title: D2D: Detector-to-Differentiable Critic for Improved Numeracy in Text-to-Image Generation
---

# D2D: Detector-to-Differentiable Critic for Improved Numeracy in Text-to-Image Generation
**arXiv**：[2510.19278v1](https://arxiv.org/abs/2510.19278) · [PDF](https://arxiv.org/pdf/2510.19278.pdf)  
**作者**：Nobline Yoo, Olga Russakovsky, Ye Zhu  

**一句话要点**：提出D2D框架将非可微检测器转化为可微批评器，以提升文本到图像生成中的对象计数准确性

**关键词**：文本到图像生成, 对象计数, 可微批评器, 检测器转换, 扩散模型优化

## 3 点简述
- 核心问题：文本到图像扩散模型在生成指定对象数量时存在困难，现有方法受限于可微性而无法使用高性能检测器
- 方法要点：设计自定义激活函数将检测器输出转换为软二进制指示器，用于在推理时优化噪声先验
- 实验或效果：在多个基准测试中显著提升计数准确率，最高达13.7%，且图像质量和计算开销影响小

## 摘要（原文）

> Text-to-image (T2I) diffusion models have achieved strong performance in
> semantic alignment, yet they still struggle with generating the correct number
> of objects specified in prompts. Existing approaches typically incorporate
> auxiliary counting networks as external critics to enhance numeracy. However,
> since these critics must provide gradient guidance during generation, they are
> restricted to regression-based models that are inherently differentiable, thus
> excluding detector-based models with superior counting ability, whose
> count-via-enumeration nature is non-differentiable. To overcome this
> limitation, we propose Detector-to-Differentiable (D2D), a novel framework that
> transforms non-differentiable detection models into differentiable critics,
> thereby leveraging their superior counting ability to guide numeracy
> generation. Specifically, we design custom activation functions to convert
> detector logits into soft binary indicators, which are then used to optimize
> the noise prior at inference time with pre-trained T2I models. Our extensive
> experiments on SDXL-Turbo, SD-Turbo, and Pixart-DMD across four benchmarks of
> varying complexity (low-density, high-density, and multi-object scenarios)
> demonstrate consistent and substantial improvements in object counting accuracy
> (e.g., boosting up to 13.7% on D2D-Small, a 400-prompt, low-density benchmark),
> with minimal degradation in overall image quality and computational overhead.

