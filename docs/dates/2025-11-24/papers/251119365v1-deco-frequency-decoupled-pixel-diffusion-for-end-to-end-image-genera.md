---
layout: default
title: DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation
---

# DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation
**arXiv**：[2511.19365v1](https://arxiv.org/abs/2511.19365) · [PDF](https://arxiv.org/pdf/2511.19365.pdf)  
**作者**：Zehong Ma, Longhui Wei, Shuai Wang, Shiliang Zhang, Qi Tian  

**一句话要点**：提出频率解耦像素扩散框架以提升端到端图像生成效率

**关键词**：像素扩散, 频率解耦, 端到端图像生成, 扩散变换器, 流匹配损失

## 3 点简述
- 现有像素扩散模型在单一DiT中建模高低频信号，导致训练和推理缓慢
- 使用轻量像素解码器生成高频细节，DiT专注低频语义，并引入频率感知流匹配损失
- 在ImageNet上FID达1.62（256x256），文本到图像模型在GenEval得分0.86领先

## 摘要（原文）

> Pixel diffusion aims to generate images directly in pixel space in an end-to-end fashion. This approach avoids the limitations of VAE in the two-stage latent diffusion, offering higher model capacity. Existing pixel diffusion models suffer from slow training and inference, as they usually model both high-frequency signals and low-frequency semantics within a single diffusion transformer (DiT). To pursue a more efficient pixel diffusion paradigm, we propose the frequency-DeCoupled pixel diffusion framework. With the intuition to decouple the generation of high and low frequency components, we leverage a lightweight pixel decoder to generate high-frequency details conditioned on semantic guidance from the DiT. This thus frees the DiT to specialize in modeling low-frequency semantics. In addition, we introduce a frequency-aware flow-matching loss that emphasizes visually salient frequencies while suppressing insignificant ones. Extensive experiments show that DeCo achieves superior performance among pixel diffusion models, attaining FID of 1.62 (256x256) and 2.22 (512x512) on ImageNet, closing the gap with latent diffusion methods. Furthermore, our pretrained text-to-image model achieves a leading overall score of 0.86 on GenEval in system-level comparison. Codes are publicly available at https://github.com/Zehong-Ma/DeCo.

