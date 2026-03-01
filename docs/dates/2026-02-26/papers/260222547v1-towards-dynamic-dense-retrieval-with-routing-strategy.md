---
layout: default
title: Towards Dynamic Dense Retrieval with Routing Strategy
---

# Towards Dynamic Dense Retrieval with Routing Strategy
**arXiv**：[2602.22547v1](https://arxiv.org/abs/2602.22547) · [PDF](https://arxiv.org/pdf/2602.22547.pdf)  
**作者**：Zhan Su, Fengran Mo, Jinghan Zhang, Yuchen Hui, Jia Ao Sun, Bingbing Wen, Jian-Yun Nie  

**一句话要点**：提出动态稠密检索以解决稠密检索在领域适应和模型更新中的高成本问题

**关键词**：稠密检索, 动态路由, 前缀调谐, 领域适应, 零样本学习, 信息检索

## 3 点简述
- 核心问题：稠密检索在有限训练数据下难以适应新领域，且频繁更新模型成本高昂
- 方法要点：使用前缀调谐作为领域专用模块，结合动态路由策略实现灵活组合
- 实验或效果：在六个零样本下游任务上超越传统稠密检索，仅需2%训练参数

## 摘要（原文）

> The \textit{de facto} paradigm for applying dense retrieval (DR) to new tasks involves fine-tuning a pre-trained model for a specific task. However, this paradigm has two significant limitations: (1) It is difficult adapt the DR to a new domain if the training dataset is limited.
>   (2) Old DR models are simply replaced by newer models that are trained from scratch when the former are no longer up to date. Especially for scenarios where the model needs to be updated frequently, this paradigm is prohibitively expensive. To address these challenges, we propose a novel dense retrieval approach, termed \textit{dynamic dense retrieval} (DDR). DDR uses \textit{prefix tuning} as a \textit{module} specialized for a specific domain. These modules can then be compositional combined with a dynamic routing strategy, enabling highly flexible domain adaptation in the retrieval part. Extensive evaluation on six zero-shot downstream tasks demonstrates that this approach can surpass DR while utilizing only 2\% of the training parameters, paving the way to achieve more flexible dense retrieval in IR. We see it as a promising future direction for applying dense retrieval to various tasks.

