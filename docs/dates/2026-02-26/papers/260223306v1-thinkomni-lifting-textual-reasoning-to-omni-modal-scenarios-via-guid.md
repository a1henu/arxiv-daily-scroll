---
layout: default
title: ThinkOmni: Lifting Textual Reasoning to Omni-modal Scenarios via Guidance Decoding
---

# ThinkOmni: Lifting Textual Reasoning to Omni-modal Scenarios via Guidance Decoding
**arXiv**：[2602.23306v1](https://arxiv.org/abs/2602.23306) · [PDF](https://arxiv.org/pdf/2602.23306.pdf)  
**作者**：Yiran Guan, Sifan Tu, Dingkang Liang, Linghao Zhu, Jianzhong Ju, Zhenbo Luo, Jian Luan, Yuliang Liu, Xiang Bai  

**一句话要点**：提出ThinkOmni框架，通过引导解码将文本推理能力提升至全模态场景

**关键词**：全模态推理, 引导解码, 步进对比缩放, 训练免费框架, 多模态基准测试

## 3 点简述
- 核心问题：现有全模态大语言模型感知能力强但推理能力不足，增强训练面临数据、计算等挑战
- 方法要点：利用现成大推理模型引导解码，结合步进对比缩放自适应平衡感知与推理信号
- 实验或效果：在六个多模态推理基准上性能提升，如MathVista达70.2，MMAU达75.5

## 摘要（原文）

> Omni-modal reasoning is essential for intelligent systems to understand and draw inferences from diverse data sources. While existing omni-modal large language models (OLLM) excel at perceiving diverse modalities, they lack the complex reasoning abilities of recent large reasoning models (LRM). However, enhancing the reasoning ability of OLLMs through additional training presents significant challenges, including the need for high-quality data, task-specific adaptation, and substantial computational costs. To address these limitations, we propose ThinkOmni, a training-free and data-free framework that lifts textual reasoning to omni-modal scenarios. ThinkOmni introduces two key components: 1) LRM-as-a-Guide, which leverages off-the-shelf LRMs to guide the OLLM decoding process; 2) Stepwise Contrastive Scaling, which adaptively balances perception and reasoning signals without manual hyperparameter tuning. Experiments on six multi-modal reasoning benchmarks demonstrate that ThinkOmni consistently delivers performance improvements, with main results achieving 70.2 on MathVista and 75.5 on MMAU. Overall, ThinkOmni offers a flexible and generalizable solution for omni-modal reasoning and provides new insights into the generalization and application of reasoning capabilities.

