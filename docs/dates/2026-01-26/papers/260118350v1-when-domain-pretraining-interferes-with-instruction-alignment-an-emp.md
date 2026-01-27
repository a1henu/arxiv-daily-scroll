---
layout: default
title: When Domain Pretraining Interferes with Instruction Alignment: An Empirical Study of Adapter Merging in Medical LLMs
---

# When Domain Pretraining Interferes with Instruction Alignment: An Empirical Study of Adapter Merging in Medical LLMs
**arXiv**：[2601.18350v1](https://arxiv.org/abs/2601.18350) · [PDF](https://arxiv.org/pdf/2601.18350.pdf)  
**作者**：Junyi Zou  

**一句话要点**：提出加权适配器合并方法以平衡医学大语言模型的指令对齐与领域知识保留。

**关键词**：医学大语言模型, 适配器合并, 指令对齐, 领域自适应预训练, 监督微调

## 3 点简述
- 核心问题：大语言模型在医学领域存在术语精度不足和指令遵循安全问题。
- 方法要点：采用两阶段LoRA流程，结合领域自适应预训练和监督微调，并通过加权合并适配器。
- 实验或效果：在医学验证集上，合并模型在BLEU-4和ROUGE指标上取得具体性能提升。

## 摘要（原文）

> Large language models (LLMs) show strong general capability but often struggle with medical terminology precision and safety-critical instruction following. We present a case study for adapter interference in safety-critical domains using a 14B-parameter base model through a two-stage LoRA pipeline: (1) domain-adaptive pre-training (PT) to inject broad medical knowledge via continued pre-training (DAPT), and (2) supervised fine-tuning (SFT) to align the model with medical question-answering behaviors through instruction-style data. To balance instruction-following ability and domain knowledge retention, we propose Weighted Adapter Merging, linearly combining SFT and PT adapters before exporting a merged base-model checkpoint. On a held-out medical validation set (F5/F6), the merged model achieves BLEU-4 = 16.38, ROUGE-1 = 20.42, ROUGE-2 = 4.60, and ROUGE-L = 11.54 under a practical decoding configuration. We further analyze decoding sensitivity and training stability with loss curves and controlled decoding comparisons.

