---
layout: default
title: DSH-Bench: A Difficulty- and Scenario-Aware Benchmark with Hierarchical Subject Taxonomy for Subject-Driven Text-to-Image Generation
---

# DSH-Bench: A Difficulty- and Scenario-Aware Benchmark with Hierarchical Subject Taxonomy for Subject-Driven Text-to-Image Generation
**arXiv**：[2603.08090v1](https://arxiv.org/abs/2603.08090) · [PDF](https://arxiv.org/pdf/2603.08090.pdf)  
**作者**：Zhenyu Hu, Qing Wang, Te Cao, Luo Liao, Longfei Lu, Liqun Liu, Shuang Li, Hang Chen, Mengge Xue, Yuan Chen, Chao Deng, Peng Shu, Huan Yu, Jie Jiang  

**一句话要点**：提出DSH-Bench基准，通过分层分类和难度场景评估解决主题驱动文本到图像生成模型评估不足的问题。

**关键词**：主题驱动文本到图像生成, 基准评估, 分层分类, 难度场景分类, 主题一致性评分, 模型诊断

## 3 点简述
- 现有基准在主题多样性、评估粒度及诊断指导方面存在局限，阻碍模型优化。
- 引入分层分类、难度场景分类和新指标SICS，实现多角度系统分析。
- 评估19个模型，揭示隐藏限制，为未来研究和数据策略提供具体方向。

## 摘要（原文）

> Significant progress has been achieved in subject-driven text-to-image (T2I) generation, which aims to synthesize new images depicting target subjects according to user instructions. However, evaluating these models remains a significant challenge. Existing benchmarks exhibit critical limitations: 1) insufficient diversity and comprehensiveness in subject images, 2) inadequate granularity in assessing model performance across different subject difficulty levels and prompt scenarios, and 3) a profound lack of actionable insights and diagnostic guidance for subsequent model refinement. To address these limitations, we propose DSH-Bench, a comprehensive benchmark that enables systematic multi-perspective analysis of subject-driven T2I models through four principal innovations: 1) a hierarchical taxonomy sampling mechanism ensuring comprehensive subject representation across 58 fine-grained categories, 2) an innovative classification scheme categorizing both subject difficulty level and prompt scenario for granular capability assessment, 3) a novel Subject Identity Consistency Score (SICS) metric demonstrating a 9.4\% higher correlation with human evaluation compared to existing measures in quantifying subject preservation, and 4) a comprehensive set of diagnostic insights derived from the benchmark, offering critical guidance for optimizing future model training paradigms and data construction strategies. Through an extensive empirical evaluation of 19 leading models, DSH-Bench uncovers previously obscured limitations in current approaches, establishing concrete directions for future research and development.

