---
layout: default
title: LLM Prompt Evaluation for Educational Applications
---

# LLM Prompt Evaluation for Educational Applications
**arXiv**：[2601.16134v1](https://arxiv.org/abs/2601.16134) · [PDF](https://arxiv.org/pdf/2601.16134.pdf)  
**作者**：Langdon Holmes, Adam Coscia, Scott Crossley, Joon Suh Choi, Wesley Morris  

**一句话要点**：提出基于锦标赛评估框架的系统化方法，以优化教育应用中大语言模型提示设计。

**关键词**：大语言模型提示评估, 教育技术, 锦标赛评估框架, Glicko2评级系统, 教学策略, 个性化学习

## 3 点简述
- 核心问题：教育应用中大语言模型提示缺乏基于证据的设计与评估方法，影响个性化与教学对齐输出。
- 方法要点：设计六种强调不同教学策略的提示模板，采用Glicko2评级系统进行锦标赛式多维度评估。
- 实验或效果：在真实用户交互数据中，结合角色与上下文管理模式的提示在成对比较中胜率高达81%-100%。

## 摘要（原文）

> As large language models (LLMs) become increasingly common in educational applications, there is a growing need for evidence-based methods to design and evaluate LLM prompts that produce personalized and pedagogically aligned out-puts. This study presents a generalizable, systematic approach for evaluating prompts, demonstrated through an analysis of LLM-generated follow-up questions in a structured dialogue activity. Six prompt templates were designed and tested. The templates incorporated established prompt engineering patterns, with each prompt emphasizing distinct pedagogical strategies. The prompt templates were compared through a tournament-style evaluation framework that can be adapted for other educational applications. The tournament employed the Glicko2 rating system with eight judges evaluating question pairs across three dimensions: format, dialogue support, and appropriateness for learners. Data was sourced from 120 authentic user interactions across three distinct educational deployments. Results showed that a single prompt related to strategic reading out-performed other templates with win probabilities ranging from 81% to 100% in pairwise comparisons. This prompt combined persona and context manager pat-terns and was designed to support metacognitive learning strategies such as self-directed learning. The methodology showcases how educational technology re- searchers can systematically evaluate and improve prompt designs, moving beyond ad-hoc prompt engineering toward evidence-based prompt development for educational applications.

