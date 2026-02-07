---
layout: default
title: DLM-Scope: Mechanistic Interpretability of Diffusion Language Models via Sparse Autoencoders
---

# DLM-Scope: Mechanistic Interpretability of Diffusion Language Models via Sparse Autoencoders
**arXiv**：[2602.05859v1](https://arxiv.org/abs/2602.05859) · [PDF](https://arxiv.org/pdf/2602.05859.pdf)  
**作者**：Xu Wang, Bingqing Jiang, Yu Wan, Baosong Yang, Lingpeng Kong, Difan Zou  

**一句话要点**：提出DLM-Scope框架，基于稀疏自编码器实现扩散语言模型的机制可解释性

**关键词**：扩散语言模型, 稀疏自编码器, 机制可解释性, 特征提取, 模型干预

## 3 点简述
- 核心问题：扩散语言模型缺乏定制化的机制可解释性工具，需开发类似自回归大语言模型的稀疏特征提取方法
- 方法要点：首次将稀疏自编码器应用于扩散语言模型，训练Top-K稀疏自编码器以提取可解释特征
- 实验或效果：稀疏自编码器插入在扩散语言模型早期层可降低交叉熵损失，支持更有效的扩散时间干预和模型解码顺序分析

## 摘要（原文）

> Sparse autoencoders (SAEs) have become a standard tool for mechanistic interpretability in autoregressive large language models (LLMs), enabling researchers to extract sparse, human-interpretable features and intervene on model behavior. Recently, as diffusion language models (DLMs) have become an increasingly promising alternative to the autoregressive LLMs, it is essential to develop tailored mechanistic interpretability tools for this emerging class of models. In this work, we present DLM-Scope, the first SAE-based interpretability framework for DLMs, and demonstrate that trained Top-K SAEs can faithfully extract interpretable features. Notably, we find that inserting SAEs affects DLMs differently than autoregressive LLMs: while SAE insertion in LLMs typically incurs a loss penalty, in DLMs it can reduce cross-entropy loss when applied to early layers, a phenomenon absent or markedly weaker in LLMs. Additionally, SAE features in DLMs enable more effective diffusion-time interventions, often outperforming LLM steering. Moreover, we pioneer certain new SAE-based research directions for DLMs: we show that SAEs can provide useful signals for DLM decoding order; and the SAE features are stable during the post-training phase of DLMs. Our work establishes a foundation for mechanistic interpretability in DLMs and shows a great potential of applying SAEs to DLM-related tasks and algorithms.

