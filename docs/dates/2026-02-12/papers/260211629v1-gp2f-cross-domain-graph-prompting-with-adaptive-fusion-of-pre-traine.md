---
layout: default
title: GP2F: Cross-Domain Graph Prompting with Adaptive Fusion of Pre-trained Graph Neural Networks
---

# GP2F: Cross-Domain Graph Prompting with Adaptive Fusion of Pre-trained Graph Neural Networks
**arXiv**：[2602.11629v1](https://arxiv.org/abs/2602.11629) · [PDF](https://arxiv.org/pdf/2602.11629.pdf)  
**作者**：Dongxiao He, Wenxuan Sun, Yongqi Huang, Jitao Zhao, Di Jin  

**一句话要点**：提出GP2F方法，通过自适应融合预训练图神经网络解决跨域图提示学习问题

**关键词**：图提示学习, 跨域适应, 预训练图神经网络, 自适应融合, 少样本分类

## 3 点简述
- 核心问题：跨域图提示学习在数据分布差异下为何有效，缺乏理论解释
- 方法要点：设计双分支结构，结合冻结预训练知识和轻量适配器，进行自适应融合
- 实验或效果：在跨域少样本节点和图分类任务中，性能优于现有方法

## 摘要（原文）

> Graph Prompt Learning (GPL) has recently emerged as a promising paradigm for downstream adaptation of pre-trained graph models, mitigating the misalignment between pre-training objectives and downstream tasks. Recently, the focus of GPL has shifted from in-domain to cross-domain scenarios, which is closer to the real world applications, where the pre-training source and downstream target often differ substantially in data distribution. However, why GPLs remain effective under such domain shifts is still unexplored. Empirically, we observe that representative GPL methods are competitive with two simple baselines in cross-domain settings: full fine-tuning (FT) and linear probing (LP), motivating us to explore a deeper understanding of the prompting mechanism. We provide a theoretical analysis demonstrating that jointly leveraging these two complementary branches yields a smaller estimation error than using either branch alone, formally proving that cross-domain GPL benefits from the integration between pre-trained knowledge and task-specific adaptation. Based on this insight, we propose GP2F, a dual-branch GPL method that explicitly instantiates the two extremes: (1) a frozen branch that retains pre-trained knowledge, and (2) an adapted branch with lightweight adapters for task-specific adaptation. We then perform adaptive fusion under topology constraints via a contrastive loss and a topology-consistent loss. Extensive experiments on cross-domain few-shot node and graph classification demonstrate that our method outperforms existing methods.

