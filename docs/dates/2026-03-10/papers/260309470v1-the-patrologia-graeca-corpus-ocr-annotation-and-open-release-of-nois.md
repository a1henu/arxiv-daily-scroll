---
layout: default
title: The Patrologia Graeca Corpus: OCR, Annotation, and Open Release of Noisy Nineteenth-Century Polytonic Greek Editions
---

# The Patrologia Graeca Corpus: OCR, Annotation, and Open Release of Noisy Nineteenth-Century Polytonic Greek Editions
**arXiv**：[2603.09470v1](https://arxiv.org/abs/2603.09470) · [PDF](https://arxiv.org/pdf/2603.09470.pdf)  
**作者**：Chahan Vidal-Gorène, Bastien Kindt  

**一句话要点**：提出Patrologia Graeca Corpus，通过OCR和标注流程解决十九世纪多调希腊语古籍数字化问题。

**关键词**：多调希腊语OCR, 古籍数字化, 布局检测, 文本识别, 语料库构建, 基准数据集

## 3 点简述
- 核心问题：数字化十九世纪双语布局、字体退化的多调希腊语古籍，现有OCR系统性能不足。
- 方法要点：结合YOLO布局检测和CRNN文本识别的专用流程，实现高精度OCR。
- 实验或效果：字符错误率1.05%，词错误率4.69%，包含约六百万标注词元，建立新基准。

## 摘要（原文）

> We present the Patrologia Graeca Corpus, the first large-scale open OCR and linguistic resource for nineteenthcentury editions of Ancient Greek. The collection covers the remaining undigitized volumes of the Patrologia Graeca (PG), printed in complex bilingual (Greek-Latin) layouts and characterized by highly degraded polytonic Greek typography. Through a dedicated pipeline combining YOLO-based layout detection and CRNN-based text recognition, we achieve a character error rate (CER) of 1.05% and a word error rate (WER) of 4.69%, largely outperforming existing OCR systems for polytonic Greek. The resulting corpus contains around six million lemmatized and part-of-speech tagged tokens, aligned with full OCR and layout annotations. Beyond its philological value, this corpus establishes a new benchmark for OCR on noisy polytonic Greek and provides training material for future models, including LLMs.

