---
layout: default
title: Epistemic diversity across language models mitigates knowledge collapse
---

# Epistemic diversity across language models mitigates knowledge collapse
**arXiv**：[2512.15011v1](https://arxiv.org/abs/2512.15011) · [PDF](https://arxiv.org/pdf/2512.15011.pdf)  
**作者**：Damian Hodel, Jevin D. West  

**一句话要点**：提出语言模型生态系统多样性以缓解知识崩溃问题

**关键词**：知识崩溃, 语言模型生态系统, 自训练, 多样性优化, AI monoculture

## 3 点简述
- 核心问题：AI模型自训练导致知识崩溃，即知识向主导思想集中。
- 方法要点：通过分割训练数据构建多样化模型生态系统，研究多样性对性能的影响。
- 实验或效果：发现适度多样性可缓解崩溃，但过多或过少模型均导致性能下降。

## 摘要（原文）

> The growing use of artificial intelligence (AI) raises concerns of knowledge collapse, i.e., a reduction to the most dominant and central set of ideas. Prior work has demonstrated single-model collapse, defined as performance decay in an AI model trained on its own output. Inspired by ecology, we ask whether AI ecosystem diversity, that is, diversity among models, can mitigate such a collapse. We build on the single-model approach but focus on ecosystems of models trained on their collective output. To study the effect of diversity on model performance, we segment the training data across language models and evaluate the resulting ecosystems over ten, self-training iterations. We find that increased epistemic diversity mitigates collapse, but, interestingly, only up to an optimal level. Our results suggest that an ecosystem containing only a few diverse models fails to express the rich mixture of the full, true distribution, resulting in rapid performance decay. Yet distributing the data across too many models reduces each model's approximation capacity on the true distribution, leading to poor performance already in the first iteration step. In the context of AI monoculture, our results suggest the need to monitor diversity across AI systems and to develop policies that incentivize more domain- and community-specific models.

