---
layout: default
title: Pedagogically-Inspired Data Synthesis for Language Model Knowledge Distillation
---

# Pedagogically-Inspired Data Synthesis for Language Model Knowledge Distillation
**arXiv**：[2602.12172v1](https://arxiv.org/abs/2602.12172) · [PDF](https://arxiv.org/pdf/2602.12172.pdf)  
**作者**：Bowei He, Yankai Chen, Xiaokun Zhang, Linghe Kong, Philip S. Yu, Xue Liu, Chen Ma  

**一句话要点**：提出基于教学原则的三阶段框架IOA，以提升大语言模型向小模型的知识蒸馏效果。

**关键词**：知识蒸馏, 教学原则, 数据合成, 渐进式学习, 大语言模型

## 3 点简述
- 核心问题：现有蒸馏方法缺乏教学意识，将知识转移视为一次性数据合成任务。
- 方法要点：引入知识识别、组织和适配三阶段，结合掌握学习和最近发展区原则进行渐进式蒸馏。
- 实验或效果：在LLaMA和Qwen2.5上验证，IOA在推理任务中显著优于基线，参数减少超90%。

## 摘要（原文）

> Knowledge distillation from Large Language Models (LLMs) to smaller models has emerged as a critical technique for deploying efficient AI systems. However, current methods for distillation via synthetic data lack pedagogical awareness, treating knowledge transfer as a one-off data synthesis and training task rather than a systematic learning process. In this paper, we propose a novel pedagogically-inspired framework for LLM knowledge distillation that draws from fundamental educational principles. Our approach introduces a three-stage pipeline -- Knowledge Identifier, Organizer, and Adapter (IOA) -- that systematically identifies knowledge deficiencies in student models, organizes knowledge delivery through progressive curricula, and adapts representations to match the cognitive capacity of student models. We integrate Bloom's Mastery Learning Principles and Vygotsky's Zone of Proximal Development to create a dynamic distillation process where student models approach teacher model's performance on prerequisite knowledge before advancing, and new knowledge is introduced with controlled, gradual difficulty increments. Extensive experiments using LLaMA-3.1/3.2 and Qwen2.5 as student models demonstrate that IOA achieves significant improvements over baseline distillation methods, with student models retaining 94.7% of teacher performance on DollyEval while using less than 1/10th of the parameters. Our framework particularly excels in complex reasoning tasks, showing 19.2% improvement on MATH and 22.3% on HumanEval compared with state-of-the-art baselines.

