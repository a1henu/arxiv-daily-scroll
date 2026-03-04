---
layout: default
title: SpatialText: A Pure-Text Cognitive Benchmark for Spatial Understanding in Large Language Models
---

# SpatialText: A Pure-Text Cognitive Benchmark for Spatial Understanding in Large Language Models
**arXiv**：[2603.03002v1](https://arxiv.org/abs/2603.03002) · [PDF](https://arxiv.org/pdf/2603.03002.pdf)  
**作者**：Peiyao Jiang, Zequn Qin, Xi Li  

**一句话要点**：提出SpatialText纯文本基准以诊断大语言模型的空间认知能力

**关键词**：空间推理, 大语言模型, 认知基准, 纯文本评估, 心理模型

## 3 点简述
- 核心问题：现有基准无法区分大语言模型的空间推理与语言统计启发式
- 方法要点：结合人类标注描述与代码生成场景，隔离文本空间推理
- 实验或效果：模型在自我中心视角转换和局部参考系推理中表现系统性失败

## 摘要（原文）

> Genuine spatial reasoning relies on the capacity to construct and manipulate coherent internal spatial representations, often conceptualized as mental models, rather than merely processing surface linguistic associations. While large language models exhibit advanced capabilities across various domains, existing benchmarks fail to isolate this intrinsic spatial cognition from statistical language heuristics. Furthermore, multimodal evaluations frequently conflate genuine spatial reasoning with visual perception. To systematically investigate whether models construct flexible spatial mental models, we introduce SpatialText, a theory-driven diagnostic framework. Rather than functioning simply as a dataset, SpatialText isolates text-based spatial reasoning through a dual-source methodology. It integrates human-annotated descriptions of real 3D indoor environments, which capture natural ambiguities, perspective shifts, and functional relations, with code-generated, logically precise scenes designed to probe formal spatial deduction and epistemic boundaries. Systematic evaluation across state-of-the-art models reveals fundamental representational limitations. Although models demonstrate proficiency in retrieving explicit spatial facts and operating within global, allocentric coordinate systems, they exhibit critical failures in egocentric perspective transformation and local reference frame reasoning. These systematic errors provide strong evidence that current models rely heavily on linguistic co-occurrence heuristics rather than constructing coherent, verifiable internal spatial representations. SpatialText thus serves as a rigorous instrument for diagnosing the cognitive boundaries of artificial spatial intelligence.

