---
layout: default
title: PMCE: Probabilistic Multi-Granularity Semantics with Caption-Guided Enhancement for Few-Shot Learning
---

# PMCE: Probabilistic Multi-Granularity Semantics with Caption-Guided Enhancement for Few-Shot Learning
**arXiv**：[2601.14111v1](https://arxiv.org/abs/2601.14111) · [PDF](https://arxiv.org/pdf/2601.14111.pdf)  
**作者**：Jiaying Wu, Can Gao, Jinglu Hu, Hui Li, Xiaofeng Cao, Jingcai Guo  

**一句话要点**：提出PMCE框架，利用多粒度语义与描述引导增强解决小样本学习中原型偏差问题

**关键词**：小样本学习, 多粒度语义, 描述引导增强, 原型优化, 非参数知识库, 一致性正则化

## 3 点简述
- 小样本学习中，基于稀缺数据估计的原型存在偏差且泛化能力差，语义方法多仅用于支持集
- PMCE构建非参数知识库，检索相关基类统计作为先验，融合支持集原型，并利用BLIP生成描述优化特征
- 在四个基准测试中，PMCE优于强基线，在MiniImageNet 1-shot设置上相对最强语义方法提升7.71%

## 摘要（原文）

> Few-shot learning aims to identify novel categories from only a handful of labeled samples, where prototypes estimated from scarce data are often biased and generalize poorly. Semantic-based methods alleviate this by introducing coarse class-level information, but they are mostly applied on the support side, leaving query representations unchanged. In this paper, we present PMCE, a Probabilistic few-shot framework that leverages Multi-granularity semantics with Caption-guided Enhancement. PMCE constructs a nonparametric knowledge bank that stores visual statistics for each category as well as CLIP-encoded class name embeddings of the base classes. At meta-test time, the most relevant base classes are retrieved based on the similarities of class name embeddings for each novel category. These statistics are then aggregated into category-specific prior information and fused with the support set prototypes via a simple MAP update. Simultaneously, a frozen BLIP captioner provides label-free instance-level image descriptions, and a lightweight enhancer trained on base classes optimizes both support prototypes and query features under an inductive protocol with a consistency regularization to stabilize noisy captions. Experiments on four benchmarks show that PMCE consistently improves over strong baselines, achieving up to 7.71% absolute gain over the strongest semantic competitor on MiniImageNet in the 1-shot setting. Our code is available at https://anonymous.4open.science/r/PMCE-275D

