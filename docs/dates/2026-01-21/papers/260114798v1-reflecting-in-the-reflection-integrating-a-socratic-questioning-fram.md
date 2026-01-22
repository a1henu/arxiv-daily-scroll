---
layout: default
title: Reflecting in the Reflection: Integrating a Socratic Questioning Framework into Automated AI-Based Question Generation
---

# Reflecting in the Reflection: Integrating a Socratic Questioning Framework into Automated AI-Based Question Generation
**arXiv**：[2601.14798v1](https://arxiv.org/abs/2601.14798) · [PDF](https://arxiv.org/pdf/2601.14798.pdf)  
**作者**：Ondřej Holub, Essi Ryymin, Rodrigo Alves  

**一句话要点**：提出基于苏格拉底对话的双智能体框架，用于自动生成反思问题以支持教学。

**关键词**：反思问题生成, 苏格拉底对话, 大型语言模型, 多智能体系统, 教学支持

## 3 点简述
- 核心问题：设计高质量反思问题耗时且教师支持不均，需自动化生成。
- 方法要点：协调学生-教师和教师-教育者双智能体，通过多轮对话迭代精炼问题。
- 实验或效果：动态停止结合上下文信息优于固定迭代，双智能体协议在相关性和深度上显著优于单次基线。

## 摘要（原文）

> Designing good reflection questions is pedagogically important but time-consuming and unevenly supported across teachers. This paper introduces a reflection-in-reflection framework for automated generation of reflection questions with large language models (LLMs). Our approach coordinates two role-specialized agents, a Student-Teacher and a Teacher-Educator, that engage in a Socratic multi-turn dialogue to iteratively refine a single question given a teacher-specified topic, key concepts, student level, and optional instructional materials. The Student-Teacher proposes candidate questions with brief rationales, while the Teacher-Educator evaluates them along clarity, depth, relevance, engagement, and conceptual interconnections, responding only with targeted coaching questions or a fixed signal to stop the dialogue. We evaluate the framework in an authentic lower-secondary ICT setting on the topic, using GPT-4o-mini as the backbone model and a stronger GPT- 4-class LLM as an external evaluator in pairwise comparisons of clarity, relevance, depth, and overall quality. First, we study how interaction design and context (dynamic vs.fixed iteration counts; presence or absence of student level and materials) affect question quality. Dynamic stopping combined with contextual information consistently outperforms fixed 5- or 10-step refinement, with very long dialogues prone to drift or over-complication. Second, we show that our two-agent protocol produces questions that are judged substantially more relevant and deeper, and better overall, than a one-shot baseline using the same backbone model.

