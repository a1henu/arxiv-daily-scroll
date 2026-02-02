---
layout: default
title: Structured Over Scale: Learning Spatial Reasoning from Educational Video
---

# Structured Over Scale: Learning Spatial Reasoning from Educational Video
**arXiv**：[2601.23251v1](https://arxiv.org/abs/2601.23251) · [PDF](https://arxiv.org/pdf/2601.23251.pdf)  
**作者**：Bishoy Galoaa, Xiangyu Bai, Sarah Ostadabbas  

**一句话要点**：提出DoraVQA数据集与GRPO微调方法，利用教育视频结构化内容提升视觉语言模型的空间推理能力。

**关键词**：视觉语言模型, 空间推理, 教育视频, 数据集构建, 强化学习微调, 多模态理解

## 3 点简述
- 核心问题：视觉语言模型在简单推理任务（如计数、空间推理）上表现不佳，落后于学龄前儿童水平。
- 方法要点：从《爱探险的朵拉》自动提取DoraVQA数据集，采用Group Relative Policy Optimization微调Qwen模型。
- 实验或效果：在DoraVQA上提升8-14点，CVBench达到86.16%，并有效泛化至Video-MME和NExT-QA。

## 摘要（原文）

> Vision-language models (VLMs) demonstrate impressive performance on standard video understanding benchmarks yet fail systematically on simple reasoning tasks that preschool children can solve, including counting, spatial reasoning, and compositional understanding. We hypothesize that the pedagogically-structured content of educational videos provides an ideal training signal for improving these capabilities. We introduce DoraVQA, a dataset of 5,344 question-answer pairs automatically extracted from 8 seasons of Dora the Explorer with precise timestamp alignment. Each episode follows a consistent \textit{context-question-pause-answer} structure that creates a self-contained learning environment analogous to interactive tutoring. We fine-tune both Qwen2 and Qwen3 using Group Relative Policy Optimization (GRPO), leveraging the clear correctness signals and structured reasoning traces inherent in educational content. Despite training exclusively on 38 hours of children's educational videos, our approach achieves improvements of 8-14 points on DoraVQA and state-of-the-art 86.16\% on CVBench, with strong transfer to Video-MME and NExT-QA, demonstrating effective generalization from narrow pedagogical content to broad multimodal understanding. Through cross-domain benchmarks, we show that VLMs can perform tasks that require robust reasoning learned from structured educational content, suggesting that content structure matters as much as content scale.

