---
layout: default
title: Life Cycle-Aware Evaluation of Knowledge Distillation for Machine Translation: Environmental Impact and Translation Quality Trade-offs
---

# Life Cycle-Aware Evaluation of Knowledge Distillation for Machine Translation: Environmental Impact and Translation Quality Trade-offs
**arXiv**：[2602.09691v1](https://arxiv.org/abs/2602.09691) · [PDF](https://arxiv.org/pdf/2602.09691.pdf)  
**作者**：Joseph Attieh, Timothee Mickus, Anne-Laure Ligozat, Aurélie Névéol, Jörg Tiedemann  

**一句话要点**：评估知识蒸馏在机器翻译中的生命周期影响，权衡环境足迹与翻译质量

**关键词**：知识蒸馏, 机器翻译, 生命周期评估, 碳足迹, 计算成本, 翻译质量

## 3 点简述
- 核心问题：现有研究忽略知识蒸馏的计算成本，难以在计算约束下选择方法
- 方法要点：使用机器学习生命周期评估工具量化碳足迹，涵盖训练、蒸馏和推理阶段
- 实验或效果：发现蒸馏开销在小规模部署中主导，大规模时推理主导，词级蒸馏通常更优

## 摘要（原文）

> Knowledge distillation (KD) is a tool to compress a larger system (teacher) into a smaller one (student). In machine translation, studies typically report only the translation quality of the student and omit the computational complexity of performing KD, making it difficult to select among the many available KD choices under compute-induced constraints. In this study, we evaluate representative KD methods by considering both translation quality and computational cost. We express computational cost as a carbon footprint using the machine learning life cycle assessment (MLCA) tool. This assessment accounts for runtime operational emissions and amortized hardware production costs throughout the KD model life cycle (teacher training, distillation, and inference). We find that (i) distillation overhead dominates the total footprint at small deployment volumes, (ii) inference dominates at scale, making KD beneficial only beyond a task-dependent usage threshold, and (iii) word-level distillation typically offers more favorable footprint-quality trade-offs than sequence-level distillation. Our protocol provides reproducible guidance for selecting KD methods under explicit quality and compute-induced constraints.

