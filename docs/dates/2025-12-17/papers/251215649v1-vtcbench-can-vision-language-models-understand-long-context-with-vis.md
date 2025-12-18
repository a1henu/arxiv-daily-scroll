---
layout: default
title: VTCBench: Can Vision-Language Models Understand Long Context with Vision-Text Compression?
---

# VTCBench: Can Vision-Language Models Understand Long Context with Vision-Text Compression?
**arXiv**：[2512.15649v1](https://arxiv.org/abs/2512.15649) · [PDF](https://arxiv.org/pdf/2512.15649.pdf)  
**作者**：Hongbo Zhao, Meng Wang, Fei Zhu, Wenzhuo Liu, Bolin Ni, Fanhu Zeng, Gaofeng Meng, Zhaoxiang Zhang  

**一句话要点**：提出VTCBench基准以评估视觉语言模型在视觉文本压缩下的长上下文理解能力

**关键词**：视觉文本压缩, 长上下文理解, 视觉语言模型, 基准评估, 信息检索, 对话记忆

## 3 点简述
- 核心问题：视觉文本压缩（VTC）对视觉语言模型长上下文理解能力的影响未知
- 方法要点：建立首个VTC基准，包含检索、推理和记忆三个评估设置
- 实验或效果：评估显示多数模型在VTC压缩信息下长上下文理解能力较差

## 摘要（原文）

> The computational and memory overheads associated with expanding the context window of LLMs severely limit their scalability. A noteworthy solution is vision-text compression (VTC), exemplified by frameworks like DeepSeek-OCR and Glyph, which convert long texts into dense 2D visual representations, thereby achieving token compression ratios of 3x-20x. However, the impact of this high information density on the core long-context capabilities of vision-language models (VLMs) remains under-investigated. To address this gap, we introduce the first benchmark for VTC and systematically assess the performance of VLMs across three long-context understanding settings: VTC-Retrieval, which evaluates the model's ability to retrieve and aggregate information; VTC-Reasoning, which requires models to infer latent associations to locate facts with minimal lexical overlap; and VTC-Memory, which measures comprehensive question answering within long-term dialogue memory. Furthermore, we establish the VTCBench-Wild to simulate diverse input scenarios.We comprehensively evaluate leading open-source and proprietary models on our benchmarks. The results indicate that, despite being able to decode textual information (e.g., OCR) well, most VLMs exhibit a surprisingly poor long-context understanding ability with VTC-compressed information, failing to capture long associations or dependencies in the context.This study provides a deep understanding of VTC and serves as a foundation for designing more efficient and scalable VLMs.

