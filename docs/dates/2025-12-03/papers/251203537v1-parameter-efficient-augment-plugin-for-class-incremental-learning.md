---
layout: default
title: Parameter-Efficient Augment Plugin for Class-Incremental Learning
---

# Parameter-Efficient Augment Plugin for Class-Incremental Learning
**arXiv**：[2512.03537v1](https://arxiv.org/abs/2512.03537) · [PDF](https://arxiv.org/pdf/2512.03537.pdf)  
**作者**：Zhiming Xu, Baile Xu, Jian Zhao, Furao Shen, Suorong Yang  

**一句话要点**：提出DLC插件范式，通过LoRA组件增强非预训练类增量学习，提升效率与准确性。

**关键词**：类增量学习, 参数高效, LoRA适配, 插件扩展, 非预训练场景, 特征聚合

## 3 点简述
- 现有类增量学习方法受遗忘或稳定性-可塑性困境限制，扩展方法参数开销大。
- DLC使用LoRA注入任务特定残差到基础模型，并引入轻量加权单元减少干扰。
- 在ImageNet-100上，仅用4%参数实现8%准确率提升，超越固定内存预算下先进方法。

## 摘要（原文）

> Existing class-incremental learning (CIL) approaches based on replay or knowledge distillation are often constrained by forgetting or the stability-plasticity dilemma. Some expansion-based approaches could achieve higher accuracy. However, they always require significant parameter increases. In this paper, we propose a plugin extension paradigm termed the Deployment of extra LoRA Components (DLC) for non-pre-trained CIL scenarios.We treat the feature extractor trained through replay or distillation as a base model with rich knowledge. For each task, we use Low-Rank Adaptation (LoRA) to inject task-specific residuals into the base model's deep layers. During inference, representations with task-specific residuals are aggregated to produce classification predictions. To mitigate interference from non-target LoRA plugins, we introduce a lightweight weighting unit. This unit learns to assign importance scores to different LoRA-tuned representations. Like downloadable contents in software, our method serves as a plug-and-play enhancement that efficiently extends the base methods. Remarkably, on the large-scale ImageNet-100, with merely 4 % of the parameters of a standard ResNet-18, our DLC model achieves a significant 8 % improvement in accuracy, demonstrating exceptional efficiency. Moreover, it could surpass state-of-the-art methods under the fixed memory budget.

