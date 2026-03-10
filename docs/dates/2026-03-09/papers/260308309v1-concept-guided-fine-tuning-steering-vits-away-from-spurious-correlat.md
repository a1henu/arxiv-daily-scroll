---
layout: default
title: Concept-Guided Fine-Tuning: Steering ViTs away from Spurious Correlations to Improve Robustness
---

# Concept-Guided Fine-Tuning: Steering ViTs away from Spurious Correlations to Improve Robustness
**arXiv**：[2603.08309v1](https://arxiv.org/abs/2603.08309) · [PDF](https://arxiv.org/pdf/2603.08309.pdf)  
**作者**：Yehonatan Elisha, Oren Barkan, Noam Koenigstein  

**一句话要点**：提出概念引导微调框架，通过对齐概念掩码提升ViT在分布偏移下的鲁棒性。

**关键词**：视觉Transformer, 鲁棒性, 概念引导微调, 分布偏移, 相关性图对齐

## 3 点简述
- 核心问题：ViT依赖虚假相关性（如背景线索），导致分布偏移下性能下降。
- 方法要点：自动生成概念掩码，微调时对齐内部相关性图并抑制背景关注。
- 实验或效果：在五个分布偏移基准上验证鲁棒性提升，相关性图更对齐语义对象部分。

## 摘要（原文）

> Vision Transformers (ViTs) often degrade under distribution shifts because they rely on spurious correlations, such as background cues, rather than semantically meaningful features. Existing regularization methods, typically relying on simple foreground-background masks, which fail to capture the fine-grained semantic concepts that define an object (e.g., ``long beak'' and ``wings'' for a ``bird''). As a result, these methods provide limited robustness to distribution shifts. To address this limitation, we introduce a novel finetuning framework that steers model reasoning toward concept-level semantics. Our approach optimizes the model's internal relevance maps to align with spatially grounded concept masks. These masks are generated automatically, without manual annotation: class-relevant concepts are first proposed using an LLM-based, label-free method, and then segmented using a VLM. The finetuning objective aligns relevance with these concept regions while simultaneously suppressing focus on spurious background areas. Notably, this process requires only a minimal set of images and uses half of the dataset classes. Extensive experiments on five out-of-distribution benchmarks demonstrate that our method improves robustness across multiple ViT-based models. Furthermore, we show that the resulting relevance maps exhibit stronger alignment with semantic object parts, offering a scalable path toward more robust and interpretable vision models. Finally, we confirm that concept-guided masks provide more effective supervision for model robustness than conventional segmentation maps, supporting our central hypothesis.

