---
layout: default
title: Paper2Rebuttal: A Multi-Agent Framework for Transparent Author Response Assistance
---

# Paper2Rebuttal: A Multi-Agent Framework for Transparent Author Response Assistance
**arXiv**：[2601.14171v1](https://arxiv.org/abs/2601.14171) · [PDF](https://arxiv.org/pdf/2601.14171.pdf)  
**作者**：Qianli Ma, Chang Guo, Zhiheng Tian, Siyu Wang, Jipeng Xiao, Yuanhao Yue, Zhipeng Zhang  

**一句话要点**：提出多智能体框架RebuttalAgent，通过证据中心规划解决审稿回复生成中的幻觉和缺乏可验证基础问题。

**关键词**：多智能体框架, 审稿回复生成, 证据中心规划, 外部搜索模块, 可验证基础, 透明助手

## 3 点简述
- 核心问题：现有审稿回复生成方法存在幻觉、忽略批评和缺乏可验证基础，需精确对齐审稿人意图与稿件细节。
- 方法要点：引入多智能体框架，将回复生成重构为证据中心规划任务，分解反馈为原子关注点并动态构建混合上下文，集成外部搜索模块。
- 实验或效果：在RebuttalBench上验证，在覆盖率、忠实度和策略连贯性上优于基线，提供透明可控的审稿过程助手。

## 摘要（原文）

> Writing effective rebuttals is a high-stakes task that demands more than linguistic fluency, as it requires precise alignment between reviewer intent and manuscript details. Current solutions typically treat this as a direct-to-text generation problem, suffering from hallucination, overlooked critiques, and a lack of verifiable grounding. To address these limitations, we introduce $\textbf{RebuttalAgent}$, the first multi-agents framework that reframes rebuttal generation as an evidence-centric planning task. Our system decomposes complex feedback into atomic concerns and dynamically constructs hybrid contexts by synthesizing compressed summaries with high-fidelity text while integrating an autonomous and on-demand external search module to resolve concerns requiring outside literature. By generating an inspectable response plan before drafting, $\textbf{RebuttalAgent}$ ensures that every argument is explicitly anchored in internal or external evidence. We validate our approach on the proposed $\textbf{RebuttalBench}$ and demonstrate that our pipeline outperforms strong baselines in coverage, faithfulness, and strategic coherence, offering a transparent and controllable assistant for the peer review process. Code will be released.

