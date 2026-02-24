---
layout: default
title: HDR Reconstruction Boosting with Training-Free and Exposure-Consistent Diffusion
---

# HDR Reconstruction Boosting with Training-Free and Exposure-Consistent Diffusion
**arXiv**：[2602.19706v1](https://arxiv.org/abs/2602.19706) · [PDF](https://arxiv.org/pdf/2602.19706.pdf)  
**作者**：Yo-Tin Lin, Su-Kai Chen, Hou-Ning Hu, Yen-Yu Lin, Yu-Lun Liu  

**一句话要点**：提出无需训练的扩散增强方法，提升单LDR到HDR重建在过曝区域的性能

**关键词**：HDR重建, 扩散模型, 过曝修复, 无需训练, 多曝光一致性

## 3 点简述
- 核心问题：单LDR到HDR重建在过曝区域因信息丢失而困难，传统方法常失效。
- 方法要点：结合文本引导扩散模型与SDEdit细化，通过迭代补偿机制生成过曝内容，保持多曝光一致性。
- 实验或效果：在标准HDR数据集和真实捕获中，显著提升感知质量和量化指标，有效恢复自然细节。

## 摘要（原文）

> Single LDR to HDR reconstruction remains challenging for over-exposed regions where traditional methods often fail due to complete information loss. We present a training-free approach that enhances existing indirect and direct HDR reconstruction methods through diffusion-based inpainting. Our method combines text-guided diffusion models with SDEdit refinement to generate plausible content in over-exposed areas while maintaining consistency across multi-exposure LDR images. Unlike previous approaches requiring extensive training, our method seamlessly integrates with existing HDR reconstruction techniques through an iterative compensation mechanism that ensures luminance coherence across multiple exposures. We demonstrate significant improvements in both perceptual quality and quantitative metrics on standard HDR datasets and in-the-wild captures. Results show that our method effectively recovers natural details in challenging scenarios while preserving the advantages of existing HDR reconstruction pipelines. Project page: https://github.com/EusdenLin/HDR-Reconstruction-Boosting

