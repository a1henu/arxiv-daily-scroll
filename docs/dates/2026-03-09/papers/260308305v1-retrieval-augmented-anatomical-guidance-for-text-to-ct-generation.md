---
layout: default
title: Retrieval-Augmented Anatomical Guidance for Text-to-CT Generation
---

# Retrieval-Augmented Anatomical Guidance for Text-to-CT Generation
**arXiv**：[2603.08305v1](https://arxiv.org/abs/2603.08305) · [PDF](https://arxiv.org/pdf/2603.08305.pdf)  
**作者**：Daniele Molino, Camillo Maria Caruso, Paolo Soda, Valerio Guarrasi  

**一句话要点**：提出检索增强的解剖引导方法，以解决文本到CT生成中语义控制与解剖一致性的平衡问题。

**关键词**：文本到CT生成, 检索增强, 解剖引导, ControlNet, 医学图像合成, 3D视觉语言编码

## 3 点简述
- 核心问题：文本条件生成模型缺乏解剖引导，导致空间模糊或解剖不一致。
- 方法要点：通过3D视觉语言编码器检索语义相关临床案例，利用其解剖注释作为结构代理，注入ControlNet分支。
- 实验或效果：在CT-RATE数据集上，相比纯文本基线，提高了图像保真度和临床一致性，并实现空间可控性。

## 摘要（原文）

> Text-conditioned generative models for volumetric medical imaging provide semantic control but lack explicit anatomical guidance, often resulting in outputs that are spatially ambiguous or anatomically inconsistent. In contrast, structure-driven methods ensure strong anatomical consistency but typically assume access to ground-truth annotations, which are unavailable when the target image is to be synthesized. We propose a retrieval-augmented approach for Text-to-CT generation that integrates semantic and anatomical information under a realistic inference setting. Given a radiology report, our method retrieves a semantically related clinical case using a 3D vision-language encoder and leverages its associated anatomical annotation as a structural proxy. This proxy is injected into a text-conditioned latent diffusion model via a ControlNet branch, providing coarse anatomical guidance while maintaining semantic flexibility. Experiments on the CT-RATE dataset show that retrieval-augmented generation improves image fidelity and clinical consistency compared to text-only baselines, while additionally enabling explicit spatial controllability, a capability inherently absent in such approaches. Further analysis highlights the importance of retrieval quality, with semantically aligned proxies yielding consistent gains across all evaluation axes. This work introduces a principled and scalable mechanism to bridge semantic conditioning and anatomical plausibility in volumetric medical image synthesis. Code will be released.

