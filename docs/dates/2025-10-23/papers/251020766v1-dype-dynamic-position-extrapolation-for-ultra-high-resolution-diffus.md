---
layout: default
title: DyPE: Dynamic Position Extrapolation for Ultra High Resolution Diffusion
---

# DyPE: Dynamic Position Extrapolation for Ultra High Resolution Diffusion
**arXiv**：[2510.20766v1](https://arxiv.org/abs/2510.20766) · [PDF](https://arxiv.org/pdf/2510.20766.pdf)  
**作者**：Noam Issachar, Guy Yariv, Sagie Benaim, Yossi Adi, Dani Lischinski, Raanan Fattal  

**一句话要点**：提出动态位置外推方法，实现预训练扩散模型在超高分辨率图像生成中的零成本扩展。

**关键词**：扩散模型, 位置编码, 超高分辨率生成, 训练免费方法, 图像合成

## 3 点简述
- 扩散变换器在超高分辨率训练中因自注意力二次缩放而成本高昂。
- DyPE 动态调整位置编码，匹配扩散过程频谱，无需额外训练。
- 实验显示，DyPE 在超高分辨率生成中提升性能，达到最先进保真度。

## 摘要（原文）

> Diffusion Transformer models can generate images with remarkable fidelity and
> detail, yet training them at ultra-high resolutions remains extremely costly
> due to the self-attention mechanism's quadratic scaling with the number of
> image tokens. In this paper, we introduce Dynamic Position Extrapolation
> (DyPE), a novel, training-free method that enables pre-trained diffusion
> transformers to synthesize images at resolutions far beyond their training
> data, with no additional sampling cost. DyPE takes advantage of the spectral
> progression inherent to the diffusion process, where low-frequency structures
> converge early, while high-frequencies take more steps to resolve.
> Specifically, DyPE dynamically adjusts the model's positional encoding at each
> diffusion step, matching their frequency spectrum with the current stage of the
> generative process. This approach allows us to generate images at resolutions
> that exceed the training resolution dramatically, e.g., 16 million pixels using
> FLUX. On multiple benchmarks, DyPE consistently improves performance and
> achieves state-of-the-art fidelity in ultra-high-resolution image generation,
> with gains becoming even more pronounced at higher resolutions. Project page is
> available at https://noamissachar.github.io/DyPE/.

