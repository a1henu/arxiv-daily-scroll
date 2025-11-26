---
layout: default
title: OmniRefiner: Reinforcement-Guided Local Diffusion Refinement
---

# OmniRefiner: Reinforcement-Guided Local Diffusion Refinement
**arXiv**：[2511.19990v1](https://arxiv.org/abs/2511.19990) · [PDF](https://arxiv.org/pdf/2511.19990.pdf)  
**作者**：Yaoli Liu, Ziheng Ouyang, Shengtao Lou, Yiren Song  

**一句话要点**：提出OmniRefiner框架以解决参考图像引导生成中细节丢失问题

**关键词**：参考图像引导生成, 扩散模型细化, 强化学习优化, 细节保留, 像素级一致性

## 3 点简述
- 核心问题：扩散模型在参考图像引导下难以保留细粒度视觉细节，VAE压缩导致纹理信息丢失
- 方法要点：采用两阶段参考驱动校正，结合扩散编辑和强化学习优化细节准确性与语义一致性
- 实验或效果：在参考引导恢复基准测试中，显著提升对齐度和细节保真度，优于开源和商业模型

## 摘要（原文）

> Reference-guided image generation has progressed rapidly, yet current diffusion models still struggle to preserve fine-grained visual details when refining a generated image using a reference. This limitation arises because VAE-based latent compression inherently discards subtle texture information, causing identity- and attribute-specific cues to vanish. Moreover, post-editing approaches that amplify local details based on existing methods often produce results inconsistent with the original image in terms of lighting, texture, or shape. To address this, we introduce \ourMthd{}, a detail-aware refinement framework that performs two consecutive stages of reference-driven correction to enhance pixel-level consistency. We first adapt a single-image diffusion editor by fine-tuning it to jointly ingest the draft image and the reference image, enabling globally coherent refinement while maintaining structural fidelity. We then apply reinforcement learning to further strengthen localized editing capability, explicitly optimizing for detail accuracy and semantic consistency. Extensive experiments demonstrate that \ourMthd{} significantly improves reference alignment and fine-grained detail preservation, producing faithful and visually coherent edits that surpass both open-source and commercial models on challenging reference-guided restoration benchmarks.

