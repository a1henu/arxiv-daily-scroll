---
layout: default
title: EditInfinity: Image Editing with Binary-Quantized Generative Models
---

# EditInfinity: Image Editing with Binary-Quantized Generative Models
**arXiv**：[2510.20217v1](https://arxiv.org/abs/2510.20217) · [PDF](https://arxiv.org/pdf/2510.20217.pdf)  
**作者**：Jiahuan Wang, Yuxin Chen, Jun Yu, Guangming Lu, Wenjie Pei  

**一句话要点**：提出EditInfinity方法，利用二进制量化生成模型解决图像编辑中的反演误差问题。

**关键词**：图像编辑, 生成模型, 二进制量化, 图像反演, 文本驱动编辑

## 3 点简述
- 核心问题：扩散模型图像反演因缺乏中间步骤精确监督而产生近似误差，限制编辑性能。
- 方法要点：基于Infinity模型，实现精确图像反演，集成文本提示修正和风格保留机制。
- 实验或效果：在PIE-Bench基准测试中，优于现有扩散基线，支持添加、更改和删除操作。

## 摘要（原文）

> Adapting pretrained diffusion-based generative models for text-driven image
> editing with negligible tuning overhead has demonstrated remarkable potential.
> A classical adaptation paradigm, as followed by these methods, first infers the
> generative trajectory inversely for a given source image by image inversion,
> then performs image editing along the inferred trajectory guided by the target
> text prompts. However, the performance of image editing is heavily limited by
> the approximation errors introduced during image inversion by diffusion models,
> which arise from the absence of exact supervision in the intermediate
> generative steps. To circumvent this issue, we investigate the
> parameter-efficient adaptation of VQ-based generative models for image editing,
> and leverage their inherent characteristic that the exact intermediate
> quantized representations of a source image are attainable, enabling more
> effective supervision for precise image inversion. Specifically, we propose
> \emph{EditInfinity}, which adapts \emph{Infinity}, a binary-quantized
> generative model, for image editing. We propose an efficient yet effective
> image inversion mechanism that integrates text prompting rectification and
> image style preservation, enabling precise image inversion. Furthermore, we
> devise a holistic smoothing strategy which allows our \emph{EditInfinity} to
> perform image editing with high fidelity to source images and precise semantic
> alignment to the text prompts. Extensive experiments on the PIE-Bench benchmark
> across "add", "change", and "delete" editing operations, demonstrate the
> superior performance of our model compared to state-of-the-art diffusion-based
> baselines. Code available at: https://github.com/yx-chen-ust/EditInfinity.

