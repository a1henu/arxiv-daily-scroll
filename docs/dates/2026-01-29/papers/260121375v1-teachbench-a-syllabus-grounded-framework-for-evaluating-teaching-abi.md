---
layout: default
title: TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models
---

# TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models
**arXiv**：[2601.21375v1](https://arxiv.org/abs/2601.21375) · [PDF](https://arxiv.org/pdf/2601.21375.pdf)  
**作者**：Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui  

**一句话要点**：提出基于教学大纲的框架TeachBench，以评估大语言模型在多轮教学中的教学能力。

**关键词**：教学能力评估, 大语言模型, 教学大纲, 多轮教学, 高考数据, 知识中心教学

## 3 点简述
- 核心问题：现有基准未充分评估大语言模型的知识中心教学能力，侧重于问题解决或问题级指导。
- 方法要点：通过限制教师代理使用结构化知识点和示例问题，避免信息泄露，并复用现有基准进行多轮教学评估。
- 实验或效果：在高考数据上实验显示，模型教学效果因学科和模型而异，数学表现较好，物理和化学教学仍具挑战性。

## 摘要（原文）

> Large language models (LLMs) show promise as teaching assistants, yet their teaching capability remains insufficiently evaluated. Existing benchmarks mainly focus on problem-solving or problem-level guidance, leaving knowledge-centered teaching underexplored. We propose a syllabus-grounded evaluation framework that measures LLM teaching capability via student performance improvement after multi-turn instruction. By restricting teacher agents to structured knowledge points and example problems, the framework avoids information leakage and enables reuse of existing benchmarks. We instantiate the framework on Gaokao data across multiple subjects. Experiments reveal substantial variation in teaching effectiveness across models and domains: some models perform well in mathematics, while teaching remains challenging in physics and chemistry. We also find that incorporating example problems does not necessarily improve teaching, as models often shift toward example-specific error correction. Overall, our results highlight teaching ability as a distinct and measurable dimension of LLM behavior.

