---
layout: default
title: CoG: Controllable Graph Reasoning via Relational Blueprints and Failure-Aware Refinement over Knowledge Graphs
---

# CoG: Controllable Graph Reasoning via Relational Blueprints and Failure-Aware Refinement over Knowledge Graphs
**arXiv**：[2601.11047v1](https://arxiv.org/abs/2601.11047) · [PDF](https://arxiv.org/pdf/2601.11047.pdf)  
**作者**：Yuanxiang Liu, Songze Li, Xiaoke Guo, Zhaoyan Gong, Qifei Zhang, Huajun Chen, Wen Zhang  

**一句话要点**：提出CoG框架，通过关系蓝图和失败感知精炼解决知识图谱增强大语言模型中的认知刚性问题

**关键词**：知识图谱推理, 大语言模型增强, 双过程理论, 关系蓝图, 失败感知精炼, 可控图推理

## 3 点简述
- 核心问题：知识图谱增强大语言模型存在认知刚性，易受噪声和结构错配影响导致推理停滞
- 方法要点：基于双过程理论，设计关系蓝图引导模块快速稳定搜索方向，失败感知精炼模块处理推理瓶颈
- 实验或效果：在三个基准测试中，CoG在准确性和效率上显著优于现有方法

## 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable reasoning capabilities but often grapple with reliability challenges like hallucinations. While Knowledge Graphs (KGs) offer explicit grounding, existing paradigms of KG-augmented LLMs typically exhibit cognitive rigidity--applying homogeneous search strategies that render them vulnerable to instability under neighborhood noise and structural misalignment leading to reasoning stagnation. To address these challenges, we propose CoG, a training-free framework inspired by Dual-Process Theory that mimics the interplay between intuition and deliberation. First, functioning as the fast, intuitive process, the Relational Blueprint Guidance module leverages relational blueprints as interpretable soft structural constraints to rapidly stabilize the search direction against noise. Second, functioning as the prudent, analytical process, the Failure-Aware Refinement module intervenes upon encountering reasoning impasses. It triggers evidence-conditioned reflection and executes controlled backtracking to overcome reasoning stagnation. Experimental results on three benchmarks demonstrate that CoG significantly outperforms state-of-the-art approaches in both accuracy and efficiency.

