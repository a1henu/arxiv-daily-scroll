---
layout: default
title: MIND: Multi-rationale INtegrated Discriminative Reasoning Framework for Multi-modal Large Models
---

# MIND: Multi-rationale INtegrated Discriminative Reasoning Framework for Multi-modal Large Models
**arXiv**：[2512.05530v1](https://arxiv.org/abs/2512.05530) · [PDF](https://arxiv.org/pdf/2512.05530.pdf)  
**作者**：Chuang Yu, Jinmiao Zhao, Mingxuan Zhao, Yunpeng Liu, Xiujun Shu, Yuanhao Feng, Bo Wang, Xiangyu Yue  

**一句话要点**：提出MIND框架以解决多模态大模型在多理性推理中的语义建模不足和逻辑鲁棒性问题。

**关键词**：多模态大模型, 多理性推理, 判别性推理, 语义对齐, 数据集扩展, 逻辑校正

## 3 点简述
- 核心问题：多模态大模型在多理性语义建模有限、逻辑鲁棒性不足，易受复杂场景误导。
- 方法要点：引入RAD范式扩展数据集，设计P2CL策略进行两阶段校正学习，采用MCA优化策略对齐语义。
- 实验或效果：在多个公开数据集上实现SOTA性能，涵盖科学、常识和数学场景。

## 摘要（原文）

> Recently, multimodal large language models (MLLMs) have been widely applied to reasoning tasks. However, they suffer from limited multi-rationale semantic modeling, insufficient logical robustness, and are susceptible to misleading interpretations in complex scenarios. Therefore, we propose a Multi-rationale INtegrated Discriminative (MIND) reasoning framework, which is designed to endow MLLMs with human-like cognitive abilities of "Understand -> Rethink -> Correct", and achieves a paradigm evolution from passive imitation-based reasoning to active discriminative reasoning. Specifically, we introduce a Rationale Augmentation and Discrimination (RAD) paradigm, which automatically and efficiently expands existing datasets by generating diverse rationales, providing a unified and extensible data foundation. Meanwhile, we design a Progressive Two-stage Correction Learning (P2CL) strategy. The first phase enhances multi-rationale positive learning, while the second phase enables active logic discrimination and correction. In addition, to mitigate representation entanglement in the multi-rationale semantic space, we propose a Multi-rationale Contrastive Alignment (MCA) optimization strategy, which achieves semantic aggregation of correct reasoning and boundary separation of incorrect reasoning. Extensive experiments demonstrate that the proposed MIND reasoning framework achieves state-of-the-art (SOTA) performance on multiple public datasets covering scientific, commonsense, and mathematical scenarios. It provides a new perspective for advancing MLLMs towards higher levels of cognitive intelligence. Our code is available at https://github.com/YuChuang1205/MIND

