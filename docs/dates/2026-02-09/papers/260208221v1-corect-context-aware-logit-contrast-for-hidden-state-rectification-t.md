---
layout: default
title: CoRect: Context-Aware Logit Contrast for Hidden State Rectification to Resolve Knowledge Conflicts
---

# CoRect: Context-Aware Logit Contrast for Hidden State Rectification to Resolve Knowledge Conflicts
**arXiv**：[2602.08221v1](https://arxiv.org/abs/2602.08221) · [PDF](https://arxiv.org/pdf/2602.08221.pdf)  
**作者**：Xuhua Ma, Richong Zhang, Zhijie Nie  

**一句话要点**：提出CoRect方法，通过上下文感知的logit对比和隐藏状态校正，解决检索增强生成中的知识冲突问题。

**关键词**：检索增强生成, 知识冲突, 隐藏状态校正, logit对比, 参数偏差, 幻觉减少

## 3 点简述
- 核心问题：检索增强生成中，模型内部参数知识覆盖检索证据，导致输出不忠实。
- 方法要点：通过对比上下文化和非上下文化前向传播的logit，识别参数偏差层，校正隐藏状态以保留证据信息。
- 实验或效果：在问答和摘要基准测试中，相比强基线，CoRect一致提升忠实度并减少幻觉。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) often struggles with knowledge conflicts, where model-internal parametric knowledge overrides retrieved evidence, leading to unfaithful outputs. Existing approaches are often limited, relying either on superficial decoding adjustments or weight editing that necessitates ground-truth targets. Through layer-wise analysis, we attribute this failure to a parametric suppression phenomenon: specifically, in deep layers, certain FFN layers overwrite context-sensitive representations with memorized priors. To address this, we propose CoRect (Context-Aware Logit Contrast for Hidden State Rectification). By contrasting logits from contextualized and non-contextualized forward passes, CoRect identifies layers that exhibit high parametric bias without requiring ground-truth labels. It then rectifies the hidden states to preserve evidence-grounded information. Across question answering (QA) and summarization benchmarks, CoRect consistently improves faithfulness and reduces hallucinations compared to strong baselines.

