---
layout: default
title: Multimodal In-context Learning for ASR of Low-resource Languages
---

# Multimodal In-context Learning for ASR of Low-resource Languages
**arXiv**：[2601.05707v1](https://arxiv.org/abs/2601.05707) · [PDF](https://arxiv.org/pdf/2601.05707.pdf)  
**作者**：Zhaolin Li, Jan Niehues  

**一句话要点**：提出多模态上下文学习以提升低资源语言自动语音识别性能

**关键词**：多模态上下文学习, 低资源语言ASR, 跨语言迁移, 语音大模型, 注意力机制分析

## 3 点简述
- 研究多模态上下文学习在未见语言自动语音识别中的应用，利用语音和文本模态
- 通过跨语言迁移学习提升效率，无需目标语言训练数据
- 结合强声学模型与语音大模型，基于上下文学习选择假设，改善识别效果

## 摘要（原文）

> Automatic speech recognition (ASR) still covers only a small fraction of the world's languages, mainly due to supervised data scarcity. In-context learning (ICL) with large language models (LLMs) addresses this problem, but prior work largely focuses on high-resource languages covered during training and text-only settings. This paper investigates whether speech LLMs can learn unseen languages with multimodal ICL (MICL), and how this learning can be used to improve ASR. We conduct experiments with two speech LLMs, Phi-4 and Qwen3-Omni, on three diverse endangered languages. Firstly, we find that MICL is effective for unseen languages, leveraging both speech and text modalities. We further show that cross-lingual transfer learning improves MICL efficiency on target languages without training on them. Moreover, we analyze attention patterns to interpret MICL mechanisms, and we observe layer-dependent preferences between audio and text context, with an overall bias towards text. Finally, we show that prompt-based ASR with speech LLMs performs poorly on unseen languages, motivating a simple ASR system that combines a stronger acoustic model with a speech LLM via MICL-based selection of acoustic hypotheses. Results show that MICL consistently improves ASR performance, and that cross-lingual transfer learning matches or outperforms corpus-trained language models without using target-language data. Our code is publicly available.

