---
layout: default
title: ILRR: Inference-Time Steering Method for Masked Diffusion Language Models
---

# ILRR: Inference-Time Steering Method for Masked Diffusion Language Models
**arXiv**：[2601.21647v1](https://arxiv.org/abs/2601.21647) · [PDF](https://arxiv.org/pdf/2601.21647.pdf)  
**作者**：Eden Avrahami, Eliya Nachmani  

**一句话要点**：提出ILRR方法，通过动态对齐内部激活实现掩码扩散语言模型的推理时控制

**关键词**：推理时控制, 掩码扩散语言模型, 内部激活对齐, 无学习框架, 属性指导

## 3 点简述
- 核心问题：离散扩散语言模型缺乏有效的推理时控制机制，现有方法包括采样级指导或轨迹优化
- 方法要点：ILRR是无学习框架，使用单个参考序列在去噪过程中动态对齐生成序列的内部激活，可调节指导强度
- 实验或效果：在LLaDA和MDLM架构上，ILRR以较小计算开销提升属性准确率10%至60%，保持高生成质量

## 摘要（原文）

> Discrete Diffusion Language Models (DLMs) offer a promising non-autoregressive alternative for text generation, yet effective mechanisms for inference-time control remain relatively underexplored. Existing approaches include sampling-level guidance procedures or trajectory optimization mechanisms. In this work, we introduce Iterative Latent Representation Refinement (ILRR), a learning-free framework for steering DLMs using a single reference sequence. ILRR guides generation by dynamically aligning the internal activations of the generated sequence with those of a given reference throughout the denoising process. This approach captures and transfers high-level semantic properties, with a tunable steering scale enabling flexible control over attributes such as sentiment. We further introduce Spatially Modulated Steering, an extension that enables steering long texts using shorter references by regulating guidance intensity across the sequence. Empirically, we demonstrate that ILRR achieves effective attribute steering on LLaDA and MDLM architectures with a minor computational overhead, requiring only one additional parallel forward pass per denoising step. Under the same compute budget, ILRR improves attribute accuracy over comparable baselines by 10$\%$ to 60$\%$ points, while maintaining high generation quality.

