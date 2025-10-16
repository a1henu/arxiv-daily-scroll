---
layout: default
title: Generating healthy counterfactuals with denoising diffusion bridge models
---

# Generating healthy counterfactuals with denoising diffusion bridge models
**arXiv**：[2510.13684v1](https://arxiv.org/abs/2510.13684) · [PDF](https://arxiv.org/pdf/2510.13684.pdf)  
**作者**：Ana Lawry Aguila, Peirong Liu, Marina Crespo Aguirre, Juan Eugenio Iglesias  

**一句话要点**：提出基于去噪扩散桥模型的健康反事实生成方法，以改进医学图像异常检测。

**关键词**：医学图像生成, 反事实生成, 去噪扩散模型, 异常检测, 图像分割

## 3 点简述
- 核心问题：现有方法难以平衡异常移除与个体解剖特征保留。
- 方法要点：使用扩散桥模型，结合健康与合成病理图像指导生成。
- 实验或效果：在分割和异常检测任务中优于先前扩散模型和监督方法。

## 摘要（原文）

> Generating healthy counterfactuals from pathological images holds significant
> promise in medical imaging, e.g., in anomaly detection or for application of
> analysis tools that are designed for healthy scans. These counterfactuals
> should represent what a patient's scan would plausibly look like in the absence
> of pathology, preserving individual anatomical characteristics while modifying
> only the pathological regions. Denoising diffusion probabilistic models (DDPMs)
> have become popular methods for generating healthy counterfactuals of pathology
> data. Typically, this involves training on solely healthy data with the
> assumption that a partial denoising process will be unable to model disease
> regions and will instead reconstruct a closely matched healthy counterpart.
> More recent methods have incorporated synthetic pathological images to better
> guide the diffusion process. However, it remains challenging to guide the
> generative process in a way that effectively balances the removal of anomalies
> with the retention of subject-specific features. To solve this problem, we
> propose a novel application of denoising diffusion bridge models (DDBMs) -
> which, unlike DDPMs, condition the diffusion process not only on the initial
> point (i.e., the healthy image), but also on the final point (i.e., a
> corresponding synthetically generated pathological image). Treating the
> pathological image as a structurally informative prior enables us to generate
> counterfactuals that closely match the patient's anatomy while selectively
> removing pathology. The results show that our DDBM outperforms previously
> proposed diffusion models and fully supervised approaches at segmentation and
> anomaly detection tasks.

