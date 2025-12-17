---
layout: default
title: Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed
---

# Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed
**arXiv**：[2512.14067v1](https://arxiv.org/abs/2512.14067) · [PDF](https://arxiv.org/pdf/2512.14067.pdf)  
**作者**：Yonggan Fu, Lexington Whalen, Zhifan Ye, Xin Dong, Shizhe Diao, Jingyu Liu, Chengyue Wu, Hao Zhang, Enze Xie, Song Han, Maksim Khadkevich, Jan Kautz, Yingyan Celine Lin, Pavlo Molchanov  

**一句话要点**：提出Efficient-DLM方法，通过改进AR-to-dLM转换实现高效扩散语言模型，提升生成速度与任务精度。

**关键词**：扩散语言模型, 自回归模型转换, 注意力模式, 掩码策略, 高效生成

## 3 点简述
- 核心问题：扩散语言模型训练效率低，难以从零开始超越自回归模型。
- 方法要点：采用块级注意力模式和位置依赖掩码策略，优化AR-to-dLM转换。
- 实验或效果：Efficient-DLM 8B在准确率和吞吐量上优于现有AR和dLM模型。

## 摘要（原文）

> Diffusion language models (dLMs) have emerged as a promising paradigm that enables parallel, non-autoregressive generation, but their learning efficiency lags behind that of autoregressive (AR) language models when trained from scratch. To this end, we study AR-to-dLM conversion to transform pretrained AR models into efficient dLMs that excel in speed while preserving AR models' task accuracy. We achieve this by identifying limitations in the attention patterns and objectives of existing AR-to-dLM methods and then proposing principles and methodologies for more effective AR-to-dLM conversion. Specifically, we first systematically compare different attention patterns and find that maintaining pretrained AR weight distributions is critical for effective AR-to-dLM conversion. As such, we introduce a continuous pretraining scheme with a block-wise attention pattern, which remains causal across blocks while enabling bidirectional modeling within each block. We find that this approach can better preserve pretrained AR models' weight distributions than fully bidirectional modeling, in addition to its known benefit of enabling KV caching, and leads to a win-win in accuracy and efficiency. Second, to mitigate the training-test gap in mask token distributions (uniform vs. highly left-to-right), we propose a position-dependent token masking strategy that assigns higher masking probabilities to later tokens during training to better mimic test-time behavior. Leveraging this framework, we conduct extensive studies of dLMs' attention patterns, training dynamics, and other design choices, providing actionable insights into scalable AR-to-dLM conversion. These studies lead to the Efficient-DLM family, which outperforms state-of-the-art AR models and dLMs, e.g., our Efficient-DLM 8B achieves +5.4%/+2.7% higher accuracy with 4.5x/2.7x higher throughput compared to Dream 7B and Qwen3 4B, respectively.

