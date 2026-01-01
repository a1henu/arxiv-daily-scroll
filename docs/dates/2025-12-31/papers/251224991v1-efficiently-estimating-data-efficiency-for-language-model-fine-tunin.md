---
layout: default
title: Efficiently Estimating Data Efficiency for Language Model Fine-tuning
---

# Efficiently Estimating Data Efficiency for Language Model Fine-tuning
**arXiv**：[2512.24991v1](https://arxiv.org/abs/2512.24991) · [PDF](https://arxiv.org/pdf/2512.24991.pdf)  
**作者**：Gyung Hyun Je, Colin Raffel  

**一句话要点**：提出基于梯度余弦相似度的方法，以预测语言模型微调的数据效率，减少标注成本。

**关键词**：语言模型微调, 数据效率预测, 梯度余弦相似度, 标注成本优化, 任务性能评估

## 3 点简述
- 核心问题：语言模型微调中数据效率未知，导致标注和重训练成本高。
- 方法要点：使用低置信度样本的梯度余弦相似度，基于少量标注预测数据效率。
- 实验或效果：在30个任务上验证，预测误差8.6%，显著减少不必要标注。

## 摘要（原文）

> While large language models (LLMs) demonstrate reasonable zero-shot capability across many downstream tasks, fine-tuning is a common practice to improve their performance. However, a task's data efficiency--i.e., the number of fine-tuning examples needed to achieve a desired level of performance--is often unknown, resulting in costly cycles of incremental annotation and retraining. Indeed, we demonstrate across a curated set of 30 specialized tasks that performant LLMs may struggle zero-shot but can attain stronger performance after fine-tuning. This motivates the need for methods to predict a task's data efficiency without requiring incremental annotation. After introducing a concrete metric that quantifies a task's data efficiency, we propose using the gradient cosine similarity of low-confidence examples to predict data efficiency based on a small number of labeled samples. We validate our approach on a diverse set of tasks with varying data efficiencies, attaining 8.6% error in overall data efficiency prediction and typically eliminating hundreds of unnecessary annotations on each task. Our experiment results and implementation code are available on GitHub.

