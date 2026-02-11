---
layout: default
title: Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?
---

# Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?
**arXiv**：[2602.09937v1](https://arxiv.org/abs/2602.09937) · [PDF](https://arxiv.org/pdf/2602.09937.pdf)  
**作者**：Taeyoon Kim, Woohyeok Park, Hoyeong Yun, Kyungyong Lee  

**一句话要点**：提出基于LLM的云根因分析代理过程级失败分类与诊断方法，揭示架构性缺陷。

**关键词**：云根因分析, LLM代理, 失败分类, 过程级诊断, 通信协议优化

## 3 点简述
- 核心问题：LLM代理在云根因分析中准确率低，现有评估仅关注答案正确性，缺乏过程失败分析。
- 方法要点：在OpenRCA基准上执行1,675次代理运行，将失败分类为12种陷阱类型，涵盖推理、通信和交互。
- 实验或效果：发现幻觉数据解释和不完全探索等陷阱普遍存在，提示工程无法解决，增强通信协议可减少15%通信失败。

## 摘要（原文）

> Failures in large-scale cloud systems incur substantial financial losses, making automated Root Cause Analysis (RCA) essential for operational stability. Recent efforts leverage Large Language Model (LLM) agents to automate this task, yet existing systems exhibit low detection accuracy even with capable models, and current evaluation frameworks assess only final answer correctness without revealing why the agent's reasoning failed. This paper presents a process level failure analysis of LLM-based RCA agents. We execute the full OpenRCA benchmark across five LLM models, producing 1,675 agent runs, and classify observed failures into 12 pitfall types across intra-agent reasoning, inter-agent communication, and agent-environment interaction. Our analysis reveals that the most prevalent pitfalls, notably hallucinated data interpretation and incomplete exploration, persist across all models regardless of capability tier, indicating that these failures originate from the shared agent architecture rather than from individual model limitations. Controlled mitigation experiments further show that prompt engineering alone cannot resolve the dominant pitfalls, whereas enriching the inter-agent communication protocol reduces communication-related failures by up to 15 percentage points. The pitfall taxonomy and diagnostic methodology developed in this work provide a foundation for designing more reliable autonomous agents for cloud RCA.

