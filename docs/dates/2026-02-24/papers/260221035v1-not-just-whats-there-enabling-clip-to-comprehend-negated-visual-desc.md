---
layout: default
title: Not Just What's There: Enabling CLIP to Comprehend Negated Visual Descriptions Without Fine-tuning
---

# Not Just What's There: Enabling CLIP to Comprehend Negated Visual Descriptions Without Fine-tuning
**arXiv**：[2602.21035v1](https://arxiv.org/abs/2602.21035) · [PDF](https://arxiv.org/pdf/2602.21035.pdf)  
**作者**：Junhao Xiao, Zhiyu Wu, Hao Lin, Yi Chen, Yahui Liu, Xiaoran Zhao, Zixu Wang, Zejiang He  

**一句话要点**：提出CLIPGlasses框架以增强CLIP对否定视觉描述的理解能力

**关键词**：视觉语言模型, 否定理解, 跨域泛化, 低资源学习, 相似度计算

## 3 点简述
- 核心问题：CLIP等视觉语言模型难以理解否定语义，常将肯定与否定嵌入相似。
- 方法要点：采用双阶段设计，包括解耦否定语义的Lens模块和预测排斥强度的Frame模块。
- 实验或效果：在跨域泛化中优于现有方法，低资源条件下表现更稳健。

## 摘要（原文）

> Vision-Language Models (VLMs) like CLIP struggle to understand negation, often embedding affirmatives and negatives similarly (e.g., matching "no dog" with dog images). Existing methods refine negation understanding via fine-tuning CLIP's text encoder, risking overfitting. In this work, we propose CLIPGlasses, a plug-and-play framework that enhances CLIP's ability to comprehend negated visual descriptions. CLIPGlasses adopts a dual-stage design: a Lens module disentangles negated semantics from text embeddings, and a Frame module predicts context-aware repulsion strength, which is integrated into a modified similarity computation to penalize alignment with negated semantics, thereby reducing false positive matches. Experiments show that CLIP equipped with CLIPGlasses achieves competitive in-domain performance and outperforms state-of-the-art methods in cross-domain generalization. Its superiority is especially evident under low-resource conditions, indicating stronger robustness across domains.

