---
layout: default
title: MacVQA: Adaptive Memory Allocation and Global Noise Filtering for Continual Visual Question Answering
---

# MacVQA: Adaptive Memory Allocation and Global Noise Filtering for Continual Visual Question Answering
**arXiv**：[2601.01926v1](https://arxiv.org/abs/2601.01926) · [PDF](https://arxiv.org/pdf/2601.01926.pdf)  
**作者**：Zhifei Li, Yiran Wang, Chenyi Xiong, Yujing Xia, Xiaoju Hou, Yue Zhao, Miao Zhang, Kui Xiao, Bing Yang  

**一句话要点**：提出MacVQA框架，通过自适应内存分配和全局噪声过滤解决持续视觉问答中的知识保留与适应平衡问题。

**关键词**：持续学习, 视觉问答, 自适应内存分配, 噪声过滤, 原型学习, 多模态融合

## 3 点简述
- 核心问题：持续视觉问答中知识保留、适应和鲁棒特征表示的平衡挑战。
- 方法要点：融合视觉与问题信息，过滤噪声，采用原型内存分配优化特征质量和内存使用。
- 实验或效果：在十个持续VQA任务上超越基线，标准任务平均准确率43.38%，遗忘率2.32%。

## 摘要（原文）

> Visual Question Answering (VQA) requires models to reason over multimodal information, combining visual and textual data. With the development of continual learning, significant progress has been made in retaining knowledge and adapting to new information in the VQA domain. However, current methods often struggle with balancing knowledge retention, adaptation, and robust feature representation. To address these challenges, we propose a novel framework with adaptive memory allocation and global noise filtering called MacVQA for visual question answering. MacVQA fuses visual and question information while filtering noise to ensure robust representations, and employs prototype-based memory allocation to optimize feature quality and memory usage. These designs enable MacVQA to balance knowledge acquisition, retention, and compositional generalization in continual VQA learning. Experiments on ten continual VQA tasks show that MacVQA outperforms existing baselines, achieving 43.38% average accuracy and 2.32% average forgetting on standard tasks, and 42.53% average accuracy and 3.60% average forgetting on novel composition tasks.

