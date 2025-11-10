---
layout: default
title: PySlyde: A Lightweight, Open-Source Toolkit for Pathology Preprocessing
---

# PySlyde: A Lightweight, Open-Source Toolkit for Pathology Preprocessing
**arXiv**：[2511.05183v1](https://arxiv.org/abs/2511.05183) · [PDF](https://arxiv.org/pdf/2511.05183.pdf)  
**作者**：Gregory Verghese, Anthony Baptista, Chima Eke, Holly Rafique, Mengyuan Li, Fathima Mohamed, Ananya Bhalla, Lucy Ryan, Michael Pitcher, Enrico Parisini, Concetta Piazzese, Liz Ing-Simmons, Anita Grigoriadis  

**一句话要点**：提出PySlyde工具包以简化病理全切片图像的预处理流程

**关键词**：病理图像预处理, 全切片图像分析, 开源工具包, 组织检测, 特征提取

## 3 点简述
- 病理全切片图像规模大、变异性高，标准化预处理困难
- 基于OpenSlide构建轻量Python工具，提供组织检测、分块和特征提取API
- 统一预处理流程，提升可重复性并加速AI数据集生成

## 摘要（原文）

> The integration of artificial intelligence (AI) into pathology is advancing
> precision medicine by improving diagnosis, treatment planning, and patient
> outcomes. Digitised whole-slide images (WSIs) capture rich spatial and
> morphological information vital for understanding disease biology, yet their
> gigapixel scale and variability pose major challenges for standardisation and
> analysis. Robust preprocessing, covering tissue detection, tessellation, stain
> normalisation, and annotation parsing is critical but often limited by
> fragmented and inconsistent workflows. We present PySlyde, a lightweight,
> open-source Python toolkit built on OpenSlide to simplify and standardise WSI
> preprocessing. PySlyde provides an intuitive API for slide loading, annotation
> management, tissue detection, tiling, and feature extraction, compatible with
> modern pathology foundation models. By unifying these processes, it streamlines
> WSI preprocessing, enhances reproducibility, and accelerates the generation of
> AI-ready datasets, enabling researchers to focus on model development and
> downstream analysis.

