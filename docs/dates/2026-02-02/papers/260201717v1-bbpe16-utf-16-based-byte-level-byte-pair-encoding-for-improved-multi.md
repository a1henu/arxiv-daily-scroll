---
layout: default
title: BBPE16: UTF-16-based byte-level byte-pair encoding for improved multilingual speech recognition
---

# BBPE16: UTF-16-based byte-level byte-pair encoding for improved multilingual speech recognition
**arXiv**：[2602.01717v1](https://arxiv.org/abs/2602.01717) · [PDF](https://arxiv.org/pdf/2602.01717.pdf)  
**作者**：Hyunsik Kim, Haeri Kim, Munhak Lee, Kyungmin Lee  

**一句话要点**：提出BBPE16，一种基于UTF-16的字节级字节对编码，以改进多语言语音识别中的标记化效率。

**关键词**：多语言语音识别, 字节级字节对编码, UTF-16编码, 标记化优化, 计算效率提升

## 3 点简述
- 核心问题：UTF-8字节级BPE在多语言ASR中，对非拉丁文字（如中文）产生变长编码，增加计算和内存负担。
- 方法要点：采用UTF-16编码，使大多数现代文字统一为2字节单元，提升跨语言标记共享，保持语言无关性。
- 实验或效果：在单语、双语、三语及持续学习ASR中，BBPE16实现相当或更高准确率，中文标记数减少达10.4%，解码迭代降低达10.3%。

## 摘要（原文）

> Multilingual automatic speech recognition (ASR) requires tokenization that efficiently covers many writing systems. Byte-level BPE (BBPE) using UTF-8 is widely adopted for its language-agnostic design and full Unicode coverage, but its variable-length encoding inflates token sequences for non-Latin scripts, such as Chinese, Japanese, and Korean (CJK). Longer sequences increase computational load and memory use. We propose BBPE16, a UTF-16-based BBPE tokenizer that represents most modern scripts with a uniform 2-byte code unit. BBPE16 preserves BBPE's language-agnostic properties while substantially improving cross-lingual token sharing. Across monolingual, bilingual, and trilingual ASR, and in a multilingual continual-learning setup, BBPE16 attains comparable or better accuracy; for Chinese, it reduces token counts by up to 10.4% and lowers decoding iterations by up to 10.3%. These reductions speed up fine-tuning and inference and decrease memory usage, making BBPE16 a practical tokenization choice for multilingual ASR.

