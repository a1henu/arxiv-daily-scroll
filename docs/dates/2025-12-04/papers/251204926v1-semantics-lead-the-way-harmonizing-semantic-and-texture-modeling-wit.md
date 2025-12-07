---
layout: default
title: Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion
---

# Semantics Lead the Way: Harmonizing Semantic and Texture Modeling with Asynchronous Latent Diffusion
**arXiv**：[2512.04926v1](https://arxiv.org/abs/2512.04926) · [PDF](https://arxiv.org/pdf/2512.04926.pdf)  
**作者**：Yueming Pan, Ruoyu Feng, Qi Dai, Yuqi Wang, Wenfeng Lin, Mingyu Guo, Chong Luo, Nanning Zheng  

**一句话要点**：提出语义优先扩散以异步建模语义与纹理，提升潜在扩散模型的生成质量与效率。

**关键词**：潜在扩散模型, 语义优先生成, 异步去噪, 图像生成, 语义建模, 纹理优化

## 3 点简述
- 潜在扩散模型生成中语义与纹理同步去噪，忽略语义先于纹理的顺序，影响生成效果。
- 构建复合潜在空间，通过专用语义VAE提取语义，并异步去噪语义与纹理，语义先行提供高层指导。
- 在ImageNet 256x256上实现FID 1.04，收敛速度提升达100倍，并改进现有方法如ReDi和VA-VAE。

## 摘要（原文）

> Latent Diffusion Models (LDMs) inherently follow a coarse-to-fine generation process, where high-level semantic structure is generated slightly earlier than fine-grained texture. This indicates the preceding semantics potentially benefit texture generation by providing a semantic anchor. Recent advances have integrated semantic priors from pretrained visual encoders to further enhance LDMs, yet they still denoise semantic and VAE-encoded texture synchronously, neglecting such ordering. Observing these, we propose Semantic-First Diffusion (SFD), a latent diffusion paradigm that explicitly prioritizes semantic formation. SFD first constructs composite latents by combining a compact semantic latent, which is extracted from a pretrained visual encoder via a dedicated Semantic VAE, with the texture latent. The core of SFD is to denoise the semantic and texture latents asynchronously using separate noise schedules: semantics precede textures by a temporal offset, providing clearer high-level guidance for texture refinement and enabling natural coarse-to-fine generation. On ImageNet 256x256 with guidance, SFD achieves FID 1.06 (LightningDiT-XL) and FID 1.04 (1.0B LightningDiT-XXL), while achieving up to 100x faster convergence than the original DiT. SFD also improves existing methods like ReDi and VA-VAE, demonstrating the effectiveness of asynchronous, semantics-led modeling. Project page and code: https://yuemingpan.github.io/SFD.github.io/.

