---
layout: default
title: Modeling LLM Agent Reviewer Dynamics in Elo-Ranked Review System
---

# Modeling LLM Agent Reviewer Dynamics in Elo-Ranked Review System
**arXiv**：[2601.08829v1](https://arxiv.org/abs/2601.08829) · [PDF](https://arxiv.org/pdf/2601.08829.pdf)  
**作者**：Hsiang-Wei Huang, Junbin Lu, Kuang-Ming Chen, Jenq-Neng Hwang  

**一句话要点**：提出基于Elo排名的LLM代理审稿人动态模型，以提升会议审稿决策准确性。

**关键词**：LLM代理审稿人, Elo排名系统, 多轮审稿交互, 会议审稿模拟, 自适应策略

## 3 点简述
- 研究LLM代理审稿人在多轮审稿中的动态行为，模拟真实会议审稿场景。
- 引入Elo评分和审稿人记忆机制，对比基线设置分析其对决策的影响。
- 实验显示Elo评分提高主席决策准确性，审稿人策略自适应但未增加审稿努力。

## 摘要（原文）

> In this work, we explore the Large Language Model (LLM) agent reviewer dynamics in an Elo-ranked review system using real-world conference paper submissions. Multiple LLM agent reviewers with different personas are engage in multi round review interactions moderated by an Area Chair. We compare a baseline setting with conditions that incorporate Elo ratings and reviewer memory. Our simulation results showcase several interesting findings, including how incorporating Elo improves Area Chair decision accuracy, as well as reviewers' adaptive review strategy that exploits our Elo system without improving review effort. Our code is available at https://github.com/hsiangwei0903/EloReview.

