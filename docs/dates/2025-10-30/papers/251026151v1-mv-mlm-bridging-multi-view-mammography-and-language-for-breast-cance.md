---
layout: default
title: MV-MLM: Bridging Multi-View Mammography and Language for Breast Cancer Diagnosis and Risk Prediction
---

# MV-MLM: Bridging Multi-View Mammography and Language for Breast Cancer Diagnosis and Risk Prediction
**arXiv**：[2510.26151v1](https://arxiv.org/abs/2510.26151) · [PDF](https://arxiv.org/pdf/2510.26151.pdf)  
**作者**：Shunjie-Fabian Zheng, Hyeonjun Lee, Thijs Kooi, Ali Diba  

**一句话要点**：提出多视图乳腺X光与语言模型，用于乳腺癌诊断和风险预测

**关键词**：多视图乳腺X光, 视觉语言模型, 乳腺癌诊断, 风险预测, 跨模态学习, 自监督学习

## 3 点简述
- 核心问题：乳腺X光图像标注数据稀缺，成本高，影响CAD模型训练。
- 方法要点：利用多视图图像与合成报告进行跨模态自监督学习，提升表示能力。
- 实验或效果：在私有和公开数据集上，恶性分类、亚型分类和风险预测任务达到SOTA。

## 摘要（原文）

> Large annotated datasets are essential for training robust Computer-Aided
> Diagnosis (CAD) models for breast cancer detection or risk prediction. However,
> acquiring such datasets with fine-detailed annotation is both costly and
> time-consuming. Vision-Language Models (VLMs), such as CLIP, which are
> pre-trained on large image-text pairs, offer a promising solution by enhancing
> robustness and data efficiency in medical imaging tasks. This paper introduces
> a novel Multi-View Mammography and Language Model for breast cancer
> classification and risk prediction, trained on a dataset of paired mammogram
> images and synthetic radiology reports. Our MV-MLM leverages multi-view
> supervision to learn rich representations from extensive radiology data by
> employing cross-modal self-supervision across image-text pairs. This includes
> multiple views and the corresponding pseudo-radiology reports. We propose a
> novel joint visual-textual learning strategy to enhance generalization and
> accuracy performance over different data types and tasks to distinguish breast
> tissues or cancer characteristics(calcification, mass) and utilize these
> patterns to understand mammography images and predict cancer risk. We evaluated
> our method on both private and publicly available datasets, demonstrating that
> the proposed model achieves state-of-the-art performance in three
> classification tasks: (1) malignancy classification, (2) subtype
> classification, and (3) image-based cancer risk prediction. Furthermore, the
> model exhibits strong data efficiency, outperforming existing fully supervised
> or VLM baselines while trained on synthetic text reports and without the need
> for actual radiology reports.

