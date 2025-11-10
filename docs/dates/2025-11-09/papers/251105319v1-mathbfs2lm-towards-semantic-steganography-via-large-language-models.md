---
layout: default
title: $\mathbf{S^2LM}$: Towards Semantic Steganography via Large Language Models
---

# $\mathbf{S^2LM}$: Towards Semantic Steganography via Large Language Models
**arXiv**：[2511.05319v1](https://arxiv.org/abs/2511.05319) · [PDF](https://arxiv.org/pdf/2511.05319.pdf)  
**作者**：Huanqi Wu, Huangbiao Xu, Runfeng Xie, Jiaxin Cai, Kaixin Zhang, Xiao Ke  

**一句话要点**：提出S^2LM模型，利用大语言模型实现句子级语义信息隐写于图像中。

**关键词**：语义隐写, 大语言模型, 句子级隐写, 图像隐写, AIGC时代

## 3 点简述
- 核心问题：传统隐写术难以嵌入语义丰富的句子级信息到载体中。
- 方法要点：设计新流程，大语言模型全程参与，嵌入句子或段落级文本。
- 实验或效果：定量与定性实验显示，方法有效解锁LLM的语义隐写能力。

## 摘要（原文）

> Although steganography has made significant advancements in recent years, it
> still struggles to embed semantically rich, sentence-level information into
> carriers. However, in the era of AIGC, the capacity of steganography is more
> critical than ever. In this work, we present Sentence-to-Image Steganography,
> an instance of Semantic Steganography, a novel task that enables the hiding of
> arbitrary sentence-level messages within a cover image. Furthermore, we
> establish a benchmark named Invisible Text (IVT), comprising a diverse set of
> sentence-level texts as secret messages for evaluation. Finally, we present
> $\mathbf{S^2LM}$: Semantic Steganographic Language Model, which utilizes large
> language models (LLMs) to embed high-level textual information, such as
> sentences or even paragraphs, into images. Unlike traditional bit-level
> counterparts, $\mathrm{S^2LM}$ enables the integration of semantically rich
> content through a newly designed pipeline in which the LLM is involved
> throughout the entire process. Both quantitative and qualitative experiments
> demonstrate that our method effectively unlocks new semantic steganographic
> capabilities for LLMs. The source code will be released soon.

