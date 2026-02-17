---
layout: default
title: Web-Scale Multimodal Summarization using CLIP-Based Semantic Alignment
---

# Web-Scale Multimodal Summarization using CLIP-Based Semantic Alignment
**arXiv**：[2602.14889v1](https://arxiv.org/abs/2602.14889) · [PDF](https://arxiv.org/pdf/2602.14889.pdf)  
**作者**：Mounvik K, N Harshit  

**一句话要点**：提出基于CLIP语义对齐的Web规模多模态摘要框架，整合检索与视觉模型生成摘要。

**关键词**：多模态摘要, CLIP语义对齐, 网络规模检索, 图像排序, 可配置管道, Gradio API

## 3 点简述
- 核心问题：从网络源中检索文本和图像数据，生成多模态摘要，需处理大规模数据和语义对齐。
- 方法要点：使用微调CLIP模型对检索图像进行语义对齐排序，可选BLIP生成图像描述以增强多模态一致性。
- 实验或效果：在500个图像-标题对评估中，ROC-AUC达0.9270，准确率96.99%，显示强大多模态对齐能力。

## 摘要（原文）

> We introduce Web-Scale Multimodal Summarization, a lightweight framework for generating summaries by combining retrieved text and image data from web sources. Given a user-defined topic, the system performs parallel web, news, and image searches. Retrieved images are ranked using a fine-tuned CLIP model to measure semantic alignment with topic and text. Optional BLIP captioning enables image-only summaries for stronger multimodal coherence.The pipeline supports features such as adjustable fetch limits, semantic filtering, summary styling, and downloading structured outputs. We expose the system via a Gradio-based API with controllable parameters and preconfigured presets.Evaluation on 500 image-caption pairs with 20:1 contrastive negatives yields a ROC-AUC of 0.9270, an F1-score of 0.6504, and an accuracy of 96.99%, demonstrating strong multimodal alignment. This work provides a configurable, deployable tool for web-scale summarization that integrates language, retrieval, and vision models in a user-extensible pipeline.

