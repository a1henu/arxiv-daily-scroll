---
layout: default
title: Lesion-Aware Post-Training of Latent Diffusion Models for Synthesizing Diffusion MRI from CT Perfusion
---

# Lesion-Aware Post-Training of Latent Diffusion Models for Synthesizing Diffusion MRI from CT Perfusion
**arXiv**：[2510.09056v1](https://arxiv.org/abs/2510.09056) · [PDF](https://arxiv.org/pdf/2510.09056.pdf)  
**作者**：Junhyeok Lee, Hyunwoong Kim, Hyungjin Chung, Heeseong Eom, Joon Jang, Chul-Ho Sohn, Kyu Sung Choi  
**一句话要点**：提出病灶感知后训练框架，以提升CT到MRI转换中病灶重建精度

**关键词**：潜在扩散模型, 医学图像转换, 病灶重建, 后训练框架, CT到MRI合成

## 3 点简述
- 潜在扩散模型在医学图像转换中可能丢失关键像素细节，影响病灶重建
- 引入病灶感知像素空间目标，增强整体图像质量和病灶描绘精度
- 在急性缺血性卒中数据集上验证，合成DWI和ADC图像优于现有方法

## 摘要（原文）

> Image-to-Image translation models can help mitigate various challenges
> inherent to medical image acquisition. Latent diffusion models (LDMs) leverage
> efficient learning in compressed latent space and constitute the core of
> state-of-the-art generative image models. However, this efficiency comes with a
> trade-off, potentially compromising crucial pixel-level detail essential for
> high-fidelity medical images. This limitation becomes particularly critical
> when generating clinically significant structures, such as lesions, which often
> occupy only a small portion of the image. Failure to accurately reconstruct
> these regions can severely impact diagnostic reliability and clinical
> decision-making. To overcome this limitation, we propose a novel post-training
> framework for LDMs in medical image-to-image translation by incorporating
> lesion-aware medical pixel space objectives. This approach is essential, as it
> not only enhances overall image quality but also improves the precision of
> lesion delineation. We evaluate our framework on brain CT-to-MRI translation in
> acute ischemic stroke patients, where early and accurate diagnosis is critical
> for optimal treatment selection and improved patient outcomes. While diffusion
> MRI is the gold standard for stroke diagnosis, its clinical utility is often
> constrained by high costs and low accessibility. Using a dataset of 817
> patients, we demonstrate that our framework improves overall image quality and
> enhances lesion delineation when synthesizing DWI and ADC images from CT
> perfusion scans, outperforming existing image-to-image translation models.
> Furthermore, our post-training strategy is easily adaptable to pre-trained LDMs
> and exhibits substantial potential for broader applications across diverse
> medical image translation tasks.

