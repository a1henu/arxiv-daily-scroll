---
layout: default
title: Concept-Enhanced Multimodal RAG: Towards Interpretable and Accurate Radiology Report Generation
---

# Concept-Enhanced Multimodal RAG: Towards Interpretable and Accurate Radiology Report Generation
**arXiv**：[2602.15650v1](https://arxiv.org/abs/2602.15650) · [PDF](https://arxiv.org/pdf/2602.15650.pdf)  
**作者**：Marco Salmè, Federico Siciliano, Fabrizio Silvestri, Paolo Soda, Rosa Sicilia, Valerio Guarrasi  

**一句话要点**：提出概念增强多模态RAG框架，以提升放射学报告生成的解释性和准确性

**关键词**：放射学报告生成, 多模态检索增强生成, 临床概念解释, 视觉语言模型, 医学影像分析

## 3 点简述
- 核心问题：放射学报告生成中视觉语言模型缺乏解释性且易产生与影像证据不符的幻觉
- 方法要点：将视觉表示分解为可解释临床概念，并与多模态检索增强生成结合
- 实验或效果：在MIMIC-CXR和IU X-Ray数据集上，临床准确性和标准NLP指标均优于传统方法

## 摘要（原文）

> Radiology Report Generation (RRG) through Vision-Language Models (VLMs) promises to reduce documentation burden, improve reporting consistency, and accelerate clinical workflows. However, their clinical adoption remains limited by the lack of interpretability and the tendency to hallucinate findings misaligned with imaging evidence. Existing research typically treats interpretability and accuracy as separate objectives, with concept-based explainability techniques focusing primarily on transparency, while Retrieval-Augmented Generation (RAG) methods targeting factual grounding through external retrieval. We present Concept-Enhanced Multimodal RAG (CEMRAG), a unified framework that decomposes visual representations into interpretable clinical concepts and integrates them with multimodal RAG. This approach exploits enriched contextual prompts for RRG, improving both interpretability and factual accuracy. Experiments on MIMIC-CXR and IU X-Ray across multiple VLM architectures, training regimes, and retrieval configurations demonstrate consistent improvements over both conventional RAG and concept-only baselines on clinical accuracy metrics and standard NLP measures. These results challenge the assumed trade-off between interpretability and performance, showing that transparent visual concepts can enhance rather than compromise diagnostic accuracy in medical VLMs. Our modular design decomposes interpretability into visual transparency and structured language model conditioning, providing a principled pathway toward clinically trustworthy AI-assisted radiology.

