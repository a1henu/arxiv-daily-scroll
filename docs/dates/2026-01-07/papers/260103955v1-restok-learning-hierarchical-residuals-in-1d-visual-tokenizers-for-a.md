---
layout: default
title: ResTok: Learning Hierarchical Residuals in 1D Visual Tokenizers for Autoregressive Image Generation
---

# ResTok: Learning Hierarchical Residuals in 1D Visual Tokenizers for Autoregressive Image Generation
**arXiv**：[2601.03955v1](https://arxiv.org/abs/2601.03955) · [PDF](https://arxiv.org/pdf/2601.03955.pdf)  
**作者**：Xu Zhang, Cheng Da, Huan Yang, Kun Gai, Ming Lu, Zhan Ma  

**一句话要点**：提出ResTok视觉分词器，通过分层残差学习提升自回归图像生成效果。

**关键词**：视觉分词器, 自回归图像生成, 分层残差学习, 潜在表示, 高效采样

## 3 点简述
- 现有1D视觉分词器基于语言模型设计，忽略视觉数据的层次性和残差特性。
- ResTok引入分层残差表示，增强特征融合并集中潜在分布，便于自回归建模。
- 实验在ImageNet-256上实现gFID 2.34，仅需9步采样，代码已开源。

## 摘要（原文）

> Existing 1D visual tokenizers for autoregressive (AR) generation largely follow the design principles of language modeling, as they are built directly upon transformers whose priors originate in language, yielding single-hierarchy latent tokens and treating visual data as flat sequential token streams. However, this language-like formulation overlooks key properties of vision, particularly the hierarchical and residual network designs that have long been essential for convergence and efficiency in visual models. To bring "vision" back to vision, we propose the Residual Tokenizer (ResTok), a 1D visual tokenizer that builds hierarchical residuals for both image tokens and latent tokens. The hierarchical representations obtained through progressively merging enable cross-level feature fusion at each layer, substantially enhancing representational capacity. Meanwhile, the semantic residuals between hierarchies prevent information overlap, yielding more concentrated latent distributions that are easier for AR modeling. Cross-level bindings consequently emerge without any explicit constraints. To accelerate the generation process, we further introduce a hierarchical AR generator that substantially reduces sampling steps by predicting an entire level of latent tokens at once rather than generating them strictly token-by-token. Extensive experiments demonstrate that restoring hierarchical residual priors in visual tokenization significantly improves AR image generation, achieving a gFID of 2.34 on ImageNet-256 with only 9 sampling steps. Code is available at https://github.com/Kwai-Kolors/ResTok.

