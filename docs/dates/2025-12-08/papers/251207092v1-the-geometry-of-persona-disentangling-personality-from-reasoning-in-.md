---
layout: default
title: The Geometry of Persona: Disentangling Personality from Reasoning in Large Language Models
---

# The Geometry of Persona: Disentangling Personality from Reasoning in Large Language Models
**arXiv**：[2512.07092v1](https://arxiv.org/abs/2512.07092) · [PDF](https://arxiv.org/pdf/2512.07092.pdf)  
**作者**：Zhixiang Wang  

**一句话要点**：提出Soul Engine框架，基于线性表示假设，实现大语言模型中人格与推理能力的解耦，以解决个性化部署中的稳定性-可塑性困境。

**关键词**：大语言模型个性化, 人格解耦, 线性表示假设, 零样本人格注入, 确定性控制, SoulBench数据集

## 3 点简述
- 核心问题：大语言模型个性化部署面临稳定性-可塑性困境，现有对齐方法如监督微调可能导致推理能力下降。
- 方法要点：基于线性表示假设，使用双头架构在冻结基座模型上提取解耦的人格向量，无需修改权重。
- 实验或效果：实现高精度人格分析、几何正交性验证和确定性行为控制，支持零样本人格注入并保持原始智能。

## 摘要（原文）

> Background: The deployment of personalized Large Language Models (LLMs) is currently constrained by the stability-plasticity dilemma. Prevailing alignment methods, such as Supervised Fine-Tuning (SFT), rely on stochastic weight updates that often incur an "alignment tax" -- degrading general reasoning capabilities.
>   Methods: We propose the Soul Engine, a framework based on the Linear Representation Hypothesis, which posits that personality traits exist as orthogonal linear subspaces. We introduce SoulBench, a dataset constructed via dynamic contextual sampling. Using a dual-head architecture on a frozen Qwen-2.5 base, we extract disentangled personality vectors without modifying the backbone weights.
>   Results: Our experiments demonstrate three breakthroughs. First, High-Precision Profiling: The model achieves a Mean Squared Error (MSE) of 0.011 against psychological ground truth. Second, Geometric Orthogonality: T-SNE visualization confirms that personality manifolds are distinct and continuous, allowing for "Zero-Shot Personality Injection" that maintains original model intelligence. Third, Deterministic Steering: We achieve robust control over behavior via vector arithmetic, validated through extensive ablation studies.
>   Conclusion: This work challenges the necessity of fine-tuning for personalization. By transitioning from probabilistic prompting to deterministic latent intervention, we provide a mathematically rigorous foundation for safe, controllable AI personalization.

