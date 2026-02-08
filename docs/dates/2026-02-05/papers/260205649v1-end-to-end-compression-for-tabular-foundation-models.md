---
layout: default
title: End-to-End Compression for Tabular Foundation Models
---

# End-to-End Compression for Tabular Foundation Models
**arXiv**：[2602.05649v1](https://arxiv.org/abs/2602.05649) · [PDF](https://arxiv.org/pdf/2602.05649.pdf)  
**作者**：Guri Zabërgja, Rafiq Kamel, Arlind Kadra, Christian M. M. Frey, Josif Grabocka  

**一句话要点**：提出TACO端到端压缩模型，以解决表格基础模型处理大规模数据时的效率瓶颈。

**关键词**：表格数据压缩, 端到端学习, Transformer效率优化, 潜在空间表示, 大规模数据集处理

## 3 点简述
- 核心问题：基于Transformer的表格基础模型因注意力机制二次复杂度，导致训练和推理开销大，难以处理大规模数据集。
- 方法要点：TACO通过将训练数据压缩到潜在空间，实现端到端压缩，减少计算和内存需求。
- 实验或效果：在TabArena基准测试中，推理速度提升高达94倍，内存消耗减少高达97%，性能无明显下降。

## 摘要（原文）

> The long-standing dominance of gradient-boosted decision trees for tabular data has recently been challenged by in-context learning tabular foundation models. In-context learning methods fit and predict in one forward pass without parameter updates by leveraging the training data as context for predicting on query test points. While recent tabular foundation models achieve state-of-the-art performance, their transformer architecture based on the attention mechanism has quadratic complexity regarding dataset size, which in turn increases the overhead on training and inference time, and limits the capacity of the models to handle large-scale datasets. In this work, we propose TACO, an end-to-end tabular compression model that compresses the training dataset in a latent space. We test our method on the TabArena benchmark, where our proposed method is up to 94x faster in inference time, while consuming up to 97\% less memory compared to the state-of-the-art tabular transformer architecture, all while retaining performance without significant degradation. Lastly, our method not only scales better with increased dataset sizes, but it also achieves better performance compared to other baselines.

