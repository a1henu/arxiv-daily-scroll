---
layout: default
title: Validating Political Position Predictions of Arguments
---

# Validating Political Position Predictions of Arguments
**arXiv**：[2602.18351v1](https://arxiv.org/abs/2602.18351) · [PDF](https://arxiv.org/pdf/2602.18351.pdf)  
**作者**：Jordan Robinson, Angus R. Williams, Katie Atkinson, Anthony G. Cohn  

**一句话要点**：提出双尺度验证框架以解决政治立场预测中主观连续属性的评估挑战

**关键词**：政治立场预测, 双尺度验证, 知识表示, 语言模型, 主观连续属性, 结构化论证

## 3 点简述
- 核心问题：现实世界知识表示需捕获主观连续属性（如政治立场），但传统成对验证方法不适用。
- 方法要点：结合点式和成对人类标注，构建大规模政治立场预测知识库，使用22个语言模型分析23,228个论点。
- 实验或效果：点式评估显示中等人机一致性（α=0.578），成对验证揭示更强排名对齐（最佳模型α=0.86）。

## 摘要（原文）

> Real-world knowledge representation often requires capturing subjective, continuous attributes -- such as political positions -- that conflict with pairwise validation, the widely accepted gold standard for human evaluation. We address this challenge through a dual-scale validation framework applied to political stance prediction in argumentative discourse, combining pointwise and pairwise human annotation. Using 22 language models, we construct a large-scale knowledge base of political position predictions for 23,228 arguments drawn from 30 debates that appeared on the UK politicial television programme \textit{Question Time}. Pointwise evaluation shows moderate human-model agreement (Krippendorff's $α=0.578$), reflecting intrinsic subjectivity, while pairwise validation reveals substantially stronger alignment between human- and model-derived rankings ($α=0.86$ for the best model). This work contributes: (i) a practical validation methodology for subjective continuous knowledge that balances scalability with reliability; (ii) a validated structured argumentation knowledge base enabling graph-based reasoning and retrieval-augmented generation in political domains; and (iii) evidence that ordinal structure can be extracted from pointwise language models predictions from inherently subjective real-world discourse, advancing knowledge representation capabilities for domains where traditional symbolic or categorical approaches are insufficient.

