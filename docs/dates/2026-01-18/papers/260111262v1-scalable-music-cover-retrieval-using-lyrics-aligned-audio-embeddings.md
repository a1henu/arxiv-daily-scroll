---
layout: default
title: Scalable Music Cover Retrieval Using Lyrics-Aligned Audio Embeddings
---

# Scalable Music Cover Retrieval Using Lyrics-Aligned Audio Embeddings
**arXiv**：[2601.11262v1](https://arxiv.org/abs/2601.11262) · [PDF](https://arxiv.org/pdf/2601.11262.pdf)  
**作者**：Joanne Affolter, Benjamin Martin, Elena V. Epure, Gabriel Meseguer-Brocal, Frédéric Kaplan  

**一句话要点**：提出LIVI方法，利用歌词对齐音频嵌入实现高效音乐翻唱检索

**关键词**：音乐翻唱检索, 歌词对齐, 音频嵌入, 轻量化模型, 版本识别

## 3 点简述
- 核心问题：音乐翻唱检索需处理音频变化，现有方法依赖复杂谐波特征，计算成本高
- 方法要点：LIVI在训练中结合转录和文本嵌入监督，推理时移除转录步骤以提升效率
- 实验或效果：检索准确率媲美或优于谐波系统，同时保持轻量化和高效性

## 摘要（原文）

> Music Cover Retrieval, also known as Version Identification, aims to recognize distinct renditions of the same underlying musical work, a task central to catalog management, copyright enforcement, and music retrieval. State-of-the-art approaches have largely focused on harmonic and melodic features, employing increasingly complex audio pipelines designed to be invariant to musical attributes that often vary widely across covers. While effective, these methods demand substantial training time and computational resources. By contrast, lyrics constitute a strong invariant across covers, though their use has been limited by the difficulty of extracting them accurately and efficiently from polyphonic audio. Early methods relied on simple frameworks that limited downstream performance, while more recent systems deliver stronger results but require large models integrated within complex multimodal architectures. We introduce LIVI (Lyrics-Informed Version Identification), an approach that seeks to balance retrieval accuracy with computational efficiency. First, LIVI leverages supervision from state-of-the-art transcription and text embedding models during training to achieve retrieval accuracy on par with--or superior to--harmonic-based systems. Second, LIVI remains lightweight and efficient by removing the transcription step at inference, challenging the dominance of complexity-heavy pipelines.

