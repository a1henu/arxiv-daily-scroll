---
layout: default
title: LoRA-MME: Multi-Model Ensemble of LoRA-Tuned Encoders for Code Comment Classification
---

# LoRA-MME: Multi-Model Ensemble of LoRA-Tuned Encoders for Code Comment Classification
**arXiv**：[2603.03959v1](https://arxiv.org/abs/2603.03959) · [PDF](https://arxiv.org/pdf/2603.03959.pdf)  
**作者**：Md Akib Haider, Ahsan Bulbul, Nafis Fuad Shahid, Aimaan Ahmed, Mohammad Ishrak Abedin  

**一句话要点**：提出LoRA-MME多模型集成架构，利用参数高效微调解决代码注释多标签分类问题。

**关键词**：代码注释分类, 多模型集成, 参数高效微调, LoRA微调, 多标签分类, 软件文档自动化

## 3 点简述
- 核心问题：代码注释多标签分类，用于自动化软件文档和分析，支持Java、Python和Pharo语言。
- 方法要点：独立微调UniXcoder、CodeBERT、GraphCodeBERT和CodeBERTa四个编码器，采用LoRA参数高效微调和加权集成策略。
- 实验或效果：在测试集上F1加权得分0.7906，宏F1得分0.6867，但计算成本导致最终提交分数41.20%。

## 摘要（原文）

> Code comment classification is a critical task for automated software documentation and analysis. In the context of the NLBSE'26 Tool Competition, we present \textbf{LoRA-MME}, a Multi-Model Ensemble architecture utilizing Parameter-Efficient Fine-Tuning (PEFT). Our approach addresses the multi-label classification challenge across Java, Python, and Pharo by combining the strengths of four distinct transformer encoders: UniXcoder, CodeBERT, GraphCodeBERT, and CodeBERTa. By independently fine-tuning these models using Low-Rank Adaptation(LoRA) and aggregating their predictions via a learned weighted ensemble strategy, we maximize classification performance without the memory overhead of full model fine-tuning. Our tool achieved an \textbf{F1 Weighted score of 0.7906} and a \textbf{Macro F1 of 0.6867} on the test set. However, the computational cost of the ensemble resulted in a final submission score of 41.20\%, highlighting the trade-off between semantic accuracy and inference efficiency.

