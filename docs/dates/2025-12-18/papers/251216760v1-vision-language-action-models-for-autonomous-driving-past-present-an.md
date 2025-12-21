---
layout: default
title: Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future
---

# Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future
**arXiv**：[2512.16760v1](https://arxiv.org/abs/2512.16760) · [PDF](https://arxiv.org/pdf/2512.16760.pdf)  
**作者**：Tianshuai Hu, Xiaolu Liu, Song Wang, Yiyao Zhu, Ao Liang, Lingdong Kong, Guoyang Zhao, Zeying Gong, Jun Cen, Zhiyu Huang, Xiaoshuai Hao, Linfeng Li, Hang Song, Xiangtai Li, Jun Ma, Shaojie Shen, Jianke Zhu, Dacheng Tao, Ziwei Liu, Junwei Liang  

**一句话要点**：综述自动驾驶中视觉-语言-动作模型的演进、范式与挑战，以提升可解释性和泛化性。

**关键词**：自动驾驶, 视觉-语言-动作模型, 端到端学习, 多模态学习, 可解释性, 泛化性

## 3 点简述
- 核心问题：模块化感知-决策-动作流水线在复杂场景中易失效，且感知误差会级联传播。
- 方法要点：提出视觉-语言-动作框架，整合视觉理解、语言推理和动作输出，分为端到端和双系统范式。
- 实验或效果：总结代表性数据集和基准，强调鲁棒性、可解释性和指令保真度等关键挑战。

## 摘要（原文）

> Autonomous driving has long relied on modular "Perception-Decision-Action" pipelines, where hand-crafted interfaces and rule-based components often break down in complex or long-tailed scenarios. Their cascaded design further propagates perception errors, degrading downstream planning and control. Vision-Action (VA) models address some limitations by learning direct mappings from visual inputs to actions, but they remain opaque, sensitive to distribution shifts, and lack structured reasoning or instruction-following capabilities. Recent progress in Large Language Models (LLMs) and multimodal learning has motivated the emergence of Vision-Language-Action (VLA) frameworks, which integrate perception with language-grounded decision making. By unifying visual understanding, linguistic reasoning, and actionable outputs, VLAs offer a pathway toward more interpretable, generalizable, and human-aligned driving policies. This work provides a structured characterization of the emerging VLA landscape for autonomous driving. We trace the evolution from early VA approaches to modern VLA frameworks and organize existing methods into two principal paradigms: End-to-End VLA, which integrates perception, reasoning, and planning within a single model, and Dual-System VLA, which separates slow deliberation (via VLMs) from fast, safety-critical execution (via planners). Within these paradigms, we further distinguish subclasses such as textual vs. numerical action generators and explicit vs. implicit guidance mechanisms. We also summarize representative datasets and benchmarks for evaluating VLA-based driving systems and highlight key challenges and open directions, including robustness, interpretability, and instruction fidelity. Overall, this work aims to establish a coherent foundation for advancing human-compatible autonomous driving systems.

