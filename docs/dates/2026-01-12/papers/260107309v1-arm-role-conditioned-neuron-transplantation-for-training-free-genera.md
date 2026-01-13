---
layout: default
title: ARM: Role-Conditioned Neuron Transplantation for Training-Free Generalist LLM Agent Merging
---

# ARM: Role-Conditioned Neuron Transplantation for Training-Free Generalist LLM Agent Merging
**arXiv**：[2601.07309v1](https://arxiv.org/abs/2601.07309) · [PDF](https://arxiv.org/pdf/2601.07309.pdf)  
**作者**：Zhuoka Feng, Kang Chen, Sihan Zhao, Kai Xiong, Yaoning Wang, Minshen Yu, Junjie Nian, Changyi Xiao, Yixin Cao, Yugang Jiang  

**一句话要点**：提出ARM方法，通过角色条件神经元移植实现免训练的大语言模型智能体合并，提升跨环境泛化能力。

**关键词**：模型合并, 大语言模型智能体, 神经元移植, 免训练优化, 跨环境泛化

## 3 点简述
- 核心问题：现有大语言模型智能体通常局限于单一环境，缺乏跨环境适应能力。
- 方法要点：基于激活引导和角色条件分析，设计三步框架进行神经元移植，无需梯度优化。
- 实验或效果：在多个领域超越先前合并方法和专家模型，展现出强泛化性能。

## 摘要（原文）

> Interactive large language model agents have advanced rapidly, but most remain specialized to a single environment and fail to adapt robustly to other environments. Model merging offers a training-free alternative by integrating multiple experts into a single model. In this paper, we propose Agent-Role Merging (ARM), an activation-guided, role-conditioned neuron transplantation method for model merging in LLM agents. ARM improves existing merging methods from static natural language tasks to multi-turn agent scenarios, and over the generalization ability across various interactive environments. This is achieved with a well designed 3-step framework: 1) constructing merged backbones, 2) selection based on its role-conditioned activation analysis, and 3) neuron transplantation for fine-grained refinements. Without gradient-based optimization, ARM improves cross-benchmark generalization while enjoying efficiency. Across diverse domains, the model obtained via ARM merging outperforms prior model merging methods and domain-specific expert models, while demonstrating strong out-of-domain generalization.

