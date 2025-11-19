---
layout: default
title: Zero-Training Task-Specific Model Synthesis for Few-Shot Medical Image Classification
---

# Zero-Training Task-Specific Model Synthesis for Few-Shot Medical Image Classification
**arXiv**：[2511.14082v1](https://arxiv.org/abs/2511.14082) · [PDF](https://arxiv.org/pdf/2511.14082.pdf)  
**作者**：Yao Qin, Yangyang Yan, YuanChao Yang, Jinhua Pang, Huanyong Bi, Yuan Liu, HaiHua Wang  

**一句话要点**：提出零训练任务特定模型合成方法，以解决少样本医学图像分类问题

**关键词**：少样本学习, 医学图像分类, 零训练模型合成, 参数生成, 罕见病诊断, 多模态输入

## 3 点简述
- 医学图像分析依赖大规模标注数据，但数据获取和标注成本高，尤其罕见病样本稀缺
- 利用预训练生成引擎，基于单图像和文本描述直接合成分类器参数，无需任务特定训练
- 在ISIC 2018和罕见病数据集上，1-shot和5-shot分类性能优于现有方法，达到新SOTA

## 摘要（原文）

> Deep learning models have achieved remarkable success in medical image analysis but are fundamentally constrained by the requirement for large-scale, meticulously annotated datasets. This dependency on "big data" is a critical bottleneck in the medical domain, where patient data is inherently difficult to acquire and expert annotation is expensive, particularly for rare diseases where samples are scarce by definition. To overcome this fundamental challenge, we propose a novel paradigm: Zero-Training Task-Specific Model Synthesis (ZS-TMS). Instead of adapting a pre-existing model or training a new one, our approach leverages a large-scale, pre-trained generative engine to directly synthesize the entire set of parameters for a task-specific classifier. Our framework, the Semantic-Guided Parameter Synthesizer (SGPS), takes as input minimal, multi-modal task information as little as a single example image (1-shot) and a corresponding clinical text description to directly synthesize the entire set of parameters for a task-specific classifier.
>   The generative engine interprets these inputs to generate the weights for a lightweight, efficient classifier (e.g., an EfficientNet-V2), which can be deployed for inference immediately without any task-specific training or fine-tuning. We conduct extensive evaluations on challenging few-shot classification benchmarks derived from the ISIC 2018 skin lesion dataset and a custom rare disease dataset. Our results demonstrate that SGPS establishes a new state-of-the-art, significantly outperforming advanced few-shot and zero-shot learning methods, especially in the ultra-low data regimes of 1-shot and 5-shot classification. This work paves the way for the rapid development and deployment of AI-powered diagnostic tools, particularly for the long tail of rare diseases where data is critically limited.

