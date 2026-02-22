---
layout: default
title: Instructor-Aligned Knowledge Graphs for Personalized Learning
---

# Instructor-Aligned Knowledge Graphs for Personalized Learning
**arXiv**：[2602.17111v1](https://arxiv.org/abs/2602.17111) · [PDF](https://arxiv.org/pdf/2602.17111.pdf)  
**作者**：Abdulrahman AlRabah, Priyanka Kargupta, Jiawei Han, Abdussalam Alawini  

**一句话要点**：提出InstructKG框架，通过自动构建教师对齐的知识图谱，以解决大规模课程中个性化学习的学习依赖关系捕获问题。

**关键词**：知识图谱构建, 个性化学习, 教育技术, 学习依赖关系, 大语言模型应用

## 3 点简述
- 核心问题：大规模课程中，教师难以诊断学生知识差距，现有知识图谱方法忽略教学材料中的教学信号。
- 方法要点：基于课程讲义材料，提取概念节点并推断学习依赖边，结合教育材料的时序语义信号与大语言模型泛化能力。
- 实验或效果：在真实多样课程材料上实验，通过人工评估验证InstructKG能捕获丰富的教师对齐学习进展。

## 摘要（原文）

> Mastering educational concepts requires understanding both their prerequisites (e.g., recursion before merge sort) and sub-concepts (e.g., merge sort as part of sorting algorithms). Capturing these dependencies is critical for identifying students' knowledge gaps and enabling targeted intervention for personalized learning. This is especially challenging in large-scale courses, where instructors cannot feasibly diagnose individual misunderstanding or determine which concepts need reinforcement. While knowledge graphs offer a natural representation for capturing these conceptual relationships at scale, existing approaches are either surface-level (focusing on course-level concepts like "Algorithms" or logistical relationships such as course enrollment), or disregard the rich pedagogical signals embedded in instructional materials. We propose InstructKG, a framework for automatically constructing instructor-aligned knowledge graphs that capture a course's intended learning progression. Given a course's lecture materials (slides, notes, etc.), InstructKG extracts significant concepts as nodes and infers learning dependencies as directed edges (e.g., "part-of" or "depends-on" relationships). The framework synergizes the rich temporal and semantic signals unique to educational materials (e.g., "recursion" is taught before "mergesort"; "recursion" is mentioned in the definition of "merge sort") with the generalizability of large language models. Through experiments on real-world, diverse lecture materials across multiple courses and human-based evaluation, we demonstrate that InstructKG captures rich, instructor-aligned learning progressions.

