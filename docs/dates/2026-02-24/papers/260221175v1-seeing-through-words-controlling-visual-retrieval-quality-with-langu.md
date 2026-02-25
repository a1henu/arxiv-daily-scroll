---
layout: default
title: Seeing Through Words: Controlling Visual Retrieval Quality with Language Models
---

# Seeing Through Words: Controlling Visual Retrieval Quality with Language Models
**arXiv**：[2602.21175v1](https://arxiv.org/abs/2602.21175) · [PDF](https://arxiv.org/pdf/2602.21175.pdf)  
**作者**：Jianglin Lu, Simon Jenni, Kushal Kafle, Jing Shi, Handong Zhao, Yun Fu  

**一句话要点**：提出质量可控检索范式，通过语言模型扩展短查询以提升文本到图像检索质量

**关键词**：文本到图像检索, 质量可控检索, 查询扩展, 语言模型, 视觉语言模型, 美学评分

## 3 点简述
- 核心问题：短查询在文本到图像检索中语义模糊，缺乏质量控制，导致结果不理想。
- 方法要点：利用生成语言模型扩展查询，结合离散化质量级别（相关性和美学评分）进行质量感知的查询丰富。
- 实验或效果：实验显示方法显著改进检索结果，提供有效质量控制，兼容现有视觉语言模型。

## 摘要（原文）

> Text-to-image retrieval is a fundamental task in vision-language learning, yet in real-world scenarios it is often challenged by short and underspecified user queries. Such queries are typically only one or two words long, rendering them semantically ambiguous, prone to collisions across diverse visual interpretations, and lacking explicit control over the quality of retrieved images. To address these issues, we propose a new paradigm of quality-controllable retrieval, which enriches short queries with contextual details while incorporating explicit notions of image quality. Our key idea is to leverage a generative language model as a query completion function, extending underspecified queries into descriptive forms that capture fine-grained visual attributes such as pose, scene, and aesthetics. We introduce a general framework that conditions query completion on discretized quality levels, derived from relevance and aesthetic scoring models, so that query enrichment is not only semantically meaningful but also quality-aware. The resulting system provides three key advantages: 1) flexibility, it is compatible with any pretrained vision-language model (VLMs) without modification; 2) transparency, enriched queries are explicitly interpretable by users; and 3) controllability, enabling retrieval results to be steered toward user-preferred quality levels. Extensive experiments demonstrate that our proposed approach significantly improves retrieval results and provides effective quality control, bridging the gap between the expressive capacity of modern VLMs and the underspecified nature of short user queries. Our code is available at https://github.com/Jianglin954/QCQC.

