---
layout: default
title: What matters for Representation Alignment: Global Information or Spatial Structure?
---

# What matters for Representation Alignment: Global Information or Spatial Structure?
**arXiv**：[2512.10794v1](https://arxiv.org/abs/2512.10794) · [PDF](https://arxiv.org/pdf/2512.10794.pdf)  
**作者**：Jaskirat Singh, Xingjian Leng, Zongze Wu, Liang Zheng, Richard Zhang, Eli Shechtman, Saining Xie  

**一句话要点**：提出iREPA方法，通过增强空间结构对齐改进生成模型训练中的表示对齐

**关键词**：表示对齐, 生成模型训练, 空间结构, 视觉编码器, 蒸馏训练, 扩散模型

## 3 点简述
- 研究表示对齐中全局语义信息与空间结构对生成性能的影响
- 发现空间结构而非全局性能驱动生成，引入卷积层和空间归一化层
- iREPA在多种编码器和训练变体中提升收敛速度，代码简洁

## 摘要（原文）

> Representation alignment (REPA) guides generative training by distilling representations from a strong, pretrained vision encoder to intermediate diffusion features. We investigate a fundamental question: what aspect of the target representation matters for generation, its \textit{global} \revision{semantic} information (e.g., measured by ImageNet-1K accuracy) or its spatial structure (i.e. pairwise cosine similarity between patch tokens)? Prevalent wisdom holds that stronger global semantic performance leads to better generation as a target representation. To study this, we first perform a large-scale empirical analysis across 27 different vision encoders and different model scales. The results are surprising; spatial structure, rather than global performance, drives the generation performance of a target representation. To further study this, we introduce two straightforward modifications, which specifically accentuate the transfer of \emph{spatial} information. We replace the standard MLP projection layer in REPA with a simple convolution layer and introduce a spatial normalization layer for the external representation. Surprisingly, our simple method (implemented in $<$4 lines of code), termed iREPA, consistently improves convergence speed of REPA, across a diverse set of vision encoders, model sizes, and training variants (such as REPA, REPA-E, Meanflow, JiT etc). %, etc. Our work motivates revisiting the fundamental working mechanism of representational alignment and how it can be leveraged for improved training of generative models. The code and project page are available at https://end2end-diffusion.github.io/irepa

