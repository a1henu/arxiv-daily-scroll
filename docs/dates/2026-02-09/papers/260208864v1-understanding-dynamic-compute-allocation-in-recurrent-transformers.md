---
layout: default
title: Understanding Dynamic Compute Allocation in Recurrent Transformers
---

# Understanding Dynamic Compute Allocation in Recurrent Transformers
**arXiv**：[2602.08864v1](https://arxiv.org/abs/2602.08864) · [PDF](https://arxiv.org/pdf/2602.08864.pdf)  
**作者**：Ibraheem Muhammad Moosa, Suhas Lohit, Ye Wang, Moitreya Chatterjee, Wenpeng Yin  

**一句话要点**：提出ANIRA框架以评估循环Transformer中动态计算分配与任务复杂度的对齐

**关键词**：自适应计算, 循环Transformer, 令牌级复杂度, 算法任务评估, 计算分配对齐, 泛化分析

## 3 点简述
- 核心问题：先前研究在自然语言基准上评估自适应计算，但令牌级难度不可观测，难以验证计算分配是否真正对齐复杂度。
- 方法要点：引入复杂度可控的评估范式，使用算法和合成语言任务，并设计ANIRA框架支持每令牌可变深度计算。
- 实验或效果：结果显示计算分配能无监督对齐复杂度，但模型无法泛化到未见输入大小，且早期决策依赖静态结构线索。

## 摘要（原文）

> Token-level adaptive computation seeks to reduce inference cost by allocating more computation to harder tokens and less to easier ones. However, prior work is primarily evaluated on natural-language benchmarks using task-level metrics, where token-level difficulty is unobservable and confounded with architectural factors, making it unclear whether compute allocation truly aligns with underlying complexity. We address this gap through three contributions. First, we introduce a complexity-controlled evaluation paradigm using algorithmic and synthetic language tasks with parameterized difficulty, enabling direct testing of token-level compute allocation. Second, we propose ANIRA, a unified recurrent Transformer framework that supports per-token variable-depth computation while isolating compute allocation decisions from other model factors. Third, we use this framework to conduct a systematic analysis of token-level adaptive computation across alignment with complexity, generalization, and decision timing. Our results show that compute allocation aligned with task complexity can emerge without explicit difficulty supervision, but such alignment does not imply algorithmic generalization: models fail to extrapolate to unseen input sizes despite allocating additional computation. We further find that early compute decisions rely on static structural cues, whereas online halting more closely tracks algorithmic execution state.

