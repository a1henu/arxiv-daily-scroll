---
layout: default
title: Git for Sketches: An Intelligent Tracking System for Capturing Design Evolution
---

# Git for Sketches: An Intelligent Tracking System for Capturing Design Evolution
**arXiv**：[2602.06047v1](https://arxiv.org/abs/2602.06047) · [PDF](https://arxiv.org/pdf/2602.06047.pdf)  
**作者**：Sankar B, Amogh A S, Sandhya Baranwal, Dibakar Sen  

**一句话要点**：提出DIMES系统，结合sGIT版本控制和生成式AI，以解决设计草图中非线性历史和认知意图丢失的问题。

**关键词**：草图版本控制, 设计意图捕获, 生成式AI, 混合深度学习, 多模态提交, 设计教育

## 3 点简述
- 核心问题：传统草图工具难以捕获设计过程中的非线性历史和认知意图，导致上下文丢失。
- 方法要点：开发基于Web的DIMES环境，集成sGIT视觉版本控制架构，使用混合深度学习模型分类笔画，并映射Git原语到设计动作。
- 实验或效果：专家使用DIMES后概念探索广度提升160%，生成式AI模块提高知识转移效果，新手复制保真度达0.97，用户对AI渲染接受度更高。

## 摘要（原文）

> During product conceptualization, capturing the non-linear history and cognitive intent is crucial. Traditional sketching tools often lose this context. We introduce DIMES (Design Idea Management and Evolution capture System), a web-based environment featuring sGIT (SketchGit), a custom visual version control architecture, and Generative AI. sGIT includes AEGIS, a module using hybrid Deep Learning and Machine Learning models to classify six stroke types. The system maps Git primitives to design actions, enabling implicit branching and multi-modal commits (stroke data + voice intent). In a comparative study, experts using DIMES demonstrated a 160% increase in breadth of concept exploration. Generative AI modules generated narrative summaries that enhanced knowledge transfer; novices achieved higher replication fidelity (Neural Transparency-based Cosine Similarity: 0.97 vs. 0.73) compared to manual summaries. AI-generated renderings also received higher user acceptance (Purchase Likelihood: 4.2 vs 3.1). This work demonstrates that intelligent version control bridges creative action and cognitive documentation, offering a new paradigm for design education.

