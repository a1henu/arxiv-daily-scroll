---
layout: default
title: ChartE$^{3}$: A Comprehensive Benchmark for End-to-End Chart Editing
---

# ChartE$^{3}$: A Comprehensive Benchmark for End-to-End Chart Editing
**arXiv**：[2601.21694v1](https://arxiv.org/abs/2601.21694) · [PDF](https://arxiv.org/pdf/2601.21694.pdf)  
**作者**：Shuo Li, Jiajun Sun, Zhekai Wang, Xiaoran Fan, Hui Li, Dingwen Yang, Zhiheng Xi, Yijun Wang, Zifei Shan, Tao Gui, Qi Zhang, Xuanjing Huang  

**一句话要点**：提出ChartE³基准以评估端到端图表编辑模型，避免中间表示限制。

**关键词**：图表编辑, 端到端评估, 多模态基准, 局部编辑, 全局编辑, 大语言模型

## 3 点简述
- 核心问题：现有图表编辑方法依赖自然语言或代码作为中间表示，难以忠实执行复杂编辑。
- 方法要点：ChartE³直接评估模型，包含局部和全局编辑任务，基于高质量多模态样本。
- 实验或效果：基准测试显示当前模型在全局编辑任务上存在显著性能差距。

## 摘要（原文）

> Charts are a fundamental visualization format for structured data analysis. Enabling end-to-end chart editing according to user intent is of great practical value, yet remains challenging due to the need for both fine-grained control and global structural consistency. Most existing approaches adopt pipeline-based designs, where natural language or code serves as an intermediate representation, limiting their ability to faithfully execute complex edits. We introduce ChartE$^{3}$, an End-to-End Chart Editing benchmark that directly evaluates models without relying on intermediate natural language programs or code-level supervision. ChartE$^{3}$ focuses on two complementary editing dimensions: local editing, which involves fine-grained appearance changes such as font or color adjustments, and global editing, which requires holistic, data-centric transformations including data filtering and trend line addition. ChartE$^{3}$ contains over 1,200 high-quality samples constructed via a well-designed data pipeline with human curation. Each sample is provided as a triplet of a chart image, its underlying code, and a multimodal editing instruction, enabling evaluation from both objective and subjective perspectives. Extensive benchmarking of state-of-the-art multimodal large language models reveals substantial performance gaps, particularly on global editing tasks, highlighting critical limitations in current end-to-end chart editing capabilities.

