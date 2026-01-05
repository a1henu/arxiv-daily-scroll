---
layout: default
title: AEGIS: Exploring the Limit of World Knowledge Capabilities for Unified Mulitmodal Models
---

# AEGIS: Exploring the Limit of World Knowledge Capabilities for Unified Mulitmodal Models
**arXiv**：[2601.00561v1](https://arxiv.org/abs/2601.00561) · [PDF](https://arxiv.org/pdf/2601.00561.pdf)  
**作者**：Jintao Lin, Bowen Dong, Weikang Shi, Chenyang Lei, Suiyun Zhang, Rui Liu, Xihui Liu  

**一句话要点**：提出AEGIS基准和DCE协议，以评估统一多模态模型的世界知识能力。

**关键词**：统一多模态模型, 世界知识评估, 多任务基准, 确定性评估协议, 视觉理解与生成

## 3 点简述
- 核心问题：现有基准无法全面评估统一多模态模型的世界知识应用能力。
- 方法要点：构建多任务基准AEGIS，涵盖视觉理解、生成等，并引入确定性检查表评估协议。
- 实验或效果：实验显示模型存在知识缺陷，推理模块可部分缓解问题。

## 摘要（原文）

> The capability of Unified Multimodal Models (UMMs) to apply world knowledge across diverse tasks remains a critical, unresolved challenge. Existing benchmarks fall short, offering only siloed, single-task evaluations with limited diagnostic power. To bridge this gap, we propose AEGIS (\emph{i.e.}, \textbf{A}ssessing \textbf{E}diting, \textbf{G}eneration, \textbf{I}nterpretation-Understanding for \textbf{S}uper-intelligence), a comprehensive multi-task benchmark covering visual understanding, generation, editing, and interleaved generation. AEGIS comprises 1,050 challenging, manually-annotated questions spanning 21 topics (including STEM, humanities, daily life, etc.) and 6 reasoning types. To concretely evaluate the performance of UMMs in world knowledge scope without ambiguous metrics, we further propose Deterministic Checklist-based Evaluation (DCE), a protocol that replaces ambiguous prompt-based scoring with atomic ``Y/N'' judgments, to enhance evaluation reliability. Our extensive experiments reveal that most UMMs exhibit severe world knowledge deficits and that performance degrades significantly with complex reasoning. Additionally, simple plug-in reasoning modules can partially mitigate these vulnerabilities, highlighting a promising direction for future research. These results highlight the importance of world-knowledge-based reasoning as a critical frontier for UMMs.

