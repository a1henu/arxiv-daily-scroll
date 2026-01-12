---
layout: default
title: One Language-Free Foundation Model Is Enough for Universal Vision Anomaly Detection
---

# One Language-Free Foundation Model Is Enough for Universal Vision Anomaly Detection
**arXiv**：[2601.05552v1](https://arxiv.org/abs/2601.05552) · [PDF](https://arxiv.org/pdf/2601.05552.pdf)  
**作者**：Bin-Bin Gao, Chengjie Wang  

**一句话要点**：提出UniADet框架，通过解耦权重实现无需语言模型的通用视觉异常检测

**关键词**：通用视觉异常检测, 零样本学习, 少样本学习, 解耦权重学习, 参数高效模型, 工业与医疗应用

## 3 点简述
- 核心问题：现有视觉-语言模型方法依赖复杂提示工程和适配模块，限制通用性
- 方法要点：发现语言编码器非必需，提出解耦分类与分割及跨层特征的简单权重学习
- 实验或效果：在14个基准测试中超越零/少样本方法，参数仅0.002M，高效通用

## 摘要（原文）

> Universal visual anomaly detection (AD) aims to identify anomaly images and segment anomaly regions towards open and dynamic scenarios, following zero- and few-shot paradigms without any dataset-specific fine-tuning. We have witnessed significant progress in widely use of visual-language foundational models in recent approaches. However, current methods often struggle with complex prompt engineering, elaborate adaptation modules, and challenging training strategies, ultimately limiting their flexibility and generality. To address these issues, this paper rethinks the fundamental mechanism behind visual-language models for AD and presents an embarrassingly simple, general, and effective framework for Universal vision Anomaly Detection (UniADet). Specifically, we first find language encoder is used to derive decision weights for anomaly classification and segmentation, and then demonstrate that it is unnecessary for universal AD. Second, we propose an embarrassingly simple method to completely decouple classification and segmentation, and decouple cross-level features, i.e., learning independent weights for different tasks and hierarchical features. UniADet is highly simple (learning only decoupled weights), parameter-efficient (only 0.002M learnable parameters), general (adapting a variety of foundation models), and effective (surpassing state-of-the-art zero-/few-shot by a large margin and even full-shot AD methods for the first time) on 14 real-world AD benchmarks covering both industrial and medical domains. We will make the code and model of UniADet available at https://github.com/gaobb/UniADet.

