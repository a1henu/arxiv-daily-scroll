---
layout: default
title: Defect-aware Hybrid Prompt Optimization via Progressive Tuning for Zero-Shot Multi-type Anomaly Detection and Segmentation
---

# Defect-aware Hybrid Prompt Optimization via Progressive Tuning for Zero-Shot Multi-type Anomaly Detection and Segmentation
**arXiv**：[2512.09446v1](https://arxiv.org/abs/2512.09446) · [PDF](https://arxiv.org/pdf/2512.09446.pdf)  
**作者**：Nadeem Nazer, Hongkuan Zhou, Lavdim Halilaj, Ylli Sadikaj, Steffen Staab  

**一句话要点**：提出DAPO方法，通过渐进调优优化缺陷感知提示，以解决零样本多类型异常检测与分割中的细粒度缺陷识别问题。

**关键词**：零样本异常检测, 缺陷感知提示优化, 渐进调优, 多类型异常分割, 视觉语言模型, 分布偏移

## 3 点简述
- 核心问题：现有视觉语言模型在异常检测中忽视细粒度缺陷类型，导致无法提供具体异常洞察。
- 方法要点：DAPO结合固定文本锚点和可学习令牌嵌入，学习混合缺陷感知提示，对齐图像特征与文本语义。
- 实验或效果：在公开基准和内部数据集上，DAPO在分布偏移下图像级AUROC和平均精度平均提升3.7%，零样本设置下新异常类型定位平均提升6.5%。

## 摘要（原文）

> Recent vision language models (VLMs) like CLIP have demonstrated impressive anomaly detection performance under significant distribution shift by utilizing high-level semantic information through text prompts. However, these models often neglect fine-grained details, such as which kind of anomalies, like "hole", "cut", "scratch" that could provide more specific insight into the nature of anomalies. We argue that recognizing fine-grained anomaly types 1) enriches the representation of "abnormal" with structured semantics, narrowing the gap between coarse anomaly signals and fine-grained defect categories; 2) enables manufacturers to understand the root causes of the anomaly and implement more targeted and appropriate corrective measures quickly. While incorporating such detailed semantic information is crucial, designing handcrafted prompts for each defect type is both time-consuming and susceptible to human bias. For this reason, we introduce DAPO, a novel approach for Defect-aware Prompt Optimization based on progressive tuning for the zero-shot multi-type and binary anomaly detection and segmentation under distribution shifts. Our approach aligns anomaly-relevant image features with their corresponding text semantics by learning hybrid defect-aware prompts with both fixed textual anchors and learnable token embeddings. We conducted experiments on public benchmarks (MPDD, VisA, MVTec-AD, MAD, and Real-IAD) and an internal dataset. The results suggest that compared to the baseline models, DAPO achieves a 3.7% average improvement in AUROC and average precision metrics at the image level under distribution shift, and a 6.5% average improvement in localizing novel anomaly types under zero-shot settings.

