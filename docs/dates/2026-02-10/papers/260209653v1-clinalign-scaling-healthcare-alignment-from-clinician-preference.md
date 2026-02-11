---
layout: default
title: ClinAlign: Scaling Healthcare Alignment from Clinician Preference
---

# ClinAlign: Scaling Healthcare Alignment from Clinician Preference
**arXiv**：[2602.09653v1](https://arxiv.org/abs/2602.09653) · [PDF](https://arxiv.org/pdf/2602.09653.pdf)  
**作者**：Shiwei Lyu, Xidong Wang, Lei Liu, Hao Zhu, Chaohe Zhang, Jian Wang, Jinjie Gu, Benyou Wang, Yue Shen  

**一句话要点**：提出ClinAlign框架，通过医生验证的偏好数据和临床原则，解决大语言模型在医疗领域与细粒度临床偏好对齐的挑战。

**关键词**：医疗对齐, 临床偏好, 原则蒸馏, 离线对齐, 推理自修订, 资源高效模型

## 3 点简述
- 核心问题：大语言模型在医疗领域的开放输出难以与细粒度临床偏好对齐，现有方法依赖粗粒度目标或不可靠的自动评估。
- 方法要点：构建HealthRubrics数据集，包含医生验证的偏好示例；提炼为HealthPrinciples原则，用于离线对齐和推理时自修订。
- 实验或效果：30B参数模型仅激活3B参数，在HealthBench-Hard上达到33.4%，优于更大模型，建立资源高效的临床对齐基线。

## 摘要（原文）

> Although large language models (LLMs) demonstrate expert-level medical knowledge, aligning their open-ended outputs with fine-grained clinician preferences remains challenging. Existing methods often rely on coarse objectives or unreliable automated judges that are weakly grounded in professional guidelines. We propose a two-stage framework to address this gap. First, we introduce HealthRubrics, a dataset of 7,034 physician-verified preference examples in which clinicians refine LLM-drafted rubrics to meet rigorous medical standards. Second, we distill these rubrics into HealthPrinciples: 119 broadly reusable, clinically grounded principles organized by clinical dimensions, enabling scalable supervision beyond manual annotation. We use HealthPrinciples for (1) offline alignment by synthesizing rubrics for unlabeled queries and (2) an inference-time tool for guided self-revision. A 30B parameter model that activates only 3B parameters at inference trained with our framework achieves 33.4% on HealthBench-Hard, outperforming much larger models including Deepseek-R1 and o3, establishing a resource-efficient baseline for clinical alignment.

