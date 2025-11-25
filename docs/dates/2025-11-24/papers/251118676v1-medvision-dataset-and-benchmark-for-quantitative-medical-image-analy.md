---
layout: default
title: MedVision: Dataset and Benchmark for Quantitative Medical Image Analysis
---

# MedVision: Dataset and Benchmark for Quantitative Medical Image Analysis
**arXiv**：[2511.18676v1](https://arxiv.org/abs/2511.18676) · [PDF](https://arxiv.org/pdf/2511.18676.pdf)  
**作者**：Yongcheng Yao, Yongshuo Zong, Raman Dutt, Yongxin Yang, Sotirios A Tsaftaris, Timothy Hospedales  

**一句话要点**：提出MedVision数据集与基准以增强医学视觉语言模型的定量分析能力

**关键词**：医学视觉语言模型, 定量图像分析, 数据集构建, 监督微调, 肿瘤大小估计, 角度测量

## 3 点简述
- 当前医学视觉语言模型缺乏定量推理能力，如肿瘤大小测量
- 构建大规模数据集，覆盖22个公共数据集，含3080万图像-标注对
- 通过监督微调显著提升检测、大小估计和角度测量任务的性能

## 摘要（原文）

> Current vision-language models (VLMs) in medicine are primarily designed for categorical question answering (e.g., "Is this normal or abnormal?") or qualitative descriptive tasks. However, clinical decision-making often relies on quantitative assessments, such as measuring the size of a tumor or the angle of a joint, from which physicians draw their own diagnostic conclusions. This quantitative reasoning capability remains underexplored and poorly supported in existing VLMs. In this work, we introduce MedVision, a large-scale dataset and benchmark specifically designed to evaluate and improve VLMs on quantitative medical image analysis. MedVision spans 22 public datasets covering diverse anatomies and modalities, with 30.8 million image-annotation pairs. We focus on three representative quantitative tasks: (1) detection of anatomical structures and abnormalities, (2) tumor/lesion (T/L) size estimation, and (3) angle/distance (A/D) measurement. Our benchmarks show that current off-the-shelf VLMs perform poorly on these tasks. However, with supervised fine-tuning on MedVision, we significantly enhance their performance across detection, T/L estimation, and A/D measurement, demonstrating reduced error rates and improved precision. This work provides a foundation for developing VLMs with robust quantitative reasoning capabilities in medical imaging. Code and data are available at https://medvision-vlm.github.io.

