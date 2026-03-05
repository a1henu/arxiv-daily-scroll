---
layout: default
title: Seeing as Experts Do: A Knowledge-Augmented Agent for Open-Set Fine-Grained Visual Understanding
---

# Seeing as Experts Do: A Knowledge-Augmented Agent for Open-Set Fine-Grained Visual Understanding
**arXiv**：[2603.03762v1](https://arxiv.org/abs/2603.03762) · [PDF](https://arxiv.org/pdf/2603.03762.pdf)  
**作者**：Junhan Chen, Zilu Zhou, Yujun Tong, Dongliang Chang, Yitao Luo, Zhanyu Ma  

**一句话要点**：提出知识增强细粒度推理代理KFRA，以解决开放集细粒度视觉理解中的推理与可解释性问题。

**关键词**：细粒度视觉理解, 知识增强推理, 开放集识别, 检索-定位耦合, 可解释人工智能, 多模态模型

## 3 点简述
- 核心问题：现有方法受限于闭集分类和单标签预测，在开放集或上下文依赖条件下性能显著下降。
- 方法要点：KFRA通过三阶段闭环推理模拟专家分析，包括开放词汇检测、检索-定位耦合和证据集成，实现可解释推理。
- 实验或效果：在FGExpertBench基准上，KFRA推理准确率提升高达19%，超越现有大模型和代理框架，提供证据驱动的可解释性。

## 摘要（原文）

> Fine-grained visual understanding is shifting from static classification to knowledge-augmented reasoning, where models must justify as well as recognise. Existing approaches remain limited by closed-set taxonomies and single-label prediction, leading to significant degradation under open-set or context-dependent conditions. We present the Knowledge-Augmented Fine-Grained Reasoning Agent (KFRA), a unified framework that transforms fine-grained perception into evidence-driven reasoning. KFRA operates through a three-stage closed reasoning loop that emulates expert analysis. It first performs open-vocabulary detection and web-scale retrieval to generate category hypotheses. It then conducts discriminative regions localisation by aligning textual knowledge with visual evidence through a global-to-local focusing mechanism. Finally, it integrates all multimodal evidence within a large multimodal model to perform interpretable reasoning. Unlike existing agents that treat retrieval and reasoning as independent processes, KFRA establishes a retrieval-grounding coupling that converts retrieved knowledge into spatially grounded evidence for verification. This design enables factual, interpretable, and task-agnostic reasoning across diverse fine-grained scenarios. To evaluate this capability, we construct FGExpertBench, a benchmark designed to assess reasoning depth and cross-task generalisation across six knowledge dimensions. Extensive experiments demonstrate that KFRA consistently surpasses both standalone large multimodal models and current agent frameworks, achieving up to 19 percent improvement in reasoning accuracy and delivering evidence-grounded interpretability in open-set fine-grained visual understanding.

