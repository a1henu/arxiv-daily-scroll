---
layout: default
title: Mechanisms are Transferable: Data-Efficient Low-Resource Adaptation via Circuit-Targeted Supervised Fine-Tuning
---

# Mechanisms are Transferable: Data-Efficient Low-Resource Adaptation via Circuit-Targeted Supervised Fine-Tuning
**arXiv**：[2601.08146v1](https://arxiv.org/abs/2601.08146) · [PDF](https://arxiv.org/pdf/2601.08146.pdf)  
**作者**：Khumaisa Nur'aini, Ayu Purwarianti, Alham Fikri Aji, Derry Wijaya  

**一句话要点**：提出电路目标监督微调以解决低资源语言适应中的数据稀缺和灾难性遗忘问题

**关键词**：低资源语言适应, 电路目标监督微调, 注意力头稀疏化, 跨语言迁移学习, 灾难性遗忘缓解

## 3 点简述
- 核心问题：低资源语言适应中标注数据稀缺、全模型微调不稳定且易导致灾难性遗忘
- 方法要点：基于代理语言检查点识别任务相关稀疏注意力头，仅更新这些头及LayerNorm进行迁移学习
- 实验或效果：在NusaX-Senti和XNLI上提升跨语言准确率，减少参数更新并显著降低灾难性遗忘

## 摘要（原文）

> Adapting LLMs to low-resource languages is difficult: labeled data is scarce, full-model fine-tuning is unstable, and continued cross-lingual tuning can cause catastrophic forgetting. We propose Circuit-Targeted Supervised Fine-Tuning (CT-SFT): a counterfactual-free adaptation of CD-T (Contextual Decomposition Transformer) that uses a label-balanced mean baseline and task-directional relevance scoring to identify a sparse set of task-relevant attention heads in a proxy-language checkpoint, then transfer learns to a target language by updating only those heads (plus LayerNorm) via head-level gradient masking. Across NusaX-Senti and XNLI, CT-SFT improves cross-lingual accuracy over continued full fine-tuning while updating only a small subset of model parameters. We find an editing-preserving trade-off: harder transfers favor editing circuit heads, while easier transfers often favor near-zero (i.e., low-relevance heads) updates, preserving the source mechanism. CT-SFT also substantially reduces catastrophic forgetting, preserving proxy/source-language competence during transfer.

