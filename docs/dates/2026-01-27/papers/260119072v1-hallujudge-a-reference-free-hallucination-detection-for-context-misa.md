---
layout: default
title: HalluJudge: A Reference-Free Hallucination Detection for Context Misalignment in Code Review Automation
---

# HalluJudge: A Reference-Free Hallucination Detection for Context Misalignment in Code Review Automation
**arXiv**：[2601.19072v1](https://arxiv.org/abs/2601.19072) · [PDF](https://arxiv.org/pdf/2601.19072.pdf)  
**作者**：Kla Tantithamthavorn, Hong Yi Lin, Patanamon Thongtanunam, Wachiraphan Charoenwet, Minwoo Jeong, Ming Wu  

**一句话要点**：提出HalluJudge以无参考方式检测代码审查自动化中的幻觉问题

**关键词**：代码审查自动化, 幻觉检测, 上下文对齐, 无参考评估, LLM生成评论, 成本效益分析

## 3 点简述
- 核心问题：LLM生成的代码审查评论存在幻觉，即评论未基于实际代码，阻碍AI辅助审查的采用。
- 方法要点：设计HalluJudge，通过上下文对齐评估评论的根基性，采用从直接评估到结构化多分支推理的策略。
- 实验或效果：在企业级软件项目中评估，F1分数达0.85，成本平均$0.009，67%评估与开发者偏好对齐。

## 摘要（原文）

> Large Language models (LLMs) have shown strong capabilities in code review automation, such as review comment generation, yet they suffer from hallucinations -- where the generated review comments are ungrounded in the actual code -- poses a significant challenge to the adoption of LLMs in code review workflows. To address this, we explore effective and scalable methods for a hallucination detection in LLM-generated code review comments without the reference. In this work, we design HalluJudge that aims to assess the grounding of generated review comments based on the context alignment. HalluJudge includes four key strategies ranging from direct assessment to structured multi-branch reasoning (e.g., Tree-of-Thoughts). We conduct a comprehensive evaluation of these assessment strategies across Atlassian's enterprise-scale software projects to examine the effectiveness and cost-efficiency of HalluJudge. Furthermore, we analyze the alignment between HalluJudge's judgment and developer preference of the actual LLM-generated code review comments in the real-world production. Our results show that the hallucination assessment in HalluJudge is cost-effective with an F1 score of 0.85 and an average cost of $0.009. On average, 67% of the HalluJudge assessments are aligned with the developer preference of the actual LLM-generated review comments in the online production. Our results suggest that HalluJudge can serve as a practical safeguard to reduce developers' exposure to hallucinated comments, fostering trust in AI-assisted code reviews.

