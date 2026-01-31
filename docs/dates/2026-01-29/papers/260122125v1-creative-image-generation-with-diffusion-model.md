---
layout: default
title: Creative Image Generation with Diffusion Model
---

# Creative Image Generation with Diffusion Model
**arXiv**：[2601.22125v1](https://arxiv.org/abs/2601.22125) · [PDF](https://arxiv.org/pdf/2601.22125.pdf)  
**作者**：Kunpeng Song, Ahmed Elgammal  

**一句话要点**：提出基于扩散模型的创意图像生成框架，通过驱动图像概率分布至低概率区域以产生新颖图像。

**关键词**：扩散模型, 创意图像生成, CLIP嵌入, 概率分布驱动, 回拉机制, 文本到图像生成

## 3 点简述
- 核心问题：传统方法依赖手动概念混合或子类别排除，难以自动生成高创意图像。
- 方法要点：利用CLIP嵌入空间中的图像逆概率定义创意，并引入回拉机制保持视觉保真度。
- 实验或效果：在文本到图像扩散模型上验证，能高效生成独特、新颖且引人深思的图像。

## 摘要（原文）

> Creative image generation has emerged as a compelling area of research, driven by the need to produce novel and high-quality images that expand the boundaries of imagination. In this work, we propose a novel framework for creative generation using diffusion models, where creativity is associated with the inverse probability of an image's existence in the CLIP embedding space. Unlike prior approaches that rely on a manual blending of concepts or exclusion of subcategories, our method calculates the probability distribution of generated images and drives it towards low-probability regions to produce rare, imaginative, and visually captivating outputs. We also introduce pullback mechanisms, achieving high creativity without sacrificing visual fidelity. Extensive experiments on text-to-image diffusion models demonstrate the effectiveness and efficiency of our creative generation framework, showcasing its ability to produce unique, novel, and thought-provoking images. This work provides a new perspective on creativity in generative models, offering a principled method to foster innovation in visual content synthesis.

