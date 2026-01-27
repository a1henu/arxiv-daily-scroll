---
layout: default
title: Making medical vision-language models think causally across modalities with retrieval-augmented cross-modal reasoning
---

# Making medical vision-language models think causally across modalities with retrieval-augmented cross-modal reasoning
**arXiv**：[2601.18356v1](https://arxiv.org/abs/2601.18356) · [PDF](https://arxiv.org/pdf/2601.18356.pdf)  
**作者**：Weiqin Yang, Haowen Xue, Qingyi Peng, Hexuan Hu, Qian Huang, Tingbo Zhang  

**一句话要点**：提出多模态因果检索增强生成框架，以提升医学视觉语言模型在临床决策中的因果推理能力。

**关键词**：医学视觉语言模型, 因果推理, 检索增强生成, 多模态检索, 临床决策支持

## 3 点简述
- 医学视觉语言模型依赖统计关联，缺乏因果推理，易产生幻觉和偏差。
- 框架整合因果推断与多模态检索，基于反事实和干预证据增强模型推理。
- 应用于放射学报告生成等任务，提高准确性、鲁棒性和可解释性。

## 摘要（原文）

> Medical vision-language models (VLMs) achieve strong performance in diagnostic reporting and image-text alignment, yet their underlying reasoning mechanisms remain fundamentally correlational, exhibiting reliance on superficial statistical associations that fail to capture the causal pathophysiological mechanisms central to clinical decision-making. This limitation makes them fragile, prone to hallucinations, and sensitive to dataset biases. Retrieval-augmented generation (RAG) offers a partial remedy by grounding predictions in external knowledge. However, conventional RAG depends on semantic similarity, introducing new spurious correlations. We propose Multimodal Causal Retrieval-Augmented Generation, a framework that integrates causal inference principles with multimodal retrieval. It retrieves clinically relevant exemplars and causal graphs from external sources, conditioning model reasoning on counterfactual and interventional evidence rather than correlations alone. Applied to radiology report generation, diagnosis prediction, and visual question answering, it improves factual accuracy, robustness to distribution shifts, and interpretability. Our results highlight causal retrieval as a scalable path toward medical VLMs that think beyond pattern matching, enabling trustworthy multimodal reasoning in high-stakes clinical settings.

