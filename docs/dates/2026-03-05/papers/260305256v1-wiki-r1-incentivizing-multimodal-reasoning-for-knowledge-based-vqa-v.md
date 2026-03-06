---
layout: default
title: Wiki-R1: Incentivizing Multimodal Reasoning for Knowledge-based VQA via Data and Sampling Curriculum
---

# Wiki-R1: Incentivizing Multimodal Reasoning for Knowledge-based VQA via Data and Sampling Curriculum
**arXiv**：[2603.05256v1](https://arxiv.org/abs/2603.05256) · [PDF](https://arxiv.org/pdf/2603.05256.pdf)  
**作者**：Shan Ning, Longtian Qiu, Xuming He  

**一句话要点**：提出Wiki-R1框架，通过数据和采样课程激励多模态大语言模型在知识库视觉问答中的推理能力。

**关键词**：知识库视觉问答, 课程强化学习, 多模态大语言模型, 数据生成, 采样策略, 分布适应

## 3 点简述
- 核心问题：知识库视觉问答中，噪声检索和知识库结构化特性导致与预训练模型分布不匹配，阻碍推理和领域适应。
- 方法要点：采用课程强化学习，通过可控课程数据生成和课程采样策略，构建渐进训练分布以弥合分布差距。
- 实验或效果：在Encyclopedic VQA和InfoSeek基准上实现新SOTA，准确率分别提升至37.1%和44.1%。

## 摘要（原文）

> Knowledge-Based Visual Question Answering (KB-VQA) requires models to answer questions about an image by integrating external knowledge, posing significant challenges due to noisy retrieval and the structured, encyclopedic nature of the knowledge base. These characteristics create a distributional gap from pretrained multimodal large language models (MLLMs), making effective reasoning and domain adaptation difficult in the post-training stage. In this work, we propose \textit{Wiki-R1}, a data-generation-based curriculum reinforcement learning framework that systematically incentivizes reasoning in MLLMs for KB-VQA. Wiki-R1 constructs a sequence of training distributions aligned with the model's evolving capability, bridging the gap from pretraining to the KB-VQA target distribution. We introduce \textit{controllable curriculum data generation}, which manipulates the retriever to produce samples at desired difficulty levels, and a \textit{curriculum sampling strategy} that selects informative samples likely to yield non-zero advantages during RL updates. Sample difficulty is estimated using observed rewards and propagated to unobserved samples to guide learning. Experiments on two KB-VQA benchmarks, Encyclopedic VQA and InfoSeek, demonstrate that Wiki-R1 achieves new state-of-the-art results, improving accuracy from 35.5\% to 37.1\% on Encyclopedic VQA and from 40.1\% to 44.1\% on InfoSeek. The project page is available at https://artanic30.github.io/project_pages/WikiR1/.

