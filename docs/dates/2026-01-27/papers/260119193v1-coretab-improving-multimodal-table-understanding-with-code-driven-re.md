---
layout: default
title: CoReTab: Improving Multimodal Table Understanding with Code-driven Reasoning
---

# CoReTab: Improving Multimodal Table Understanding with Code-driven Reasoning
**arXiv**：[2601.19193v1](https://arxiv.org/abs/2601.19193) · [PDF](https://arxiv.org/pdf/2601.19193.pdf)  
**作者**：Van-Quang Nguyen, Takayuki Okatani  

**一句话要点**：提出CoReTab框架，通过代码驱动推理提升多模态表格理解的多步推理能力。

**关键词**：多模态表格理解, 代码驱动推理, 多步推理监督, 可解释人工智能, 表格问答, 数据集构建

## 3 点简述
- 现有数据集如MMTab缺乏多步推理监督，导致模型回答简短、准确性不足且可解释性差。
- CoReTab结合多步推理与可执行Python代码，生成可扩展、可解释且自动验证的标注。
- 在17个MMTab基准测试中，CoReTab训练模型在问答、事实验证和结构理解任务上分别提升6.2%、5.7%和25.6%。

## 摘要（原文）

> Existing datasets for multimodal table understanding, such as MMTab, primarily provide short factual answers without explicit multi-step reasoning supervision. Models trained on these datasets often generate brief responses that offers insufficient accuracy and limited interpretability into how these models arrive at the final answer. We introduce CoReTab, a code-driven reasoning framework that produces scalable, interpretable, and automatically verifiable annotations by coupling multi-step reasoning with executable Python code. Using the CoReTab framework, we curate a dataset of 115K verified samples averaging 529 tokens per response and fine-tune open-source MLLMs through a three-stage pipeline. We evaluate the resulting model trained on CoReTab across 17 MMTab benchmarks spanning table question answering, fact verification, and table structure understanding. Our model achieves significant gains of +6.2%, +5.7%, and +25.6%, respectively, over MMTab-trained baselines, while producing transparent and verifiable reasoning traces. These results establish CoReTab as a robust and generalizable supervision framework for improving multi-step reasoning in multimodal table understanding.

