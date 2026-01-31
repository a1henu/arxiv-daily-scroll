---
layout: default
title: FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks
---

# FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks
**arXiv**：[2601.21165v1](https://arxiv.org/abs/2601.21165) · [PDF](https://arxiv.org/pdf/2601.21165.pdf)  
**作者**：Miles Wang, Robi Lin, Kat Hu, Joy Jiao, Neil Chowdhury, Ethan Chang, Tejal Patwardhan  

**一句话要点**：提出FrontierScience基准以评估前沿语言模型在专家级科学任务中的能力

**关键词**：科学推理基准, 语言模型评估, 专家级任务, 奥赛问题, 研究子任务, 细粒度评估

## 3 点简述
- 核心问题：现有科学基准因依赖选择题或已发表信息而饱和，需评估模型在专家级科学推理中的表现
- 方法要点：通过Olympiad和Research双轨制，涵盖国际奥赛题和博士级开放式研究子任务
- 实验或效果：包含数百问题，由专家制作和验证，并引入基于细粒度量规的评估框架

## 摘要（原文）

> We introduce FrontierScience, a benchmark evaluating expert-level scientific reasoning in frontier language models. Recent model progress has nearly saturated existing science benchmarks, which often rely on multiple-choice knowledge questions or already published information. FrontierScience addresses this gap through two complementary tracks: (1) Olympiad, consisting of international olympiad problems at the level of IPhO, IChO, and IBO, and (2) Research, consisting of PhD-level, open-ended problems representative of sub-tasks in scientific research.
>   FrontierScience contains several hundred questions (including 160 in the open-sourced gold set) covering subfields across physics, chemistry, and biology, from quantum electrodynamics to synthetic organic chemistry. All Olympiad problems are originally produced by international Olympiad medalists and national team coaches to ensure standards of difficulty, originality, and factuality. All Research problems are research sub-tasks written and verified by PhD scientists (doctoral candidates, postdoctoral researchers, or professors). For Research, we introduce a granular rubric-based evaluation framework to assess model capabilities throughout the process of solving a research task, rather than judging only a standalone final answer.

