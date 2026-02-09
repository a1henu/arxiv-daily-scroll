---
layout: default
title: Improve Large Language Model Systems with User Logs
---

# Improve Large Language Model Systems with User Logs
**arXiv**：[2602.06470v1](https://arxiv.org/abs/2602.06470) · [PDF](https://arxiv.org/pdf/2602.06470.pdf)  
**作者**：Changyue Wang, Weihang Su, Qingyao Ai, Yiqun Liu  

**一句话要点**：提出UNO框架，利用用户日志优化大语言模型系统，解决反馈噪声与异构数据挑战。

**关键词**：用户日志优化, 大语言模型系统, 反馈蒸馏, 数据聚类, 认知差距量化, 噪声过滤

## 3 点简述
- 核心问题：用户日志噪声大且非结构化，传统LLM系统难以有效利用反馈信号。
- 方法要点：UNO将日志蒸馏为规则和偏好对，通过聚类管理数据，量化认知差距以过滤噪声。
- 实验或效果：在实验中超越RAG和基于记忆的基线方法，实现高效优化。

## 摘要（原文）

> Scaling training data and model parameters has long driven progress in large language models (LLMs), but this paradigm is increasingly constrained by the scarcity of high-quality data and diminishing returns from rising computational costs. As a result, recent work is increasing the focus on continual learning from real-world deployment, where user interaction logs provide a rich source of authentic human feedback and procedural knowledge. However, learning from user logs is challenging due to their unstructured and noisy nature. Vanilla LLM systems often struggle to distinguish useful feedback signals from noisy user behavior, and the disparity between user log collection and model optimization (e.g., the off-policy optimization problem) further strengthens the problem. To this end, we propose UNO (User log-driveN Optimization), a unified framework for improving LLM systems (LLMsys) with user logs. UNO first distills logs into semi-structured rules and preference pairs, then employs query-and-feedback-driven clustering to manage data heterogeneity, and finally quantifies the cognitive gap between the model's prior knowledge and the log data. This assessment guides the LLMsys to adaptively filter out noisy feedback and construct different modules for primary and reflective experiences extracted from user logs, thereby improving future responses. Extensive experiments show that UNO achieves state-of-the-art effectiveness and efficiency, significantly outperforming Retrieval Augmented Generation (RAG) and memory-based baselines. We have open-sourced our code at https://github.com/bebr2/UNO .

