---
layout: default
title: EMO-R3: Reflective Reinforcement Learning for Emotional Reasoning in Multimodal Large Language Models
---

# EMO-R3: Reflective Reinforcement Learning for Emotional Reasoning in Multimodal Large Language Models
**arXiv**：[2602.23802v1](https://arxiv.org/abs/2602.23802) · [PDF](https://arxiv.org/pdf/2602.23802.pdf)  
**作者**：Yiyang Fang, Wenke Huang, Pei Fu, Yihao Yang, Kehua Su, Zhenbo Luo, Jian Luan, Mang Ye  

**一句话要点**：提出EMO-R3框架以增强多模态大语言模型的情感推理能力

**关键词**：情感推理, 多模态大语言模型, 强化学习, 可解释性, 视觉情感理解

## 3 点简述
- 多模态大语言模型在情感理解上存在泛化性和可解释性不足的问题
- 引入结构化情感思维和反思情感奖励，实现逐步推理和一致性评估
- 实验表明EMO-R3在多个视觉情感理解基准上显著提升性能

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown remarkable progress in visual reasoning and understanding tasks but still struggle to capture the complexity and subjectivity of human emotions. Existing approaches based on supervised fine-tuning often suffer from limited generalization and poor interpretability, while reinforcement learning methods such as Group Relative Policy Optimization fail to align with the intrinsic characteristics of emotional cognition. To address these challenges, we propose Reflective Reinforcement Learning for Emotional Reasoning (EMO-R3), a framework designed to enhance the emotional reasoning ability of MLLMs. Specifically, we introduce Structured Emotional Thinking to guide the model to perform step-by-step emotional reasoning in a structured and interpretable manner, and design a Reflective Emotional Reward that enables the model to re-evaluate its reasoning based on visual-text consistency and emotional coherence. Extensive experiments demonstrate that EMO-R3 significantly improves both the interpretability and emotional intelligence of MLLMs, achieving superior performance across multiple visual emotional understanding benchmarks.

