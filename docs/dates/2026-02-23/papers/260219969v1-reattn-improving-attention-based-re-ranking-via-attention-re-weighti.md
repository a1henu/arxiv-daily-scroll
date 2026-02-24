---
layout: default
title: ReAttn: Improving Attention-based Re-ranking via Attention Re-weighting
---

# ReAttn: Improving Attention-based Re-ranking via Attention Re-weighting
**arXiv**：[2602.19969v1](https://arxiv.org/abs/2602.19969) · [PDF](https://arxiv.org/pdf/2602.19969.pdf)  
**作者**：Yuxing Tian, Fengran Mo, Weixu Zhang, Yiyan Qi, Jian-Yun Nie  

**一句话要点**：提出ReAttn注意力重加权策略以改进基于注意力的重排序方法

**关键词**：注意力重排序, 零样本重排序, 大语言模型, 注意力重加权, 词汇偏差缓解, 熵正则化

## 3 点简述
- 核心问题：注意力信号集中于少数文档的少量标记，且过度强调查询的词汇相似性，导致排序偏差。
- 方法要点：通过跨文档IDF加权降低查询重叠标记的注意力，并利用熵正则化平衡注意力分布，无需额外训练。
- 实验或效果：广泛实验验证了方法的有效性，提升了重排序的准确性和可解释性。

## 摘要（原文）

> The strong capabilities of recent Large Language Models (LLMs) have made them highly effective for zero-shot re-ranking task. Attention-based re-ranking methods, which derive relevance scores directly from attention weights, offer an efficient and interpretable alternative to generation-based re-ranking methods. However, they still face two major limitations. First, attention signals are highly concentrated a small subset of tokens within a few documents, making others indistinguishable. Second, attention often overemphasizes phrases lexically similar to the query, yielding biased rankings that irrelevant documents with mere lexical resemblance are regarded as relevant. In this paper, we propose \textbf{ReAttn}, a post-hoc re-weighting strategy for attention-based re-ranking methods. It first compute the cross-document IDF weighting to down-weight attention on query-overlapping tokens that frequently appear across the candidate documents, reducing lexical bias and emphasizing distinctive terms. It then employs entropy-based regularization to mitigate over-concentrated attention, encouraging a more balanced distribution across informative tokens. Both adjustments operate directly on existing attention weights without additional training or supervision. Extensive experiments demonstrate the effectiveness of our method.

