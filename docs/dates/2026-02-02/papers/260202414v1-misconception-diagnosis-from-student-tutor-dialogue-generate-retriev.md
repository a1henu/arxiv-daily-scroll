---
layout: default
title: Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank
---

# Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank
**arXiv**：[2602.02414v1](https://arxiv.org/abs/2602.02414) · [PDF](https://arxiv.org/pdf/2602.02414.pdf)  
**作者**：Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, Simon Woodhead  

**一句话要点**：提出生成-检索-重排方法，利用大语言模型从学生-导师对话中检测学习误解

**关键词**：学习误解检测, 学生-导师对话分析, 大语言模型微调, 生成-检索-重排, 教育技术

## 3 点简述
- 核心问题：学生误解的及时准确识别依赖教师直觉，自动化检测需求高
- 方法要点：先微调LLM生成可能误解，再通过嵌入相似性检索，最后重排提升相关性
- 实验或效果：在真实对话数据上评估，微调模型优于基线，生成和重排步骤对质量关键

## 摘要（原文）

> Timely and accurate identification of student misconceptions is key to improving learning outcomes and pre-empting the compounding of student errors. However, this task is highly dependent on the effort and intuition of the teacher. In this work, we present a novel approach for detecting misconceptions from student-tutor dialogues using large language models (LLMs). First, we use a fine-tuned LLM to generate plausible misconceptions, and then retrieve the most promising candidates among these using embedding similarity with the input dialogue. These candidates are then assessed and re-ranked by another fine-tuned LLM to improve misconception relevance. Empirically, we evaluate our system on real dialogues from an educational tutoring platform. We consider multiple base LLM models including LLaMA, Qwen and Claude on zero-shot and fine-tuned settings. We find that our approach improves predictive performance over baseline models and that fine-tuning improves both generated misconception quality and can outperform larger closed-source models. Finally, we conduct ablation studies to both validate the importance of our generation and reranking steps on misconception generation quality.

