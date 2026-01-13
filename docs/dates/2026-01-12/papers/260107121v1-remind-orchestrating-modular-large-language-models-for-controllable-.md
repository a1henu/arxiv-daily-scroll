---
layout: default
title: ReMIND: Orchestrating Modular Large Language Models for Controllable Serendipity A REM-Inspired System Design for Emergent Creative Ideation
---

# ReMIND: Orchestrating Modular Large Language Models for Controllable Serendipity A REM-Inspired System Design for Emergent Creative Ideation
**arXiv**：[2601.07121v1](https://arxiv.org/abs/2601.07121) · [PDF](https://arxiv.org/pdf/2601.07121.pdf)  
**作者**：Makoto Sato  

**一句话要点**：提出ReMIND框架，通过模块化LLM编排实现可控的意外创意生成

**关键词**：大型语言模型, 创意生成, 模块化框架, 意外性控制, 语义探索, 系统设计

## 3 点简述
- 核心问题：LLM创意生成中新颖性与一致性难以兼顾，意外洞察难以稳定产生。
- 方法要点：基于REM启发，设计四阶段模块化框架（唤醒、梦境、评判、再唤醒），分离探索与巩固功能。
- 实验或效果：参数扫描显示ReMIND能可靠诱导语义探索并保持稳定性，嵌入分析确认梦境阶段产生显著语义位移。

## 摘要（原文）

> Large language models (LLMs) are used not only for problem solving but also for creative ideation; however, eliciting serendipitous insights that are both novel and internally coherent remains difficult. While stochastic sampling promotes novelty, it often degrades consistency. Here, we propose ReMIND, a REM-inspired modular framework for ideation. ReMIND consists of four stages: wake, which generates a stable low-temperature semantic baseline; dream, which performs high-temperature exploratory generation; judge, which applies coarse evaluation to filter incoherent outputs and extract candidate ideas; and re-wake, which re-articulates selected ideas into coherent final outputs. By instantiating each stage as an independent LLM, ReMIND enables functional separation between exploration and consolidation. Parameter sweeps show that ReMIND reliably induces semantic exploration while preserving downstream stability. Embedding-based analyses confirm substantial semantic displacement during the dream phase, whereas external evaluations reveal that high-quality ideas emerge sporadically rather than as extrema along any single metric. These results suggest that serendipitous ideation in LLMs is a rare-event process best approached through system level design that shapes the conditions under which valuable ideas can emerge and be stabilized. ReMIND provides a general framework for studying the computational basis of serendipity and illustrates how modular LLM orchestration can bridge exploration and stabilization.

