---
layout: default
title: Adapting Self-Supervised Representations as a Latent Space for Efficient Generation
---

# Adapting Self-Supervised Representations as a Latent Space for Efficient Generation
**arXiv**：[2510.14630v1](https://arxiv.org/abs/2510.14630) · [PDF](https://arxiv.org/pdf/2510.14630.pdf)  
**作者**：Ming Gui, Johannes Schusterbauer, Timy Phan, Felix Krause, Josh Susskind, Miguel Angel Bautista, Björn Ommer  

**一句话要点**：提出RepTok框架，利用自监督表示作为紧凑潜空间，实现高效图像生成。

**关键词**：自监督学习, 图像生成, 潜空间优化, 流匹配, 令牌化表示

## 3 点简述
- 核心问题：传统2D潜空间存在空间冗余，训练成本高，影响生成效率。
- 方法要点：基于预训练SSL编码器，微调语义令牌嵌入，结合流匹配目标训练解码器。
- 实验效果：在ImageNet类条件生成和MS-COCO文本到图像合成中达到竞争性结果。

## 摘要（原文）

> We introduce Representation Tokenizer (RepTok), a generative modeling
> framework that represents an image using a single continuous latent token
> obtained from self-supervised vision transformers. Building on a pre-trained
> SSL encoder, we fine-tune only the semantic token embedding and pair it with a
> generative decoder trained jointly using a standard flow matching objective.
> This adaptation enriches the token with low-level, reconstruction-relevant
> details, enabling faithful image reconstruction. To preserve the favorable
> geometry of the original SSL space, we add a cosine-similarity loss that
> regularizes the adapted token, ensuring the latent space remains smooth and
> suitable for generation. Our single-token formulation resolves spatial
> redundancies of 2D latent spaces and significantly reduces training costs.
> Despite its simplicity and efficiency, RepTok achieves competitive results on
> class-conditional ImageNet generation and naturally extends to text-to-image
> synthesis, reaching competitive zero-shot performance on MS-COCO under
> extremely limited training budgets. Our findings highlight the potential of
> fine-tuned SSL representations as compact and effective latent spaces for
> efficient generative modeling.

