---
layout: default
title: Instructor-Aligned Knowledge Graphs for Personalized Learning
---

# Instructor-Aligned Knowledge Graphs for Personalized Learning
**arXiv**：[2602.17111v1](https://arxiv.org/abs/2602.17111) · [PDF](https://arxiv.org/pdf/2602.17111.pdf)  
**作者**：Abdulrahman AlRabah, Priyanka Kargupta, Jiawei Han, Abdussalam Alawini  

**一句话要点**：提出InstructKG框架，自动构建教师对齐的知识图谱以支持大规模课程的个性化学习。

**关键词**：知识图谱构建, 个性化学习, 教育技术, 概念依赖, 大语言模型

## 3 点简述
- 核心问题：大规模课程中难以捕获概念间的学习依赖关系，以诊断学生知识缺口。
- 方法要点：利用课程材料提取概念节点，推断学习依赖边，结合教育信号与大语言模型。
- 实验或效果：在真实多样课程材料上验证，捕获教师对齐的学习进展。

## 摘要（原文）

> Mastering educational concepts requires understanding both their prerequisites (e.g., recursion before merge sort) and sub-concepts (e.g., merge sort as part of sorting algorithms). Capturing these dependencies is critical for identifying students' knowledge gaps and enabling targeted intervention for personalized learning. This is especially challenging in large-scale courses, where instructors cannot feasibly diagnose individual misunderstanding or determine which concepts need reinforcement. While knowledge graphs offer a natural representation for capturing these conceptual relationships at scale, existing approaches are either surface-level (focusing on course-level concepts like "Algorithms" or logistical relationships such as course enrollment), or disregard the rich pedagogical signals embedded in instructional materials. We propose InstructKG, a framework for automatically constructing instructor-aligned knowledge graphs that capture a course's intended learning progression. Given a course's lecture materials (slides, notes, etc.), InstructKG extracts significant concepts as nodes and infers learning dependencies as directed edges (e.g., "part-of" or "depends-on" relationships). The framework synergizes the rich temporal and semantic signals unique to educational materials (e.g., "recursion" is taught before "mergesort"; "recursion" is mentioned in the definition of "merge sort") with the generalizability of large language models. Through experiments on real-world, diverse lecture materials across multiple courses and human-based evaluation, we demonstrate that InstructKG captures rich, instructor-aligned learning progressions.

