---
layout: default
title: IGAN: A New Inception-based Model for Stable and High-Fidelity Image Synthesis Using Generative Adversarial Networks
---

# IGAN: A New Inception-based Model for Stable and High-Fidelity Image Synthesis Using Generative Adversarial Networks
**arXiv**：[2601.08332v1](https://arxiv.org/abs/2601.08332) · [PDF](https://arxiv.org/pdf/2601.08332.pdf)  
**作者**：Ahmed A. Hashim, Ali Al-Shuwaili, Asraa Saeed, Ali Al-Bayaty  

**一句话要点**：提出IGAN模型，结合Inception与空洞卷积，以提升GAN的图像生成质量与训练稳定性。

**关键词**：生成对抗网络, 图像合成, 训练稳定性, Inception结构, 空洞卷积, 谱归一化

## 3 点简述
- 核心问题：GAN在高质量图像生成与训练稳定性间难以平衡，易出现模式崩溃和梯度不稳定。
- 方法要点：引入Inception启发的深度卷积和空洞卷积，结合Dropout与谱归一化技术。
- 实验或效果：在CUB-200和ImageNet数据集上FID提升28-33%，IS分数显示图像多样性与质量改善。

## 摘要（原文）

> Generative Adversarial Networks (GANs) face a significant challenge of striking an optimal balance between high-quality image generation and training stability. Recent techniques, such as DCGAN, BigGAN, and StyleGAN, improve visual fidelity; however, such techniques usually struggle with mode collapse and unstable gradients at high network depth. This paper proposes a novel GAN structural model that incorporates deeper inception-inspired convolution and dilated convolution. This novel model is termed the Inception Generative Adversarial Network (IGAN). The IGAN model generates high-quality synthetic images while maintaining training stability, by reducing mode collapse as well as preventing vanishing and exploding gradients. Our proposed IGAN model achieves the Frechet Inception Distance (FID) of 13.12 and 15.08 on the CUB-200 and ImageNet datasets, respectively, representing a 28-33% improvement in FID over the state-of-the-art GANs. Additionally, the IGAN model attains an Inception Score (IS) of 9.27 and 68.25, reflecting improved image diversity and generation quality. Finally, the two techniques of dropout and spectral normalization are utilized in both the generator and discriminator structures to further mitigate gradient explosion and overfitting. These findings confirm that the IGAN model potentially balances training stability with image generation quality, constituting a scalable and computationally efficient framework for high-fidelity image synthesis.

