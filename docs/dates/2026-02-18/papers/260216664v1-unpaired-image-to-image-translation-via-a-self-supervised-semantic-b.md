---
layout: default
title: Unpaired Image-to-Image Translation via a Self-Supervised Semantic Bridge
---

# Unpaired Image-to-Image Translation via a Self-Supervised Semantic Bridge
**arXiv**：[2602.16664v1](https://arxiv.org/abs/2602.16664) · [PDF](https://arxiv.org/pdf/2602.16664.pdf)  
**作者**：Jiaming Liu, Felix Petersen, Yunhe Gao, Yabin Zhang, Hyojin Kim, Akshay S. Chaudhari, Yu Sun, Stefano Ermon, Sergios Gatidis  

**一句话要点**：提出自监督语义桥框架，通过语义先验增强扩散桥模型，实现无配对图像翻译

**关键词**：无配对图像翻译, 扩散模型, 自监督学习, 语义先验, 医学图像合成

## 3 点简述
- 核心问题：现有无配对图像翻译方法存在泛化受限或保真度低的问题
- 方法要点：利用自监督视觉编码器学习几何不变表示，构建共享潜在空间以条件化扩散桥
- 实验或效果：在医学图像合成中优于先前方法，并扩展到高质量文本引导编辑

## 摘要（原文）

> Adversarial diffusion and diffusion-inversion methods have advanced unpaired image-to-image translation, but each faces key limitations. Adversarial approaches require target-domain adversarial loss during training, which can limit generalization to unseen data, while diffusion-inversion methods often produce low-fidelity translations due to imperfect inversion into noise-latent representations. In this work, we propose the Self-Supervised Semantic Bridge (SSB), a versatile framework that integrates external semantic priors into diffusion bridge models to enable spatially faithful translation without cross-domain supervision. Our key idea is to leverage self-supervised visual encoders to learn representations that are invariant to appearance changes but capture geometric structure, forming a shared latent space that conditions the diffusion bridges. Extensive experiments show that SSB outperforms strong prior methods for challenging medical image synthesis in both in-domain and out-of-domain settings, and extends easily to high-quality text-guided editing.

