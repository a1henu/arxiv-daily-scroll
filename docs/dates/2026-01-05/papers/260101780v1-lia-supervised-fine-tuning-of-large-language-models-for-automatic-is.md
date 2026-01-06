---
layout: default
title: LIA: Supervised Fine-Tuning of Large Language Models for Automatic Issue Assignment
---

# LIA: Supervised Fine-Tuning of Large Language Models for Automatic Issue Assignment
**arXiv**：[2601.01780v1](https://arxiv.org/abs/2601.01780) · [PDF](https://arxiv.org/pdf/2601.01780.pdf)  
**作者**：Arsham Khosravani, Alireza Hosseinpour, Arshia Akhavan, Mehdi Keshani, Abbas Heydarnoori  

**一句话要点**：提出LIA方法，通过监督微调大语言模型实现软件问题自动分配

**关键词**：问题自动分配, 大语言模型微调, 软件维护, 开发者推荐, 排名学习

## 3 点简述
- 核心问题：软件维护中手动问题分配不一致且易错，现有方法依赖大量项目特定数据或稀疏关系信息。
- 方法要点：基于DeepSeek-R1-Distill-Llama-8B模型，利用其预训练语义理解，从问题标题和描述生成开发者排名推荐。
- 实验或效果：相比基础模型和先进基线，LIA在Hit@1指标上提升高达+187.8%和+211.2%。

## 摘要（原文）

> Issue assignment is a critical process in software maintenance, where new issue reports are validated and assigned to suitable developers. However, manual issue assignment is often inconsistent and error-prone, especially in large open-source projects where thousands of new issues are reported monthly. Existing automated approaches have shown promise, but many rely heavily on large volumes of project-specific training data or relational information that is often sparse and noisy, which limits their effectiveness. To address these challenges, we propose LIA (LLM-based Issue Assignment), which employs supervised fine-tuning to adapt an LLM, DeepSeek-R1-Distill-Llama-8B in this work, for automatic issue assignment. By leveraging the LLM's pretrained semantic understanding of natural language and software-related text, LIA learns to generate ranked developer recommendations directly from issue titles and descriptions. The ranking is based on the model's learned understanding of historical issue-to-developer assignments, using patterns from past tasks to infer which developers are most likely to handle new issues. Through comprehensive evaluation, we show that LIA delivers substantial improvements over both its base pretrained model and state-of-the-art baselines. It achieves up to +187.8% higher Hit@1 compared to the DeepSeek-R1-Distill-Llama-8B pretrained base model, and outperforms four leading issue assignment methods by as much as +211.2% in Hit@1 score. These results highlight the effectiveness of domain-adapted LLMs for software maintenance tasks and establish LIA as a practical, high-performing solution for issue assignment.

