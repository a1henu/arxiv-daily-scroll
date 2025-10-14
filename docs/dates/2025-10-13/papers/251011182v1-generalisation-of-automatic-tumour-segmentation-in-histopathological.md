---
layout: default
title: Generalisation of automatic tumour segmentation in histopathological whole-slide images across multiple cancer types
---

# Generalisation of automatic tumour segmentation in histopathological whole-slide images across multiple cancer types
**arXiv**：[2510.11182v1](https://arxiv.org/abs/2510.11182) · [PDF](https://arxiv.org/pdf/2510.11182.pdf)  
**作者**：Ole-Johan Skrede, Manohar Pradhan, Maria Xepapadakis Isaksen, Tarjei Sveinsgjerd Hveem, Ljiljana Vlatkovic, Arild Nesbakken, Kristina Lindemann, Gunnar B Kristensen, Jenneke Kasius, Alain G Zeimet, Odd Terje Brustugun, Lill-Tove Rasmussen Busund, Elin H Richardsen, Erik Skaaheim Haug, Bjørn Brennhovd, Emma Rewcastle, Melinda Lillesand, Vebjørn Kvikstad, Emiel Janssen, David J Kerr, Knut Liestøl, Fritz Albregtsen, Andreas Kleppe  

**一句话要点**：提出通用肿瘤分割模型，在多种癌症类型中实现高精度分割。

**关键词**：肿瘤分割, 深度学习, 组织病理学图像, 多癌症类型, 通用模型

## 3 点简述
- 核心问题：开发单一模型在组织病理学全切片图像中通用肿瘤分割，适应不同癌症类型。
- 方法要点：使用深度学习，基于超过20000张全切片图像训练模型，涵盖四种癌症类型。
- 实验或效果：在外部验证队列中平均Dice系数超过80%，性能与专用模型相当。

## 摘要（原文）

> Deep learning is expected to aid pathologists by automating tasks such as
> tumour segmentation. We aimed to develop one universal tumour segmentation
> model for histopathological images and examine its performance in different
> cancer types. The model was developed using over 20 000 whole-slide images from
> over 4 000 patients with colorectal, endometrial, lung, or prostate carcinoma.
> Performance was validated in pre-planned analyses on external cohorts with over
> 3 000 patients across six cancer types. Exploratory analyses included over 1
> 500 additional patients from The Cancer Genome Atlas. Average Dice coefficient
> was over 80% in all validation cohorts with en bloc resection specimens and in
> The Cancer Genome Atlas cohorts. No loss of performance was observed when
> comparing the universal model with models specialised on single cancer types.
> In conclusion, extensive and rigorous evaluations demonstrate that generic
> tumour segmentation by a single model is possible across cancer types, patient
> populations, sample preparations, and slide scanners.

