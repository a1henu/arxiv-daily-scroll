---
layout: default
title: FormuLLA: A Large Language Model Approach to Generating Novel 3D Printable Formulations
---

# FormuLLA: A Large Language Model Approach to Generating Novel 3D Printable Formulations
**arXiv**：[2601.02071v1](https://arxiv.org/abs/2601.02071) · [PDF](https://arxiv.org/pdf/2601.02071.pdf)  
**作者**：Adeshola Okubena, Yusuf Ali Mohammed, Moe Elbadawi  

**一句话要点**：提出FormuLLA方法，利用大语言模型生成3D打印药物配方，以解决个性化制剂开发挑战。

**关键词**：药物3D打印, 大语言模型微调, 辅料推荐, 丝材机械性能预测, 灾难性遗忘, 个性化制剂

## 3 点简述
- 核心问题：现有AI方法在药物3D打印中范围狭窄，未全面应对配方挑战，需提升通用推理能力。
- 方法要点：基于1400多个配方的数据集微调四种大语言模型，用于推荐辅料和预测丝材机械性能。
- 实验或效果：Llama2模型在辅料推荐上表现最佳，但模型选择和参数化显著影响性能，小模型易出现灾难性遗忘。

## 摘要（原文）

> Pharmaceutical three-dimensional (3D) printing is an advanced fabrication technology with the potential to enable truly personalised dosage forms. Recent studies have integrated artificial intelligence (AI) to accelerate formulation and process development, drastically transforming current approaches to pharmaceutical 3D printing. To date, most AI-driven efforts remain narrowly focused, while failing to account for the broader formulation challenges inherent to the technology. Recent advances in AI have introduced artificial general intelligence concepts, wherein systems extend beyond conventional predictive modelling toward more generalised, human-like reasoning. In this work, we investigate the application of large language models (LLMs), fine-tuned on a fused deposition modelling (FDM) dataset comprising over 1400 formulations, to recommend suitable excipients based on active pharmaceutical ingredient (API) dose, and predict filament mechanical properties. Four LLM architectures were fine-tuned, with systematic evaluation of both fine-tuning and generative parameter configurations. Our results demonstrate that Llama2 was best suited for recommending excipients for FDM formulations. Additionally, model selection and parameterisation significantly influence performance, with smaller LLMs exhibiting instances of catastrophic forgetting. Furthermore, we demonstrate: (i) even with relatively small dataset of over 1400 formulations, it can lead to model catastrophic forgetting; (ii) standard LLM metrics only evaluate linguistic performance but not formulation processability; and (iii) LLMs trained on biomedically-related data do not always produce the best results. Addressing these challenges is essential to advancing LLMs beyond linguistic proficiency and toward reliable systems for pharmaceutical formulation development.

