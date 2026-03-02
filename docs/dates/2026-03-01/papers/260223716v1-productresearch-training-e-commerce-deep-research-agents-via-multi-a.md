---
layout: default
title: ProductResearch: Training E-Commerce Deep Research Agents via Multi-Agent Synthetic Trajectory Distillation
---

# ProductResearch: Training E-Commerce Deep Research Agents via Multi-Agent Synthetic Trajectory Distillation
**arXiv**：[2602.23716v1](https://arxiv.org/abs/2602.23716) · [PDF](https://arxiv.org/pdf/2602.23716.pdf)  
**作者**：Jiangyuan Wang, Kejun Xiao, Huaipeng Zhao, Tao Luo, Xiaoyi Zeng  

**一句话要点**：提出ProductResearch多智能体框架，通过合成轨迹蒸馏训练电商深度研究智能体。

**关键词**：多智能体框架, 合成轨迹蒸馏, 电商购物智能体, 工具使用轨迹, 深度研究, LLM微调

## 3 点简述
- 问题：现有LLM智能体在电商对话购物中缺乏深度交互和上下文广度，Deep Research范式存在领域迁移差距。
- 方法：采用多智能体框架生成高保真工具使用轨迹，通过用户和监管智能体协作合成产品研究报告，并蒸馏为单角色训练样本。
- 效果：实验显示，基于合成数据微调的紧凑MoE模型在响应全面性、研究深度和用户效用上显著提升，接近前沿专有系统性能。

## 摘要（原文）

> Large Language Model (LLM)-based agents show promise for e-commerce conversational shopping, yet existing implementations lack the interaction depth and contextual breadth required for complex product research. Meanwhile, the Deep Research paradigm, despite advancing information synthesis in web search, suffers from domain gaps when transferred to e-commerce. We propose ProductResearch, a multi-agent framework that synthesizes high-fidelity, long-horizon tool-use trajectories for training robust e-commerce shopping agents. The framework employs a User Agent to infer nuanced shopping intents from behavioral histories, and a Supervisor Agent that orchestrates iterative collaboration with a Research Agent to generate synthetic trajectories culminating in comprehensive, insightful product research reports. These trajectories are rigorously filtered and distilled through a reflective internalization process that consolidates multi-agent supervisory interactions into coherent single-role training examples, enabling effective fine-tuning of LLM agents for complex shopping inquiries. Extensive experiments show that a compact MoE model fine-tuned on our synthetic data achieves substantial improvements over its base model in response comprehensiveness, research depth, and user-perceived utility, approaching the performance of frontier proprietary deep research systems and establishing multi-agent synthetic trajectory training as an effective and scalable paradigm for enhancing LLM-based shopping assistance.

