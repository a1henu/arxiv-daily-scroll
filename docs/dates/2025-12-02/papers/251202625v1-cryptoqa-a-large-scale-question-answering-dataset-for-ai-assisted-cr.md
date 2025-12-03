---
layout: default
title: CryptoQA: A Large-scale Question-answering Dataset for AI-assisted Cryptography
---

# CryptoQA: A Large-scale Question-answering Dataset for AI-assisted Cryptography
**arXiv**：[2512.02625v1](https://arxiv.org/abs/2512.02625) · [PDF](https://arxiv.org/pdf/2512.02625.pdf)  
**作者**：Mayar Elfares, Pascal Reisert, Tilman Dietz, Manpa Barman, Ahmed Zaki, Ralf Küsters, Andreas Bulling  

**一句话要点**：提出CryptoQA数据集以评估和训练大语言模型在密码学任务中的能力

**关键词**：密码学问答数据集, 大语言模型评估, 数学推理能力, 模型微调, 对抗样本鲁棒性

## 3 点简述
- 核心问题：大语言模型在密码学等需要深度推理和数学分析的任务中表现不佳，缺乏合适的数据集进行评估和训练。
- 方法要点：构建首个大规模密码学问答数据集CryptoQA，包含超过两百万对问答和上下文元数据，用于测试和训练模型。
- 实验或效果：基准测试15个先进大语言模型，揭示其在形式推理和精确数学知识方面的显著缺陷，并通过微调展示性能提升。

## 摘要（原文）

> Large language models (LLMs) excel at many general-purpose natural language processing tasks. However, their ability to perform deep reasoning and mathematical analysis, particularly for complex tasks as required in cryptography, remains poorly understood, largely due to the lack of suitable data for evaluation and training. To address this gap, we present CryptoQA, the first large-scale question-answering (QA) dataset specifically designed for cryptography. CryptoQA contains over two million QA pairs drawn from curated academic sources, along with contextual metadata that can be used to test the cryptographic capabilities of LLMs and to train new LLMs on cryptographic tasks. We benchmark 15 state-of-the-art LLMs on CryptoQA, evaluating their factual accuracy, mathematical reasoning, consistency, referencing, backward reasoning, and robustness to adversarial samples. In addition to quantitative metrics, we provide expert reviews that qualitatively assess model outputs and establish a gold-standard baseline. Our results reveal significant performance deficits of LLMs, particularly on tasks that require formal reasoning and precise mathematical knowledge. This shows the urgent need for LLM assistants tailored to cryptography research and development. We demonstrate that, by using CryptoQA, LLMs can be fine-tuned to exhibit better performance on cryptographic tasks.

