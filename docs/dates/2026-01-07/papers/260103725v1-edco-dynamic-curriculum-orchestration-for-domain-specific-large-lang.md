---
layout: default
title: EDCO: Dynamic Curriculum Orchestration for Domain-specific Large Language Model Fine-tuning
---

# EDCO: Dynamic Curriculum Orchestration for Domain-specific Large Language Model Fine-tuning
**arXiv**：[2601.03725v1](https://arxiv.org/abs/2601.03725) · [PDF](https://arxiv.org/pdf/2601.03725.pdf)  
**作者**：Jing-Cheng Pang, Liu Sun, Chang Zhou, Xian Tang, Haichuan Ma, Kun Jiang, Jianlong Wang, Kai Zhang, Sijie Wu, Haoran Cai, Chenwei Wu, Xubin Li, Xin Chen  

**一句话要点**：提出EDCO框架，通过动态课程编排解决领域特定大语言模型微调中静态课程缺乏适应性的问题。

**关键词**：大语言模型微调, 动态课程学习, 推理熵估计, 领域特定模型, 高效训练

## 3 点简述
- 核心问题：现有大语言模型微调多采用静态课程，无法适应训练中模型动态需求，影响学习效率。
- 方法要点：基于推理熵和动态编排，优先高熵样本，集成高效熵估计器、课程生成器和训练器。
- 实验或效果：在通信、医学和法律领域实验中，EDCO优于传统课程策略，熵估计计算时间减少83.5%。

## 摘要（原文）

> Domain-specific large language models (LLMs), typically developed by fine-tuning a pre-trained general-purpose LLM on specialized datasets, represent a significant advancement in applied AI. A common strategy in LLM fine-tuning is curriculum learning, which pre-orders training samples based on metrics like difficulty to improve learning efficiency compared to a random sampling strategy. However, most existing methods for LLM fine-tuning rely on a static curriculum, designed prior to training, which lacks adaptability to the model's evolving needs during fine-tuning. To address this, we propose EDCO, a novel framework based on two key concepts: inference entropy and dynamic curriculum orchestration. Inspired by recent findings that maintaining high answer entropy benefits long-term reasoning gains, EDCO prioritizes samples with high inference entropy in a continuously adapted curriculum. EDCO integrates three core components: an efficient entropy estimator that uses prefix tokens to approximate full-sequence entropy, an entropy-based curriculum generator that selects data points with the highest inference entropy, and an LLM trainer that optimizes the model on the selected curriculum. Comprehensive experiments in communication, medicine and law domains, EDCO outperforms traditional curriculum strategies for fine-tuning Qwen3-4B and Llama3.2-3B models under supervised and reinforcement learning settings. Furthermore, the proposed efficient entropy estimation reduces computational time by 83.5% while maintaining high accuracy.

