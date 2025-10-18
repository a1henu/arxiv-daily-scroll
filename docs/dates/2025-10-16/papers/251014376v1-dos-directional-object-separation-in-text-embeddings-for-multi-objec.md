---
layout: default
title: DOS: Directional Object Separation in Text Embeddings for Multi-Object Image Generation
---

# DOS: Directional Object Separation in Text Embeddings for Multi-Object Image Generation
**arXiv**：[2510.14376v1](https://arxiv.org/abs/2510.14376) · [PDF](https://arxiv.org/pdf/2510.14376.pdf)  
**作者**：Dongnam Byun, Jungwon Park, Jumgmin Ko, Changin Choi, Wonjong Rhee  

**一句话要点**：提出DOS方法以解决多对象图像生成中的对象忽略与混合问题

**关键词**：多对象图像生成, 文本到图像模型, CLIP嵌入, 对象分离, 文本提示对齐

## 3 点简述
- 多对象图像生成常出现对象忽略或混合，源于相似形状、纹理、背景偏差和对象过多
- DOS通过修改CLIP文本嵌入，分离对象方向，提升多对象生成成功率
- 实验显示DOS显著优于其他方法，人类评估中获26.24%-43.04%更多投票

## 摘要（原文）

> Recent progress in text-to-image (T2I) generative models has led to
> significant improvements in generating high-quality images aligned with text
> prompts. However, these models still struggle with prompts involving multiple
> objects, often resulting in object neglect or object mixing. Through extensive
> studies, we identify four problematic scenarios, Similar Shapes, Similar
> Textures, Dissimilar Background Biases, and Many Objects, where inter-object
> relationships frequently lead to such failures. Motivated by two key
> observations about CLIP embeddings, we propose DOS (Directional Object
> Separation), a method that modifies three types of CLIP text embeddings before
> passing them into text-to-image models. Experimental results show that DOS
> consistently improves the success rate of multi-object image generation and
> reduces object mixing. In human evaluations, DOS significantly outperforms four
> competing methods, receiving 26.24%-43.04% more votes across four benchmarks.
> These results highlight DOS as a practical and effective solution for improving
> multi-object image generation.

