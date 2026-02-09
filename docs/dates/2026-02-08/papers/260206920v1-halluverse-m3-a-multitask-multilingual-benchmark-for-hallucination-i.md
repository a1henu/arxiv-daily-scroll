---
layout: default
title: Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs
---

# Halluverse-M^3: A multitask multilingual benchmark for hallucination in LLMs
**arXiv**：[2602.06920v1](https://arxiv.org/abs/2602.06920) · [PDF](https://arxiv.org/pdf/2602.06920.pdf)  
**作者**：Samir Abdaljalil, Parichit Sharma, Erchin Serpedin, Hasan Kurban  

**一句话要点**：提出Halluverse-M^3数据集以评估多语言多任务下大语言模型的幻觉问题

**关键词**：幻觉检测, 多语言基准, 生成任务, 数据集构建, 大语言模型评估, 事实一致性

## 3 点简述
- 核心问题：大语言模型在多语言和生成任务中幻觉持续存在，缺乏系统评估基准。
- 方法要点：构建覆盖四语言、两任务、三幻觉类别的数据集，通过可控编辑和人工验证确保质量。
- 实验或效果：评估显示问答任务较易，句子级幻觉挑战大，英语表现最佳，印地语检测准确率最低。

## 摘要（原文）

> Hallucinations in large language models remain a persistent challenge, particularly in multilingual and generative settings where factual consistency is difficult to maintain. While recent models show strong performance on English-centric benchmarks, their behavior across languages, tasks, and hallucination types is not yet well understood. In this work, we introduce Halluverse-M^3, a dataset designed to enable systematic analysis of hallucinations across multiple languages, multiple generation tasks, and multiple hallucination categories. Halluverse-M^3 covers four languages, English, Arabic, Hindi, and Turkish, and supports two generation tasks: question answering and dialogue summarization. The dataset explicitly distinguishes between entity-level, relation-level, and sentence-level hallucinations. Hallucinated outputs are constructed through a controlled editing process and validated by human annotators, ensuring clear alignment between original content and hallucinated generations. Using this dataset, we evaluate a diverse set of contemporary open-source and proprietary language models on fine-grained hallucination detection. Our results show that question answering is consistently easier than dialogue summarization, while sentence-level hallucinations remain challenging even for the strongest models. Performance is highest in English and degrades in lower-resource languages, with Hindi exhibiting the lowest detection accuracy. Overall, Halluverse-M^3 provides a realistic and challenging benchmark for studying hallucinations in multilingual, multi-task settings. We release the dataset to support future research on hallucination detection and mitigation\footnote{https://huggingface.co/datasets/sabdalja/HalluVerse-M3}.

