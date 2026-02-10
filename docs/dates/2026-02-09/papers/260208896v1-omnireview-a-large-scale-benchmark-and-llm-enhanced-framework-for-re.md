---
layout: default
title: OmniReview: A Large-scale Benchmark and LLM-enhanced Framework for Realistic Reviewer Recommendation
---

# OmniReview: A Large-scale Benchmark and LLM-enhanced Framework for Realistic Reviewer Recommendation
**arXiv**：[2602.08896v1](https://arxiv.org/abs/2602.08896) · [PDF](https://arxiv.org/pdf/2602.08896.pdf)  
**作者**：Yehua Huang, Penglei Sun, Zebin Chen, Zhenheng Tang, Xiaowen Chu  

**一句话要点**：提出OmniReview数据集与Pro-MMoE框架以解决学术审稿人推荐中的数据和方法挑战

**关键词**：审稿人推荐, 大规模数据集, LLM增强, 多任务学习, 评估框架

## 3 点简述
- 核心问题：现有研究缺乏大规模验证数据集和反映真实编辑流程的评估指标
- 方法要点：利用LLM生成语义档案保留细粒度专业知识，结合多门混合专家动态平衡评估目标
- 实验或效果：Pro-MMoE在七项指标中六项达到最优，为现实审稿人推荐设立新基准

## 摘要（原文）

> Academic peer review remains the cornerstone of scholarly validation, yet the field faces some challenges in data and methods. From the data perspective, existing research is hindered by the scarcity of large-scale, verified benchmarks and oversimplified evaluation metrics that fail to reflect real-world editorial workflows. To bridge this gap, we present OmniReview, a comprehensive dataset constructed by integrating multi-source academic platforms encompassing comprehensive scholarly profiles through the disambiguation pipeline, yielding 202, 756 verified review records. Based on this data, we introduce a three-tier hierarchical evaluaion framework to assess recommendations from recall to precise expert identification. From the method perspective, existing embedding-based approaches suffer from the information bottleneck of semantic compression and limited interpretability. To resolve these method limitations, we propose Profiling Scholars with Multi-gate Mixture-of-Experts (Pro-MMoE), a novel framework that synergizes Large Language Models (LLMs) with Multi-task Learning. Specifically, it utilizes LLM-generated semantic profiles to preserve fine-grained expertise nuances and interpretability, while employing a Task-Adaptive MMoE architecture to dynamically balance conflicting evaluation goals. Comprehensive experiments demonstrate that Pro-MMoE achieves state-of-the-art performance across six of seven metrics, establishing a new benchmark for realistic reviewer recommendation.

