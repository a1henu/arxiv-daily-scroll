---
layout: default
title: START: Spatial and Textual Learning for Chart Understanding
---

# START: Spatial and Textual Learning for Chart Understanding
**arXiv**：[2512.07186v1](https://arxiv.org/abs/2512.07186) · [PDF](https://arxiv.org/pdf/2512.07186.pdf)  
**作者**：Zhuoming Liu, Xiaofeng Gao, Feiyang Niu, Qiaozi Gao, Liu Liu, Robinson Piramuthu  

**一句话要点**：提出START方法以增强多模态大语言模型在图表理解中的空间与文本学习能力

**关键词**：图表理解, 多模态大语言模型, 空间学习, 文本学习, 图表元素定位, 图表到代码生成

## 3 点简述
- 核心问题：图表结合结构化视觉布局与底层数据表示，需同时理解两者以实现精确推理
- 方法要点：引入图表元素定位和图表到代码生成，通过START-Dataset和CS-Bench支持学习与评估
- 实验或效果：START在不同模型规模和基准上优于基线及先前方法，代码、数据和模型将公开

## 摘要（原文）

> Chart understanding is crucial for deploying multimodal large language models (MLLMs) in real-world scenarios such as analyzing scientific papers and technical reports. Unlike natural images, charts pair a structured visual layout (spatial property) with an underlying data representation (textual property) -- grasping both is essential for precise, fine-grained chart reasoning. Motivated by this observation, we propose START, the Spatial and Textual learning for chART understanding. Specifically, we introduce (i) chart-element grounding and (ii) chart-to-code generation to strengthen an MLLM's understanding of both chart visual layout and data details. To facilitate spatial and textual learning, we propose the START-Dataset generated with a novel data-generation pipeline that first leverages an MLLM to translate real chart images into executable chart code, recovering the underlying data representation while preserving the visual distribution of real-world charts. We then evolve the code with a Large Language Model (LLM) to ascertain the positions of chart elements that capture the chart's visual structure, addressing challenges that existing methods cannot handle. To evaluate a model's ability to understand chart spatial structures, we propose the Chart Spatial understanding Benchmark (CS-Bench), filling a critical gap in comprehensive chart understanding evaluation. Leveraging spatial and textual learning, START delivers consistent gains across model sizes and benchmarks over the base models and surpasses prior state-of-the-art by a clear margin. Code, data and models will be publicly available.

