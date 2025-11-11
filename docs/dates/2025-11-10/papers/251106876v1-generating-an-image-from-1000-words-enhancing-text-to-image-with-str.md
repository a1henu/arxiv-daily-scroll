---
layout: default
title: Generating an Image From 1,000 Words: Enhancing Text-to-Image With Structured Captions
---

# Generating an Image From 1,000 Words: Enhancing Text-to-Image With Structured Captions
**arXiv**：[2511.06876v1](https://arxiv.org/abs/2511.06876) · [PDF](https://arxiv.org/pdf/2511.06876.pdf)  
**作者**：Eyal Gutflaish, Eliran Kachlon, Hezi Zisman, Tal Hacham, Nimrod Sarid, Alexander Visheratin, Saar Huberman, Gal Davidi, Guy Bukchin, Kfir Goldberg, Ron Mokady  

**一句话要点**：提出基于长结构化描述的文本到图像生成模型，以解决输入稀疏导致的控制性问题。

**关键词**：文本到图像生成, 长结构化描述, DimFusion机制, TaBR评估协议, FIBO模型, 控制性增强

## 3 点简述
- 核心问题：短提示与丰富视觉输出不匹配，导致模型控制性差和细节填充偏差。
- 方法要点：训练首个开源模型使用长结构化描述，并引入DimFusion机制高效处理长输入。
- 实验或效果：通过TaBR评估协议和FIBO模型，在开源模型中实现最先进的提示对齐。

## 摘要（原文）

> Text-to-image models have rapidly evolved from casual creative tools to
> professional-grade systems, achieving unprecedented levels of image quality and
> realism. Yet, most models are trained to map short prompts into detailed
> images, creating a gap between sparse textual input and rich visual outputs.
> This mismatch reduces controllability, as models often fill in missing details
> arbitrarily, biasing toward average user preferences and limiting precision for
> professional use. We address this limitation by training the first open-source
> text-to-image model on long structured captions, where every training sample is
> annotated with the same set of fine-grained attributes. This design maximizes
> expressive coverage and enables disentangled control over visual factors. To
> process long captions efficiently, we propose DimFusion, a fusion mechanism
> that integrates intermediate tokens from a lightweight LLM without increasing
> token length. We also introduce the Text-as-a-Bottleneck Reconstruction (TaBR)
> evaluation protocol. By assessing how well real images can be reconstructed
> through a captioning-generation loop, TaBR directly measures controllability
> and expressiveness, even for very long captions where existing evaluation
> methods fail. Finally, we demonstrate our contributions by training the
> large-scale model FIBO, achieving state-of-the-art prompt alignment among
> open-source models. Model weights are publicly available at
> https://huggingface.co/briaai/FIBO

