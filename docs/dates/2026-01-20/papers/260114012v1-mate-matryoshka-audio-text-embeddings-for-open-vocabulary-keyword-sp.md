---
layout: default
title: MATE: Matryoshka Audio-Text Embeddings for Open-Vocabulary Keyword Spotting
---

# MATE: Matryoshka Audio-Text Embeddings for Open-Vocabulary Keyword Spotting
**arXiv**：[2601.14012v1](https://arxiv.org/abs/2601.14012) · [PDF](https://arxiv.org/pdf/2601.14012.pdf)  
**作者**：Youngmoon Jung, Myunghun Jung, Joon-Young Yang, Yong-Hyeok Lee, Jaeyoung Roh, Hoon-Young Cho  

**一句话要点**：提出MATE框架，通过嵌套子嵌入实现多粒度音频-文本匹配，用于开放词汇关键词检测。

**关键词**：开放词汇关键词检测, 音频-文本嵌入, 嵌套嵌入, PCA对齐, 双编码器框架

## 3 点简述
- 核心问题：现有开放词汇关键词检测方法使用固定维度嵌入，限制了匹配灵活性。
- 方法要点：采用双编码器框架，通过PCA引导的前缀对齐，在单个向量中编码多个粒度嵌入。
- 实验或效果：在WSJ和LibriPhrase数据集上达到先进性能，无推理开销。

## 摘要（原文）

> Open-vocabulary keyword spotting (KWS) with text-based enrollment has emerged as a flexible alternative to fixed-phrase triggers. Prior utterance-level matching methods, from an embedding-learning standpoint, learn embeddings at a single fixed dimensionality. We depart from this design and propose Matryoshka Audio-Text Embeddings (MATE), a dual-encoder framework that encodes multiple embedding granularities within a single vector via nested sub-embeddings ("prefixes"). Specifically, we introduce a PCA-guided prefix alignment: PCA-compressed versions of the full text embedding for each prefix size serve as teacher targets to align both audio and text prefixes. This alignment concentrates salient keyword cues in lower-dimensional prefixes, while higher dimensions add detail. MATE is trained with standard deep metric learning objectives for audio-text KWS, and is loss-agnostic. To our knowledge, this is the first application of matryoshka-style embeddings to KWS, achieving state-of-the-art results on WSJ and LibriPhrase without any inference overhead.

