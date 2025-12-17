---
layout: default
title: A Comparative Analysis of Retrieval-Augmented Generation Techniques for Bengali Standard-to-Dialect Machine Translation Using LLMs
---

# A Comparative Analysis of Retrieval-Augmented Generation Techniques for Bengali Standard-to-Dialect Machine Translation Using LLMs
**arXiv**：[2512.14179v1](https://arxiv.org/abs/2512.14179) · [PDF](https://arxiv.org/pdf/2512.14179.pdf)  
**作者**：K. M. Jubair Sami, Dipto Sumit, Ariyan Hossain, Farig Sadeque  

**一句话要点**：提出两种检索增强生成管道，用于孟加拉语标准语到方言的机器翻译，以解决数据稀缺和语言变异问题。

**关键词**：检索增强生成, 孟加拉语方言翻译, 低资源机器翻译, 标准语到方言转换, 无微调方法, 语言多样性保护

## 3 点简述
- 核心问题：孟加拉语标准语到方言翻译面临数据稀缺和语言变异挑战，影响翻译质量。
- 方法要点：比较基于音频转录的管道和基于标准化句对的管道，后者利用结构化数据提升检索效果。
- 实验或效果：在六个方言上评估，句对管道显著降低词错误率，使小模型超越大模型，提供无微调解决方案。

## 摘要（原文）

> Translating from a standard language to its regional dialects is a significant NLP challenge due to scarce data and linguistic variation, a problem prominent in the Bengali language. This paper proposes and compares two novel RAG pipelines for standard-to-dialectal Bengali translation. The first, a Transcript-Based Pipeline, uses large dialect sentence contexts from audio transcripts. The second, a more effective Standardized Sentence-Pairs Pipeline, utilizes structured local\_dialect:standard\_bengali sentence pairs. We evaluated both pipelines across six Bengali dialects and multiple LLMs using BLEU, ChrF, WER, and BERTScore. Our findings show that the sentence-pair pipeline consistently outperforms the transcript-based one, reducing Word Error Rate (WER) from 76\% to 55\% for the Chittagong dialect. Critically, this RAG approach enables smaller models (e.g., Llama-3.1-8B) to outperform much larger models (e.g., GPT-OSS-120B), demonstrating that a well-designed retrieval strategy can be more crucial than model size. This work contributes an effective, fine-tuning-free solution for low-resource dialect translation, offering a practical blueprint for preserving linguistic diversity.

