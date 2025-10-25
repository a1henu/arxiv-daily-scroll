---
layout: default
title: Mitigating Cross-modal Representation Bias for Multicultural Image-to-Recipe Retrieval
---

# Mitigating Cross-modal Representation Bias for Multicultural Image-to-Recipe Retrieval
**arXiv**：[2510.20393v1](https://arxiv.org/abs/2510.20393) · [PDF](https://arxiv.org/pdf/2510.20393.pdf)  
**作者**：Qing Wang, Chong-Wah Ngo, Yu Cao, Ee-Peng Lim  

**一句话要点**：提出因果表示学习方法以缓解多文化图像-食谱检索中的跨模态表示偏差

**关键词**：图像-食谱检索, 跨模态表示学习, 因果推理, 多文化数据集, 表示偏差缓解

## 3 点简述
- 核心问题：图像仅反映菜肴视觉结果，忽略食谱中不可见的细节，导致表示学习偏向主导视觉元素。
- 方法要点：预测图像中可能被忽略的烹饪元素，并将其注入跨模态表示学习以减轻偏差。
- 实验或效果：在单语和多语言多文化数据集上验证，能发现细微成分和烹饪动作，提升检索性能。

## 摘要（原文）

> Existing approaches for image-to-recipe retrieval have the implicit
> assumption that a food image can fully capture the details textually documented
> in its recipe. However, a food image only reflects the visual outcome of a
> cooked dish and not the underlying cooking process. Consequently, learning
> cross-modal representations to bridge the modality gap between images and
> recipes tends to ignore subtle, recipe-specific details that are not visually
> apparent but are crucial for recipe retrieval. Specifically, the
> representations are biased to capture the dominant visual elements, resulting
> in difficulty in ranking similar recipes with subtle differences in use of
> ingredients and cooking methods. The bias in representation learning is
> expected to be more severe when the training data is mixed of images and
> recipes sourced from different cuisines. This paper proposes a novel causal
> approach that predicts the culinary elements potentially overlooked in images,
> while explicitly injecting these elements into cross-modal representation
> learning to mitigate biases. Experiments are conducted on the standard
> monolingual Recipe1M dataset and a newly curated multilingual multicultural
> cuisine dataset. The results indicate that the proposed causal representation
> learning is capable of uncovering subtle ingredients and cooking actions and
> achieves impressive retrieval performance on both monolingual and multilingual
> multicultural datasets.

