---
layout: default
title: Persian-Phi: Efficient Cross-Lingual Adaptation of Compact LLMs via Curriculum Learning
---

# Persian-Phi: Efficient Cross-Lingual Adaptation of Compact LLMs via Curriculum Learning
**arXiv**：[2512.07454v1](https://arxiv.org/abs/2512.07454) · [PDF](https://arxiv.org/pdf/2512.07454.pdf)  
**作者**：Amir Mohammad Akhlaghi, Amirhossein Shabani, Mostafa Abdolmaleki, Saeed Reza Kheradpisheh  

**一句话要点**：提出Persian-Phi模型，通过课程学习高效适配低资源波斯语，挑战大规模多语言模型假设。

**关键词**：跨语言适配, 课程学习, 参数高效微调, 低资源语言, 波斯语模型

## 3 点简述
- 核心问题：低资源语言训练大语言模型计算成本高，阻碍AI民主化。
- 方法要点：采用课程学习，先双语叙事预热对齐嵌入，再持续预训练和指令调优。
- 实验或效果：模型在Open Persian LLM Leaderboard上取得竞争性结果，提供可扩展框架。

## 摘要（原文）

> The democratization of AI is currently hindered by the immense computational costs required to train Large Language Models (LLMs) for low-resource languages. This paper presents Persian-Phi, a 3.8B parameter model that challenges the assumption that robust multilingual capabilities require massive model sizes or multilingual baselines. We demonstrate how Microsoft Phi-3 Mini -- originally a monolingual English model -- can be effectively adapted to Persian through a novel, resource-efficient curriculum learning pipeline. Our approach employs a unique "warm-up" stage using bilingual narratives (Tiny Stories) to align embeddings prior to heavy training, followed by continual pretraining and instruction tuning via Parameter-Efficient Fine-Tuning (PEFT). Despite its compact size, Persian-Phi achieves competitive results on Open Persian LLM Leaderboard in HuggingFace. Our findings provide a validated, scalable framework for extending the reach of state-of-the-art LLMs to underrepresented languages with minimal hardware resources. The Persian-Phi model is publicly available at https://huggingface.co/amirakhlaghiqqq/PersianPhi.

