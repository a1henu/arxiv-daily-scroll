---
layout: default
title: AWDiff: An a trous wavelet diffusion model for lung ultrasound image synthesis
---

# AWDiff: An a trous wavelet diffusion model for lung ultrasound image synthesis
**arXiv**：[2603.03125v1](https://arxiv.org/abs/2603.03125) · [PDF](https://arxiv.org/pdf/2603.03125.pdf)  
**作者**：Maryam Heidari, Nantheera Anantrasirichai, Steven Walker, Rahul Bhatnagar, Alin Achim  

**一句话要点**：提出AWDiff以解决肺超声图像合成中细节丢失问题，通过小波变换和语义条件增强数据生成。

**关键词**：肺超声图像合成, à trous小波扩散模型, 语义条件生成, 数据增强, 医学图像生成

## 3 点简述
- 核心问题：肺超声数据稀缺，现有生成方法如GANs和扩散模型易丢失B线等细微诊断线索。
- 方法要点：集成à trous小波变换避免破坏性下采样，结合BioMedCLIP进行语义条件控制。
- 实验或效果：在肺超声数据集上，AWDiff相比现有方法实现更低失真和更高感知质量，保持结构保真度和临床多样性。

## 摘要（原文）

> Lung ultrasound (LUS) is a safe and portable imaging modality, but the scarcity of data limits the development of machine learning methods for image interpretation and disease monitoring. Existing generative augmentation methods, such as Generative Adversarial Networks (GANs) and diffusion models, often lose subtle diagnostic cues due to resolution reduction, particularly B-lines and pleural irregularities. We propose A trous Wavelet Diffusion (AWDiff), a diffusion based augmentation framework that integrates the a trous wavelet transform to preserve fine-scale structures while avoiding destructive downsampling. In addition, semantic conditioning with BioMedCLIP, a vision language foundation model trained on large scale biomedical corpora, enforces alignment with clinically meaningful labels. On a LUS dataset, AWDiff achieved lower distortion and higher perceptual quality compared to existing methods, demonstrating both structural fidelity and clinical diversity.

