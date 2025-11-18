---
layout: default
title: MRIQT: Physics-Aware Diffusion Model for Image Quality Transfer in Neonatal Ultra-Low-Field MRI
---

# MRIQT: Physics-Aware Diffusion Model for Image Quality Transfer in Neonatal Ultra-Low-Field MRI
**arXiv**：[2511.13232v1](https://arxiv.org/abs/2511.13232) · [PDF](https://arxiv.org/pdf/2511.13232.pdf)  
**作者**：Malek Al Abed, Sebiha Demir, Anne Groteklaes, Elodie Germani, Shahrooz Faghihroohi, Hemmen Sabir, Shadi Albarqouni  

**一句话要点**：提出MRIQT扩散模型以提升新生儿超低场MRI图像质量

**关键词**：图像质量迁移, 扩散模型, 超低场MRI, 新生儿神经影像, 3D图像增强

## 3 点简述
- 超低场MRI图像信噪比低，诊断质量差，影响新生儿脑部评估。
- 采用3D条件扩散框架，结合K空间退化和SNR加权损失，实现物理一致增强。
- 在新生儿数据集上超越GAN和CNN基线，85%输出被医生评为高质量。

## 摘要（原文）

> Portable ultra-low-field MRI (uLF-MRI, 0.064 T) offers accessible neuroimaging for neonatal care but suffers from low signal-to-noise ratio and poor diagnostic quality compared to high-field (HF) MRI. We propose MRIQT, a 3D conditional diffusion framework for image quality transfer (IQT) from uLF to HF MRI. MRIQT combines realistic K-space degradation for physics-consistent uLF simulation, v-prediction with classifier-free guidance for stable image-to-image generation, and an SNR-weighted 3D perceptual loss for anatomical fidelity. The model denoises from a noised uLF input conditioned on the same scan, leveraging volumetric attention-UNet architecture for structure-preserving translation. Trained on a neonatal cohort with diverse pathologies, MRIQT surpasses recent GAN and CNN baselines in PSNR 15.3% with 1.78% over the state of the art, while physicians rated 85% of its outputs as good quality with clear pathology present. MRIQT enables high-fidelity, diffusion-based enhancement of portable ultra-low-field (uLF) MRI for deliable neonatal brain assessment.

