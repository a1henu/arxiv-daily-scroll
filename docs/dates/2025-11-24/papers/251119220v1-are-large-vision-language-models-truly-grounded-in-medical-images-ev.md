---
layout: default
title: Are Large Vision Language Models Truly Grounded in Medical Images? Evidence from Italian Clinical Visual Question Answering
---

# Are Large Vision Language Models Truly Grounded in Medical Images? Evidence from Italian Clinical Visual Question Answering
**arXiv**：[2511.19220v1](https://arxiv.org/abs/2511.19220) · [PDF](https://arxiv.org/pdf/2511.19220.pdf)  
**作者**：Federico Felizzi, Olivia Riccomi, Michele Ferramola, Francesco Andrea Causio, Manuel Del Medico, Vittorio De Vita, Lorenzo De Mori, Alessandra Piscitelli Pietro Eric Risuleo, Bianca Destro Castaniti, Antonio Cristiano Alessia Longo, Luigi De Angelis, Mariapia Vassalli, Marcello Di Pumpo  

**一句话要点**：评估大型视觉语言模型在意大利医学视觉问答中的视觉依赖性，揭示模型差异。

**关键词**：视觉语言模型, 医学视觉问答, 视觉依赖性评估, 模型鲁棒性, 意大利数据集

## 3 点简述
- 核心问题：大型视觉语言模型是否真正依赖医学图像进行视觉问答。
- 方法要点：使用空白图像替换测试模型视觉依赖性，分析四种前沿模型。
- 实验效果：GPT-4o视觉依赖性最强，其他模型依赖文本捷径，准确率下降不一。

## 摘要（原文）

> Large vision language models (VLMs) have achieved impressive performance on medical visual question answering benchmarks, yet their reliance on visual information remains unclear. We investigate whether frontier VLMs demonstrate genuine visual grounding when answering Italian medical questions by testing four state-of-the-art models: Claude Sonnet 4.5, GPT-4o, GPT-5-mini, and Gemini 2.0 flash exp. Using 60 questions from the EuropeMedQA Italian dataset that explicitly require image interpretation, we substitute correct medical images with blank placeholders to test whether models truly integrate visual and textual information. Our results reveal striking variability in visual dependency: GPT-4o shows the strongest visual grounding with a 27.9pp accuracy drop (83.2% [74.6%, 91.7%] to 55.3% [44.1%, 66.6%]), while GPT-5-mini, Gemini, and Claude maintain high accuracy with modest drops of 8.5pp, 2.4pp, and 5.6pp respectively. Analysis of model-generated reasoning reveals confident explanations for fabricated visual interpretations across all models, suggesting varying degrees of reliance on textual shortcuts versus genuine visual analysis. These findings highlight critical differences in model robustness and the need for rigorous evaluation before clinical deployment.

