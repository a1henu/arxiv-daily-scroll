---
layout: default
title: Tabular Incremental Inference
---

# Tabular Incremental Inference
**arXiv**：[2601.15751v1](https://arxiv.org/abs/2601.15751) · [PDF](https://arxiv.org/pdf/2601.15751.pdf)  
**作者**：Xinda Chen, Xing Zhen, Hanyu Zhang, Weimin Tan, Bo Yan  

**一句话要点**：提出Tabular Incremental Inference方法，以解决动态表格列变化下的AI模型推理问题。

**关键词**：表格数据推理, 增量学习, 信息瓶颈理论, 无监督学习, 动态表格处理

## 3 点简述
- 核心问题：传统固定列训练模型无法处理表格列动态变化，需无监督高效方法。
- 方法要点：基于信息瓶颈理论，设计LLM占位符、预训练TabAdapter和增量样本压缩块。
- 实验或效果：在八个公共数据集上验证，有效利用增量属性，达到先进性能。

## 摘要（原文）

> Tabular data is a fundamental form of data structure. The evolution of table analysis tools reflects humanity's continuous progress in data acquisition, management, and processing. The dynamic changes in table columns arise from technological advancements, changing needs, data integration, etc. However, the standard process of training AI models on tables with fixed columns and then performing inference is not suitable for handling dynamically changed tables. Therefore, new methods are needed for efficiently handling such tables in an unsupervised manner. In this paper, we introduce a new task, Tabular Incremental Inference (TabII), which aims to enable trained models to incorporate new columns during the inference stage, enhancing the practicality of AI models in scenarios where tables are dynamically changed. Furthermore, we demonstrate that this new task can be framed as an optimization problem based on the information bottleneck theory, which emphasizes that the key to an ideal tabular incremental inference approach lies in minimizing mutual information between tabular data and representation while maximizing between representation and task labels. Under this guidance, we design a TabII method with Large Language Model placeholders and Pretrained TabAdapter to provide external knowledge and Incremental Sample Condensation blocks to condense the task-relevant information given by incremental column attributes. Experimental results across eight public datasets show that TabII effectively utilizes incremental attributes, achieving state-of-the-art performance.

