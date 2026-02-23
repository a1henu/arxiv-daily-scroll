---
layout: default
title: Spatio-temporal Decoupled Knowledge Compensator for Few-Shot Action Recognition
---

# Spatio-temporal Decoupled Knowledge Compensator for Few-Shot Action Recognition
**arXiv**：[2602.18043v1](https://arxiv.org/abs/2602.18043) · [PDF](https://arxiv.org/pdf/2602.18043.pdf)  
**作者**：Hongyu Qu, Xiangbo Shu, Rui Yan, Hailiang Gao, Wenguan Wang, Jinhui Tang  

**一句话要点**：提出DiST框架，利用解耦的时空知识增强少样本动作识别性能

**关键词**：少样本动作识别, 时空解耦, 知识补偿, 多粒度原型, 大语言模型

## 3 点简述
- 少样本动作识别中，动作名称提供的语义上下文有限，难以捕捉新颖时空概念。
- DiST框架分解动作名称为时空属性描述，并设计空间/时间知识补偿器学习多粒度原型。
- 在五个标准数据集上实现最先进结果，验证了方法的有效性。

## 摘要（原文）

> Few-Shot Action Recognition (FSAR) is a challenging task that requires recognizing novel action categories with a few labeled videos. Recent works typically apply semantically coarse category names as auxiliary contexts to guide the learning of discriminative visual features. However, such context provided by the action names is too limited to provide sufficient background knowledge for capturing novel spatial and temporal concepts in actions. In this paper, we propose DiST, an innovative Decomposition-incorporation framework for FSAR that makes use of decoupled Spatial and Temporal knowledge provided by large language models to learn expressive multi-granularity prototypes. In the decomposition stage, we decouple vanilla action names into diverse spatio-temporal attribute descriptions (action-related knowledge). Such commonsense knowledge complements semantic contexts from spatial and temporal perspectives. In the incorporation stage, we propose Spatial/Temporal Knowledge Compensators (SKC/TKC) to discover discriminative object-level and frame-level prototypes, respectively. In SKC, object-level prototypes adaptively aggregate important patch tokens under the guidance of spatial knowledge. Moreover, in TKC, frame-level prototypes utilize temporal attributes to assist in inter-frame temporal relation modeling. These learned prototypes thus provide transparency in capturing fine-grained spatial details and diverse temporal patterns. Experimental results show DiST achieves state-of-the-art results on five standard FSAR datasets.

