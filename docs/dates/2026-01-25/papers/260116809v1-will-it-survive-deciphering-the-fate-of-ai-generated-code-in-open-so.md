---
layout: default
title: Will It Survive? Deciphering the Fate of AI-Generated Code in Open Source
---

# Will It Survive? Deciphering the Fate of AI-Generated Code in Open Source
**arXiv**：[2601.16809v1](https://arxiv.org/abs/2601.16809) · [PDF](https://arxiv.org/pdf/2601.16809.pdf)  
**作者**：Musfiqur Rahman, Emad Shihab  

**一句话要点**：通过生存分析揭示AI生成代码在开源项目中比人类代码更持久，挑战了其‘一次性’假设。

**关键词**：生存分析, AI生成代码, 开源软件, 代码维护, 修改预测

## 3 点简述
- 核心问题：AI助手生成的代码是否如假设般‘一次性’，影响软件维护负担。
- 方法要点：对201个开源项目进行生存分析，比较AI与人类代码的修改率和生存时间。
- 实验或效果：AI代码修改率低15.8%，生存时间更长，但修改类型略有差异，预测修改时机仍具挑战。

## 摘要（原文）

> The integration of AI agents as coding assistants into software development has raised questions about the long-term viability of AI agent-generated code. A prevailing hypothesis within the software engineering community suggests this code is "disposable", meaning it is merged quickly but discarded shortly thereafter. If true, organizations risk shifting maintenance burden from generation to post-deployment remediation. We investigate this hypothesis through survival analysis of 201 open-source projects, tracking over 200,000 code units authored by AI agents versus humans. Contrary to the disposable code narrative, agent-authored code survives significantly longer: at the line level, it exhibits a 15.8 percentage-point lower modification rate and 16% lower hazard of modification (HR = 0.842, p < 0.001). However, modification profiles differ. Agent-authored code shows modestly elevated corrective rates (26.3% vs. 23.0%), while human code shows higher adaptive rates. However, the effect sizes are small (Cramér's V = 0.116), and per-agent variation exceeds the agent-human gap. Turning to prediction, textual features can identify modification-prone code (AUC-ROC = 0.671), but predicting when modifications occur remains challenging (Macro F1 = 0.285), suggesting timing depends on external organizational dynamics. The bottleneck for agent-generated code may not be generation quality, but the organizational practices that govern its long-term evolution.

