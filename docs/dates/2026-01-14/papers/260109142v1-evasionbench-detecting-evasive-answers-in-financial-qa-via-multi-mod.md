---
layout: default
title: EvasionBench: Detecting Evasive Answers in Financial Q&A via Multi-Model Consensus and LLM-as-Judge
---

# EvasionBench: Detecting Evasive Answers in Financial Q&A via Multi-Model Consensus and LLM-as-Judge
**arXiv**：[2601.09142v1](https://arxiv.org/abs/2601.09142) · [PDF](https://arxiv.org/pdf/2601.09142.pdf)  
**作者**：Shijian Ma, Yan Lin, Yi Yang  

**一句话要点**：提出EvasionBench基准和多模型共识框架，以检测财报问答中的规避性回答。

**关键词**：规避性回答检测, 财报问答, 多模型共识, 边界案例挖掘, 模型蒸馏, 金融透明度

## 3 点简述
- 核心问题：缺乏大规模基准阻碍财报问答中规避性回答的检测进展。
- 方法要点：利用前沿大语言模型间的分歧挖掘边界案例，通过法官模型解决标签。
- 实验或效果：训练模型Eva-4B准确率达81.3%，推理成本远低于前沿大模型。

## 摘要（原文）

> Detecting evasive answers in earnings calls is critical for financial transparency, yet progress is hindered by the lack of large-scale benchmarks. We introduce EvasionBench, comprising 30,000 training samples and 1,000 human-annotated test samples (Cohen's Kappa 0.835) across three evasion levels. Our key contribution is a multi-model annotation framework leveraging a core insight: disagreement between frontier LLMs signals hard examples most valuable for training. We mine boundary cases where two strong annotators conflict, using a judge to resolve labels. This approach outperforms single-model distillation by 2.4 percent, with judge-resolved samples improving generalization despite higher training loss (0.421 vs 0.393) - evidence that disagreement mining acts as implicit regularization. Our trained model Eva-4B (4B parameters) achieves 81.3 percent accuracy, outperforming its base by 25 percentage points and approaching frontier LLM performance at a fraction of inference cost.

