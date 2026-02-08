---
layout: default
title: PATHWAYS: Evaluating Investigation and Context Discovery in AI Web Agents
---

# PATHWAYS: Evaluating Investigation and Context Discovery in AI Web Agents
**arXiv**：[2602.05354v1](https://arxiv.org/abs/2602.05354) · [PDF](https://arxiv.org/pdf/2602.05354.pdf)  
**作者**：Shifat E. Arman, Syed Nazmus Sakib, Tapodhir Karmakar Taton, Nafiul Haque, Shahrear Bin Amin  

**一句话要点**：提出PATHWAYS基准以评估AI网络代理在隐藏上下文发现与决策中的能力

**关键词**：网络代理评估, 上下文发现, 多步决策, 基准测试, 证据整合

## 3 点简述
- 核心问题：评估网络代理能否发现并整合隐藏上下文信息以完成多步决策任务
- 方法要点：构建包含250个多步决策任务的基准，测试代理在封闭和开放模型下的表现
- 实验或效果：代理常无法发现关键证据，性能在需要推翻误导信号时降至接近随机水平

## 摘要（原文）

> We introduce PATHWAYS, a benchmark of 250 multi-step decision tasks that test whether web-based agents can discover and correctly use hidden contextual information. Across both closed and open models, agents typically navigate to relevant pages but retrieve decisive hidden evidence in only a small fraction of cases. When tasks require overturning misleading surface-level signals, performance drops sharply to near chance accuracy. Agents frequently hallucinate investigative reasoning by claiming to rely on evidence they never accessed. Even when correct context is discovered, agents often fail to integrate it into their final decision. Providing more explicit instructions improves context discovery but often reduces overall accuracy, revealing a tradeoff between procedural compliance and effective judgement. Together, these results show that current web agent architectures lack reliable mechanisms for adaptive investigation, evidence integration, and judgement override.

