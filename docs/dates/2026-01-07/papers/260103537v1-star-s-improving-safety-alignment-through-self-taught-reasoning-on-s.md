---
layout: default
title: STAR-S: Improving Safety Alignment through Self-Taught Reasoning on Safety Rules
---

# STAR-S: Improving Safety Alignment through Self-Taught Reasoning on Safety Rules
**arXiv**：[2601.03537v1](https://arxiv.org/abs/2601.03537) · [PDF](https://arxiv.org/pdf/2601.03537.pdf)  
**作者**：Di Wu, Yanyan Zhao, Xin Lu, Mingzhe Li, Bing Qin  

**一句话要点**：提出STAR-S框架，通过自教循环学习安全规则推理以防御大语言模型的越狱攻击。

**关键词**：大语言模型安全, 越狱攻击防御, 安全规则推理, 自教学习, 模型微调

## 3 点简述
- 核心问题：现有方法难以确定有效防御越狱攻击的安全规则推理形式。
- 方法要点：STAR-S集成安全规则引导的推理与反思，通过微调增强推理能力，形成自教循环。
- 实验或效果：实验显示STAR-S在防御越狱攻击上优于基线，代码已开源。

## 摘要（原文）

> Defending against jailbreak attacks is crucial for the safe deployment of Large Language Models (LLMs). Recent research has attempted to improve safety by training models to reason over safety rules before responding. However, a key issue lies in determining what form of safety reasoning effectively defends against jailbreak attacks, which is difficult to explicitly design or directly obtain. To address this, we propose \textbf{STAR-S} (\textbf{S}elf-\textbf{TA}ught \textbf{R}easoning based on \textbf{S}afety rules), a framework that integrates the learning of safety rule reasoning into a self-taught loop. The core of STAR-S involves eliciting reasoning and reflection guided by safety rules, then leveraging fine-tuning to enhance safety reasoning. Repeating this process creates a synergistic cycle. Improvements in the model's reasoning and interpretation of safety rules allow it to produce better reasoning data under safety rule prompts, which is then utilized for further training. Experiments show that STAR-S effectively defends against jailbreak attacks, outperforming baselines. Code is available at: https://github.com/pikepokenew/STAR_S.git.

