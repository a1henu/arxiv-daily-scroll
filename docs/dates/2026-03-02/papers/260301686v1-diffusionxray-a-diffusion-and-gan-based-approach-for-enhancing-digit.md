---
layout: default
title: DiffusionXRay: A Diffusion and GAN-Based Approach for Enhancing Digitally Reconstructed Chest Radiographs
---

# DiffusionXRay: A Diffusion and GAN-Based Approach for Enhancing Digitally Reconstructed Chest Radiographs
**arXiv**：[2603.01686v1](https://arxiv.org/abs/2603.01686) · [PDF](https://arxiv.org/pdf/2603.01686.pdf)  
**作者**：Aryan Goyal, Ashish Mittal, Pranav Rao, Manoj Tadepalli, Preetham Putha  

**一句话要点**：提出DiffusionXRay以增强数字重建胸片，结合扩散模型与GAN提升图像质量。

**关键词**：图像增强, 扩散模型, 生成对抗网络, 胸片重建, 医学影像处理

## 3 点简述
- 核心问题：数字重建胸片质量差，影响肺癌自动诊断模型训练。
- 方法要点：采用两阶段训练，先生成低质量图像，再用扩散模型恢复高质量细节。
- 实验或效果：通过定量指标和专家评估验证，提升图像清晰度和诊断价值。

## 摘要（原文）

> Deep learning-based automated diagnosis of lung cancer has emerged as a crucial advancement that enables healthcare professionals to detect and initiate treatment earlier. However, these models require extensive training datasets with diverse case-specific properties. High-quality annotated data is particularly challenging to obtain, especially for cases with subtle pulmonary nodules that are difficult to detect even for experienced radiologists. This scarcity of well-labeled datasets can limit model performance and generalization across different patient populations. Digitally reconstructed radiographs (DRR) using CT-Scan to generate synthetic frontal chest X-rays with artificially inserted lung nodules offers one potential solution. However, this approach suffers from significant image quality degradation, particularly in the form of blurred anatomical features and loss of fine lung field structures. To overcome this, we introduce DiffusionXRay, a novel image restoration pipeline for Chest X-ray images that synergistically leverages denoising diffusion probabilistic models (DDPMs) and generative adversarial networks (GANs). DiffusionXRay incorporates a unique two-stage training process: First, we investigate two independent approaches, DDPM-LQ and GAN-based MUNIT-LQ, to generate low-quality CXRs, addressing the challenge of training data scarcity, posing this as a style transfer problem. Subsequently, we train a DDPM-based model on paired low-quality and high-quality images, enabling it to learn the nuances of X-ray image restoration. Our method demonstrates promising results in enhancing image clarity, contrast, and overall diagnostic value of chest X-rays while preserving subtle yet clinically significant artifacts, validated by both quantitative metrics and expert radiological assessment.

