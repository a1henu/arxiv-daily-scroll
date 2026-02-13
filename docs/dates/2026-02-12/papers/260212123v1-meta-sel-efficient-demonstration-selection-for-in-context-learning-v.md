---
layout: default
title: Meta-Sel: Efficient Demonstration Selection for In-Context Learning via Supervised Meta-Learning
---

# Meta-Sel: Efficient Demonstration Selection for In-Context Learning via Supervised Meta-Learning
**arXiv**：[2602.12123v1](https://arxiv.org/abs/2602.12123) · [PDF](https://arxiv.org/pdf/2602.12123.pdf)  
**作者**：Xubin Wang, Weijia Jia  

**一句话要点**：提出Meta-Sel，通过监督元学习高效选择上下文学习中的演示示例

**关键词**：上下文学习, 演示选择, 监督元学习, 意图分类, TF-IDF相似度

## 3 点简述
- 核心问题：上下文学习中演示示例选择是实际瓶颈，需在有限提示预算下提升准确性并保持低成本
- 方法要点：基于训练数据构建元数据集，使用TF-IDF相似度和长度兼容比训练校准逻辑回归器进行快速评分
- 实验或效果：在四个意图数据集和五个开源LLM上评估，Meta-Sel性能稳定领先，尤其适用于小模型

## 摘要（原文）

> Demonstration selection is a practical bottleneck in in-context learning (ICL): under a tight prompt budget, accuracy can change substantially depending on which few-shot examples are included, yet selection must remain cheap enough to run per query over large candidate pools. We propose Meta-Sel, a lightweight supervised meta-learning approach for intent classification that learns a fast, interpretable scoring function for (candidate, query) pairs from labeled training data.
>   Meta-Sel constructs a meta-dataset by sampling pairs from the training split and using class agreement as supervision, then trains a calibrated logistic regressor on two inexpensive meta-features: TF--IDF cosine similarity and a length-compatibility ratio. At inference time, the selector performs a single vectorized scoring pass over the full candidate pool and returns the top-k demonstrations, requiring no model fine-tuning, no online exploration, and no additional LLM calls. This yields deterministic rankings and makes the selection mechanism straightforward to audit via interpretable feature weights.
>   Beyond proposing Meta-Sel, we provide a broad empirical study of demonstration selection, benchmarking 12 methods -- spanning prompt engineering baselines, heuristic selection, reinforcement learning, and influence-based approaches -- across four intent datasets and five open-source LLMs. Across this benchmark, Meta-Sel consistently ranks among the top-performing methods, is particularly effective for smaller models where selection quality can partially compensate for limited model capacity, and maintains competitive selection-time overhead.

