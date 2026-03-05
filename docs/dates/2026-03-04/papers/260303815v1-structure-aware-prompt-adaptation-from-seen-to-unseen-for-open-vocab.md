---
layout: default
title: Structure-aware Prompt Adaptation from Seen to Unseen for Open-Vocabulary Compositional Zero-Shot Learning
---

# Structure-aware Prompt Adaptation from Seen to Unseen for Open-Vocabulary Compositional Zero-Shot Learning
**arXiv**：[2603.03815v1](https://arxiv.org/abs/2603.03815) · [PDF](https://arxiv.org/pdf/2603.03815.pdf)  
**作者**：Yihang Duan, Jiong Wang, Pengpeng Zeng, Ji Zhang, Lei Zhao, Chong Wang, Jingkuan Song, Lianli Gao  

**一句话要点**：提出结构感知提示适应方法，以提升开放词汇组合零样本学习中的未见概念泛化能力

**关键词**：开放词汇组合零样本学习, 提示调优, 结构感知适应, 嵌入空间局部结构, 泛化能力, 属性对象组合

## 3 点简述
- 核心问题：开放词汇组合零样本学习中，现有提示调优方法难以泛化到未见属性和对象及其组合
- 方法要点：基于嵌入空间局部结构一致性，设计结构感知一致性损失和结构引导适应策略
- 实验或效果：在开放词汇组合零样本学习基准上，保持闭集性能的同时显著提升开放词汇结果

## 摘要（原文）

> The goal of Open-Vocabulary Compositional Zero-Shot Learning (OV-CZSL) is to recognize attribute-object compositions in the open-vocabulary setting, where compositions of both seen and unseen attributes and objects are evaluated. Recently, prompt tuning methods have demonstrated strong generalization capabilities in the closed setting, where only compositions of seen attributes and objects are evaluated, i.e., Compositional Zero-Shot Learning (CZSL). However, directly applying these methods to OV-CZSL may not be sufficient to generalize to unseen attributes, objects and their compositions, as it is limited to seen attributes and objects. Normally, when faced with unseen concepts, humans adopt analogies with seen concepts that have the similar semantics thereby inferring their meaning (e.g., "wet" and "damp", "shirt" and "jacket"). In this paper, we experimentally show that the distribution of semantically related attributes or objects tends to form consistent local structures in the embedding space. Based on the above structures, we propose Structure-aware Prompt Adaptation (SPA) method, which enables models to generalize from seen to unseen attributes and objects. Specifically, in the training stage, we design a Structure-aware Consistency Loss (SCL) that encourages the local structure's consistency of seen attributes and objects in each iteration. In the inference stage, we devise a Structure-guided Adaptation Strategy (SAS) that adaptively aligns the structures of unseen attributes and objects with those of trained seen attributes and objects with similar semantics. Notably, SPA is a plug-and-play method that can be seamlessly integrated into existing CZSL prompt tuning methods. Extensive experiments on OV-CZSL benchmarks demonstrate that SPA achieves competitive closed-set performance while significantly improving open-vocabulary results.

