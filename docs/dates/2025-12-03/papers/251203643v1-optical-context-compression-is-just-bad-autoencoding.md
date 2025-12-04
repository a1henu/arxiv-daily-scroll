---
layout: default
title: Optical Context Compression Is Just (Bad) Autoencoding
---

# Optical Context Compression Is Just (Bad) Autoencoding
**arXiv**：[2512.03643v1](https://arxiv.org/abs/2512.03643) · [PDF](https://arxiv.org/pdf/2512.03643.pdf)  
**作者**：Ivan Yee Lee, Cheng Yang, Taylor Berg-Kirkpatrick  

**一句话要点**：质疑视觉上下文压缩优势，通过简单编码器在重建与语言建模中超越视觉方法

**关键词**：上下文压缩, 视觉编码, 语言建模, 文本重建, 压缩表示

## 3 点简述
- 核心问题：视觉上下文压缩是否对文本重建和语言建模有独特优势，现有评估仅关注重建
- 方法要点：比较视觉编码器与参数无关均值池化和学习分层编码器，在相同压缩比下测试
- 实验或效果：简单方法在重建上匹配或超越视觉编码器，语言建模中视觉压缩未优于截断

## 摘要（原文）

> DeepSeek-OCR demonstrates that rendered text can be reconstructed with high fidelity from a small number of vision tokens. This finding has sparked excitement about vision-based context compression for language models. But the evaluation stops at reconstruction; whether these representations help language modeling remains untested. We test two assumptions implicit in the optical-compression narrative: that vision-based compression provides unique advantages for text reconstruction from compressed representations, and that DeepSeek-OCR's reconstruction results are evidence that vision-based compression will be useful for language modeling. Comparing their vision encoder against simple alternatives--parameter-free mean pooling and a learned hierarchical encoder--we find that these simple approaches match or surpass vision for reconstruction at matched compression ratios, and outperform it for language modeling--where vision-based compression fails to beat truncation. The excitement around optical context compression outpaces the evidence. Code and checkpoints are available at https://github.com/ivnle/bad-autoencoding

