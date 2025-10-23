---
layout: default
title: Multi-modal Co-learning for Earth Observation: Enhancing single-modality models via modality collaboration
---

# Multi-modal Co-learning for Earth Observation: Enhancing single-modality models via modality collaboration
**arXiv**：[2510.19579v1](https://arxiv.org/abs/2510.19579) · [PDF](https://arxiv.org/pdf/2510.19579.pdf)  
**作者**：Francisco Mena, Dino Ienco, Cassio F. Dantas, Roberto Interdonato, Andreas Dengel  

**一句话要点**：提出多模态协同学习框架，以提升地球观测中单模态模型的预测性能

**关键词**：多模态协同学习, 地球观测, 单模态推理, 对比学习, 模态判别学习, 遥感数据分析

## 3 点简述
- 核心问题：地球观测中训练与推理阶段模态访问不一致，影响单模态模型部署
- 方法要点：结合对比学习和模态判别学习，分离模态共享与特定信息
- 实验或效果：在四个基准测试中优于现有方法，验证单模态推理场景有效性

## 摘要（原文）

> Multi-modal co-learning is emerging as an effective paradigm in machine
> learning, enabling models to collaboratively learn from different modalities to
> enhance single-modality predictions. Earth Observation (EO) represents a
> quintessential domain for multi-modal data analysis, wherein diverse remote
> sensors collect data to sense our planet. This unprecedented volume of data
> introduces novel challenges. Specifically, the access to the same sensor
> modalities at both training and inference stages becomes increasingly complex
> based on real-world constraints affecting remote sensing platforms. In this
> context, multi-modal co-learning presents a promising strategy to leverage the
> vast amount of sensor-derived data available at the training stage to improve
> single-modality models for inference-time deployment. Most current research
> efforts focus on designing customized solutions for either particular
> downstream tasks or specific modalities available at the inference stage. To
> address this, we propose a novel multi-modal co-learning framework capable of
> generalizing across various tasks without targeting a specific modality for
> inference. Our approach combines contrastive and modality discriminative
> learning together to guide single-modality models to structure the internal
> model manifold into modality-shared and modality-specific information. We
> evaluate our framework on four EO benchmarks spanning classification and
> regression tasks across different sensor modalities, where only one of the
> modalities available during training is accessible at inference time. Our
> results demonstrate consistent predictive improvements over state-of-the-art
> approaches from the recent machine learning and computer vision literature, as
> well as EO-specific methods. The obtained findings validate our framework in
> the single-modality inference scenarios across a diverse range of EO
> applications.

