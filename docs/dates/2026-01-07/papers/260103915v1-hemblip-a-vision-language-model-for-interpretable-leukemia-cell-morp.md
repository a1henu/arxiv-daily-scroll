---
layout: default
title: HemBLIP: A Vision-Language Model for Interpretable Leukemia Cell Morphology Analysis
---

# HemBLIP: A Vision-Language Model for Interpretable Leukemia Cell Morphology Analysis
**arXiv**：[2601.03915v1](https://arxiv.org/abs/2601.03915) · [PDF](https://arxiv.org/pdf/2601.03915.pdf)  
**作者**：Julie van Logtestijn, Petru Manescu  

**一句话要点**：提出HemBLIP视觉语言模型以生成可解释的白血病细胞形态描述，提升临床诊断透明度。

**关键词**：视觉语言模型, 白血病细胞形态分析, 可解释性诊断, 参数高效训练, 医学图像描述

## 3 点简述
- 核心问题：白血病诊断中深度学习模型常为黑箱，限制临床信任与应用。
- 方法要点：基于新构建的细胞数据集，通过全微调和LoRA高效训练适配通用VLM。
- 实验或效果：在描述质量和形态准确性上优于MedGEMMA，LoRA适配进一步降低计算成本。

## 摘要（原文）

> Microscopic evaluation of white blood cell morphology is central to leukemia diagnosis, yet current deep learning models often act as black boxes, limiting clinical trust and adoption. We introduce HemBLIP, a vision language model designed to generate interpretable, morphology aware descriptions of peripheral blood cells. Using a newly constructed dataset of 14k healthy and leukemic cells paired with expert-derived attribute captions, we adapt a general-purpose VLM via both full fine-tuning and LoRA based parameter efficient training, and benchmark against the biomedical foundation model MedGEMMA. HemBLIP achieves higher caption quality and morphological accuracy, while LoRA adaptation provides further gains with significantly reduced computational cost. These results highlight the promise of vision language models for transparent and scalable hematological diagnostics.

