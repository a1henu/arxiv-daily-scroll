---
layout: default
title: Fool Me If You Can: On the Robustness of Binary Code Similarity Detection Models against Semantics-preserving Transformations
---

# Fool Me If You Can: On the Robustness of Binary Code Similarity Detection Models against Semantics-preserving Transformations
**arXiv**：[2602.12681v1](https://arxiv.org/abs/2602.12681) · [PDF](https://arxiv.org/pdf/2602.12681.pdf)  
**作者**：Jiyong Uhm, Minseok Kim, Michalis Polychronakis, Hyungjoon Koo  

**一句话要点**：提出asmFooler系统以评估二进制代码相似性检测模型在语义保持变换下的鲁棒性

**关键词**：二进制代码分析, 代码相似性检测, 对抗变换, 语义保持, 深度学习鲁棒性, 网络安全

## 3 点简述
- 核心问题：机器学习模型在二进制代码相似性检测任务中对语义保持变换的鲁棒性未充分探索
- 方法要点：设计多样化的语义保持对抗变换，构建数据集评估六个代表性模型
- 实验或效果：发现模型鲁棒性依赖处理流程，变换有效性受预算约束，最小扰动可高效误导模型

## 摘要（原文）

> Binary code analysis plays an essential role in cybersecurity, facilitating reverse engineering to reveal the inner workings of programs in the absence of source code. Traditional approaches, such as static and dynamic analysis, extract valuable insights from stripped binaries, but often demand substantial expertise and manual effort. Recent advances in deep learning have opened promising opportunities to enhance binary analysis by capturing latent features and disclosing underlying code semantics. Despite the growing number of binary analysis models based on machine learning, their robustness to adversarial code transformations at the binary level remains underexplored. We evaluate the robustness of deep learning models for the task of binary code similarity detection (BCSD) under semantics-preserving transformations. The unique nature of machine instructions presents distinct challenges compared to the typical input perturbations found in other domains. We introduce asmFooler, a system that evaluates the resilience of BCSD models using a diverse set of adversarial code transformations that preserve functional semantics. We construct a dataset of 9,565 binary variants from 620 baseline samples by applying eight semantics-preserving transformations across six representative BCSD models. Our major findings highlight several key insights: i) model robustness relies on the processing pipeline, including code pre-processing, architecture, and feature selection; ii) adversarial transformation effectiveness is bounded by a budget shaped by model-specific constraints like input size and instruction expressive capacity; iii) well-crafted transformations can be highly effective with minimal perturbations; and iv) such transformations efficiently disrupt model decisions (e.g., misleading to false positives or false negatives) by focusing on semantically significant instructions.

