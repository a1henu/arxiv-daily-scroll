---
layout: default
title: Diffusion-Based Data Augmentation for Image Recognition: A Systematic Analysis and Evaluation
---

# Diffusion-Based Data Augmentation for Image Recognition: A Systematic Analysis and Evaluation
**arXiv**：[2603.08364v1](https://arxiv.org/abs/2603.08364) · [PDF](https://arxiv.org/pdf/2603.08364.pdf)  
**作者**：Zekun Li, Yinghuan Shi, Yang Gao, Dong Xu  

**一句话要点**：提出统一分析框架UniDiffDA以系统评估扩散数据增强在低数据分类中的有效性

**关键词**：扩散数据增强, 低数据分类, 统一分析框架, 系统评估, 图像识别

## 3 点简述
- 核心问题：现有扩散数据增强方法在任务配置、模型选择和实验流程上差异大，缺乏公平比较和系统理解
- 方法要点：将扩散数据增强分解为模型微调、样本生成和样本利用三个核心组件，构建统一分析框架
- 实验或效果：通过全面评估协议，在多样低数据分类任务中基准测试代表性方法，揭示不同策略的相对优势和局限性

## 摘要（原文）

> Diffusion-based data augmentation (DiffDA) has emerged as a promising approach to improving classification performance under data scarcity. However, existing works vary significantly in task configurations, model choices, and experimental pipelines, making it difficult to fairly compare methods or assess their effectiveness across different scenarios. Moreover, there remains a lack of systematic understanding of the full DiffDA workflow. In this work, we introduce UniDiffDA, a unified analytical framework that decomposes DiffDA methods into three core components: model fine-tuning, sample generation, and sample utilization. This perspective enables us to identify key differences among existing methods and clarify the overall design space. Building on this framework, we develop a comprehensive and fair evaluation protocol, benchmarking representative DiffDA methods across diverse low-data classification tasks. Extensive experiments reveal the relative strengths and limitations of different DiffDA strategies and offer practical insights into method design and deployment. All methods are re-implemented within a unified codebase, with full release of code and configurations to ensure reproducibility and to facilitate future research.

