---
layout: default
title: REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion
---

# REGLUE Your Latents with Global and Local Semantics for Entangled Diffusion
**arXiv**：[2512.16636v1](https://arxiv.org/abs/2512.16636) · [PDF](https://arxiv.org/pdf/2512.16636.pdf)  
**作者**：Giorgos Petsangourakis, Christos Sgouropoulos, Bill Psomas, Theodoros Giannakopoulos, Giorgos Sfikas, Ioannis Kakogeorgiou  

**一句话要点**：提出REGLUE框架，通过全局-局部语义与潜在编码的联合建模，提升潜在扩散模型的图像合成质量与训练效率。

**关键词**：潜在扩散模型, 语义注入, 全局-局部建模, 非线性压缩, 图像合成, 训练加速

## 3 点简述
- 潜在扩散模型因重建式去噪目标仅间接监督语义，导致高级语义学习缓慢，影响样本质量与训练时长。
- REGLUE统一建模VAE潜在编码、局部（补丁级）VFM语义和全局（图像级）[CLS]标记，利用轻量卷积语义压缩器非线性聚合多层VFM特征。
- 在ImageNet 256x256上，REGLUE持续改进FID并加速收敛，实验验证空间语义、非线性压缩及全局标记与外部对齐的重要性。

## 摘要（原文）

> Latent diffusion models (LDMs) achieve state-of-the-art image synthesis, yet their reconstruction-style denoising objective provides only indirect semantic supervision: high-level semantics emerge slowly, requiring longer training and limiting sample quality. Recent works inject semantics from Vision Foundation Models (VFMs) either externally via representation alignment or internally by jointly modeling only a narrow slice of VFM features inside the diffusion process, under-utilizing the rich, nonlinear, multi-layer spatial semantics available. We introduce REGLUE (Representation Entanglement with Global-Local Unified Encoding), a unified latent diffusion framework that jointly models (i) VAE image latents, (ii) compact local (patch-level) VFM semantics, and (iii) a global (image-level) [CLS] token within a single SiT backbone. A lightweight convolutional semantic compressor nonlinearly aggregates multi-layer VFM features into a low-dimensional, spatially structured representation, which is entangled with the VAE latents in the diffusion process. An external alignment loss further regularizes internal representations toward frozen VFM targets. On ImageNet 256x256, REGLUE consistently improves FID and accelerates convergence over SiT-B/2 and SiT-XL/2 baselines, as well as over REPA, ReDi, and REG. Extensive experiments show that (a) spatial VFM semantics are crucial, (b) non-linear compression is key to unlocking their full benefit, and (c) global tokens and external alignment act as complementary, lightweight enhancements within our global-local-latent joint modeling framework. The code is available at https://github.com/giorgospets/reglue .

