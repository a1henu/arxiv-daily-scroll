---
layout: default
title: Socratic Students: Teaching Language Models to Learn by Asking Questions
---

# Socratic Students: Teaching Language Models to Learn by Asking Questions
**arXiv**：[2512.13102v1](https://arxiv.org/abs/2512.13102) · [PDF](https://arxiv.org/pdf/2512.13102.pdf)  
**作者**：Rajeev Bhatt Ambati, Tianyi Niu, Aashu Singh, Shlok Mishra, Shashank Srivastava, Snigdha Chaturvedi  

**一句话要点**：提出学生主导提问方法以提升语言模型在动态交互中的学习效率

**关键词**：语言模型学习, 动态交互, 提问策略, 直接偏好优化, 教育辅导

## 3 点简述
- 核心问题：语言模型在静态交互中表现优异，但在需要主动获取信息的动态场景（如教育辅导）中效率不足
- 方法要点：通过学生模型主动向教师提问，并利用直接偏好优化训练提升问题质量
- 实验或效果：在数学和编码基准测试中，学生主导方法相比静态基线带来至少0.5的绝对Pass@k提升

## 摘要（原文）

> Large Language Models (LLMs) excel at static interactions, where they answer user queries by retrieving knowledge encoded in their parameters. However, in many real-world settings, such as educational tutoring or medical assistance, relevant information is not directly available and must be actively acquired through dynamic interactions. An interactive agent would recognize its own uncertainty, ask targeted questions, and retain new knowledge efficiently. Prior work has primarily explored effective ways for a teacher to instruct the student, where the teacher identifies student gaps and provides guidance. In this work, we shift the focus to the student and investigate effective strategies to actively query the teacher in seeking useful information. Across math and coding benchmarks, where baseline student models begin with near-zero performance, we show that student-led approaches consistently yield absolute Pass@k improvements of at least 0.5 over static baselines. To improve question quality, we train students using Direct Preference Optimization (DPO) with guidance from either self or stronger students. We find that this guided training enables smaller models to learn how to ask better questions, further enhancing learning efficiency.

