---
layout: default
title: DR-LoRA: Dynamic Rank LoRA for Mixture-of-Experts Adaptation
---

# DR-LoRA: Dynamic Rank LoRA for Mixture-of-Experts Adaptation
**arXiv**：[2601.04823v1](https://arxiv.org/abs/2601.04823) · [PDF](https://arxiv.org/pdf/2601.04823.pdf)  
**作者**：Guanzhi Deng, Bo Li, Ronghao Chen, Huacan Wang, Linqi Song, Lijie Wen  

**一句话要点**：提出动态秩LoRA框架以解决MoE LLMs微调中专家资源分配不均问题

**关键词**：混合专家模型, 参数高效微调, LoRA, 动态秩分配, 专家显著性评分

## 3 点简述
- 核心问题：现有LoRA方法为MoE LLMs所有专家分配相同秩，忽略功能专业化，导致资源错配
- 方法要点：基于专家路由频率和LoRA秩重要性动态扩展专家秩，形成异质秩分布
- 实验或效果：在相同参数预算下，优于标准LoRA和静态策略，提升任务性能和参数利用率

## 摘要（原文）

> Mixture-of-Experts (MoE) has become a prominent paradigm for scaling Large Language Models (LLMs). Parameter-efficient fine-tuning (PEFT), such as LoRA, is widely adopted to adapt pretrained MoE LLMs to downstream tasks. However, existing approaches assign identical LoRA ranks to all experts, overlooking the intrinsic functional specialization within MoE LLMs. This uniform allocation leads to resource mismatch, task-relevant experts are under-provisioned while less relevant ones receive redundant parameters. We propose a Dynamic Rank LoRA framework named DR-LoRA, which dynamically grows expert LoRA ranks during fine-tuning based on task-specific demands. DR-LoRA employs an Expert Saliency Scoring mechanism that integrates expert routing frequency and LoRA rank importance to quantify each expert's demand for additional capacity. Experts with higher saliency scores are prioritized for rank expansion, enabling the automatic formation of a heterogeneous rank distribution tailored to the target task. Experiments on multiple benchmarks demonstrate that DR-LoRA consistently outperforms standard LoRA and static allocation strategies under the same parameter budget, achieving superior task performance with more efficient parameter utilization.

