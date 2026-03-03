---
layout: default
title: FireRed-OCR Technical Report
---

# FireRed-OCR Technical Report
**arXiv**：[2603.01840v1](https://arxiv.org/abs/2603.01840) · [PDF](https://arxiv.org/pdf/2603.01840.pdf)  
**作者**：Hao Wu, Haoran Lou, Xinyue Li, Zuodong Zhong, Zhaojun Sun, Phellon Chen, Xuanhe Zhou, Kai Zuo, Yibo Chen, Xu Tang, Yao Hu, Boxiang Zhou, Jian Wu, Yongji Wu, Wenxin Yu, Yingmiao Liu, Yuhao Huang, Manjie Xu, Gang Liu, Yidong Ma, Zhichao Sun, Changhao Qiao  

**一句话要点**：提出FireRed-OCR框架，将通用视觉语言模型转化为高精度文档解析专家，以解决工业OCR中的结构幻觉问题。

**关键词**：文档解析, 视觉语言模型, 结构幻觉, 几何语义数据, 渐进训练, 强化学习

## 3 点简述
- 核心问题：通用视觉语言模型在处理复杂文档时易产生结构幻觉，限制工业OCR应用。
- 方法要点：构建几何+语义数据工厂，采用三阶段渐进训练策略，从像素感知到逻辑结构生成。
- 实验或效果：在OmniDocBench v1.5上达到92.94%的总体得分，超越DeepSeek-OCR 2等基线模型。

## 摘要（原文）

> We present FireRed-OCR, a systematic framework to specialize general VLMs into high-performance OCR models. Large Vision-Language Models (VLMs) have demonstrated impressive general capabilities but frequently suffer from ``structural hallucination'' when processing complex documents, limiting their utility in industrial OCR applications. In this paper, we introduce FireRed-OCR, a novel framework designed to transform general-purpose VLMs (based on Qwen3-VL) into pixel-precise structural document parsing experts. To address the scarcity of high-quality structured data, we construct a ``Geometry + Semantics'' Data Factory. Unlike traditional random sampling, our pipeline leverages geometric feature clustering and multi-dimensional tagging to synthesize and curate a highly balanced dataset, effectively handling long-tail layouts and rare document types. Furthermore, we propose a Three-Stage Progressive Training strategy that guides the model from pixel-level perception to logical structure generation. This curriculum includes: (1) Multi-task Pre-alignment to ground the model's understanding of document structure; (2) Specialized SFT for standardizing full-image Markdown output; and (3) Format-Constrained Group Relative Policy Optimization (GRPO), which utilizes reinforcement learning to enforce strict syntactic validity and structural integrity (e.g., table closure, formula syntax). Extensive evaluations on OmniDocBench v1.5 demonstrate that FireRed-OCR achieves state-of-the-art performance with an overall score of 92.94\%, significantly outperforming strong baselines such as DeepSeek-OCR 2 and OCRVerse across text, formula, table, and reading order metrics. We open-source our code and model weights to facilitate the ``General VLM to Specialized Structural Expert'' paradigm.

