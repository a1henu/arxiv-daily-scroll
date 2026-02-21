---
layout: default
title: ArXiv-to-Model: A Practical Study of Scientific LM Training
---

# ArXiv-to-Model: A Practical Study of Scientific LM Training
**arXiv**：[2602.17288v1](https://arxiv.org/abs/2602.17288) · [PDF](https://arxiv.org/pdf/2602.17288.pdf)  
**作者**：Anuj Gupta  

**一句话要点**：提出从arXiv LaTeX源训练科学语言模型的端到端流程，分析预处理与训练稳定性。

**关键词**：科学语言模型, LaTeX预处理, 领域专用训练, 训练稳定性分析, 计算约束优化

## 3 点简述
- 核心问题：训练领域专用科学语言模型的实践过程缺乏详细文档。
- 方法要点：构建从元数据过滤到密集Transformer训练的完整管道，使用2xA100 GPU。
- 实验或效果：通过24次实验分析数据损失、收敛动态，展示在52B令牌下的稳定训练。

## 摘要（原文）

> While frontier large language models demonstrate strong reasoning and mathematical capabilities, the practical process of training domain-specialized scientific language models from raw sources remains under-documented. In this work, we present a detailed case study of training a 1.36B-parameter scientific language model directly from raw arXiv LaTeX sources spanning mathematics, computer science, and theoretical physics. We describe an end-to-end pipeline covering metadata filtering, archive validation, LaTeX extraction, text normalization, domain-aware tokenization, and dense transformer training under constrained compute (2xA100 GPUs). Through 24 experimental runs, we analyze training stability, scaling behavior, data yield losses, and infrastructure bottlenecks. Our findings highlight how preprocessing decisions significantly affect usable token volume, how tokenization impacts symbolic stability, and how storage and I/O constraints can rival compute as limiting factors. We further analyze convergence dynamics and show stable training behavior in a data-rich regime (52B pretraining tokens). Rather than proposing a novel architecture, this work provides an engineering-grounded, transparent account of training a small scientific language model from scratch. We hope these insights support researchers operating under moderate compute budgets who seek to build domain-specialized models.

