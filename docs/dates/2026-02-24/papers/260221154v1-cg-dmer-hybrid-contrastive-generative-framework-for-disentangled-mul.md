---
layout: default
title: CG-DMER: Hybrid Contrastive-Generative Framework for Disentangled Multimodal ECG Representation Learning
---

# CG-DMER: Hybrid Contrastive-Generative Framework for Disentangled Multimodal ECG Representation Learning
**arXiv**：[2602.21154v1](https://arxiv.org/abs/2602.21154) · [PDF](https://arxiv.org/pdf/2602.21154.pdf)  
**作者**：Ziwei Niu, Hao Sun, Shujun Bian, Xihong Yang, Lanfen Lin, Yuxin Liu, Yueming Jin  

**一句话要点**：提出CG-DMER框架，通过对比-生成方法解决心电图多模态表示学习中的模态内和模态间问题。

**关键词**：多模态学习, 心电图分析, 表示解缠, 对比学习, 生成建模, 时空建模

## 3 点简述
- 核心问题：现有方法忽略心电图导联间时空依赖，且直接对齐信号与临床报告引入模态特定偏差。
- 方法要点：设计时空掩码建模捕获细粒度模式，并采用表示解缠与对齐策略分离模态不变和特定表示。
- 实验或效果：在三个公共数据集上验证，CG-DMER在多种下游任务中达到最先进性能。

## 摘要（原文）

> Accurate interpretation of electrocardiogram (ECG) signals is crucial for diagnosing cardiovascular diseases. Recent multimodal approaches that integrate ECGs with accompanying clinical reports show strong potential, but they still face two main concerns from a modality perspective: (1) intra-modality: existing models process ECGs in a lead-agnostic manner, overlooking spatial-temporal dependencies across leads, which restricts their effectiveness in modeling fine-grained diagnostic patterns; (2) inter-modality: existing methods directly align ECG signals with clinical reports, introducing modality-specific biases due to the free-text nature of the reports. In light of these two issues, we propose CG-DMER, a contrastive-generative framework for disentangled multimodal ECG representation learning, powered by two key designs: (1) Spatial-temporal masked modeling is designed to better capture fine-grained temporal dynamics and inter-lead spatial dependencies by applying masking across both spatial and temporal dimensions and reconstructing the missing information. (2) A representation disentanglement and alignment strategy is designed to mitigate unnecessary noise and modality-specific biases by introducing modality-specific and modality-shared encoders, ensuring a clearer separation between modality-invariant and modality-specific representations. Experiments on three public datasets demonstrate that CG-DMER achieves state-of-the-art performance across diverse downstream tasks.

