---
layout: default
title: Personalized Medication Planning via Direct Domain Modeling and LLM-Generated Heuristics
---

# Personalized Medication Planning via Direct Domain Modeling and LLM-Generated Heuristics
**arXiv**：[2601.03687v1](https://arxiv.org/abs/2601.03687) · [PDF](https://arxiv.org/pdf/2601.03687.pdf)  
**作者**：Yonatan Vernik, Alexander Tuisov, David Izhaki, Hana Weitman, Gal A. Kaminka, Alexander Shleyfman  

**一句话要点**：提出基于直接领域建模与LLM生成启发式的方法，以扩展个性化用药规划至28种药物

**关键词**：个性化用药规划, 自动化规划, LLM生成启发式, 直接领域建模, GBFS搜索

## 3 点简述
- 核心问题：现有自动化规划器在个性化用药规划中最多处理7种药物，临床实用性受限
- 方法要点：通过程序化领域建模和LLM生成问题特定启发式，结合通用搜索算法GBFS
- 实验或效果：显著提升覆盖率和规划时间，药物数量扩展至至少28种，接近实际应用

## 摘要（原文）

> Personalized medication planning involves selecting medications and determining a dosing schedule to achieve medical goals specific to each individual patient. Previous work successfully demonstrated that automated planners, using general domain-independent heuristics, are able to generate personalized treatments, when the domain and problems are modeled using a general domain description language (\pddlp). Unfortunately, this process was limited in practice to consider no more than seven medications. In clinical terms, this is a non-starter. In this paper, we explore the use of automatically-generated domain- and problem-specific heuristics to be used with general search, as a method of scaling up medication planning to levels allowing closer work with clinicians. Specifically, we specify the domain programmatically (specifying an initial state and a successor generation procedure), and use an LLM to generate a problem specific heuristic that can be used by a fixed search algorithm (GBFS). The results indicate dramatic improvements in coverage and planning time, scaling up the number of medications to at least 28, and bringing medication planning one step closer to practical applications.

