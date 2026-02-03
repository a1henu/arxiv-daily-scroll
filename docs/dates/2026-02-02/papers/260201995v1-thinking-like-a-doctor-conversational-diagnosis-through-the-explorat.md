---
layout: default
title: Thinking Like a Doctor: Conversational Diagnosis through the Exploration of Diagnostic Knowledge Graphs
---

# Thinking Like a Doctor: Conversational Diagnosis through the Exploration of Diagnostic Knowledge Graphs
**arXiv**：[2602.01995v1](https://arxiv.org/abs/2602.01995) · [PDF](https://arxiv.org/pdf/2602.01995.pdf)  
**作者**：Jeongmoon Won, Seungwon Kook, Yohan Jo  

**一句话要点**：提出基于诊断知识图谱的对话诊断系统，通过假设生成与验证提升诊断准确性和效率。

**关键词**：对话诊断, 知识图谱, 假设生成, 患者模拟器, 临床推理

## 3 点简述
- 核心问题：现有对话诊断方法依赖模型参数知识或假设患者提供丰富信息，不切实际。
- 方法要点：系统探索诊断知识图谱，分两步推理：生成诊断假设并验证，通过澄清问题迭代优化。
- 实验或效果：使用MIMIC-IV患者模拟器评估，显示诊断准确性和效率优于基线，医生评估支持临床实用性。

## 摘要（原文）

> Conversational diagnosis requires multi-turn history-taking, where an agent asks clarifying questions to refine differential diagnoses under incomplete information. Existing approaches often rely on the parametric knowledge of a model or assume that patients provide rich and concrete information, which is unrealistic. To address these limitations, we propose a conversational diagnosis system that explores a diagnostic knowledge graph to reason in two steps: (i) generating diagnostic hypotheses from the dialogue context, and (ii) verifying hypotheses through clarifying questions, which are repeated until a final diagnosis is reached. Since evaluating the system requires a realistic patient simulator that responds to the system's questions, we adopt a well-established simulator along with patient profiles from MIMIC-IV. We further adapt it to describe symptoms vaguely to reflect real-world patients during early clinical encounters. Experiments show improved diagnostic accuracy and efficiency over strong baselines, and evaluations by physicians support the realism of our simulator and the clinical utility of the generated questions. Our code will be released upon publication.

