---
layout: default
title: Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution
---

# Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution
**arXiv**：[2602.14869v1](https://arxiv.org/abs/2602.14869) · [PDF](https://arxiv.org/pdf/2602.14869.pdf)  
**作者**：Matthew Kowal, Goncalo Paulo, Louis Jaburi, Tom Tseng, Lev E McKinney, Stefan Heimersheim, Aaron David Tucker, Adam Gleave, Kellin Pelrine  

**一句话要点**：提出概念影响力方法，利用可解释结构提升训练数据归因的性能与效率

**关键词**：训练数据归因, 可解释性, 语义方向, 概念影响力, 探针近似, 模型行为控制

## 3 点简述
- 核心问题：现有训练数据归因方法计算成本高且易偏向句法相似，难以处理抽象行为。
- 方法要点：引入概念影响力，将模型行为归因于语义方向而非单个测试示例，并基于探针近似实现快速计算。
- 实验或效果：在基准和真实数据集上验证，性能媲美传统方法，计算效率大幅提升。

## 摘要（原文）

> As large language models are increasingly trained and fine-tuned, practitioners need methods to identify which training data drive specific behaviors, particularly unintended ones. Training Data Attribution (TDA) methods address this by estimating datapoint influence. Existing approaches like influence functions are both computationally expensive and attribute based on single test examples, which can bias results toward syntactic rather than semantic similarity. To address these issues of scalability and influence to abstract behavior, we leverage interpretable structures within the model during the attribution. First, we introduce Concept Influence which attribute model behavior to semantic directions (such as linear probes or sparse autoencoder features) rather than individual test examples. Second, we show that simple probe-based attribution methods are first-order approximations of Concept Influence that achieve comparable performance while being over an order-of-magnitude faster. We empirically validate Concept Influence and approximations across emergent misalignment benchmarks and real post-training datasets, and demonstrate they achieve comparable performance to classical influence functions while being substantially more scalable. More broadly, we show that incorporating interpretable structure within traditional TDA pipelines can enable more scalable, explainable, and better control of model behavior through data.

