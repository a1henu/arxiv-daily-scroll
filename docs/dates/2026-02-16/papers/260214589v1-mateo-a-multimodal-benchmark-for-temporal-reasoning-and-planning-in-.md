---
layout: default
title: MATEO: A Multimodal Benchmark for Temporal Reasoning and Planning in LVLMs
---

# MATEO: A Multimodal Benchmark for Temporal Reasoning and Planning in LVLMs
**arXiv**：[2602.14589v1](https://arxiv.org/abs/2602.14589) · [PDF](https://arxiv.org/pdf/2602.14589.pdf)  
**作者**：Gabriel Roccabruna, Olha Khomyn, Giuseppe Riccardi  

**一句话要点**：提出MATEO基准以评估和改进LVLMs在真实世界规划中的时序推理能力

**关键词**：时序推理, 多模态基准, 大视觉语言模型, 规划任务, 众包标注

## 3 点简述
- 核心问题：现有研究对基础模型时序执行理解有限，依赖自动标注、线性近似或纯文本输入
- 方法要点：基于高质量多模态食谱语料，通过众包标注获取TEO图，构建MATEO基准
- 实验或效果：评估六种先进LVLMs，考察模型规模、语言上下文、多模态输入结构和微调策略

## 摘要（原文）

> AI agents need to plan to achieve complex goals that involve orchestrating perception, sub-goal decomposition, and execution. These plans consist of ordered steps structured according to a Temporal Execution Order (TEO, a directed acyclic graph that ensures each step executes only after its preconditions are satisfied. Existing research on foundational models' understanding of temporal execution is limited to automatically derived annotations, approximations of the TEO as a linear chain, or text-only inputs. To address this gap, we introduce MATEO (MultimodAl Temporal Execution Order), a benchmark designed to assess and improve the temporal reasoning abilities of Large Vision Language Models (LVLMs) required for real-world planning. We acquire a high-quality professional multimodal recipe corpus, authored through a standardized editorial process that decomposes instructions into discrete steps, each paired with corresponding images. We collect TEO annotations as graphs by designing and using a scalable crowdsourcing pipeline. Using MATEO, we evaluate six state-of-the-art LVLMs across model scales, varying language context, multimodal input structure, and fine-tuning strategies.

