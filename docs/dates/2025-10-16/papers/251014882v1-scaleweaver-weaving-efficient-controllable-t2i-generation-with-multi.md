---
layout: default
title: ScaleWeaver: Weaving Efficient Controllable T2I Generation with Multi-Scale Reference Attention
---

# ScaleWeaver: Weaving Efficient Controllable T2I Generation with Multi-Scale Reference Attention
**arXiv**：[2510.14882v1](https://arxiv.org/abs/2510.14882) · [PDF](https://arxiv.org/pdf/2510.14882.pdf)  
**作者**：Keli Liu, Zhendong Wang, Wengang Zhou, Shaodong Xu, Ruixiao Dong, Houqiang Li  

**一句话要点**：提出ScaleWeaver框架，通过多尺度参考注意力实现高效可控文本到图像生成。

**关键词**：文本到图像生成, 视觉自回归模型, 可控生成, 参考注意力, 参数高效微调, 多尺度处理

## 3 点简述
- 核心问题：视觉自回归模型中可控生成机制不足，难以实现精确灵活控制。
- 方法要点：引入参考注意力模块，优化MMDiT块，减少计算成本并稳定控制注入。
- 实验或效果：实验显示生成质量高、控制精确，效率优于基于扩散的方法。

## 摘要（原文）

> Text-to-image generation with visual autoregressive~(VAR) models has recently
> achieved impressive advances in generation fidelity and inference efficiency.
> While control mechanisms have been explored for diffusion models, enabling
> precise and flexible control within VAR paradigm remains underexplored. To
> bridge this critical gap, in this paper, we introduce ScaleWeaver, a novel
> framework designed to achieve high-fidelity, controllable generation upon
> advanced VAR models through parameter-efficient fine-tuning. The core module in
> ScaleWeaver is the improved MMDiT block with the proposed Reference Attention
> module, which efficiently and effectively incorporates conditional information.
> Different from MM Attention, the proposed Reference Attention module discards
> the unnecessary attention from image$\rightarrow$condition, reducing
> computational cost while stabilizing control injection. Besides, it
> strategically emphasizes parameter reuse, leveraging the capability of the VAR
> backbone itself with a few introduced parameters to process control
> information, and equipping a zero-initialized linear projection to ensure that
> control signals are incorporated effectively without disrupting the generative
> capability of the base model. Extensive experiments show that ScaleWeaver
> delivers high-quality generation and precise control while attaining superior
> efficiency over diffusion-based methods, making ScaleWeaver a practical and
> effective solution for controllable text-to-image generation within the visual
> autoregressive paradigm. Code and models will be released.

