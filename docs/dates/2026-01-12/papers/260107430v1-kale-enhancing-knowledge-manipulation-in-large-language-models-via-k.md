---
layout: default
title: KALE: Enhancing Knowledge Manipulation in Large Language Models via Knowledge-aware Learning
---

# KALE: Enhancing Knowledge Manipulation in Large Language Models via Knowledge-aware Learning
**arXiv**：[2601.07430v1](https://arxiv.org/abs/2601.07430) · [PDF](https://arxiv.org/pdf/2601.07430.pdf)  
**作者**：Qitan Lv, Tianyu Liu, Qiaosheng Zhang, Xingcheng Xu, Chaochao Lu  

**一句话要点**：提出KALE框架，通过知识图谱增强大语言模型的知识操纵能力，解决已知但错误回答的问题。

**关键词**：知识图谱, 大语言模型, 知识操纵, 推理增强, 微调框架

## 3 点简述
- 核心问题：大语言模型在知识操纵中存在已知但错误回答现象，即拥有相关知识却无法正确利用。
- 方法要点：KALE利用知识图谱合成高质量推理路径，并通过知识感知微调最小化预测差异来内部化推理。
- 实验或效果：在八个基准测试和六个大语言模型上验证，最高提升准确率11.72%，平均提升4.18%。

## 摘要（原文）

> Despite the impressive performance of large language models (LLMs) pretrained on vast knowledge corpora, advancing their knowledge manipulation-the ability to effectively recall, reason, and transfer relevant knowledge-remains challenging. Existing methods mainly leverage Supervised Fine-Tuning (SFT) on labeled datasets to enhance LLMs' knowledge manipulation ability. However, we observe that SFT models still exhibit the known&incorrect phenomenon, where they explicitly possess relevant knowledge for a given question but fail to leverage it for correct answers. To address this challenge, we propose KALE (Knowledge-Aware LEarning)-a post-training framework that leverages knowledge graphs (KGs) to generate high-quality rationales and enhance LLMs' knowledge manipulation ability. Specifically, KALE first introduces a Knowledge-Induced (KI) data synthesis method that efficiently extracts multi-hop reasoning paths from KGs to generate high-quality rationales for question-answer pairs. Then, KALE employs a Knowledge-Aware (KA) fine-tuning paradigm that enhances knowledge manipulation by internalizing rationale-guided reasoning through minimizing the KL divergence between predictions with and without rationales. Extensive experiments on eight popular benchmarks across six different LLMs demonstrate the effectiveness of KALE, achieving accuracy improvements of up to 11.72% and an average of 4.18%.

