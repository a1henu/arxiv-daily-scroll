---
layout: default
title: GUITester: Enabling GUI Agents for Exploratory Defect Discovery
---

# GUITester: Enabling GUI Agents for Exploratory Defect Discovery
**arXiv**：[2601.04500v1](https://arxiv.org/abs/2601.04500) · [PDF](https://arxiv.org/pdf/2601.04500.pdf)  
**作者**：Yifei Gao, Jiang Wu, Xiaoyi Chen, Yifan Yang, Zhe Cui, Tianyi Ma, Jiaming Zhang, Jitao Sang  

**一句话要点**：提出GUITester框架以解决GUI探索性测试中多模态大语言模型代理的缺陷发现难题

**关键词**：GUI测试, 多模态大语言模型, 探索性缺陷发现, 多代理框架, 交互基准

## 3 点简述
- 核心问题：多模态大语言模型代理在GUI测试中因目标导向掩蔽和执行偏差归因而无法自主发现缺陷
- 方法要点：通过规划执行模块主动探测缺陷，结合分层反思模块分析交互历史以解决归因模糊性
- 实验或效果：在GUITestBench基准上达到48.90% F1分数，优于现有基线33.35%

## 摘要（原文）

> Exploratory GUI testing is essential for software quality but suffers from high manual costs. While Multi-modal Large Language Model (MLLM) agents excel in navigation, they fail to autonomously discover defects due to two core challenges: \textit{Goal-Oriented Masking}, where agents prioritize task completion over reporting anomalies, and \textit{Execution-Bias Attribution}, where system defects are misidentified as agent errors. To address these, we first introduce \textbf{GUITestBench}, the first interactive benchmark for this task, featuring 143 tasks across 26 defects. We then propose \textbf{GUITester}, a multi-agent framework that decouples navigation from verification via two modules: (i) a \textit{Planning-Execution Module (PEM)} that proactively probes for defects via embedded testing intents, and (ii) a \textit{Hierarchical Reflection Module (HRM)} that resolves attribution ambiguity through interaction history analysis. GUITester achieves an F1-score of 48.90\% (Pass@3) on GUITestBench, outperforming state-of-the-art baselines (33.35\%). Our work demonstrates the feasibility of autonomous exploratory testing and provides a robust foundation for future GUI quality assurance~\footnote{Our code is now available in~\href{https://github.com/ADaM-BJTU/GUITestBench}{https://github.com/ADaM-BJTU/GUITestBench}}.

