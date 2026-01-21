---
layout: default
title: APEX-Agents
---

# APEX-Agents
**arXiv**：[2601.14242v1](https://arxiv.org/abs/2601.14242) · [PDF](https://arxiv.org/pdf/2601.14242.pdf)  
**作者**：Bertie Vidgen, Austin Mann, Abby Fennelly, John Wright Stanly, Lucas Rothman, Marco Burstein, Julien Benchek, David Ostrofsky, Anirudh Ravichandran, Debnil Sur, Neel Venugopal, Alannah Hsia, Isaac Robinson, Calix Huang, Olivia Varones, Daniyal Khan, Michael Haines, Zach Richards, Chirag Mahapatra, Brendan Foody, Osvald Nitski  

**一句话要点**：提出APEX-Agents基准以评估AI代理在投资银行、咨询和法律领域的跨应用长程任务执行能力。

**关键词**：AI代理基准, 长程任务评估, 跨应用任务, 投资银行分析, 开源基础设施, Pass@1测试

## 3 点简述
- 核心问题：评估AI代理在真实工作环境中执行长程、跨应用任务的能力，涉及文件与工具操作。
- 方法要点：开源APEX-Agents基准（n=480），包含提示、评分标准、黄金输出、文件和元数据，并开源Archipelago基础设施用于代理执行与评估。
- 实验或效果：使用Pass@1测试八个代理，Gemini 3 Flash（Thinking=High）以24.0%得分最高，其次是GPT-5.2、Claude Opus 4.5和Gemini 3 Pro（均开启高级思考模式）。

## 摘要（原文）

> We introduce the AI Productivity Index for Agents (APEX-Agents), a benchmark for assessing whether AI agents can execute long-horizon, cross-application tasks created by investment banking analysts, management consultants, and corporate lawyers. APEX-Agents requires agents to navigate realistic work environments with files and tools. We test eight agents for the leaderboard using Pass@1. Gemini 3 Flash (Thinking=High) achieves the highest score of 24.0%, followed by GPT-5.2 (Thinking=High), Claude Opus 4.5 (Thinking=High), and Gemini 3 Pro (Thinking=High). We open source the APEX-Agents benchmark (n=480) with all prompts, rubrics, gold outputs, files, and metadata. We also open-source Archipelago, our infrastructure for agent execution and evaluation.

