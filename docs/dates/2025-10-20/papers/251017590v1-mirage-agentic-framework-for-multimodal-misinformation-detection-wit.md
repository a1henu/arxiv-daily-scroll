---
layout: default
title: MIRAGE: Agentic Framework for Multimodal Misinformation Detection with Web-Grounded Reasoning
---

# MIRAGE: Agentic Framework for Multimodal Misinformation Detection with Web-Grounded Reasoning
**arXiv**：[2510.17590v1](https://arxiv.org/abs/2510.17590) · [PDF](https://arxiv.org/pdf/2510.17590.pdf)  
**作者**：Mir Nafis Sharear Shopnil, Sharad Duwal, Abhishek Tyagi, Adiba Mahbub Proma  

**一句话要点**：提出MIRAGE框架以解决多模态虚假信息检测问题，通过分解推理与网络检索实现零样本高性能。

**关键词**：多模态虚假信息检测, 代理推理框架, 检索增强生成, 视觉语言模型, 零样本学习, 网络检索

## 3 点简述
- 核心问题：多模态虚假信息泛滥，监督模型泛化差且依赖标注数据。
- 方法要点：框架分解为视觉真实性、跨模态一致性、检索增强事实检查和校准判断模块。
- 实验效果：在MMFakeBench上F1达81.65%，优于零-shot基线，无需领域特定训练。

## 摘要（原文）

> Misinformation spreads across web platforms through billions of daily
> multimodal posts that combine text and images, overwhelming manual
> fact-checking capacity. Supervised detection models require domain-specific
> training data and fail to generalize across diverse manipulation tactics. We
> present MIRAGE, an inference-time, model-pluggable agentic framework that
> decomposes multimodal verification into four sequential modules: visual
> veracity assessment detects AI-generated images, cross-modal consistency
> analysis identifies out-of-context repurposing, retrieval-augmented factual
> checking grounds claims in web evidence through iterative question generation,
> and a calibrated judgment module integrates all signals. MIRAGE orchestrates
> vision-language model reasoning with targeted web retrieval, outputs structured
> and citation-linked rationales. On MMFakeBench validation set (1,000 samples),
> MIRAGE with GPT-4o-mini achieves 81.65% F1 and 75.1% accuracy, outperforming
> the strongest zero-shot baseline (GPT-4V with MMD-Agent at 74.0% F1) by 7.65
> points while maintaining 34.3% false positive rate versus 97.3% for a
> judge-only baseline. Test set results (5,000 samples) confirm generalization
> with 81.44% F1 and 75.08% accuracy. Ablation studies show visual verification
> contributes 5.18 F1 points and retrieval-augmented reasoning contributes 2.97
> points. Our results demonstrate that decomposed agentic reasoning with web
> retrieval can match supervised detector performance without domain-specific
> training, enabling misinformation detection across modalities where labeled
> data remains scarce.

