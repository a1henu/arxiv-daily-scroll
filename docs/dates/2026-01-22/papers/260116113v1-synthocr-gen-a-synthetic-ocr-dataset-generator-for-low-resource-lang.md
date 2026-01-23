---
layout: default
title: synthocr-gen: A synthetic ocr dataset generator for low-resource languages- breaking the data barrier
---

# synthocr-gen: A synthetic ocr dataset generator for low-resource languages- breaking the data barrier
**arXiv**：[2601.16113v1](https://arxiv.org/abs/2601.16113) · [PDF](https://arxiv.org/pdf/2601.16113.pdf)  
**作者**：Haq Nawaz Malik, Kh Mohmad Shafi, Tanveer Ahmad Reshi  

**一句话要点**：提出SynthOCR-Gen合成OCR数据集生成器，以解决低资源语言因缺乏标注数据而难以开发OCR系统的问题。

**关键词**：合成数据集生成, 低资源语言OCR, 数据增强, 克什米尔语, 开源工具

## 3 点简述
- 核心问题：低资源语言如克什米尔语缺乏大规模标注OCR数据集，导致主流OCR系统不支持其复杂文字。
- 方法要点：通过文本分割、Unicode标准化、多字体渲染和25+数据增强技术，从数字文本语料库生成合成训练数据集。
- 实验或效果：生成了60万样本的克什米尔语OCR数据集并公开，为低资源语言OCR开发提供实用路径。

## 摘要（原文）

> Optical Character Recognition (OCR) for low-resource languages remains a significant challenge due to the scarcity of large-scale annotated training datasets. Languages such as Kashmiri, with approximately 7 million speakers and a complex Perso-Arabic script featuring unique diacritical marks, currently lack support in major OCR systems including Tesseract, TrOCR, and PaddleOCR. Manual dataset creation for such languages is prohibitively expensive, time-consuming, and error-prone, often requiring word by word transcription of printed or handwritten text.
>   We present SynthOCR-Gen, an open-source synthetic OCR dataset generator specifically designed for low-resource languages. Our tool addresses the fundamental bottleneck in OCR development by transforming digital Unicode text corpora into ready-to-use training datasets. The system implements a comprehensive pipeline encompassing text segmentation (character, word, n-gram, sentence, and line levels), Unicode normalization with script purity enforcement, multi-font rendering with configurable distribution, and 25+ data augmentation techniques simulating real-world document degradations including rotation, blur, noise, and scanner artifacts.
>   We demonstrate the efficacy of our approach by generating a 600,000-sample word-segmented Kashmiri OCR dataset, which we release publicly on HuggingFace. This work provides a practical pathway for bringing low-resource languages into the era of vision-language AI models, and the tool is openly available for researchers and practitioners working with underserved writing systems worldwide.

