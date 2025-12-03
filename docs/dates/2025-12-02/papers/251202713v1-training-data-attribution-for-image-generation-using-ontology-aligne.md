---
layout: default
title: Training Data Attribution for Image Generation using Ontology-Aligned Knowledge Graphs
---

# Training Data Attribution for Image Generation using Ontology-Aligned Knowledge Graphs
**arXiv**：[2512.02713v1](https://arxiv.org/abs/2512.02713) · [PDF](https://arxiv.org/pdf/2512.02713.pdf)  
**作者**：Theodoros Aivalis, Iraklis A. Klampanos, Antonis Troumpoukis, Joemon M. Jose  

**一句话要点**：提出基于本体对齐知识图谱的训练数据归因框架，以增强图像生成模型的透明度和可解释性。

**关键词**：训练数据归因, 知识图谱构建, 多模态大语言模型, 图像生成透明度, 本体对齐

## 3 点简述
- 核心问题：生成模型透明度不足，难以追踪训练数据对输出的贡献，引发版权和问责担忧。
- 方法要点：利用多模态大语言模型从图像提取结构化三元组，构建本体对齐知识图谱，比较生成与训练图像的图谱以归因影响。
- 实验或效果：通过局部模型遗忘实验和风格特定实验验证框架，支持版权分析和AI可解释性。

## 摘要（原文）

> As generative models become powerful, concerns around transparency, accountability, and copyright violations have intensified. Understanding how specific training data contributes to a model's output is critical. We introduce a framework for interpreting generative outputs through the automatic construction of ontologyaligned knowledge graphs (KGs). While automatic KG construction from natural text has advanced, extracting structured and ontology-consistent representations from visual content remains challenging -- due to the richness and multi-object nature of images. Leveraging multimodal large language models (LLMs), our method extracts structured triples from images, aligned with a domain-specific ontology. By comparing the KGs of generated and training images, we can trace potential influences, enabling copyright analysis, dataset transparency, and interpretable AI. We validate our method through experiments on locally trained models via unlearning, and on large-scale models through a style-specific experiment. Our framework supports the development of AI systems that foster human collaboration, creativity and stimulate curiosity.

