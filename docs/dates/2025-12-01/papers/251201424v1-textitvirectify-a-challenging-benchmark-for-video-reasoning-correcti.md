---
layout: default
title: \textit{ViRectify}: A Challenging Benchmark for Video Reasoning Correction with Multimodal Large Language Models
---

# \textit{ViRectify}: A Challenging Benchmark for Video Reasoning Correction with Multimodal Large Language Models
**arXiv**：[2512.01424v1](https://arxiv.org/abs/2512.01424) · [PDF](https://arxiv.org/pdf/2512.01424.pdf)  
**作者**：Xusen Hei, Jiali Chen, Jinyu Yang, Mengchen Zhao, Yi Cai  

**一句话要点**：提出ViRectify基准以评估多模态大语言模型在视频推理错误纠正中的能力

**关键词**：视频推理纠正, 多模态大语言模型, 错误识别, 轨迹证据, 基准评估, 数据集构建

## 3 点简述
- 多模态大语言模型在复杂视频推理中常出错，缺乏系统性评估其错误识别与纠正能力的基准
- 通过AI辅助标注构建超3万实例数据集，涵盖动态感知、科学推理和具身决策领域，要求模型进行逐步错误识别和基于视频证据的纠正
- 提出轨迹证据驱动的纠正框架，评估16个先进模型，GPT-5纠正准确率仅31.94%，框架使Qwen2.5-VL-7B优于72B变体

## 摘要（原文）

> As multimodal large language models (MLLMs) frequently exhibit errors in complex video reasoning scenarios, correcting these errors is critical for uncovering their weaknesses and improving performance. However, existing benchmarks lack systematic evaluation of MLLMs' ability to identify and correct these video reasoning errors. To bridge this gap, we propose \textit{ViRectify}, a comprehensive benchmark to evaluate their fine-grained correction capability. Through an AI-assisted annotation pipeline with human verification, we construct a dataset of over 30\textit{K} instances spanning dynamic perception, scientific reasoning, and embodied decision-making domains. In \textit{ViRectify}, we challenge MLLMs to perform step-wise error identification and generate rationales with key video evidence grounding. In addition, we further propose the trajectory evidence-driven correction framework, comprising step-wise error trajectory and reward modeling on visual evidence-grounded correction. It encourages the model to explicitly concentrate on error propagation and key timestamps for correction. Extensive evaluation across 16 advanced MLLMs demonstrates that our \textit{ViRectify} serves as a challenging testbed, where GPT-5 achieves only 31.94\% correction accuracy. Our framework enables a Qwen2.5-VL-7B to consistently outperform the variants of 72B on \textit{ViRectify}, showing the effectiveness of our approach. Further analysis uncovers systematic asymmetries in error correction across models, and our dataset is also a valuable data resource to perform reflection learning. We believe \textit{ViRectify} provides a new direction for comprehensively evaluating the advanced MLLMs in video reasoning.

