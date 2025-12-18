---
layout: default
title: How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness
---

# How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness
**arXiv**：[2512.15634v1](https://arxiv.org/abs/2512.15634) · [PDF](https://arxiv.org/pdf/2512.15634.pdf)  
**作者**：Darshita Rathore, Vineet Kumar, Chetna Bansal, Anindya Moitra  

**一句话要点**：探索LoRA秩配置在问答任务中平衡知识保留与领域鲁棒性的影响

**关键词**：参数高效微调, LoRA秩配置, 问答任务泛化, 注意力结构分析, 知识保留

## 3 点简述
- 核心问题：LoRA等参数高效微调方法在问答任务中的秩配置对性能与泛化的影响未知
- 方法要点：通过秩扫描实验比较LoRA与全监督微调在推理和召回数据集上的表现
- 实验或效果：LoRA在特定秩值下推理任务表现优于全监督微调，并分析注意力结构变化

## 摘要（原文）

> Large language models are increasingly adapted to downstream tasks through fine-tuning. Full supervised fine-tuning (SFT) and parameter-efficient fine-tuning (PEFT) methods, such as Low-Rank Adaptation (LoRA), are two dominant approaches. While PEFT methods are widely used for their computational efficiency, the implications of their configurations (e.g., rank) remain under-explored in downstream Q&A tasks and generalisation. In this work, we perform a comprehensive evaluation across multiple reasoning and recall datasets, conducting a rank sweep to quantify the trade-off between SFT and PEFT. We also compare the accuracy of PEFT and SFT models across in-domain and out-of-domain adaptation, highlighting distinct generalisation behaviour and task-specific forgetting. We demonstrate that LoRA achieves competitive and in some cases superior performance compared to SFT, particularly on reasoning tasks at specific rank values. Additionally, we analyze the internal representations via spectral features and layer-wise attention structures, offering insights into representational drift and structural changes in attention patterns.

