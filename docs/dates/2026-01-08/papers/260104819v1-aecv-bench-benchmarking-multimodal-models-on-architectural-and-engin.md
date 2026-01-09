---
layout: default
title: AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding
---

# AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding
**arXiv**：[2601.04819v1](https://arxiv.org/abs/2601.04819) · [PDF](https://arxiv.org/pdf/2601.04819.pdf)  
**作者**：Aleksei Kondratenko, Mussie Birhane, Houssame E. Hsain, Guido Maciocci  

**一句话要点**：提出AECV-Bench基准，评估多模态模型在建筑与工程图纸理解上的性能

**关键词**：多模态模型评估, 建筑图纸理解, 对象计数, 文档问答, 空间推理, 基准测试

## 3 点简述
- 核心问题：现代多模态模型能否可靠解释AEC图纸的图形语言，如符号和布局。
- 方法要点：通过对象计数和图纸文档问答两个用例，使用统一协议评估模型。
- 实验或效果：OCR和文本相关任务表现强，但符号理解和计数任务准确率低，显示模型缺乏图纸素养。

## 摘要（原文）

> AEC drawings encode geometry and semantics through symbols, layout conventions, and dense annotation, yet it remains unclear whether modern multimodal and vision-language models can reliably interpret this graphical language. We present AECV-Bench, a benchmark for evaluating multimodal and vision-language models on realistic AEC artefacts via two complementary use cases: (i) object counting on 120 high-quality floor plans (doors, windows, bedrooms, toilets), and (ii) drawing-grounded document QA spanning 192 question-answer pairs that test text extraction (OCR), instance counting, spatial reasoning, and comparative reasoning over common drawing regions. Object-counting performance is reported using per-field exact-match accuracy and MAPE results, while document-QA performance is reported using overall accuracy and per-category breakdowns with an LLM-as-a-judge scoring pipeline and targeted human adjudication for edge cases. Evaluating a broad set of state-of-the-art models under a unified protocol, we observe a stable capability gradient; OCR and text-centric document QA are strongest (up to 0.95 accuracy), spatial reasoning is moderate, and symbol-centric drawing understanding - especially reliable counting of doors and windows - remains unsolved (often 0.40-0.55 accuracy) with substantial proportional errors. These results suggest that current systems function well as document assistants but lack robust drawing literacy, motivating domain-specific representations and tool-augmented, human-in-the-loop workflows for an efficient AEC automation.

