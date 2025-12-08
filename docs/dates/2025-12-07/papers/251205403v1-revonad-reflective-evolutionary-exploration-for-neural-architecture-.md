---
layout: default
title: RevoNAD: Reflective Evolutionary Exploration for Neural Architecture Design
---

# RevoNAD: Reflective Evolutionary Exploration for Neural Architecture Design
**arXiv**：[2512.05403v1](https://arxiv.org/abs/2512.05403) · [PDF](https://arxiv.org/pdf/2512.05403.pdf)  
**作者**：Gyusam Chang, Jeongyoon Yoon, Shin han yi, JaeHyeok Lee, Sujin Jang, Sangpil Kim  

**一句话要点**：提出RevoNAD以解决LLM驱动神经架构设计中的反馈引导和模式崩溃问题

**关键词**：神经架构设计, 大语言模型, 进化算法, 反馈对齐, 多目标优化, 计算机视觉

## 3 点简述
- 核心问题：LLM驱动的神经架构设计存在离散、不可微的生成过程，导致反馈难以平滑引导改进，易陷入冗余结构或不可行设计
- 方法要点：采用多轮多专家共识、自适应反射探索和帕累托引导进化选择，结合LLM推理与反馈对齐搜索
- 实验或效果：在CIFAR10、CIFAR100、ImageNet16-120、COCO-5K和Cityscape数据集上实现最先进性能，验证了实用可靠性和可部署性

## 摘要（原文）

> Recent progress in leveraging large language models (LLMs) has enabled Neural Architecture Design (NAD) systems to generate new architecture not limited from manually predefined search space. Nevertheless, LLM-driven generation remains challenging: the token-level design loop is discrete and non-differentiable, preventing feedback from smoothly guiding architectural improvement. These methods, in turn, commonly suffer from mode collapse into redundant structures or drift toward infeasible designs when constructive reasoning is not well grounded. We introduce RevoNAD, a reflective evolutionary orchestrator that effectively bridges LLM-based reasoning with feedback-aligned architectural search. First, RevoNAD presents a Multi-round Multi-expert Consensus to transfer isolated design rules into meaningful architectural clues. Then, Adaptive Reflective Exploration adjusts the degree of exploration leveraging reward variance; it explores when feedback is uncertain and refines when stability is reached. Finally, Pareto-guided Evolutionary Selection effectively promotes architectures that jointly optimize accuracy, efficiency, latency, confidence, and structural diversity. Across CIFAR10, CIFAR100, ImageNet16-120, COCO-5K, and Cityscape, RevoNAD achieves state-of-the-art performance. Ablation and transfer studies further validate the effectiveness of RevoNAD in allowing practically reliable, and deployable neural architecture design.

