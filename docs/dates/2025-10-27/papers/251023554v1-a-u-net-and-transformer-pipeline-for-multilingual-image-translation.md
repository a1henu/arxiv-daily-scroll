---
layout: default
title: A U-Net and Transformer Pipeline for Multilingual Image Translation
---

# A U-Net and Transformer Pipeline for Multilingual Image Translation
**arXiv**：[2510.23554v1](https://arxiv.org/abs/2510.23554) · [PDF](https://arxiv.org/pdf/2510.23554.pdf)  
**作者**：Siddharth Sahay, Radhika Agarwal  

**一句话要点**：提出基于U-Net和Transformer的多语言图像翻译管道，用于从图像中直接翻译文本。

**关键词**：图像文本检测, 多语言机器翻译, U-Net模型, Transformer架构, 端到端管道

## 3 点简述
- 核心问题：从图像中检测、识别并翻译多语言文本，避免依赖预训练模型。
- 方法要点：使用U-Net检测文本区域，Tesseract识别文本，自定义Transformer进行翻译。
- 实验或效果：评估文本检测准确性、识别质量和翻译BLEU分数，结果表现良好。

## 摘要（原文）

> This paper presents an end-to-end multilingual translation pipeline that
> integrates a custom U-Net for text detection, the Tesseract engine for text
> recognition, and a from-scratch sequence-to-sequence (Seq2Seq) Transformer for
> Neural Machine Translation (NMT). Our approach first utilizes a U-Net model,
> trained on a synthetic dataset , to accurately segment and detect text regions
> from an image. These detected regions are then processed by Tesseract to
> extract the source text. This extracted text is fed into a custom Transformer
> model trained from scratch on a multilingual parallel corpus spanning 5
> languages. Unlike systems reliant on monolithic pre-trained models, our
> architecture emphasizes full customization and adaptability. The system is
> evaluated on its text detection accuracy, text recognition quality, and
> translation performance via BLEU scores. The complete pipeline demonstrates
> promising results, validating the viability of a custom-built system for
> translating text directly from images.

