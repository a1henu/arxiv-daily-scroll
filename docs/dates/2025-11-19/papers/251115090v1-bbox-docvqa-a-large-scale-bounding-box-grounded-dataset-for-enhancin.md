---
layout: default
title: BBox DocVQA: A Large Scale Bounding Box Grounded Dataset for Enhancing Reasoning in Document Visual Question Answer
---

# BBox DocVQA: A Large Scale Bounding Box Grounded Dataset for Enhancing Reasoning in Document Visual Question Answer
**arXiv**：[2511.15090v1](https://arxiv.org/abs/2511.15090) · [PDF](https://arxiv.org/pdf/2511.15090.pdf)  
**作者**：Wenhan Yu, Wang Chen, Guanqiang Qi, Weikang Li, Yang Li, Lei Sha, Deguo Xia, Jizhou Huang  

**一句话要点**：提出BBox DocVQA数据集以增强文档视觉问答中的空间推理能力

**关键词**：文档视觉问答, 空间推理, 边界框标注, 自动化数据集构建, 视觉语言模型评估

## 3 点简述
- 现有DocVQA数据集缺乏细粒度空间标注，限制视觉语言模型的推理能力
- 采用自动化流水线Segment Judge and Generate构建数据集，包含3.6K文档和32K QA对
- 基准测试显示模型在空间定位上存在挑战，微调后定位和答案生成能力显著提升

## 摘要（原文）

> Document Visual Question Answering (DocVQA) is a fundamental task for multimodal document understanding and a key testbed for vision language reasoning. However, most existing DocVQA datasets are limited to the page level and lack fine grained spatial grounding, constraining the interpretability and reasoning capability of Vision Language Models (VLMs). To address this gap, we introduce BBox DocVQA a large scale, bounding box grounded dataset designed to enhance spatial reasoning and evidence localization in visual documents. We further present an automated construction pipeline, Segment Judge and Generate, which integrates a segment model for region segmentation, a VLM for semantic judgment, and another advanced VLM for question answer generation, followed by human verification for quality assurance. The resulting dataset contains 3.6 K diverse documents and 32 K QA pairs, encompassing single and multi region as well as single and multi page scenarios. Each QA instance is grounded on explicit bounding boxes, enabling fine grained evaluation of spatial semantic alignment. Benchmarking multiple state of the art VLMs (e.g., GPT 5, Qwen2.5 VL, and InternVL) on BBox DocVQA reveals persistent challenges in spatial grounding and reasoning accuracy. Furthermore, fine tuning on BBox DocVQA substantially improves both bounding box localization and answer generation, validating its effectiveness for enhancing the reasoning ability of VLMs. Our dataset and code will be publicly released to advance research on interpretable and spatially grounded vision language reasoning.

