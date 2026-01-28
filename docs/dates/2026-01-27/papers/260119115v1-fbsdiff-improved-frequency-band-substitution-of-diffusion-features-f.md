---
layout: default
title: FBSDiff++: Improved Frequency Band Substitution of Diffusion Features for Efficient and Highly Controllable Text-Driven Image-to-Image Translation
---

# FBSDiff++: Improved Frequency Band Substitution of Diffusion Features for Efficient and Highly Controllable Text-Driven Image-to-Image Translation
**arXiv**：[2601.19115v1](https://arxiv.org/abs/2601.19115) · [PDF](https://arxiv.org/pdf/2601.19115.pdf)  
**作者**：Xiang Gao, Yunpeng Jia  

**一句话要点**：提出FBSDiff++以改进扩散模型特征频带替换，实现高效可控的文本驱动图像到图像翻译

**关键词**：图像到图像翻译, 扩散模型, 频域分析, 可控生成, 高效推理, 文本驱动

## 3 点简述
- 核心问题：如何将现成文本到图像扩散模型高效适配到图像到图像翻译任务，并增强可控性。
- 方法要点：通过动态频带替换扩散特征，实现即插即用的外观、布局和轮廓引导翻译，FBSDiff++优化架构加速推理并支持任意分辨率输入。
- 实验或效果：在视觉质量、效率、多功能性和可控性上优于先进方法，推理速度提升8.9倍。

## 摘要（原文）

> With large-scale text-to-image (T2I) diffusion models achieving significant advancements in open-domain image creation, increasing attention has been focused on their natural extension to the realm of text-driven image-to-image (I2I) translation, where a source image acts as visual guidance to the generated image in addition to the textual guidance provided by the text prompt. We propose FBSDiff, a novel framework adapting off-the-shelf T2I diffusion model into the I2I paradigm from a fresh frequency-domain perspective. Through dynamic frequency band substitution of diffusion features, FBSDiff realizes versatile and highly controllable text-driven I2I in a plug-and-play manner (without need for model training, fine-tuning, or online optimization), allowing appearance-guided, layout-guided, and contour-guided I2I translation by progressively substituting low-frequency band, mid-frequency band, and high-frequency band of latent diffusion features, respectively. In addition, FBSDiff flexibly enables continuous control over I2I correlation intensity simply by tuning the bandwidth of the substituted frequency band. To further promote image translation efficiency, flexibility, and functionality, we propose FBSDiff++ which improves upon FBSDiff mainly in three aspects: (1) accelerate inference speed by a large margin (8.9$\times$ speedup in inference) with refined model architecture; (2) improve the Frequency Band Substitution module to allow for input source images of arbitrary resolution and aspect ratio; (3) extend model functionality to enable localized image manipulation and style-specific content creation with only subtle adjustments to the core method. Extensive qualitative and quantitative experiments verify superiority of FBSDiff++ in I2I translation visual quality, efficiency, versatility, and controllability compared to related advanced approaches.

