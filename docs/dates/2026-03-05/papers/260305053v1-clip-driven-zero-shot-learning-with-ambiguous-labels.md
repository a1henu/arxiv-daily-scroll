---
layout: default
title: CLIP-driven Zero-shot Learning with Ambiguous Labels
---

# CLIP-driven Zero-shot Learning with Ambiguous Labels
**arXiv**：[2603.05053v1](https://arxiv.org/abs/2603.05053) · [PDF](https://arxiv.org/pdf/2603.05053.pdf)  
**作者**：Jinfu Fan, Jiangnan Li, Xiaowen Yan, Xiaohui Zhong, Wenpeng Lu, Linqing Huang  

**一句话要点**：提出CLIP驱动的部分标签零样本学习框架以处理现实场景中的标签模糊问题

**关键词**：零样本学习, 标签模糊, CLIP模型, 语义对齐, 部分标签学习

## 3 点简述
- 核心问题：零样本学习中训练实例的标签常存在噪声和模糊，降低模型性能
- 方法要点：利用CLIP提取特征，通过语义挖掘块和部分零样本损失逐步识别真实标签
- 实验或效果：在多个数据集上验证了CLIP-PZSL的优势，提升了语义对齐和识别准确性

## 摘要（原文）

> Zero-shot learning (ZSL) aims to recognize unseen classes by leveraging semantic information from seen classes, but most existing methods assume accurate class labels for training instances. However, in real-world scenarios, noise and ambiguous labels can significantly reduce the performance of ZSL. To address this, we propose a new CLIP-driven partial label zero-shot learning (CLIP-PZSL) framework to handle label ambiguity. First, we use CLIP to extract instance and label features. Then, a semantic mining block fuses these features to extract discriminative label embeddings. We also introduce a partial zero-shot loss, which assigns weights to candidate labels based on their relevance to the instance and aligns instance and label embeddings to minimize semantic mismatch. As the training goes on, the ground-truth labels are progressively identified, and the refined labels and label embeddings in turn help improve the semantic alignment of instance and label features. Comprehensive experiments on several datasets demonstrate the advantage of CLIP-PZSL.

