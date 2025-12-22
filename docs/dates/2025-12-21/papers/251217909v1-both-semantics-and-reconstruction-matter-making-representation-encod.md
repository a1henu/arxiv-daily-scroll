---
layout: default
title: Both Semantics and Reconstruction Matter: Making Representation Encoders Ready for Text-to-Image Generation and Editing
---

# Both Semantics and Reconstruction Matter: Making Representation Encoders Ready for Text-to-Image Generation and Editing
**arXiv**：[2512.17909v1](https://arxiv.org/abs/2512.17909) · [PDF](https://arxiv.org/pdf/2512.17909.pdf)  
**作者**：Shilong Zhang, He Zhang, Zhifei Zhang, Chongjian Ge, Shuchen Xue, Shaoteng Liu, Mengwei Ren, Soo Ye Kim, Yuqian Zhou, Qing Liu, Daniil Pakhomov, Kai Zhang, Zhe Lin, Ping Luo  

**一句话要点**：提出语义-像素重建框架，使表征编码器适应文本到图像生成与编辑任务。

**关键词**：表征编码器适配, 语义-像素重建, 紧凑潜在空间, 文本到图像生成, 图像编辑, 潜在扩散模型

## 3 点简述
- 问题：表征编码器特征缺乏紧凑正则化，导致扩散模型生成结构不准确；像素级重建能力弱，影响几何纹理细节。
- 方法：引入语义-像素重建目标，压缩语义与细节到紧凑表示（96通道，16x16下采样），确保语义丰富与高重建质量。
- 效果：在文本到图像生成和编辑任务中实现最优重建、更快收敛和显著性能提升，验证编码器可有效适配为生成组件。

## 摘要（原文）

> Modern Latent Diffusion Models (LDMs) typically operate in low-level Variational Autoencoder (VAE) latent spaces that are primarily optimized for pixel-level reconstruction. To unify vision generation and understanding, a burgeoning trend is to adopt high-dimensional features from representation encoders as generative latents. However, we empirically identify two fundamental obstacles in this paradigm: (1) the discriminative feature space lacks compact regularization, making diffusion models prone to off-manifold latents that lead to inaccurate object structures; and (2) the encoder's inherently weak pixel-level reconstruction hinders the generator from learning accurate fine-grained geometry and texture. In this paper, we propose a systematic framework to adapt understanding-oriented encoder features for generative tasks. We introduce a semantic-pixel reconstruction objective to regularize the latent space, enabling the compression of both semantic information and fine-grained details into a highly compact representation (96 channels with 16x16 spatial downsampling). This design ensures that the latent space remains semantically rich and achieves state-of-the-art image reconstruction, while remaining compact enough for accurate generation. Leveraging this representation, we design a unified Text-to-Image (T2I) and image editing model. Benchmarking against various feature spaces, we demonstrate that our approach achieves state-of-the-art reconstruction, faster convergence, and substantial performance gains in both T2I and editing tasks, validating that representation encoders can be effectively adapted into robust generative components.

