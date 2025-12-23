---
layout: default
title: Brain-Grounded Axes for Reading and Steering LLM States
---

# Brain-Grounded Axes for Reading and Steering LLM States
**arXiv**：[2512.19399v1](https://arxiv.org/abs/2512.19399) · [PDF](https://arxiv.org/pdf/2512.19399.pdf)  
**作者**：Sandro Andric  

**一句话要点**：提出基于人脑活动的坐标轴以读取和调控大语言模型状态

**关键词**：大语言模型可解释性, 脑电图分析, 模型状态调控, 轻量适配器, 词汇频率轴, 功能内容轴

## 3 点简述
- 核心问题：现有大语言模型可解释性方法依赖文本监督，缺乏外部基础。
- 方法要点：利用脑电图数据构建词级脑图谱，提取潜在轴，训练轻量适配器映射模型状态。
- 实验或效果：验证轴的有效性，调控方向产生稳健的词汇和功能轴，支持神经生理学基础接口。

## 摘要（原文）

> Interpretability methods for large language models (LLMs) typically derive directions from textual supervision, which can lack external grounding. We propose using human brain activity not as a training signal but as a coordinate system for reading and steering LLM states. Using the SMN4Lang MEG dataset, we construct a word-level brain atlas of phase-locking value (PLV) patterns and extract latent axes via ICA. We validate axes with independent lexica and NER-based labels (POS/log-frequency used as sanity checks), then train lightweight adapters that map LLM hidden states to these brain axes without fine-tuning the LLM. Steering along the resulting brain-derived directions yields a robust lexical (frequency-linked) axis in a mid TinyLlama layer, surviving perplexity-matched controls, and a brain-vs-text probe comparison shows larger log-frequency shifts (relative to the text probe) with lower perplexity for the brain axis. A function/content axis (axis 13) shows consistent steering in TinyLlama, Qwen2-0.5B, and GPT-2, with PPL-matched text-level corroboration. Layer-4 effects in TinyLlama are large but inconsistent, so we treat them as secondary (Appendix). Axis structure is stable when the atlas is rebuilt without GPT embedding-change features or with word2vec embeddings (\|r\|=0.64-0.95 across matched axes), reducing circularity concerns. Exploratory fMRI anchoring suggests potential alignment for embedding change and log frequency, but effects are sensitive to hemodynamic modeling assumptions and are treated as population-level evidence only. These results support a new interface: neurophysiology-grounded axes provide interpretable and controllable handles for LLM behavior.

