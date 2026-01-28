---
layout: default
title: DuwatBench: Bridging Language and Visual Heritage through an Arabic Calligraphy Benchmark for Multimodal Understanding
---

# DuwatBench: Bridging Language and Visual Heritage through an Arabic Calligraphy Benchmark for Multimodal Understanding
**arXiv**：[2601.19898v1](https://arxiv.org/abs/2601.19898) · [PDF](https://arxiv.org/pdf/2601.19898.pdf)  
**作者**：Shubham Patle, Sara Ghaboura, Hania Tariq, Mohammad Usman Khan, Omkar Thawakar, Rao Muhammad Anwer, Salman Khan  

**一句话要点**：提出DuwatBench阿拉伯书法基准，以解决多模态模型处理阿拉伯艺术化文字的挑战。

**关键词**：阿拉伯书法基准, 多模态理解, 视觉-文本对齐, 数据集构建, 艺术化文字处理, 文化AI

## 3 点简述
- 核心问题：多模态模型对阿拉伯艺术化书法处理能力不足，缺乏相关基准。
- 方法要点：构建包含1,272个样本的阿拉伯书法数据集，涵盖六种风格和句子级标注。
- 实验或效果：评估13个模型，显示其在书法变体、艺术扭曲和视觉-文本对齐方面表现不佳。

## 摘要（原文）

> Arabic calligraphy represents one of the richest visual traditions of the Arabic language, blending linguistic meaning with artistic form. Although multimodal models have advanced across languages, their ability to process Arabic script, especially in artistic and stylized calligraphic forms, remains largely unexplored. To address this gap, we present DuwatBench, a benchmark of 1,272 curated samples containing about 1,475 unique words across six classical and modern calligraphic styles, each paired with sentence-level detection annotations. The dataset reflects real-world challenges in Arabic writing, such as complex stroke patterns, dense ligatures, and stylistic variations that often challenge standard text recognition systems. Using DuwatBench, we evaluated 13 leading Arabic and multilingual multimodal models and showed that while they perform well on clean text, they struggle with calligraphic variation, artistic distortions, and precise visual-text alignment. By publicly releasing DuwatBench and its annotations, we aim to advance culturally grounded multimodal research, foster fair inclusion of the Arabic language and visual heritage in AI systems, and support continued progress in this area. Our dataset (https://huggingface.co/datasets/MBZUAI/DuwatBench) and evaluation suit (https://github.com/mbzuai-oryx/DuwatBench) are publicly available.

