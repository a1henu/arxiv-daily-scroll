---
layout: default
title: Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models
---

# Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models
**arXiv**：[2601.08148v1](https://arxiv.org/abs/2601.08148) · [PDF](https://arxiv.org/pdf/2601.08148.pdf)  
**作者**：Seokho Ahn, Sungbok Shin, Young-Duk Seo  

**一句话要点**：提出SPiKE模型，利用大语言模型和知识图谱增强语义画像以改进推荐系统性能。

**关键词**：语义画像, 知识图谱, 大语言模型, 推荐系统, 实体画像生成, 偏好匹配

## 3 点简述
- 核心问题：用户偏好画像构建与利用方法缺乏共识，影响推荐质量。
- 方法要点：结合大语言模型提取语义画像，知识图谱传播画像，通过配对匹配优化训练。
- 实验或效果：在真实场景中，SPiKE优于现有基于知识图谱和大语言模型的推荐方法。

## 摘要（原文）

> Rich and informative profiling to capture user preferences is essential for improving recommendation quality. However, there is still no consensus on how best to construct and utilize such profiles. To address this, we revisit recent profiling-based approaches in recommender systems along four dimensions: 1) knowledge base, 2) preference indicator, 3) impact range, and 4) subject. We argue that large language models (LLMs) are effective at extracting compressed rationales from diverse knowledge sources, while knowledge graphs (KGs) are better suited for propagating these profiles to extend their reach. Building on this insight, we propose a new recommendation model, called SPiKE. SPiKE consists of three core components: i) Entity profile generation, which uses LLMs to generate semantic profiles for all KG entities; ii) Profile-aware KG aggregation, which integrates these profiles into the KG; and iii) Pairwise profile preference matching, which aligns LLM- and KG-based representations during training. In experiments, we demonstrate that SPiKE consistently outperforms state-of-the-art KG- and LLM-based recommenders in real-world settings.

