---
layout: default
title: Quantitative Verification of Fairness in Tree Ensembles
---

# Quantitative Verification of Fairness in Tree Ensembles
**arXiv**：[2512.16386v1](https://arxiv.org/abs/2512.16386) · [PDF](https://arxiv.org/pdf/2512.16386.pdf)  
**作者**：Zhenjiang Zhao, Takahisa Toda, Takashi Kitamura  

**一句话要点**：提出高效量化验证方法，用于树集成模型的公平性评估，提供任意时刻上下界估计。

**关键词**：公平性验证, 树集成模型, 量化分析, 反例比例估计, 模型诊断

## 3 点简述
- 核心问题：传统公平性验证仅返回单个反例，缺乏反例比例和区域分析，影响偏差诊断与缓解。
- 方法要点：利用树集成的离散结构，设计高效量化技术，克服现有模型无关框架的局限，提供任意时刻上下界。
- 实验或效果：在五个常用数据集上验证，方法在公平性测试中显著优于现有技术，展示高效性和有效性。

## 摘要（原文）

> This work focuses on quantitative verification of fairness in tree ensembles. Unlike traditional verification approaches that merely return a single counterexample when the fairness is violated, quantitative verification estimates the ratio of all counterexamples and characterizes the regions where they occur, which is important information for diagnosing and mitigating bias. To date, quantitative verification has been explored almost exclusively for deep neural networks (DNNs). Representative methods, such as DeepGemini and FairQuant, all build on the core idea of Counterexample-Guided Abstraction Refinement, a generic framework that could be adapted to other model classes. We extended the framework into a model-agnostic form, but discovered two limitations: (i) it can provide only lower bounds, and (ii) its performance scales poorly. Exploiting the discrete structure of tree ensembles, our work proposes an efficient quantification technique that delivers any-time upper and lower bounds. Experiments on five widely used datasets demonstrate its effectiveness and efficiency. When applied to fairness testing, our quantification method significantly outperforms state-of-the-art testing techniques.

