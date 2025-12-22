---
layout: default
title: MMRAG-RFT: Two-stage Reinforcement Fine-tuning for Explainable Multi-modal Retrieval-augmented Generation
---

# MMRAG-RFT: Two-stage Reinforcement Fine-tuning for Explainable Multi-modal Retrieval-augmented Generation
**arXiv**：[2512.17194v1](https://arxiv.org/abs/2512.17194) · [PDF](https://arxiv.org/pdf/2512.17194.pdf)  
**作者**：Shengwei Zhao, Jingwen Yao, Sitong Wei, Linhai Xu, Yuying Liu, Dong Zhang, Zhiqiang Tian, Shaoyi Du  

**一句话要点**：提出两阶段强化微调框架以增强多模态检索增强生成的可解释性

**关键词**：多模态检索增强生成, 强化学习微调, 可解释性推理, 多模态大语言模型, 两阶段优化

## 3 点简述
- 现有MMRAG方法缺乏推理逻辑解释，限制结果可信度
- 采用两阶段强化微调：规则阶段粗粒度过滤，推理阶段联合优化排序与生成
- 在WebQA和MultimodalQA数据集上实现最优性能，并通过消融实验验证有效性

## 摘要（原文）

> Multi-modal Retrieval-Augmented Generation (MMRAG) enables highly credible generation by integrating external multi-modal knowledge, thus demonstrating impressive performance in complex multi-modal scenarios. However, existing MMRAG methods fail to clarify the reasoning logic behind retrieval and response generation, which limits the explainability of the results. To address this gap, we propose to introduce reinforcement learning into multi-modal retrieval-augmented generation, enhancing the reasoning capabilities of multi-modal large language models through a two-stage reinforcement fine-tuning framework to achieve explainable multi-modal retrieval-augmented generation. Specifically, in the first stage, rule-based reinforcement fine-tuning is employed to perform coarse-grained point-wise ranking of multi-modal documents, effectively filtering out those that are significantly irrelevant. In the second stage, reasoning-based reinforcement fine-tuning is utilized to jointly optimize fine-grained list-wise ranking and answer generation, guiding multi-modal large language models to output explainable reasoning logic in the MMRAG process. Our method achieves state-of-the-art results on WebQA and MultimodalQA, two benchmark datasets for multi-modal retrieval-augmented generation, and its effectiveness is validated through comprehensive ablation experiments.

