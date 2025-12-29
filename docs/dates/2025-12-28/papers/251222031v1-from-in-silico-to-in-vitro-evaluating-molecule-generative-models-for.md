---
layout: default
title: From In Silico to In Vitro: Evaluating Molecule Generative Models for Hit Generation
---

# From In Silico to In Vitro: Evaluating Molecule Generative Models for Hit Generation
**arXiv**：[2512.22031v1](https://arxiv.org/abs/2512.22031) · [PDF](https://arxiv.org/pdf/2512.22031.pdf)  
**作者**：Nagham Osman, Vittorio Lembo, Giovanni Bottegoni, Laura Toni  

**一句话要点**：提出评估框架，验证生成模型在药物发现中直接生成类命中分子的能力

**关键词**：分子生成模型, 命中识别, 药物发现, 评估框架, 深度学习

## 3 点简述
- 核心问题：传统命中识别资源密集，生成模型能否替代此步骤未知
- 方法要点：设计多阶段过滤框架，结合物理化学、结构和生物活性标准
- 实验或效果：模型生成有效多样分子，部分合成并体外验证活性

## 摘要（原文）

> Hit identification is a critical yet resource-intensive step in the drug discovery pipeline, traditionally relying on high-throughput screening of large compound libraries. Despite advancements in virtual screening, these methods remain time-consuming and costly. Recent progress in deep learning has enabled the development of generative models capable of learning complex molecular representations and generating novel compounds de novo. However, using ML to replace the entire drug-discovery pipeline is highly challenging. In this work, we rather investigate whether generative models can replace one step of the pipeline: hit-like molecule generation. To the best of our knowledge, this is the first study to explicitly frame hit-like molecule generation as a standalone task and empirically test whether generative models can directly support this stage of the drug discovery pipeline. Specifically, we investigate if such models can be trained to generate hit-like molecules, enabling direct incorporation into, or even substitution of, traditional hit identification workflows. We propose an evaluation framework tailored to this task, integrating physicochemical, structural, and bioactivity-related criteria within a multi-stage filtering pipeline that defines the hit-like chemical space. Two autoregressive and one diffusion-based generative models were benchmarked across various datasets and training settings, with outputs assessed using standard metrics and target-specific docking scores. Our results show that these models can generate valid, diverse, and biologically relevant compounds across multiple targets, with a few selected GSK-3$β$ hits synthesized and confirmed active in vitro. We also identify key limitations in current evaluation metrics and available training data.

