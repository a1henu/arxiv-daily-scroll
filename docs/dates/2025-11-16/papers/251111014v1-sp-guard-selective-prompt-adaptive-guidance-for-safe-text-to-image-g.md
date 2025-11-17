---
layout: default
title: SP-Guard: Selective Prompt-adaptive Guidance for Safe Text-to-Image Generation
---

# SP-Guard: Selective Prompt-adaptive Guidance for Safe Text-to-Image Generation
**arXiv**：[2511.11014v1](https://arxiv.org/abs/2511.11014) · [PDF](https://arxiv.org/pdf/2511.11014.pdf)  
**作者**：Sumin Yu, Taesup Moon  

**一句话要点**：提出SP-Guard方法以解决文本到图像生成中的安全问题

**关键词**：文本到图像生成, 扩散模型, 安全引导, 选择性掩码, 提示自适应

## 3 点简述
- 核心问题：扩散模型易生成有害内容，现有方法缺乏自适应性和选择性。
- 方法要点：估计提示危害性，应用选择性引导掩码仅针对不安全区域。
- 实验或效果：生成更安全图像，同时最小化意外内容改变。

## 摘要（原文）

> While diffusion-based T2I models have achieved remarkable image generation quality, they also enable easy creation of harmful content, raising social concerns and highlighting the need for safer generation. Existing inference-time guiding methods lack both adaptivity--adjusting guidance strength based on the prompt--and selectivity--targeting only unsafe regions of the image. Our method, SP-Guard, addresses these limitations by estimating prompt harmfulness and applying a selective guidance mask to guide only unsafe areas. Experiments show that SP-Guard generates safer images than existing methods while minimizing unintended content alteration. Beyond improving safety, our findings highlight the importance of transparency and controllability in image generation.

