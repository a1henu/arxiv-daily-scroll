---
layout: default
title: SpatiaLQA: A Benchmark for Evaluating Spatial Logical Reasoning in Vision-Language Models
---

# SpatiaLQA: A Benchmark for Evaluating Spatial Logical Reasoning in Vision-Language Models
**arXiv**：[2602.20901v1](https://arxiv.org/abs/2602.20901) · [PDF](https://arxiv.org/pdf/2602.20901.pdf)  
**作者**：Yuechen Xie, Xiaoyan Zhang, Yicheng Shan, Hao Zhu, Rui Tang, Rong Wei, Mingli Song, Yuanyu Wan, Jie Song  

**一句话要点**：提出SpatiaLQA基准以评估视觉语言模型在复杂室内场景中的空间逻辑推理能力

**关键词**：空间逻辑推理, 视觉语言模型, 基准评估, 场景图分解, 室内场景理解, 多步任务推理

## 3 点简述
- 核心问题：现有视觉语言模型在复杂真实环境中的空间逻辑推理能力不足，需理解物体空间关系和任务步骤逻辑依赖
- 方法要点：引入递归场景图辅助推理方法，利用视觉基础模型逐步分解复杂场景为任务相关场景图
- 实验或效果：在9,605个问题对上测试41个主流模型，新方法超越所有先前方法，但先进模型仍面临挑战

## 摘要（原文）

> Vision-Language Models (VLMs) have been increasingly applied in real-world scenarios due to their outstanding understanding and reasoning capabilities. Although VLMs have already demonstrated impressive capabilities in common visual question answering and logical reasoning, they still lack the ability to make reasonable decisions in complex real-world environments. We define this ability as spatial logical reasoning, which not only requires understanding the spatial relationships among objects in complex scenes, but also the logical dependencies between steps in multi-step tasks. To bridge this gap, we introduce Spatial Logical Question Answering (SpatiaLQA), a benchmark designed to evaluate the spatial logical reasoning capabilities of VLMs. SpatiaLQA consists of 9,605 question answer pairs derived from 241 real-world indoor scenes. We conduct extensive experiments on 41 mainstream VLMs, and the results show that even the most advanced models still struggle with spatial logical reasoning. To address this issue, we propose a method called recursive scene graph assisted reasoning, which leverages visual foundation models to progressively decompose complex scenes into task-relevant scene graphs, thereby enhancing the spatial logical reasoning ability of VLMs, outperforming all previous methods. Code and dataset are available at https://github.com/xieyc99/SpatiaLQA.

