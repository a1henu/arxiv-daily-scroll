---
layout: default
title: Computing patient similarity based on unstructured clinical notes
---

# Computing patient similarity based on unstructured clinical notes
**arXiv**：[2601.07385v1](https://arxiv.org/abs/2601.07385) · [PDF](https://arxiv.org/pdf/2601.07385.pdf)  
**作者**：Petr Zelina, Marko Řeháček, Jana Halámková, Lucia Bohovicová, Martin Rusinko, Vít Nováček  

**一句话要点**：提出基于临床笔记矩阵表示的患者相似性计算方法，用于精准医疗任务。

**关键词**：患者相似性计算, 临床笔记分析, 矩阵表示, 精准医疗, 低秩表示

## 3 点简述
- 核心问题：临床笔记非结构化，难以大规模利用于患者相似性分析。
- 方法要点：将患者表示为笔记嵌入聚合的矩阵，基于低秩表示计算相似性。
- 实验或效果：在捷克乳腺癌患者数据上评估多种相似性度量，验证方法对下游任务的有效性。

## 摘要（原文）

> Clinical notes hold rich yet unstructured details about diagnoses, treatments, and outcomes that are vital to precision medicine but hard to exploit at scale. We introduce a method that represents each patient as a matrix built from aggregated embeddings of all their notes, enabling robust patient similarity computation based on their latent low-rank representations. Using clinical notes of 4,267 Czech breast-cancer patients and expert similarity labels from Masaryk Memorial Cancer Institute, we evaluate several matrix-based similarity measures and analyze their strengths and limitations across different similarity facets, such as clinical history, treatment, and adverse events. The results demonstrate the usefulness of the presented method for downstream tasks, such as personalized therapy recommendations or toxicity warnings.

