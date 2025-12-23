---
layout: default
title: Tool-Augmented Hybrid Ensemble Reasoning with Distillation for Bilingual Mathematical Problem Solving
---

# Tool-Augmented Hybrid Ensemble Reasoning with Distillation for Bilingual Mathematical Problem Solving
**arXiv**：[2512.19093v1](https://arxiv.org/abs/2512.19093) · [PDF](https://arxiv.org/pdf/2512.19093.pdf)  
**作者**：Peiqing Lu, Yuan Zhang, Haoyun Zhang, Jiasen Zheng, Kejian Tong, Wenjun Wu  

**一句话要点**：提出HERALD框架以解决双语数学问题求解中语言推理与符号计算脱节的问题

**关键词**：双语数学推理, 混合集成推理, 工具增强学习, 知识蒸馏, 自适应路由, 置信度校准

## 3 点简述
- 核心问题：大语言模型在双语数学推理中语言处理强但计算精度弱，需连接推理与计算
- 方法要点：结合NuminaMath-7B-TIR、GPT-4o和Mistral-7B，通过自适应路由、工具强化学习和知识蒸馏集成多路径
- 实验或效果：系统提升准确性、稳定性和清晰度，实现流畅推理与精确计算，减少延迟

## 摘要（原文）

> Bilingual mathematical problem solving needs a clear link between language reasoning and symbolic calculation. Large language models often handle language well but are weak in accurate computation. This paper presents HERALD (Hybrid Ensemble Reasoning with Adaptive Learning and Distillation), a framework that joins reasoning and calculation using NuminaMath-7B-TIR, GPT-4o, and Mistral-7B. HERALD uses adaptive routing, tool-based reinforcement learning, and knowledge distillation to connect different reasoning paths. Confidence calibration keeps weighting stable, and dual-path checking keeps results correct. Reinforcement learning controls tool use to cut redundancy, and distillation lowers delay without hurting accuracy. The system shows that combining symbolic checking, adaptive ensembles, and bilingual fine-tuning helps achieve both fluent reasoning and precise calculation. HERALD offers a practical solution for multilingual mathematical reasoning with better accuracy, stability, and clarity.

