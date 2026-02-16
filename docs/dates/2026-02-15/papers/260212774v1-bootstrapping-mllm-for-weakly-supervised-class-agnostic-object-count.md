---
layout: default
title: Bootstrapping MLLM for Weakly-Supervised Class-Agnostic Object Counting
---

# Bootstrapping MLLM for Weakly-Supervised Class-Agnostic Object Counting
**arXiv**：[2602.12774v1](https://arxiv.org/abs/2602.12774) · [PDF](https://arxiv.org/pdf/2602.12774.pdf)  
**作者**：Xiaowen Zhang, Zijie Yue, Yong Luo, Cairong Zhao, Qijun Chen, Miaojing Shi  

**一句话要点**：提出WS-COC框架，利用多模态大语言模型实现弱监督的类别无关物体计数

**关键词**：弱监督学习, 类别无关物体计数, 多模态大语言模型, 对话调优, 计数优化, 密集场景处理

## 3 点简述
- 核心问题：弱监督物体计数通常限于单类别，且标注成本高，需扩展至类别无关场景。
- 方法要点：采用分而治之对话调优、比较排序计数优化和全局局部计数增强三种策略引导MLLM。
- 实验或效果：在多个数据集上匹配或超越全监督方法，显著降低标注成本，代码已开源。

## 摘要（原文）

> Object counting is a fundamental task in computer vision, with broad applicability in many real-world scenarios. Fully-supervised counting methods require costly point-level annotations per object. Few weakly-supervised methods leverage only image-level object counts as supervision and achieve fairly promising results. They are, however, often limited to counting a single category, e.g. person. In this paper, we propose WS-COC, the first MLLM-driven weakly-supervised framework for class-agnostic object counting. Instead of directly fine-tuning MLLMs to predict object counts, which can be challenging due to the modality gap, we incorporate three simple yet effective strategies to bootstrap the counting paradigm in both training and testing: First, a divide-and-discern dialogue tuning strategy is proposed to guide the MLLM to determine whether the object count falls within a specific range and progressively break down the range through multi-round dialogue. Second, a compare-and-rank count optimization strategy is introduced to train the MLLM to optimize the relative ranking of multiple images according to their object counts. Third, a global-and-local counting enhancement strategy aggregates and fuses local and global count predictions to improve counting performance in dense scenes. Extensive experiments on FSC-147, CARPK, PUCPR+, and ShanghaiTech show that WS-COC matches or even surpasses many state-of-art fully-supervised methods while significantly reducing annotation costs. Code is available at https://github.com/viscom-tongji/WS-COC.

