---
layout: default
title: Comprehension of Multilingual Expressions Referring to Target Objects in Visual Inputs
---

# Comprehension of Multilingual Expressions Referring to Target Objects in Visual Inputs
**arXiv**：[2511.11427v1](https://arxiv.org/abs/2511.11427) · [PDF](https://arxiv.org/pdf/2511.11427.pdf)  
**作者**：Francisco Nogueira, Alexandre Bernardino, Bruno Martins  

**一句话要点**：提出多语言数据集与注意力锚定架构以解决多语言指代表达理解问题

**关键词**：多语言指代表达理解, 注意力锚定架构, 机器翻译数据集, 视觉语言模型, 多语言评估

## 3 点简述
- 核心问题：指代表达理解研究以英语为中心，难以满足多语言部署需求。
- 方法要点：构建统一多语言数据集，并设计基于注意力锚定的神经网络架构。
- 实验或效果：在RefCOCO多语言评估中准确率达86.9%，性能跨语言一致。

## 摘要（原文）

> Referring Expression Comprehension (REC) requires models to localize objects in images based on natural language descriptions. Research on the area remains predominantly English-centric, despite increasing global deployment demands. This work addresses multilingual REC through two main contributions. First, we construct a unified multilingual dataset spanning 10 languages, by systematically expanding 12 existing English REC benchmarks through machine translation and context-based translation enhancement. The resulting dataset comprises approximately 8 million multilingual referring expressions across 177,620 images, with 336,882 annotated objects. Second, we introduce an attention-anchored neural architecture that uses multilingual SigLIP2 encoders. Our attention-based approach generates coarse spatial anchors from attention distributions, which are subsequently refined through learned residuals. Experimental evaluation demonstrates competitive performance on standard benchmarks, e.g. achieving 86.9% accuracy at IoU@50 on RefCOCO aggregate multilingual evaluation, compared to an English-only result of 91.3%. Multilingual evaluation shows consistent capabilities across languages, establishing the practical feasibility of multilingual visual grounding systems. The dataset and model are available at $\href{https://multilingual.franreno.com}{multilingual.franreno.com}$.

