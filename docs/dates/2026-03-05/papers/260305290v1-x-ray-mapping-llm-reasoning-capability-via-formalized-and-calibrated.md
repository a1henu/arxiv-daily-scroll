---
layout: default
title: X-RAY: Mapping LLM Reasoning Capability via Formalized and Calibrated Probes
---

# X-RAY: Mapping LLM Reasoning Capability via Formalized and Calibrated Probes
**arXiv**：[2603.05290v1](https://arxiv.org/abs/2603.05290) · [PDF](https://arxiv.org/pdf/2603.05290.pdf)  
**作者**：Gao Tianxi, Cai Yufan, Yuan Yusi, Dong Jin Song  

**一句话要点**：提出X-RAY系统，通过形式化校准探针映射大语言模型推理能力

**关键词**：大语言模型评估, 推理能力分析, 形式化探针, 解空间几何, 校准验证

## 3 点简述
- 核心问题：现有评估混淆模式匹配与推理能力，缺乏对推理结构理解
- 方法要点：使用形式化工具生成探针，建模推理能力为结构函数，通过校准隔离结构信息
- 实验或效果：评估多领域问题，揭示模型在约束精炼与解空间重构上的不对称性

## 摘要（原文）

> Large language models (LLMs) achieve promising performance, yet their ability to reason remains poorly understood. Existing evaluations largely emphasize task-level accuracy, often conflating pattern matching with reasoning capability. We present X-RAY, an explainable reasoning analysis system that maps the LLM reasoning capability using calibrated, formally verified probes. We model reasoning capability as a function of extractable \textit{structure}, operationalized through formal properties such as constraint interaction, reasoning depth, and solution-space geometry. X-Ray generates probes via formal tools with controlled structural variations, enabling precise isolation of incremental structural information through formal calibration and verification. We evaluate state-of-the-art LLMs on problems ranging from junior-level to advanced in mathematics, physics, and chemistry. Our analysis reveals a systematic asymmetry in LLM reasoning: models are relatively robust to constraint refinement, where additional conditions shrink an existing solution space, but degrade sharply under solution-space restructuring, where modifications alter the underlying structural form of the solution manifold. Moreover, calibrated formal probes differentiate models that appear indistinguishable on standard benchmarks and reveal failure modes that are structurally interpretable rather than opaque. Beyond evaluation, our framework is contamination-free and supports the training and testing of reasoning models.

