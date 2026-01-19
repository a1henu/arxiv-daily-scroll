---
layout: default
title: Generation of Chest CT pulmonary Nodule Images by Latent Diffusion Models using the LIDC-IDRI Dataset
---

# Generation of Chest CT pulmonary Nodule Images by Latent Diffusion Models using the LIDC-IDRI Dataset
**arXiv**：[2601.11085v1](https://arxiv.org/abs/2601.11085) · [PDF](https://arxiv.org/pdf/2601.11085.pdf)  
**作者**：Kaito Urata, Maiko Nagao, Atsushi Teramoto, Kazuyoshi Imaizumi, Masashi Kondo, Hiroshi Fujita  

**一句话要点**：提出基于潜在扩散模型的胸部CT肺结节图像生成方法，以解决数据不平衡问题。

**关键词**：潜在扩散模型, 胸部CT图像生成, 肺结节, 数据增强, 计算机辅助诊断, LIDC-IDRI数据集

## 3 点简述
- 核心问题：临床CT图像数据不足导致计算机辅助诊断系统性能受限，特别是罕见病例或良恶性难辨肿瘤。
- 方法要点：使用LIDC-IDRI数据集构建结节图像-文本提示对，微调Stable Diffusion模型，通过调整引导尺度控制文本一致性。
- 实验或效果：SDv2在引导尺度为5时表现最佳，生成图像质量、多样性和文本一致性高，主观评估显示与真实图像无显著差异。

## 摘要（原文）

> Recently, computer-aided diagnosis systems have been developed to support diagnosis, but their performance depends heavily on the quality and quantity of training data. However, in clinical practice, it is difficult to collect the large amount of CT images for specific cases, such as small cell carcinoma with low epidemiological incidence or benign tumors that are difficult to distinguish from malignant ones. This leads to the challenge of data imbalance. In this study, to address this issue, we proposed a method to automatically generate chest CT nodule images that capture target features using latent diffusion models (LDM) and verified its effectiveness. Using the LIDC-IDRI dataset, we created pairs of nodule images and finding-based text prompts based on physician evaluations. For the image generation models, we used Stable Diffusion version 1.5 (SDv1) and 2.0 (SDv2), which are types of LDM. Each model was fine-tuned using the created dataset. During the generation process, we adjusted the guidance scale (GS), which indicates the fidelity to the input text. Both quantitative and subjective evaluations showed that SDv2 (GS = 5) achieved the best performance in terms of image quality, diversity, and text consistency. In the subjective evaluation, no statistically significant differences were observed between the generated images and real images, confirming that the quality was equivalent to real clinical images. We proposed a method for generating chest CT nodule images based on input text using LDM. Evaluation results demonstrated that the proposed method could generate high-quality images that successfully capture specific medical features.

