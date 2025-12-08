---
layout: default
title: Grounded Multilingual Medical Reasoning for Question Answering with Large Language Models
---

# Grounded Multilingual Medical Reasoning for Question Answering with Large Language Models
**arXiv**：[2512.05658v1](https://arxiv.org/abs/2512.05658) · [PDF](https://arxiv.org/pdf/2512.05658.pdf)  
**作者**：Pietro Ferrazzi, Aitor Soroa, Rodrigo Agerri  

**一句话要点**：提出基于检索增强生成的多语言医疗推理轨迹方法，以提升大型语言模型在医疗问答中的可靠性和性能。

**关键词**：医疗问答, 多语言推理, 检索增强生成, 大型语言模型, 监督微调, 上下文学习

## 3 点简述
- 核心问题：现有医疗问答方法多聚焦英语，依赖通用大型语言模型蒸馏，医疗知识可靠性存疑。
- 方法要点：使用检索增强生成技术，基于维基百科医疗信息，生成英语、意大利语和西班牙语的推理轨迹。
- 实验或效果：在医疗问答基准测试中，通过上下文学习和监督微调，推理轨迹提升了性能，在8B参数模型中达到先进水平。

## 摘要（原文）

> Large Language Models (LLMs) with reasoning capabilities have recently demonstrated strong potential in medical Question Answering (QA). Existing approaches are largely English-focused and primarily rely on distillation from general-purpose LLMs, raising concerns about the reliability of their medical knowledge. In this work, we present a method to generate multilingual reasoning traces grounded in factual medical knowledge. We produce 500k traces in English, Italian, and Spanish, using a retrievalaugmented generation approach over medical information from Wikipedia. The traces are generated to solve medical questions drawn from MedQA and MedMCQA, which we extend to Italian and Spanish. We test our pipeline in both in-domain and outof-domain settings across Medical QA benchmarks, and demonstrate that our reasoning traces improve performance both when utilized via in-context learning (few-shot) and supervised fine-tuning, yielding state-of-the-art results among 8B-parameter LLMs. We believe that these resources can support the development of safer, more transparent clinical decision-support tools in multilingual settings. We release the full suite of resources: reasoning traces, translated QA datasets, Medical-Wikipedia, and fine-tuned models.

