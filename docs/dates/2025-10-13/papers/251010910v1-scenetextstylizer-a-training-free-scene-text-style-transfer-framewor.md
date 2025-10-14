---
layout: default
title: SceneTextStylizer: A Training-Free Scene Text Style Transfer Framework with Diffusion Model
---

# SceneTextStylizer: A Training-Free Scene Text Style Transfer Framework with Diffusion Model
**arXiv**：[2510.10910v1](https://arxiv.org/abs/2510.10910) · [PDF](https://arxiv.org/pdf/2510.10910.pdf)  
**作者**：Honghui Yuan, Keiji Yanai  

**一句话要点**：提出SceneTextStylizer框架，实现无训练场景文本风格迁移

**关键词**：场景文本编辑, 扩散模型, 风格迁移, 无训练框架, 傅里叶变换

## 3 点简述
- 核心问题：现有方法难以对场景文本进行灵活、局部化风格编辑
- 方法要点：结合扩散模型反演、自注意力和傅里叶变换实现风格特征注入与增强
- 实验或效果：在视觉保真度和文本可读性上优于现有先进方法

## 摘要（原文）

> With the rapid development of diffusion models, style transfer has made
> remarkable progress. However, flexible and localized style editing for scene
> text remains an unsolved challenge. Although existing scene text editing
> methods have achieved text region editing, they are typically limited to
> content replacement and simple styles, which lack the ability of free-style
> transfer. In this paper, we introduce SceneTextStylizer, a novel training-free
> diffusion-based framework for flexible and high-fidelity style transfer of text
> in scene images. Unlike prior approaches that either perform global style
> transfer or focus solely on textual content modification, our method enables
> prompt-guided style transformation specifically for text regions, while
> preserving both text readability and stylistic consistency. To achieve this, we
> design a feature injection module that leverages diffusion model inversion and
> self-attention to transfer style features effectively. Additionally, a region
> control mechanism is introduced by applying a distance-based changing mask at
> each denoising step, enabling precise spatial control. To further enhance
> visual quality, we incorporate a style enhancement module based on the Fourier
> transform to reinforce stylistic richness. Extensive experiments demonstrate
> that our method achieves superior performance in scene text style
> transformation, outperforming existing state-of-the-art methods in both visual
> fidelity and text preservation.

