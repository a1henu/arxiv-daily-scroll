---
layout: default
title: HAG: Hierarchical Demographic Tree-based Agent Generation for Topic-Adaptive Simulation
---

# HAG: Hierarchical Demographic Tree-based Agent Generation for Topic-Adaptive Simulation
**arXiv**：[2601.05656v1](https://arxiv.org/abs/2601.05656) · [PDF](https://arxiv.org/pdf/2601.05656.pdf)  
**作者**：Rongxin Chen, Tianyu Wu, Bingbing Xu, Xiucheng Xu, Huawei Shen  

**一句话要点**：提出HAG分层代理生成框架，以解决基于代理建模中主题自适应模拟的宏观分布对齐与微观一致性难题。

**关键词**：代理生成, 主题自适应模拟, 分层决策, 宏观分布对齐, 微观一致性, 基于代理建模

## 3 点简述
- 核心问题：现有方法在主题自适应代理生成中，静态检索无法适应未见主题，而LLM生成缺乏宏观分布意识，导致微观属性与现实不一致。
- 方法要点：HAG采用两阶段决策过程，先利用世界知识模型推断分层条件概率构建主题自适应树实现宏观对齐，再基于真实数据进行实例化和代理增强确保微观一致性。
- 实验或效果：在多领域基准测试中，HAG显著优于基线，平均减少人口对齐误差37.7%，提升社会学一致性18.8%。

## 摘要（原文）

> High-fidelity agent initialization is crucial for credible Agent-Based Modeling across diverse domains. A robust framework should be Topic-Adaptive, capturing macro-level joint distributions while ensuring micro-level individual rationality. Existing approaches fall into two categories: static data-based retrieval methods that fail to adapt to unseen topics absent from the data, and LLM-based generation methods that lack macro-level distribution awareness, resulting in inconsistencies between micro-level persona attributes and reality. To address these problems, we propose HAG, a Hierarchical Agent Generation framework that formalizes population generation as a two-stage decision process. Firstly, utilizing a World Knowledge Model to infer hierarchical conditional probabilities to construct the Topic-Adaptive Tree, achieving macro-level distribution alignment. Then, grounded real-world data, instantiation and agentic augmentation are carried out to ensure micro-level consistency. Given the lack of specialized evaluation, we establish a multi-domain benchmark and a comprehensive PACE evaluation framework. Extensive experiments show that HAG significantly outperforms representative baselines, reducing population alignment errors by an average of 37.7% and enhancing sociological consistency by 18.8%.

