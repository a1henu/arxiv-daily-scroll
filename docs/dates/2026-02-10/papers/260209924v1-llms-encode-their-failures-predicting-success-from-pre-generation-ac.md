---
layout: default
title: LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations
---

# LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations
**arXiv**：[2602.09924v1](https://arxiv.org/abs/2602.09924) · [PDF](https://arxiv.org/pdf/2602.09924.pdf)  
**作者**：William Lugoloobi, Thomas Foster, William Bankes, Chris Russell  

**一句话要点**：提出基于预生成激活预测LLM成功概率的方法，以优化推理效率

**关键词**：预生成激活分析, 线性探针, 推理效率优化, 模型路由, 数学任务, 编程任务

## 3 点简述
- 核心问题：LLM推理成本高，难以预判哪些输入需要额外计算资源
- 方法要点：在预生成激活上训练线性探针，预测模型在数学和编程任务上的成功概率
- 实验或效果：在MATH数据集上，通过模型路由减少推理成本达70%，超越最佳单模型性能

## 摘要（原文）

> Running LLMs with extended reasoning on every problem is expensive, but determining which inputs actually require additional compute remains challenging. We investigate whether their own likelihood of success is recoverable from their internal representations before generation, and if this signal can guide more efficient inference. We train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks, substantially outperforming surface features such as question length and TF-IDF. Using E2H-AMC, which provides both human and model performance on identical problems, we show that models encode a model-specific notion of difficulty that is distinct from human difficulty, and that this distinction increases with extended reasoning. Leveraging these probes, we demonstrate that routing queries across a pool of models can exceed the best-performing model whilst reducing inference cost by up to 70\% on MATH, showing that internal representations enable practical efficiency gains even when they diverge from human intuitions about difficulty. Our code is available at: https://github.com/KabakaWilliam/llms_know_difficulty

