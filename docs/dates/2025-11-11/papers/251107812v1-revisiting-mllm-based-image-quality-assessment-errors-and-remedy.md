---
layout: default
title: Revisiting MLLM Based Image Quality Assessment: Errors and Remedy
---

# Revisiting MLLM Based Image Quality Assessment: Errors and Remedy
**arXiv**：[2511.07812v1](https://arxiv.org/abs/2511.07812) · [PDF](https://arxiv.org/pdf/2511.07812.pdf)  
**作者**：Zhenchen Tang, Songlin Yang, Bo Peng, Zichuan Wang, Jing Dong  

**一句话要点**：提出Q-Scorer框架以解决MLLM在图像质量评估中的离散-连续不匹配问题

**关键词**：多模态大语言模型, 图像质量评估, 离散-连续不匹配, 回归模块, 分数令牌, 基准测试

## 3 点简述
- 核心问题：MLLM离散输出与IQA连续分数不匹配，导致转换错误和语义混淆。
- 方法要点：引入轻量回归模块和IQA专用分数令牌，改进MLLM管道。
- 实验或效果：在多个IQA基准上达到SOTA，泛化性强且可与其他方法结合提升。

## 摘要（原文）

> The rapid progress of multi-modal large language models (MLLMs) has boosted the task of image quality assessment (IQA). However, a key challenge arises from the inherent mismatch between the discrete token outputs of MLLMs and the continuous nature of quality scores required by IQA tasks. This discrepancy significantly hinders the performance of MLLM-based IQA methods. Previous approaches that convert discrete token predictions into continuous scores often suffer from conversion errors. Moreover, the semantic confusion introduced by level tokens (e.g., ``good'') further constrains the performance of MLLMs on IQA tasks and degrades their original capabilities for related tasks. To tackle these problems, we provide a theoretical analysis of the errors inherent in previous approaches and, motivated by this analysis, propose a simple yet effective framework, Q-Scorer. This framework incorporates a lightweight regression module and IQA-specific score tokens into the MLLM pipeline. Extensive experiments demonstrate that Q-Scorer achieves state-of-the-art performance across multiple IQA benchmarks, generalizes well to mixed datasets, and further improves when combined with other methods.

