---
layout: default
title: MHub.ai: A Simple, Standardized, and Reproducible Platform for AI Models in Medical Imaging
---

# MHub.ai: A Simple, Standardized, and Reproducible Platform for AI Models in Medical Imaging
**arXiv**：[2601.10154v1](https://arxiv.org/abs/2601.10154) · [PDF](https://arxiv.org/pdf/2601.10154.pdf)  
**作者**：Leonard Nürnberg, Dennis Bontempi, Suraj Pai, Curtis Lisle, Steve Pieper, Ron Kikinis, Sil van de Leemput, Rahul Soni, Gowtham Murugesan, Cosmin Ciausu, Miriam Groeneveld, Felix J. Dorfner, Jue Jiang, Aneesh Rangnekar, Harini Veeraraghavan, Joeran S. Bosma, Keno Bressem, Raymond Mak, Andrey Fedorov, Hugo JWL Aerts  

**一句话要点**：提出MHub.ai平台以解决医学影像AI模型标准化与可复现性问题

**关键词**：医学影像AI, 模型容器化, 可复现性平台, DICOM处理, 开源框架

## 3 点简述
- 医学影像AI面临模型实现多样、文档不一致和可复现性差等挑战
- MHub.ai通过容器化封装模型，支持DICOM格式处理，提供统一接口和元数据
- 平台包含分割、预测等模型，通过临床用例验证，并公开数据和评估指标

## 摘要（原文）

> Artificial intelligence (AI) has the potential to transform medical imaging by automating image analysis and accelerating clinical research. However, research and clinical use are limited by the wide variety of AI implementations and architectures, inconsistent documentation, and reproducibility issues. Here, we introduce MHub.ai, an open-source, container-based platform that standardizes access to AI models with minimal configuration, promoting accessibility and reproducibility in medical imaging. MHub.ai packages models from peer-reviewed publications into standardized containers that support direct processing of DICOM and other formats, provide a unified application interface, and embed structured metadata. Each model is accompanied by publicly available reference data that can be used to confirm model operation. MHub.ai includes an initial set of state-of-the-art segmentation, prediction, and feature extraction models for different modalities. The modular framework enables adaptation of any model and supports community contributions. We demonstrate the utility of the platform in a clinical use case through comparative evaluation of lung segmentation models. To further strengthen transparency and reproducibility, we publicly release the generated segmentations and evaluation metrics and provide interactive dashboards that allow readers to inspect individual cases and reproduce or extend our analysis. By simplifying model use, MHub.ai enables side-by-side benchmarking with identical execution commands and standardized outputs, and lowers the barrier to clinical translation.

