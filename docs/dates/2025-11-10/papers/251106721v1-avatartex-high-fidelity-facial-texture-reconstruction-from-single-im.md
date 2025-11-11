---
layout: default
title: AvatarTex: High-Fidelity Facial Texture Reconstruction from Single-Image Stylized Avatars
---

# AvatarTex: High-Fidelity Facial Texture Reconstruction from Single-Image Stylized Avatars
**arXiv**：[2511.06721v1](https://arxiv.org/abs/2511.06721) · [PDF](https://arxiv.org/pdf/2511.06721.pdf)  
**作者**：Yuda Qiu, Zitong Xiao, Yiwei Zuo, Zisheng Ye, Weikai Chen, Xiaoguang Han  

**一句话要点**：提出AvatarTex框架，从单图像重建高保真面部纹理，解决风格化与几何一致性问题。

**关键词**：面部纹理重建, 扩散模型, GAN优化, UV纹理合成, 风格化头像

## 3 点简述
- 核心问题：现有方法在风格化头像上缺乏多样数据集和几何一致性。
- 方法要点：采用三阶段扩散到GAN管道，结合扩散模型多样性和GAN结构约束。
- 实验或效果：引入TexHub数据集，实现多风格纹理重建的先进性能。

## 摘要（原文）

> We present AvatarTex, a high-fidelity facial texture reconstruction framework
> capable of generating both stylized and photorealistic textures from a single
> image. Existing methods struggle with stylized avatars due to the lack of
> diverse multi-style datasets and challenges in maintaining geometric
> consistency in non-standard textures. To address these limitations, AvatarTex
> introduces a novel three-stage diffusion-to-GAN pipeline. Our key insight is
> that while diffusion models excel at generating diversified textures, they lack
> explicit UV constraints, whereas GANs provide a well-structured latent space
> that ensures style and topology consistency. By integrating these strengths,
> AvatarTex achieves high-quality topology-aligned texture synthesis with both
> artistic and geometric coherence. Specifically, our three-stage pipeline first
> completes missing texture regions via diffusion-based inpainting, refines style
> and structure consistency using GAN-based latent optimization, and enhances
> fine details through diffusion-based repainting. To address the need for a
> stylized texture dataset, we introduce TexHub, a high-resolution collection of
> 20,000 multi-style UV textures with precise UV-aligned layouts. By leveraging
> TexHub and our structured diffusion-to-GAN pipeline, AvatarTex establishes a
> new state-of-the-art in multi-style facial texture reconstruction. TexHub will
> be released upon publication to facilitate future research in this field.

