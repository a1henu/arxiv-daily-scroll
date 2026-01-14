---
layout: default
title: Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement
---

# Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement
**arXiv**：[2601.08545v1](https://arxiv.org/abs/2601.08545) · [PDF](https://arxiv.org/pdf/2601.08545.pdf)  
**作者**：Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen  

**一句话要点**：提出学习者定制程序修复框架，通过迭代编辑驱动检索增强解决编程辅导中代码修复与解释不足问题

**关键词**：程序修复, 大语言模型, 检索增强, 编程辅导, 迭代优化

## 3 点简述
- 核心问题：现有编程辅导系统修复错误代码时缺乏对错误原因的深入解释，影响学习者理解
- 方法要点：采用两阶段框架，先通过编辑驱动检索获取修复方案，再引导大语言模型修复代码并提供解释
- 实验或效果：实验显示该方法在LPR任务上显著优于基线，验证了框架的有效性和实用性

## 摘要（原文）

> With the development of large language models (LLMs) in the field of programming, intelligent programming coaching systems have gained widespread attention. However, most research focuses on repairing the buggy code of programming learners without providing the underlying causes of the bugs. To address this gap, we introduce a novel task, namely \textbf{LPR} (\textbf{L}earner-Tailored \textbf{P}rogram \textbf{R}epair). We then propose a novel and effective framework, \textbf{\textsc{\MethodName{}}} (\textbf{L}earner-Tailored \textbf{S}olution \textbf{G}enerator), to enhance program repair while offering the bug descriptions for the buggy code. In the first stage, we utilize a repair solution retrieval framework to construct a solution retrieval database and then employ an edit-driven code retrieval approach to retrieve valuable solutions, guiding LLMs in identifying and fixing the bugs in buggy code. In the second stage, we propose a solution-guided program repair method, which fixes the code and provides explanations under the guidance of retrieval solutions. Moreover, we propose an Iterative Retrieval Enhancement method that utilizes evaluation results of the generated code to iteratively optimize the retrieval direction and explore more suitable repair strategies, improving performance in practical programming coaching scenarios. The experimental results show that our approach outperforms a set of baselines by a large margin, validating the effectiveness of our framework for the newly proposed LPR task.

