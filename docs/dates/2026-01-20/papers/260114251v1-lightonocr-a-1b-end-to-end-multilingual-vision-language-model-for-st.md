---
layout: default
title: LightOnOCR: A 1B End-to-End Multilingual Vision-Language Model for State-of-the-Art OCR
---

# LightOnOCR: A 1B End-to-End Multilingual Vision-Language Model for State-of-the-Art OCR
**arXiv**：[2601.14251v1](https://arxiv.org/abs/2601.14251) · [PDF](https://arxiv.org/pdf/2601.14251.pdf)  
**作者**：Said Taghadouini, Adrien Cavaillès, Baptiste Aubertin  

**一句话要点**：提出LightOnOCR-2-1B，一个10亿参数端到端多语言视觉语言模型，用于文档图像到文本的转换。

**关键词**：端到端OCR, 多语言视觉语言模型, 文档图像处理, 边界框预测, 蒸馏训练, 模型优化

## 3 点简述
- 核心问题：传统OCR流程脆弱，难以处理多语言文档图像，如扫描件和科学PDF。
- 方法要点：通过大规模高质量蒸馏训练，覆盖扫描件和法语文档，并引入边界框预测以增强定位能力。
- 实验或效果：在OlmOCR-Bench上达到最先进结果，模型尺寸缩小9倍且速度显著提升。

## 摘要（原文）

> We present \textbf{LightOnOCR-2-1B}, a 1B-parameter end-to-end multilingual vision--language model that converts document images (e.g., PDFs) into clean, naturally ordered text without brittle OCR pipelines. Trained on a large-scale, high-quality distillation mix with strong coverage of scans, French documents, and scientific PDFs, LightOnOCR-2 achieves state-of-the-art results on OlmOCR-Bench while being 9$\times$ smaller and substantially faster than prior best-performing models. We further extend the output format to predict normalized bounding boxes for embedded images, introducing localization during pretraining via a resume strategy and refining it with RLVR using IoU-based rewards. Finally, we improve robustness with checkpoint averaging and task-arithmetic merging. We release model checkpoints under Apache 2.0, and publicly release the dataset and \textbf{LightOnOCR-bbox-bench} evaluation under their respective licenses.

