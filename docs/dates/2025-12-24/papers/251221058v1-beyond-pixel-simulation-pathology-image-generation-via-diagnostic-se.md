---
layout: default
title: Beyond Pixel Simulation: Pathology Image Generation via Diagnostic Semantic Tokens and Prototype Control
---

# Beyond Pixel Simulation: Pathology Image Generation via Diagnostic Semantic Tokens and Prototype Control
**arXiv**：[2512.21058v1](https://arxiv.org/abs/2512.21058) · [PDF](https://arxiv.org/pdf/2512.21058.pdf)  
**作者**：Minghao Han, YiChen Liu, Yizhou Liu, Zizhi Chen, Jingqun Tang, Xuecheng Wu, Dingkang Yang, Lihua Zhang  

**一句话要点**：提出UniPath框架，通过诊断语义令牌和原型控制实现病理图像的可控生成。

**关键词**：病理图像生成, 语义控制, 多流框架, 诊断语义令牌, 原型控制, 数据集构建

## 3 点简述
- 核心问题：病理图像生成面临数据稀缺、语义控制不精确和术语异构性三大挑战。
- 方法要点：采用多流控制，包括原始文本、高级语义流和原型流，以提升生成质量与可控性。
- 实验或效果：在Patho-FID上达到80.9，比次优方法提升51%，语义控制接近真实图像水平。

## 摘要（原文）

> In computational pathology, understanding and generation have evolved along disparate paths: advanced understanding models already exhibit diagnostic-level competence, whereas generative models largely simulate pixels. Progress remains hindered by three coupled factors: the scarcity of large, high-quality image-text corpora; the lack of precise, fine-grained semantic control, which forces reliance on non-semantic cues; and terminological heterogeneity, where diverse phrasings for the same diagnostic concept impede reliable text conditioning. We introduce UniPath, a semantics-driven pathology image generation framework that leverages mature diagnostic understanding to enable controllable generation. UniPath implements Multi-Stream Control: a Raw-Text stream; a High-Level Semantics stream that uses learnable queries to a frozen pathology MLLM to distill paraphrase-robust Diagnostic Semantic Tokens and to expand prompts into diagnosis-aware attribute bundles; and a Prototype stream that affords component-level morphological control via a prototype bank. On the data front, we curate a 2.65M image-text corpus and a finely annotated, high-quality 68K subset to alleviate data scarcity. For a comprehensive assessment, we establish a four-tier evaluation hierarchy tailored to pathology. Extensive experiments demonstrate UniPath's SOTA performance, including a Patho-FID of 80.9 (51% better than the second-best) and fine-grained semantic control achieving 98.7% of the real-image. The meticulously curated datasets, complete source code, and pre-trained model weights developed in this study will be made openly accessible to the public.

