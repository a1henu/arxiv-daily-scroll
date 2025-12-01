---
layout: default
title: BanglaSentNet: An Explainable Hybrid Deep Learning Framework for Multi-Aspect Sentiment Analysis with Cross-Domain Transfer Learning
---

# BanglaSentNet: An Explainable Hybrid Deep Learning Framework for Multi-Aspect Sentiment Analysis with Cross-Domain Transfer Learning
**arXiv**：[2511.23264v1](https://arxiv.org/abs/2511.23264) · [PDF](https://arxiv.org/pdf/2511.23264.pdf)  
**作者**：Ariful Islam, Md Rifat Hossen, Tanvir Mahmud  

**一句话要点**：提出BanglaSentNet框架，通过可解释混合深度学习解决孟加拉语多方面情感分析问题，并实现跨领域迁移学习。

**关键词**：孟加拉语情感分析, 混合深度学习, 可解释人工智能, 跨领域迁移学习, 电商评论分析, 低资源语言处理

## 3 点简述
- 核心问题：孟加拉语电商评论情感分析面临标注数据少、形态复杂、代码混合和领域偏移等挑战。
- 方法要点：集成LSTM、BiLSTM、GRU和BanglaBERT，结合SHAP和注意力可视化实现可解释性。
- 实验或效果：在自建数据集上达到85%准确率，跨领域零样本性能保持67-76%，少样本学习显著降低标注成本。

## 摘要（原文）

> Multi-aspect sentiment analysis of Bangla e-commerce reviews remains challenging due to limited annotated datasets, morphological complexity, code-mixing phenomena, and domain shift issues, affecting 300 million Bangla-speaking users. Existing approaches lack explainability and cross-domain generalization capabilities crucial for practical deployment. We present BanglaSentNet, an explainable hybrid deep learning framework integrating LSTM, BiLSTM, GRU, and BanglaBERT through dynamic weighted ensemble learning for multi-aspect sentiment classification. We introduce a dataset of 8,755 manually annotated Bangla product reviews across four aspects (Quality, Service, Price, Decoration) from major Bangladeshi e-commerce platforms. Our framework incorporates SHAP-based feature attribution and attention visualization for transparent insights. BanglaSentNet achieves 85% accuracy and 0.88 F1-score, outperforming standalone deep learning models by 3-7% and traditional approaches substantially. The explainability suite achieves 9.4/10 interpretability score with 87.6% human agreement. Cross-domain transfer learning experiments reveal robust generalization: zero-shot performance retains 67-76% effectiveness across diverse domains (BanglaBook reviews, social media, general e-commerce, news headlines); few-shot learning with 500-1000 samples achieves 90-95% of full fine-tuning performance, significantly reducing annotation costs. Real-world deployment demonstrates practical utility for Bangladeshi e-commerce platforms, enabling data-driven decision-making for pricing optimization, service improvement, and customer experience enhancement. This research establishes a new state-of-the-art benchmark for Bangla sentiment analysis, advances ensemble learning methodologies for low-resource languages, and provides actionable solutions for commercial applications.

