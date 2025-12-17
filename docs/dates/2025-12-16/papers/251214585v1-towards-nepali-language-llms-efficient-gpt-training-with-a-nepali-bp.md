---
layout: default
title: Towards Nepali-language LLMs: Efficient GPT training with a Nepali BPE tokenizer
---

# Towards Nepali-language LLMs: Efficient GPT training with a Nepali BPE tokenizer
**arXiv**：[2512.14585v1](https://arxiv.org/abs/2512.14585) · [PDF](https://arxiv.org/pdf/2512.14585.pdf)  
**作者**：Adarsha Shrestha, Basanta Pokharel, Binit Shrestha, Smriti Adhikari, Dinesh Gothe  

**一句话要点**：提出基于GPT-2的尼泊尔语大语言模型，采用定制BPE分词器和训练优化策略以提升生成能力。

**关键词**：尼泊尔语大语言模型, BPE分词器, GPT-2训练优化, 低资源语言处理, 文本生成

## 3 点简述
- 针对尼泊尔语作为低资源语言，面临复杂语法和语料不足的NLP挑战。
- 采用定制16k BPE分词器、GPT-3启发训练策略和FlashAttention优化训练效率。
- 模型在尼泊尔语新闻数据集上预训练后，生成连贯文本，困惑度达21.80。

## 摘要（原文）

> Nepali, a low-resource language spoken by over 32 million people, continues to face challenges in natural language processing (NLP) due to its complex grammar, agglutinative morphology, and limited availability of high-quality corpora. Most efforts to date have centered on basic encoder architectures; they remain insufficient for Nepali-specific text generation. This study presents a GPT-2-based Nepali language model trained using several training strategies inspired by GPT-3, including optimized learning rate schedules, batch scaling, and architectural refinements. A custom 16k Byte-Pair Encoding (BPE) tokenizer was trained exclusively on Nepali text to ensure more consistent segmentation and improved input representation. The model was pretrained on a combined dataset comprising a 10.75GB cleaned NepBERTa corpus and additional web-scraped Nepali news articles. FlashAttention was integrated to reduce memory usage and stabilize training. After two epochs, the model achieved a training loss of 3.168177, a validation loss of 3.081982, and a final perplexity of 21.80, demonstrating its capability to generate coherent Nepali news-style text.

