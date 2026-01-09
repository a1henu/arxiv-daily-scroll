---
layout: default
title: Agri-R1: Empowering Generalizable Agricultural Reasoning in Vision-Language Models with Reinforcement Learning
---

# Agri-R1: Empowering Generalizable Agricultural Reasoning in Vision-Language Models with Reinforcement Learning
**arXiv**：[2601.04672v1](https://arxiv.org/abs/2601.04672) · [PDF](https://arxiv.org/pdf/2601.04672.pdf)  
**作者**：Wentao Zhang, Lifei Wang, Lina Lu, MingKun Xu, Shangyang Li, Yanchao Yang, Tao Fang  

**一句话要点**：提出Agri-R1以增强视觉语言模型在农业领域的泛化推理能力

**关键词**：农业视觉语言模型, 强化学习训练, 推理数据生成, 病害诊断, 泛化能力提升

## 3 点简述
- 核心问题：农业病害诊断中，传统微调需大量标注、可解释性差且泛化能力弱。
- 方法要点：通过视觉语言合成和LLM过滤自动生成高质量推理数据，结合GRPO和领域奖励函数训练。
- 实验或效果：在CDDMBench上，3B参数模型性能媲美7B-13B基线，病害识别准确率提升23.2%。

## 摘要（原文）

> Agricultural disease diagnosis challenges VLMs, as conventional fine-tuning requires extensive labels, lacks interpretability, and generalizes poorly. While reasoning improves model robustness, existing methods rely on costly expert annotations and rarely address the open-ended, diverse nature of agricultural queries. To address these limitations, we propose \textbf{Agri-R1}, a reasoning-enhanced large model for agriculture. Our framework automates high-quality reasoning data generation via vision-language synthesis and LLM-based filtering, using only 19\% of available samples. Training employs Group Relative Policy Optimization (GRPO) with a novel proposed reward function that integrates domain-specific lexicons and fuzzy matching to assess both correctness and linguistic flexibility in open-ended responses. Evaluated on CDDMBench, our resulting 3B-parameter model achieves performance competitive with 7B- to 13B-parameter baselines, showing a +23.2\% relative gain in disease recognition accuracy, +33.3\% in agricultural knowledge QA, and a +26.10-point improvement in cross-domain generalization over standard fine-tuning. Ablation studies confirm that the synergy between structured reasoning data and GRPO-driven exploration underpins these gains, with benefits scaling as question complexity increases.

