---
layout: default
title: Towards Natural Language-Based Document Image Retrieval: New Dataset and Benchmark
---

# Towards Natural Language-Based Document Image Retrieval: New Dataset and Benchmark
**arXiv**：[2512.20174v1](https://arxiv.org/abs/2512.20174) · [PDF](https://arxiv.org/pdf/2512.20174.pdf)  
**作者**：Hao Guo, Xugong Qin, Jun Jie Ou Yang, Peng Zhang, Gangyan Zeng, Yubo Li, Hailun Lin  

**一句话要点**：提出基于自然语言的文档图像检索新基准NL-DIR，以解决细粒度语义查询下的检索难题。

**关键词**：文档图像检索, 自然语言查询, 视觉语言模型, 细粒度语义, 基准数据集, 两阶段检索

## 3 点简述
- 现有文档图像检索方法依赖图像查询，难以处理细粒度自然语言查询。
- 构建包含41K文档图像和高质量语义查询的数据集，支持零样本和微调评估。
- 评估主流视觉语言模型，并探索两阶段检索方法以提升性能与效率。

## 摘要（原文）

> Document image retrieval (DIR) aims to retrieve document images from a gallery according to a given query. Existing DIR methods are primarily based on image queries that retrieve documents within the same coarse semantic category, e.g., newspapers or receipts. However, these methods struggle to effectively retrieve document images in real-world scenarios where textual queries with fine-grained semantics are usually provided. To bridge this gap, we introduce a new Natural Language-based Document Image Retrieval (NL-DIR) benchmark with corresponding evaluation metrics. In this work, natural language descriptions serve as semantically rich queries for the DIR task. The NL-DIR dataset contains 41K authentic document images, each paired with five high-quality, fine-grained semantic queries generated and evaluated through large language models in conjunction with manual verification. We perform zero-shot and fine-tuning evaluations of existing mainstream contrastive vision-language models and OCR-free visual document understanding (VDU) models. A two-stage retrieval method is further investigated for performance improvement while achieving both time and space efficiency. We hope the proposed NL-DIR benchmark can bring new opportunities and facilitate research for the VDU community. Datasets and codes will be publicly available at huggingface.co/datasets/nianbing/NL-DIR.

