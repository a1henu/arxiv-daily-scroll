---
layout: default
title: Evaluating Multimodal Large Language Models on Vertically Written Japanese Text
---

# Evaluating Multimodal Large Language Models on Vertically Written Japanese Text
**arXiv**：[2511.15059v1](https://arxiv.org/abs/2511.15059) · [PDF](https://arxiv.org/pdf/2511.15059.pdf)  
**作者**：Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara  

**一句话要点**：评估多模态大语言模型对竖排日文文本的阅读能力，并通过合成数据集提升性能

**关键词**：多模态大语言模型, 竖排日文文本, OCR数据集, 视觉文档理解, 模型微调

## 3 点简述
- 核心问题：现有MLLMs在竖排日文文本上表现差，缺乏专门研究。
- 方法要点：生成合成日文OCR数据集，用于模型微调和评估。
- 实验或效果：训练后模型在竖排文本上性能提升，数据集公开。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have seen rapid advances in recent years and are now being applied to visual document understanding tasks. They are expected to process a wide range of document images across languages, including Japanese. Understanding documents from images requires models to read what are written in them. Since some Japanese documents are written vertically, support for vertical writing is essential. However, research specifically focused on vertically written Japanese text remains limited. In this study, we evaluate the reading capability of existing MLLMs on vertically written Japanese text. First, we generate a synthetic Japanese OCR dataset by rendering Japanese texts into images, and use it for both model fine-tuning and evaluation. This dataset includes Japanese text in both horizontal and vertical writing. We also create an evaluation dataset sourced from the real-world document images containing vertically written Japanese text. Using these datasets, we demonstrate that the existing MLLMs perform worse on vertically written Japanese text than on horizontally written Japanese text. Furthermore, we show that training MLLMs on our synthesized Japanese OCR dataset results in improving the performance of models that previously could not handle vertical writing. The datasets and code are publicly available https://github.com/llm-jp/eval_vertical_ja.

