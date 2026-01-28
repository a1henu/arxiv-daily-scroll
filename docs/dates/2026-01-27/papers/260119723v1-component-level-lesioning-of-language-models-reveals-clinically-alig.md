---
layout: default
title: Component-Level Lesioning of Language Models Reveals Clinically Aligned Aphasia Phenotypes
---

# Component-Level Lesioning of Language Models Reveals Clinically Aligned Aphasia Phenotypes
**arXiv**：[2601.19723v1](https://arxiv.org/abs/2601.19723) · [PDF](https://arxiv.org/pdf/2601.19723.pdf)  
**作者**：Yifan Wang, Jichen Zheng, Jingyuan Sun, Yunhao Zhang, Chunyu Ye, Jixing Li, Chengqing Zong, Shaonan Wang  

**一句话要点**：提出基于组件级扰动的大语言模型框架，模拟临床失语症表型以研究语言功能退化

**关键词**：大语言模型, 失语症模拟, 组件级扰动, 模块化模型, 语言认知计算, 临床神经语言学

## 3 点简述
- 核心问题：大语言模型能否通过系统扰动模拟脑损伤导致的失语症语言障碍
- 方法要点：引入临床基础组件级框架，选择性扰动功能组件，应用于模块化与密集模型
- 实验或效果：扰动产生失语症样回归，模块化模型支持更局部化表型-组件映射

## 摘要（原文）

> Large language models (LLMs) increasingly exhibit human-like linguistic behaviors and internal representations that they could serve as computational simulators of language cognition. We ask whether LLMs can be systematically manipulated to reproduce language-production impairments characteristic of aphasia following focal brain lesions. Such models could provide scalable proxies for testing rehabilitation hypotheses, and offer a controlled framework for probing the functional organization of language. We introduce a clinically grounded, component-level framework that simulates aphasia by selectively perturbing functional components in LLMs, and apply it to both modular Mixture-of-Experts models and dense Transformers using a unified intervention interface. Our pipeline (i) identifies subtype-linked components for Broca's and Wernicke's aphasia, (ii) interprets these components with linguistic probing tasks, and (iii) induces graded impairments by progressively perturbing the top-k subtype-linked components, evaluating outcomes with Western Aphasia Battery (WAB) subtests summarized by Aphasia Quotient (AQ). Across architectures and lesioning strategies, subtype-targeted perturbations yield more systematic, aphasia-like regressions than size-matched random perturbations, and MoE modularity supports more localized and interpretable phenotype-to-component mappings. These findings suggest that modular LLMs, combined with clinically informed component perturbations, provide a promising platform for simulating aphasic language production and studying how distinct language functions degrade under targeted disruptions.

