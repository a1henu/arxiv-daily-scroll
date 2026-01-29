---
layout: default
title: Deep Researcher with Sequential Plan Reflection and Candidates Crossover (Deep Researcher Reflect Evolve)
---

# Deep Researcher with Sequential Plan Reflection and Candidates Crossover (Deep Researcher Reflect Evolve)
**arXiv**：[2601.20843v1](https://arxiv.org/abs/2601.20843) · [PDF](https://arxiv.org/pdf/2601.20843.pdf)  
**作者**：Saurav Prateek  

**一句话要点**：提出Deep Researcher架构，通过顺序计划反思和候选交叉算法，解决并行扩展范式在复杂博士级研究任务中的局限性。

**关键词**：深度研究架构, 顺序计划反思, 候选交叉算法, 研究任务基准, 博士级主题, Gemini 2.5 Pro模型

## 3 点简述
- 核心问题：并行扩展范式在生成详细研究报告中存在知识孤岛和效率低下问题。
- 方法要点：采用顺序研究计划反思以维护全局研究上下文，结合候选交叉算法探索更大搜索空间。
- 实验或效果：在DeepResearch Bench基准测试中得分46.21，超越多个领先研究代理，验证顺序扩展优于并行自一致性范式。

## 摘要（原文）

> This paper introduces a novel Deep Researcher architecture designed to generate detailed research reports on complex PhD level topics by addressing the inherent limitations of the Parallel Scaling paradigm. Our system utilizes two key innovations: Sequential Research Plan Refinement via Reflection and a Candidates Crossover algorithm. The sequential refinement process is demonstrated as an efficient method that allows the agent to maintain a centralized Global Research Context, enabling it to look back at current progress, reason about the research plan, and intelligently make changes at runtime. This dynamic adaptation contrasts with parallel approaches, which often suffer from siloed knowledge. The Candidates Crossover algorithm further enhances search efficiency by deploying multiple LLM candidates with varied parameters to explore a larger search space, with their findings synthesized to curate a comprehensive final research response. The process concludes with One Shot Report Generation, ensuring the final document is informed by a unified narrative and high fact density. Powered by the Gemini 2.5 Pro model, our Deep Researcher was evaluated on the DeepResearch Bench, a globally recognized benchmark of 100 doctoral level research tasks. Our architecture achieved an overall score of 46.21, demonstrating superior performance by surpassing leading deep research agents such as Claude Researcher, Nvidia AIQ Research Assistant, Perplexity Research, Kimi Researcher and Grok Deeper Search present on the DeepResearch Bench actively running leaderboard. This performance marginally exceeds our previous work, Static DRA, and reinforces the finding that sequential scaling consistently outperforms the parallel self consistency paradigm.

