---
layout: default
title: Following the Teacher's Footsteps: Scheduled Checkpoint Distillation for Domain-Specific LLMs
---

# Following the Teacher's Footsteps: Scheduled Checkpoint Distillation for Domain-Specific LLMs
**arXiv**：[2601.10114v1](https://arxiv.org/abs/2601.10114) · [PDF](https://arxiv.org/pdf/2601.10114.pdf)  
**作者**：Cheng Feng, Chaoliang Zhong, Jun Sun, Yusuke Oishi  

**一句话要点**：提出计划检查点蒸馏方法，以提升领域特定任务中轻量学生模型的性能。

**关键词**：大语言模型, 知识蒸馏, 领域特定任务, 监督微调, 自适应加权

## 3 点简述
- 核心问题：教师与学生模型间的容量差距导致领域特定任务蒸馏性能不佳。
- 方法要点：通过模拟教师收敛过程减少教师优势子域缺陷，并自适应加权保留学生优势。
- 实验或效果：在多种领域任务中，该方法优于现有蒸馏方法，学生模型可匹配或超越教师。

## 摘要（原文）

> Large language models (LLMs) are challenging to deploy for domain-specific tasks due to their massive scale. While distilling a fine-tuned LLM into a smaller student model is a promising alternative, the capacity gap between teacher and student often leads to suboptimal performance. This raises a key question: when and how can a student model match or even surpass its teacher on domain-specific tasks? In this work, we propose a novel theoretical insight: a student can outperform its teacher if its advantage on a Student-Favored Subdomain (SFS) outweighs its deficit on the Teacher-Favored Subdomain (TFS). Guided by this insight, we propose Scheduled Checkpoint Distillation (SCD), which reduces the TFS deficit by emulating the teacher's convergence process during supervised fine-tuning (SFT) on the domain task, and a sample-wise Adaptive Weighting (AW) mechanism to preserve student strengths on SFS. Experiments across diverse domain tasks--including QA, NER, and text classification in multiple languages--show that our method consistently outperforms existing distillation approaches, allowing the student model to match or even exceed the performance of its fine-tuned teacher.

