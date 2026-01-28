---
layout: default
title: From Atoms to Chains: Divergence-Guided Reasoning Curriculum for Unlabeled LLM Domain Adaptation
---

# From Atoms to Chains: Divergence-Guided Reasoning Curriculum for Unlabeled LLM Domain Adaptation
**arXiv**：[2601.19588v1](https://arxiv.org/abs/2601.19588) · [PDF](https://arxiv.org/pdf/2601.19588.pdf)  
**作者**：Yongqi Wang, Xiaofeng Ji, Jie Wang, Qingbin Li, Xiao Xiong, Zheming Yang, Jian Xu, Minghui Qiu, Xinxiao Wu  

**一句话要点**：提出分歧引导推理课程以解决无标注数据下大语言模型领域适应中的教学困境

**关键词**：大语言模型, 领域适应, 知识蒸馏, 推理课程, 无标注学习, 分歧分析

## 3 点简述
- 核心问题：无标注数据下大语言模型领域适应时，知识蒸馏方法易导致粗粒度模仿和推理缺陷继承。
- 方法要点：基于原子子问题高保真性，通过分歧分析动态构建从原子知识到推理链的双重课程。
- 实验或效果：在医疗和法律领域验证，1.5B学生模型在医疗领域相对基线提升7.76%。

## 摘要（原文）

> Adapting Large Language Models (LLMs) to specialized domains without human-annotated data is a crucial yet formidable challenge. Widely adopted knowledge distillation methods often devolve into coarse-grained mimicry, where the student model inefficiently targets its own weaknesses and risks inheriting the teacher's reasoning flaws. This exposes a critical pedagogical dilemma: how to devise a reliable curriculum when the teacher itself is not an infallible expert. Our work resolves this by capitalizing on a key insight: while LLMs may exhibit fallibility in complex, holistic reasoning, they often exhibit high fidelity on focused, atomic sub-problems. Based on this, we propose Divergence-Guided Reasoning Curriculum (DGRC), which constructs a learning path from atomic knowledge to reasoning chains by dynamically deriving two complementary curricula from disagreements in reasoning pathways. When a student and teacher produce conflicting results, DGRC directs the teacher to perform a diagnostic analysis: it analyzes both reasoning paths to formulate atomic queries that target the specific points of divergence, and then self-answers these queries to create high-confidence atomic question-answer pairs. These pairs then serve a dual purpose: (1) providing an atomic curriculum to rectify the student's knowledge gaps, and (2) serving as factual criteria to filter the teacher's original reasoning chains, yielding a verified CoT curriculum that teaches the student how to integrate atomic knowledge into complete reasoning paths. Experiments across the medical and legal domains on student models of various sizes demonstrate the effectiveness of our DGRC framework. Notably, our method achieves a 7.76% relative improvement for the 1.5B student model in the medical domain over strong unlabeled baseline.

