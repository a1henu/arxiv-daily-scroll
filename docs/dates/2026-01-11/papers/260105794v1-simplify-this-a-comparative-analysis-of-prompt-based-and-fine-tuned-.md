---
layout: default
title: Simplify-This: A Comparative Analysis of Prompt-Based and Fine-Tuned LLMs
---

# Simplify-This: A Comparative Analysis of Prompt-Based and Fine-Tuned LLMs
**arXiv**：[2601.05794v1](https://arxiv.org/abs/2601.05794) · [PDF](https://arxiv.org/pdf/2601.05794.pdf)  
**作者**：Eilam Cohen, Itamar Bul, Danielle Inbar, Omri Loewenbach  

**一句话要点**：提出Simplify-This比较研究，评估文本简化中微调与提示工程在编码器-解码器LLMs上的性能差异。

**关键词**：文本简化, 大语言模型, 微调, 提示工程, 编码器-解码器模型, 比较分析

## 3 点简述
- 核心问题：文本简化任务中，微调与提示工程在LLMs上的实际权衡与性能比较。
- 方法要点：使用多基准和评估指标，系统比较编码器-解码器LLMs的微调与提示范式。
- 实验或效果：微调模型在结构简化上更强，提示工程语义相似度高但易复制输入，人类评估总体偏好微调输出。

## 摘要（原文）

> Large language models (LLMs) enable strong text generation, and in general there is a practical tradeoff between fine-tuning and prompt engineering. We introduce Simplify-This, a comparative study evaluating both paradigms for text simplification with encoder-decoder LLMs across multiple benchmarks, using a range of evaluation metrics. Fine-tuned models consistently deliver stronger structural simplification, whereas prompting often attains higher semantic similarity scores yet tends to copy inputs. A human evaluation favors fine-tuned outputs overall. We release code, a cleaned derivative dataset used in our study, checkpoints of fine-tuned models, and prompt templates to facilitate reproducibility and future work.

