---
layout: default
title: See, Rank, and Filter: Important Word-Aware Clip Filtering via Scene Understanding for Moment Retrieval and Highlight Detection
---

# See, Rank, and Filter: Important Word-Aware Clip Filtering via Scene Understanding for Moment Retrieval and Highlight Detection
**arXiv**：[2511.22906v1](https://arxiv.org/abs/2511.22906) · [PDF](https://arxiv.org/pdf/2511.22906.pdf)  
**作者**：YuEun Lee, Jung Uk Kim  

**一句话要点**：提出重要词感知的剪辑过滤方法，通过场景理解提升视频时刻检索和高光检测性能

**关键词**：视频时刻检索, 高光检测, 多模态大语言模型, 重要词识别, 剪辑过滤, 场景理解

## 3 点简述
- 现有方法忽视查询中单词重要性，阻碍上下文理解
- 集成多模态大语言模型，增强视频语义理解，引入特征增强和排序过滤模块
- 实验显示在时刻检索和高光检测任务上显著优于现有方法

## 摘要（原文）

> Video moment retrieval (MR) and highlight detection (HD) with natural language queries aim to localize relevant moments and key highlights in a video clips. However, existing methods overlook the importance of individual words, treating the entire text query and video clips as a black-box, which hinders contextual understanding. In this paper, we propose a novel approach that enables fine-grained clip filtering by identifying and prioritizing important words in the query. Our method integrates image-text scene understanding through Multimodal Large Language Models (MLLMs) and enhances the semantic understanding of video clips. We introduce a feature enhancement module (FEM) to capture important words from the query and a ranking-based filtering module (RFM) to iteratively refine video clips based on their relevance to these important words. Extensive experiments demonstrate that our approach significantly outperforms existing state-of-the-art methods, achieving superior performance in both MR and HD tasks. Our code is available at: https://github.com/VisualAIKHU/SRF.

