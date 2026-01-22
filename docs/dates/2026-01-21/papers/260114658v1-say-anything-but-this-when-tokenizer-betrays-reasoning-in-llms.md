---
layout: default
title: Say Anything but This: When Tokenizer Betrays Reasoning in LLMs
---

# Say Anything but This: When Tokenizer Betrays Reasoning in LLMs
**arXiv**：[2601.14658v1](https://arxiv.org/abs/2601.14658) · [PDF](https://arxiv.org/pdf/2601.14658.pdf)  
**作者**：Navid Ayoobi, Marcus I Armstrong, Arjun Mukherjee  

**一句话要点**：提出分词一致性探针以揭示分词器对LLM推理的背叛，通过分析幻影编辑现象

**关键词**：大语言模型, 分词器缺陷, 推理脆弱性, 幻影编辑, 分词一致性探针, 表示不匹配

## 3 点简述
- 核心问题：分词器非唯一编码导致LLM推理脆弱，内部表示与文本语义不匹配
- 方法要点：设计简单替换任务，隔离分词器-去分词器缺陷，避免知识或参数干扰
- 实验或效果：在开源LLM上测试超11000次，发现幻影编辑率显著，分类八种系统分词器伪影

## 摘要（原文）

> Large language models (LLMs) reason over discrete token ID sequences, yet modern subword tokenizers routinely produce non-unique encodings: multiple token ID sequences can detokenize to identical surface strings. This representational mismatch creates an unmeasured fragility wherein reasoning processes can fail. LLMs may treat two internal representations as distinct "words" even when they are semantically identical at the text level. In this work, we show that tokenization can betray LLM reasoning through one-to-many token ID mappings. We introduce a tokenization-consistency probe that requires models to replace designated target words in context while leaving all other content unchanged. The task is intentionally simple at the surface level, enabling us to attribute failures to tokenizer-detokenizer artifacts rather than to knowledge gaps or parameter limitations. Through analysis of over 11000 replacement trials across state-of-the-art open-source LLMs, we find a non-trivial rate of outputs exhibit phantom edits: cases where models operate under the illusion of correct reasoning, a phenomenon arising from tokenizer-induced representational defects. We further analyze these cases and provide a taxonomy of eight systematic tokenizer artifacts, including whitespace-boundary shifts and intra-word resegmentation. These findings indicate that part of apparent reasoning deficiency originates in the tokenizer layer, motivating tokenizer-level remedies before incurring the cost of training ever-larger models on ever-larger corpora.

