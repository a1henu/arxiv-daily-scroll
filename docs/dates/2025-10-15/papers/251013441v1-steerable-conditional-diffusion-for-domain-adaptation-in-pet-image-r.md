---
layout: default
title: Steerable Conditional Diffusion for Domain Adaptation in PET Image Reconstruction
---

# Steerable Conditional Diffusion for Domain Adaptation in PET Image Reconstruction
**arXiv**：[2510.13441v1](https://arxiv.org/abs/2510.13441) · [PDF](https://arxiv.org/pdf/2510.13441.pdf)  
**作者**：George Webber, Alexander Hammers, Andrew P. King, Andrew J. Reader  

**一句话要点**：提出可引导条件扩散方法以解决PET图像重建中的域适应问题

**关键词**：PET图像重建, 扩散模型, 域适应, 低秩适应, 图像伪影抑制

## 3 点简述
- 核心问题：扩散模型在PET图像重建中面临域偏移，导致伪影
- 方法要点：集成可引导条件扩散与似然调度扩散框架，使用LoRA实时对齐目标域
- 实验或效果：在合成脑模型上验证，抑制伪影，优于OSEM和基线扩散模型

## 摘要（原文）

> Diffusion models have recently enabled state-of-the-art reconstruction of
> positron emission tomography (PET) images while requiring only image training
> data. However, domain shift remains a key concern for clinical adoption: priors
> trained on images from one anatomy, acquisition protocol or pathology may
> produce artefacts on out-of-distribution data. We propose integrating steerable
> conditional diffusion (SCD) with our previously-introduced likelihood-scheduled
> diffusion (PET-LiSch) framework to improve the alignment of the diffusion
> model's prior to the target subject. At reconstruction time, for each diffusion
> step, we use low-rank adaptation (LoRA) to align the diffusion model prior with
> the target domain on the fly. Experiments on realistic synthetic 2D brain
> phantoms demonstrate that our approach suppresses hallucinated artefacts under
> domain shift, i.e. when our diffusion model is trained on perturbed images and
> tested on normal anatomy, our approach suppresses the hallucinated structure,
> outperforming both OSEM and diffusion model baselines qualitatively and
> quantitatively. These results provide a proof-of-concept that steerable priors
> can mitigate domain shift in diffusion-based PET reconstruction and motivate
> future evaluation on real data.

