---
layout: default
title: Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future
---

# Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future
**arXiv**：[2512.16760v1](https://arxiv.org/abs/2512.16760) · [PDF](https://arxiv.org/pdf/2512.16760.pdf)  
**作者**：Tianshuai Hu, Xiaolu Liu, Song Wang, Yiyao Zhu, Ao Liang, Lingdong Kong, Guoyang Zhao, Zeying Gong, Jun Cen, Zhiyu Huang, Xiaoshuai Hao, Linfeng Li, Hang Song, Xiangtai Li, Jun Ma, Shaojie Shen, Jianke Zhu, Dacheng Tao, Ziwei Liu, Junwei Liang  

**一句话要点**：综述自动驾驶中视觉-语言-动作模型的发展，提出分类框架以促进人机兼容系统。

**关键词**：自动驾驶, 视觉-语言-动作模型, 端到端学习, 双系统架构, 可解释性, 基准评估

## 3 点简述
- 核心问题：传统模块化驾驶系统在复杂场景中易失效，感知错误会级联影响规划与控制。
- 方法要点：将现有方法分为端到端VLA和双系统VLA，并细分为文本/数值动作生成和显式/隐式指导机制。
- 实验或效果：总结代表性数据集与基准，强调鲁棒性、可解释性和指令忠实度等关键挑战。

## 摘要（原文）

> Autonomous driving has long relied on modular "Perception-Decision-Action" pipelines, where hand-crafted interfaces and rule-based components often break down in complex or long-tailed scenarios. Their cascaded design further propagates perception errors, degrading downstream planning and control. Vision-Action (VA) models address some limitations by learning direct mappings from visual inputs to actions, but they remain opaque, sensitive to distribution shifts, and lack structured reasoning or instruction-following capabilities. Recent progress in Large Language Models (LLMs) and multimodal learning has motivated the emergence of Vision-Language-Action (VLA) frameworks, which integrate perception with language-grounded decision making. By unifying visual understanding, linguistic reasoning, and actionable outputs, VLAs offer a pathway toward more interpretable, generalizable, and human-aligned driving policies. This work provides a structured characterization of the emerging VLA landscape for autonomous driving. We trace the evolution from early VA approaches to modern VLA frameworks and organize existing methods into two principal paradigms: End-to-End VLA, which integrates perception, reasoning, and planning within a single model, and Dual-System VLA, which separates slow deliberation (via VLMs) from fast, safety-critical execution (via planners). Within these paradigms, we further distinguish subclasses such as textual vs. numerical action generators and explicit vs. implicit guidance mechanisms. We also summarize representative datasets and benchmarks for evaluating VLA-based driving systems and highlight key challenges and open directions, including robustness, interpretability, and instruction fidelity. Overall, this work aims to establish a coherent foundation for advancing human-compatible autonomous driving systems.

