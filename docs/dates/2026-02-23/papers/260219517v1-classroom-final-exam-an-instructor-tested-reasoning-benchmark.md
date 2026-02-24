---
layout: default
title: Classroom Final Exam: An Instructor-Tested Reasoning Benchmark
---

# Classroom Final Exam: An Instructor-Tested Reasoning Benchmark
**arXiv**：[2602.19517v1](https://arxiv.org/abs/2602.19517) · [PDF](https://arxiv.org/pdf/2602.19517.pdf)  
**作者**：Chongyang Gao, Diji Yang, Shuyan Zhou, Xichen Yan, Luchuan Song, Shuo Li, Kezhen Chen  

**一句话要点**：提出CFE基准以评估大语言模型在STEM领域的多模态推理能力

**关键词**：多模态基准, STEM推理, 大语言模型评估, 诊断分析, 参考解决方案

## 3 点简述
- 核心问题：大语言模型在复杂多步推理任务中表现不足，需可靠基准评估
- 方法要点：基于真实大学作业和考试问题构建多模态基准，包含参考解决方案
- 实验或效果：前沿模型如Gemini-3.1-pro-preview准确率仅59.69%，诊断分析揭示中间状态维护困难

## 摘要（原文）

> We introduce \CFE{} (\textbf{C}lassroom \textbf{F}inal \textbf{E}xam), a multimodal benchmark for evaluating the reasoning capabilities of large language models across more than 20 STEM domains. \CFE{} is curated from repeatedly used, authentic university homework and exam problems, together with reference solutions provided by course instructors. \CFE{} presents a significant challenge even for frontier models: the newly released Gemini-3.1-pro-preview achieves an overall accuracy of 59.69\%, while the second-best model, Gemini-3-flash-preview, reaches 55.46\%, leaving considerable room for improvement. Beyond leaderboard results, we perform a diagnostic analysis by decomposing reference solutions into reasoning flows. We find that although frontier models can often answer intermediate sub-questions correctly, they struggle to reliably derive and maintain correct intermediate states throughout multi-step solutions. We further observe that model-generated solutions typically have more reasoning steps than those provided by the instructor, indicating suboptimal step efficiency and a higher risk of error accumulation. The data and code are available at https://github.com/Analogy-AI/CFE_Bench.

