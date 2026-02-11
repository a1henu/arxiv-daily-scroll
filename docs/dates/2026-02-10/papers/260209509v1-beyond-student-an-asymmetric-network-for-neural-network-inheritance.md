---
layout: default
title: Beyond Student: An Asymmetric Network for Neural Network Inheritance
---

# Beyond Student: An Asymmetric Network for Neural Network Inheritance
**arXiv**：[2602.09509v1](https://arxiv.org/abs/2602.09509) · [PDF](https://arxiv.org/pdf/2602.09509.pdf)  
**作者**：Yiyun Zhou, Jingwei Shi, Mingjing Xu, Zhonghua Jiang, Jingyuan Chen  

**一句话要点**：提出InherNet以通过非对称低秩分解继承教师网络知识，超越传统蒸馏的性能限制。

**关键词**：知识蒸馏, 模型压缩, 非对称网络, 低秩分解, 神经网络继承

## 3 点简述
- 核心问题：传统知识蒸馏中容量差距限制学生网络性能，如何最大化继承教师网络知识？
- 方法要点：使用非对称低秩分解重构轻量网络，通过SVD初始化确保主知识继承，平衡深度、宽度和压缩效率。
- 实验或效果：在单模态和多模态任务中，相比参数规模相似的学生网络，InherNet实现更高性能。

## 摘要（原文）

> Knowledge Distillation (KD) has emerged as a powerful technique for model compression, enabling lightweight student networks to benefit from the performance of redundant teacher networks. However, the inherent capacity gap often limits the performance of student networks. Inspired by the expressiveness of pretrained teacher networks, a compelling research question arises: is there a type of network that can not only inherit the teacher's structure but also maximize the inheritance of its knowledge? Furthermore, how does the performance of such an inheriting network compare to that of student networks, all benefiting from the same teacher network? To further explore this question, we propose InherNet, a neural network inheritance method that performs asymmetric low-rank decomposition on the teacher's weights and reconstructs a lightweight yet expressive network without significant architectural disruption. By leveraging Singular Value Decomposition (SVD) for initialization to ensure the inheritance of principal knowledge, InherNet effectively balances depth, width, and compression efficiency. Experimental results across unimodal and multimodal tasks demonstrate that InherNet achieves higher performance compared to student networks of similar parameter sizes. Our findings reveal a promising direction for future research in efficient model compression beyond traditional distillation.

