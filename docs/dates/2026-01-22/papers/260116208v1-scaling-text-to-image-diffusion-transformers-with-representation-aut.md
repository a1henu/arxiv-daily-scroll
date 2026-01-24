---
layout: default
title: Scaling Text-to-Image Diffusion Transformers with Representation Autoencoders
---

# Scaling Text-to-Image Diffusion Transformers with Representation Autoencoders
**arXiv**：[2601.16208v1](https://arxiv.org/abs/2601.16208) · [PDF](https://arxiv.org/pdf/2601.16208.pdf)  
**作者**：Shengbang Tong, Boyang Zheng, Ziteng Wang, Bingda Tang, Nanye Ma, Ellis Brown, Jihan Yang, Rob Fergus, Yann LeCun, Saining Xie  

**一句话要点**：提出基于表示自编码器的扩散变换器，以简化框架并提升大规模文本到图像生成性能。

**关键词**：文本到图像生成, 表示自编码器, 扩散变换器, 大规模模型, 噪声调度, 多模态表示

## 3 点简述
- 研究表示自编码器框架在大规模自由文本到图像生成中的可扩展性。
- 通过实验简化框架，发现维度相关噪声调度是关键，而复杂架构在规模下效益可忽略。
- 在扩散变换器规模对比中，表示自编码器优于变分自编码器，收敛更快且生成质量更好。

## 摘要（原文）

> Representation Autoencoders (RAEs) have shown distinct advantages in diffusion modeling on ImageNet by training in high-dimensional semantic latent spaces. In this work, we investigate whether this framework can scale to large-scale, freeform text-to-image (T2I) generation. We first scale RAE decoders on the frozen representation encoder (SigLIP-2) beyond ImageNet by training on web, synthetic, and text-rendering data, finding that while scale improves general fidelity, targeted data composition is essential for specific domains like text. We then rigorously stress-test the RAE design choices originally proposed for ImageNet. Our analysis reveals that scaling simplifies the framework: while dimension-dependent noise scheduling remains critical, architectural complexities such as wide diffusion heads and noise-augmented decoding offer negligible benefits at scale Building on this simplified framework, we conduct a controlled comparison of RAE against the state-of-the-art FLUX VAE across diffusion transformer scales from 0.5B to 9.8B parameters. RAEs consistently outperform VAEs during pretraining across all model scales. Further, during finetuning on high-quality datasets, VAE-based models catastrophically overfit after 64 epochs, while RAE models remain stable through 256 epochs and achieve consistently better performance. Across all experiments, RAE-based diffusion models demonstrate faster convergence and better generation quality, establishing RAEs as a simpler and stronger foundation than VAEs for large-scale T2I generation. Additionally, because both visual understanding and generation can operate in a shared representation space, the multimodal model can directly reason over generated latents, opening new possibilities for unified models.

