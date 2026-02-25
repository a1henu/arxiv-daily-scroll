---
layout: default
title: PRECTR-V2:Unified Relevance-CTR Framework with Cross-User Preference Mining, Exposure Bias Correction, and LLM-Distilled Encoder Optimization
---

# PRECTR-V2:Unified Relevance-CTR Framework with Cross-User Preference Mining, Exposure Bias Correction, and LLM-Distilled Encoder Optimization
**arXiv**：[2602.20676v1](https://arxiv.org/abs/2602.20676) · [PDF](https://arxiv.org/pdf/2602.20676.pdf)  
**作者**：Shuzhi Cao, Rong Chen, Ailong He, Shuguang Han, Jufeng Chen  

**一句话要点**：提出PRECTR-V2统一框架，通过跨用户偏好挖掘、曝光偏差校正和LLM蒸馏编码器优化，解决搜索系统中冷启动、泛化偏差和模型对齐问题。

**关键词**：搜索系统, 统一框架, 冷启动建模, 曝光偏差校正, 知识蒸馏, 编码器优化

## 3 点简述
- 核心问题：低活跃用户行为稀疏、训练数据分布不匹配、编码器与CTR微调不对齐，影响搜索相关性和点击率预测效果。
- 方法要点：挖掘全局查询相关偏好以建模冷启动用户，通过噪声注入和标签重构构建硬负样本校正曝光偏差，蒸馏LLM预训练轻量编码器优化对齐。
- 实验或效果：未知，但方法旨在提升个性化建模、泛化能力和模型效率，可能通过基准测试验证改进。

## 摘要（原文）

> In search systems, effectively coordinating the two core objectives of search relevance matching and click-through rate (CTR) prediction is crucial for discovering users' interests and enhancing platform revenue. In our prior work PRECTR, we proposed a unified framework to integrate these two subtasks,thereby eliminating their inconsistency and leading to mutual benefit.However, our previous work still faces three main challenges. First, low-active users and new users have limited search behavioral data, making it difficult to achieve effective personalized relevance preference modeling. Second, training data for ranking models predominantly come from high-relevance exposures, creating a distribution mismatch with the broader candidate space in coarse-ranking, leading to generalization bias. Third, due to the latency constraint, the original model employs an Emb+MLP architecture with a frozen BERT encoder, which prevents joint optimization and creates misalignment between representation learning and CTR fine-tuning. To solve these issues, we further reinforce our method and propose PRECTR-V2. Specifically, we mitigate the low-activity users' sparse behavior problem by mining global relevance preferences under the specific query, which facilitates effective personalized relevance modeling for cold-start scenarios. Subsequently, we construct hard negative samples through embedding noise injection and relevance label reconstruction, and optimize their relative ranking against positive samples via pairwise loss, thereby correcting exposure bias. Finally, we pretrain a lightweight transformer-based encoder via knowledge distillation from LLM and SFT on the text relevance classification task. This encoder replaces the frozen BERT module, enabling better adaptation to CTR fine-tuning and advancing beyond the traditional Emb+MLP paradigm.

