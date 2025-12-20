---
layout: default
title: Quantitative Verification of Fairness in Tree Ensembles
---

# Quantitative Verification of Fairness in Tree Ensembles
**arXiv**：[2512.16386v1](https://arxiv.org/abs/2512.16386) · [PDF](https://arxiv.org/pdf/2512.16386.pdf)  
**作者**：Zhenjiang Zhao, Takahisa Toda, Takashi Kitamura  

**一句话要点**：提出高效量化验证方法以解决树集成模型公平性评估问题

**关键词**：树集成模型, 公平性验证, 量化分析, 反例比例, 模型诊断, 机器学习测试

## 3 点简述
- 核心问题：传统公平性验证仅返回单个反例，缺乏对反例比例和区域的量化分析
- 方法要点：利用树集成的离散结构，设计提供任意时间上下界的量化技术
- 实验或效果：在五个数据集上验证，性能优于现有测试技术

## 摘要（原文）

> This work focuses on quantitative verification of fairness in tree ensembles. Unlike traditional verification approaches that merely return a single counterexample when the fairness is violated, quantitative verification estimates the ratio of all counterexamples and characterizes the regions where they occur, which is important information for diagnosing and mitigating bias. To date, quantitative verification has been explored almost exclusively for deep neural networks (DNNs). Representative methods, such as DeepGemini and FairQuant, all build on the core idea of Counterexample-Guided Abstraction Refinement, a generic framework that could be adapted to other model classes. We extended the framework into a model-agnostic form, but discovered two limitations: (i) it can provide only lower bounds, and (ii) its performance scales poorly. Exploiting the discrete structure of tree ensembles, our work proposes an efficient quantification technique that delivers any-time upper and lower bounds. Experiments on five widely used datasets demonstrate its effectiveness and efficiency. When applied to fairness testing, our quantification method significantly outperforms state-of-the-art testing techniques.

