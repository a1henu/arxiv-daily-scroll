---
layout: default
title: Diffusion-Guided Mask-Consistent Paired Mixing for Endoscopic Image Segmentation
---

# Diffusion-Guided Mask-Consistent Paired Mixing for Endoscopic Image Segmentation
**arXiv**：[2511.03219v1](https://arxiv.org/abs/2511.03219) · [PDF](https://arxiv.org/pdf/2511.03219.pdf)  
**作者**：Pengyu Jie, Wanquan Liu, Rui He, Yihui Wen, Deyu Meng, Chenqiang Gao  

**一句话要点**：提出扩散引导掩码一致配对混合方法以增强内窥镜图像分割

**关键词**：内窥镜图像分割, 数据增强, 扩散模型, 掩码一致性, 自适应学习

## 3 点简述
- 样本混合导致掩码错位和软标签模糊，扩散合成引入域偏移。
- 使用相同掩码生成合成图像对，进行图像外观混合，保持硬掩码监督。
- 在多个数据集上实现最先进分割性能，提升鲁棒性和泛化能力。

## 摘要（原文）

> Augmentation for dense prediction typically relies on either sample mixing or
> generative synthesis. Mixing improves robustness but misaligned masks yield
> soft label ambiguity. Diffusion synthesis increases apparent diversity but,
> when trained as common samples, overlooks the structural benefit of mask
> conditioning and introduces synthetic-real domain shift. We propose a paired,
> diffusion-guided paradigm that fuses the strengths of both. For each real
> image, a synthetic counterpart is generated under the same mask and the pair is
> used as a controllable input for Mask-Consistent Paired Mixing (MCPMix), which
> mixes only image appearance while supervision always uses the original hard
> mask. This produces a continuous family of intermediate samples that smoothly
> bridges synthetic and real appearances under shared geometry, enlarging
> diversity without compromising pixel-level semantics. To keep learning aligned
> with real data, Real-Anchored Learnable Annealing (RLA) adaptively adjusts the
> mixing strength and the loss weight of mixed samples over training, gradually
> re-anchoring optimization to real data and mitigating distributional bias.
> Across Kvasir-SEG, PICCOLO, CVC-ClinicDB, a private NPC-LES cohort, and ISIC
> 2017, the approach achieves state-of-the-art segmentation performance and
> consistent gains over baselines. The results show that combining
> label-preserving mixing with diffusion-driven diversity, together with adaptive
> re-anchoring, yields robust and generalizable endoscopic segmentation.

