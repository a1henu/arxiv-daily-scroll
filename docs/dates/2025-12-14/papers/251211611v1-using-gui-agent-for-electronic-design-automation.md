---
layout: default
title: Using GUI Agent for Electronic Design Automation
---

# Using GUI Agent for Electronic Design Automation
**arXiv**：[2512.11611v1](https://arxiv.org/abs/2512.11611) · [PDF](https://arxiv.org/pdf/2512.11611.pdf)  
**作者**：Chunyi Li, Longfei Li, Zicheng Zhang, Xiaohong Liu, Min Tang, Weisi Lin, Guangtao Zhai  

**一句话要点**：提出GUI-EDA数据集与EDAgent方法，将GUI代理应用于电子设计自动化以提升工程效率。

**关键词**：GUI代理, 电子设计自动化, CAD软件, 数据集构建, 自动化评估, 工程应用

## 3 点简述
- 现有GUI代理在专业CAD软件中性能不足，无法替代EDA工程师。
- 构建大规模GUI-EDA数据集，包含5种CAD工具和2000+真实截图-动作对。
- EDAgent方法在工业CAD软件中首次超越电气工程博士生，解决EDA任务挑战。

## 摘要（原文）

> Graphical User Interface (GUI) agents adopt an end-to-end paradigm that maps a screenshot to an action sequence, thereby automating repetitive tasks in virtual environments. However, existing GUI agents are evaluated almost exclusively on commodity software such as Microsoft Word and Excel. Professional Computer-Aided Design (CAD) suites promise an order-of-magnitude higher economic return, yet remain the weakest performance domain for existing agents and are still far from replacing expert Electronic-Design-Automation (EDA) engineers. We therefore present the first systematic study that deploys GUI agents for EDA workflows. Our contributions are: (1) a large-scale dataset named GUI-EDA, including 5 CAD tools and 5 physical domains, comprising 2,000+ high-quality screenshot-answer-action pairs recorded by EDA scientists and engineers during real-world component design; (2) a comprehensive benchmark that evaluates 30+ mainstream GUI agents, demonstrating that EDA tasks constitute a major, unsolved challenge; and (3) an EDA-specialized metric named EDAgent, equipped with a reflection mechanism that achieves reliable performance on industrial CAD software and, for the first time, outperforms Ph.D. students majored in Electrical Engineering. This work extends GUI agents from generic office automation to specialized, high-value engineering domains and offers a new avenue for advancing EDA productivity. The dataset will be released at: https://github.com/aiben-ch/GUI-EDA.

