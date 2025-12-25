---
layout: default
title: Beyond Memorization: A Multi-Modal Ordinal Regression Benchmark to Expose Popularity Bias in Vision-Language Models
---

# Beyond Memorization: A Multi-Modal Ordinal Regression Benchmark to Expose Popularity Bias in Vision-Language Models
**arXiv**：[2512.21337v1](https://arxiv.org/abs/2512.21337) · [PDF](https://arxiv.org/pdf/2512.21337.pdf)  
**作者**：Li-Zhong Szu-Tu, Ting-Lin Wu, Chia-Jui Chang, He Syu, Yu-Lun Liu  

**一句话要点**：提出YearGuessr基准以揭示视觉语言模型中的流行度偏差，通过序数回归任务评估模型泛化能力。

**关键词**：视觉语言模型, 流行度偏差, 序数回归, 多模态基准, YearGuessr数据集, 泛化能力

## 3 点简述
- 核心问题：视觉语言模型存在显著流行度偏差，对知名建筑预测准确率比普通建筑高34%，依赖记忆而非泛化理解。
- 方法要点：构建YearGuessr数据集，包含55,546张建筑图像，标注建设年份、GPS和页面浏览量，作为多模态序数回归基准。
- 实验或效果：评估30+模型，包括YearCLIP，确认模型在流行项目上表现优异，但在未识别主题上显著困难，暴露推理缺陷。

## 摘要（原文）

> We expose a significant popularity bias in state-of-the-art vision-language models (VLMs), which achieve up to 34% higher accuracy on famous buildings compared to ordinary ones, indicating a reliance on memorization over generalizable understanding. To systematically investigate this, we introduce the largest open benchmark for this task: the YearGuessr dataset, a collection of 55,546 building images with multi-modal attributes from 157 countries, annotated with continuous ordinal labels of their construction year (1001-2024), GPS data, and page-view counts as a proxy for popularity. Using this dataset, we frame the construction year prediction task as ordinal regression and introduce popularity-aware interval accuracy metrics to quantify this bias. Our resulting benchmark of 30+ models, including our YearCLIP model, confirms that VLMs excel on popular, memorized items but struggle significantly with unrecognized subjects, exposing a critical flaw in their reasoning capabilities. Project page: https://sytwu.github.io/BeyondMemo/

