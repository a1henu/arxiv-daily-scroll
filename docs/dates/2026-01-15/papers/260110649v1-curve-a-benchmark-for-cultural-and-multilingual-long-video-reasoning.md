---
layout: default
title: CURVE: A Benchmark for Cultural and Multilingual Long Video Reasoning
---

# CURVE: A Benchmark for Cultural and Multilingual Long Video Reasoning
**arXiv**：[2601.10649v1](https://arxiv.org/abs/2601.10649) · [PDF](https://arxiv.org/pdf/2601.10649.pdf)  
**作者**：Darshan Singh, Arsha Nagrani, Kawshik Manikantan, Harman Singh, Dinesh Tewari, Tobias Weyand, Cordelia Schmid, Anelia Angelova, Shachi Dave  

**一句话要点**：提出CURVE基准以解决视频模型在文化和多语言长视频推理中的偏见问题

**关键词**：文化视频理解, 多语言视频推理, 长视频基准, 人工标注, 视觉文化感知, 推理错误分析

## 3 点简述
- 当前视频基准存在西方中心化和英语主导的偏见，影响评估公平性
- CURVE提供18个地区的高质量人工标注，包含复杂问题和多步推理，支持原生语言
- 评估显示先进视频-LLMs表现远低于人类，错误主要源于文化元素的视觉感知

## 摘要（原文）

> Recent advancements in video models have shown tremendous progress, particularly in long video understanding. However, current benchmarks predominantly feature western-centric data and English as the dominant language, introducing significant biases in evaluation. To address this, we introduce CURVE (Cultural Understanding and Reasoning in Video Evaluation), a challenging benchmark for multicultural and multilingual video reasoning. CURVE comprises high-quality, entirely human-generated annotations from diverse, region-specific cultural videos across 18 global locales. Unlike prior work that relies on automatic translations, CURVE provides complex questions, answers, and multi-step reasoning steps, all crafted in native languages. Making progress on CURVE requires a deeply situated understanding of visual cultural context. Furthermore, we leverage CURVE's reasoning traces to construct evidence-based graphs and propose a novel iterative strategy using these graphs to identify fine-grained errors in reasoning. Our evaluations reveal that SoTA Video-LLMs struggle significantly, performing substantially below human-level accuracy, with errors primarily stemming from the visual perception of cultural elements. CURVE will be publicly available under https://github.com/google-deepmind/neptune?tab=readme-ov-file\#minerva-cultural

