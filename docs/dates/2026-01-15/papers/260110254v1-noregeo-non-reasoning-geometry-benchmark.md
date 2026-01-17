---
layout: default
title: NoReGeo: Non-Reasoning Geometry Benchmark
---

# NoReGeo: Non-Reasoning Geometry Benchmark
**arXiv**：[2601.10254v1](https://arxiv.org/abs/2601.10254) · [PDF](https://arxiv.org/pdf/2601.10254.pdf)  
**作者**：Irina Abdullaeva, Anton Vasiliuk, Elizaveta Goncharova, Temurbek Rahmatullaev, Zagorulko Ivan, Maxim Kurkin, Andrey Kuznetsov  

**一句话要点**：提出NoReGeo基准以评估大语言模型的内在几何理解能力，无需依赖推理或代数计算。

**关键词**：几何理解基准, 大语言模型评估, 空间关系编码, 几何属性识别, 非推理几何

## 3 点简述
- 核心问题：现有基准主要评估基于推理的几何能力，而忽略模型是否天生能编码空间关系和识别几何属性。
- 方法要点：构建包含2500个简单几何问题的基准，覆盖25个类别，问题设计为仅通过几何理解即可解决。
- 实验或效果：评估包括GPT-4在内的前沿模型，最高准确率仅65%，且微调无法提升几何理解，需专门训练方法。

## 摘要（原文）

> We present NoReGeo, a novel benchmark designed to evaluate the intrinsic geometric understanding of large language models (LLMs) without relying on reasoning or algebraic computation. Unlike existing benchmarks that primarily assess models' proficiency in reasoning-based geometry-where solutions are derived using algebraic methods-NoReGeo focuses on evaluating whether LLMs can inherently encode spatial relationships and recognize geometric properties directly. Our benchmark comprises 2,500 trivial geometric problems spanning 25 categories, each carefully crafted to be solvable purely through native geometric understanding, assuming known object locations. We assess a range of state-of-the-art models on NoReGeo, including frontier models like GPT-4, observing that even the most advanced systems achieve an overall maximum of 65% accuracy in binary classification tasks. Further, our ablation experiments demonstrate that such geometric understanding does not emerge through fine-tuning alone, indicating that effective training for geometric comprehension requires a specialized approach from the outset. Our findings highlight a significant gap in current LLMs' ability to natively grasp geometric concepts, providing a foundation for future research toward models with true geometric cognition.

