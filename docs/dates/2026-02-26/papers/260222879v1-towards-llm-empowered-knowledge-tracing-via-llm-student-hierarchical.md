---
layout: default
title: Towards LLM-Empowered Knowledge Tracing via LLM-Student Hierarchical Behavior Alignment in Hyperbolic Space
---

# Towards LLM-Empowered Knowledge Tracing via LLM-Student Hierarchical Behavior Alignment in Hyperbolic Space
**arXiv**：[2602.22879v1](https://arxiv.org/abs/2602.22879) · [PDF](https://arxiv.org/pdf/2602.22879.pdf)  
**作者**：Xingcheng Fu, Shengpeng Wang, Yisen Gao, Xianxian Li, Chunpei Li, Qingyun Sun, Dongran Yu  

**一句话要点**：提出L-HAKT框架，通过LLM-学生分层行为对齐在双曲空间解决知识追踪中认知状态演化与个性化难度感知问题。

**关键词**：知识追踪, 大语言模型, 双曲空间, 分层行为对齐, 对比学习, 教育数据

## 3 点简述
- 核心问题：现有知识追踪方法难以捕捉认知状态的分层演化和个性化问题难度感知。
- 方法要点：利用LLM解析问题语义构建知识分层，通过学生代理生成合成数据，在双曲空间进行对比学习对齐特征。
- 实验或效果：在四个真实教育数据集上验证了L-HAKT框架的有效性，未知具体性能指标。

## 摘要（原文）

> Knowledge Tracing (KT) diagnoses students' concept mastery through continuous learning state monitoring in education.Existing methods primarily focus on studying behavioral sequences based on ID or textual information.While existing methods rely on ID-based sequences or shallow textual features, they often fail to capture (1) the hierarchical evolution of cognitive states and (2) individualized problem difficulty perception due to limited semantic modeling. Therefore, this paper proposes a Large Language Model Hyperbolic Aligned Knowledge Tracing(L-HAKT). First, the teacher agent deeply parses question semantics and explicitly constructs hierarchical dependencies of knowledge points; the student agent simulates learning behaviors to generate synthetic data. Then, contrastive learning is performed between synthetic and real data in hyperbolic space to reduce distribution differences in key features such as question difficulty and forgetting patterns. Finally, by optimizing hyperbolic curvature, we explicitly model the tree-like hierarchical structure of knowledge points, precisely characterizing differences in learning curve morphology for knowledge points at different levels. Extensive experiments on four real-world educational datasets validate the effectiveness of our Large Language Model Hyperbolic Aligned Knowledge Tracing (L-HAKT) framework.

