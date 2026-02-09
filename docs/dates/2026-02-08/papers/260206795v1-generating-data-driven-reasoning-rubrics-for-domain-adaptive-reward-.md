---
layout: default
title: Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling
---

# Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling
**arXiv**：[2602.06795v1](https://arxiv.org/abs/2602.06795) · [PDF](https://arxiv.org/pdf/2602.06795.pdf)  
**作者**：Kate Sanders, Nathaniel Weir, Sapana Chaudhary, Kaj Bostrom, Huzefa Rangwala  

**一句话要点**：提出数据驱动的推理错误分类法以增强大语言模型在技术领域的错误检测能力

**关键词**：推理错误检测, 奖励建模, 领域自适应, 大语言模型评估, 强化学习, 数据驱动分类

## 3 点简述
- 核心问题：大语言模型在长输出、需专家知识领域及无验证奖励问题中难以可靠识别推理错误
- 方法要点：自动构建细粒度推理错误分类法，用于强化学习中的奖励建模
- 实验或效果：在编码、数学和化学工程领域，错误识别优于基线，任务准确率提升达45%，接近可验证奖励性能

## 摘要（原文）

> An impediment to using Large Language Models (LLMs) for reasoning output verification is that LLMs struggle to reliably identify errors in thinking traces, particularly in long outputs, domains requiring expert knowledge, and problems without verifiable rewards. We propose a data-driven approach to automatically construct highly granular reasoning error taxonomies to enhance LLM-driven error detection on unseen reasoning traces. Our findings indicate that classification approaches that leverage these error taxonomies, or "rubrics", demonstrate strong error identification compared to baseline methods in technical domains like coding, math, and chemical engineering. These rubrics can be used to build stronger LLM-as-judge reward functions for reasoning model training via reinforcement learning. Experimental results show that these rewards have the potential to improve models' task accuracy on difficult domains over models trained by general LLMs-as-judges by +45%, and approach performance of models trained by verifiable rewards while using as little as 20% as many gold labels. Through our approach, we extend the usage of reward rubrics from assessing qualitative model behavior to assessing quantitative model correctness on tasks typically learned via RLVR rewards. This extension opens the door for teaching models to solve complex technical problems without a full dataset of gold labels, which are often highly costly to procure.

