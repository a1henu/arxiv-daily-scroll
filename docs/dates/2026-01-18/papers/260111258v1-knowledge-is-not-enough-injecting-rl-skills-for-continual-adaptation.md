---
layout: default
title: Knowledge is Not Enough: Injecting RL Skills for Continual Adaptation
---

# Knowledge is Not Enough: Injecting RL Skills for Continual Adaptation
**arXiv**：[2601.11258v1](https://arxiv.org/abs/2601.11258) · [PDF](https://arxiv.org/pdf/2601.11258.pdf)  
**作者**：Pingzhi Tang, Yiding Wang, Muhan Zhang  

**一句话要点**：提出参数化技能转移框架以解决大语言模型知识更新中技能缺失问题

**关键词**：大语言模型, 知识更新, 技能转移, 监督微调, 强化学习, 问答系统

## 3 点简述
- 大语言模型面临知识截止挑战，监督微调更新知识但难以提升推理技能
- 基于监督微调与强化学习参数更新正交性，提取领域无关技能向量进行线性注入
- 在问答和工具使用基准测试中显著提升性能，展示技能向量的可扩展性和跨域迁移性

## 摘要（原文）

> Large Language Models (LLMs) face the "knowledge cutoff" challenge, where their frozen parametric memory prevents direct internalization of new information. While Supervised Fine-Tuning (SFT) is commonly used to update model knowledge, it often updates factual content without reliably improving the model's ability to use the newly incorporated information for question answering or decision-making. Reinforcement Learning (RL) is essential for acquiring reasoning skills; however, its high computational cost makes it impractical for efficient online adaptation. We empirically observe that the parameter updates induced by SFT and RL are nearly orthogonal. Based on this observation, we propose Parametric Skill Transfer (PaST), a framework that supports modular skill transfer for efficient and effective knowledge adaptation. By extracting a domain-agnostic Skill Vector from a source domain, we can linearly inject knowledge manipulation skills into a target model after it has undergone lightweight SFT on new data. Experiments on knowledge-incorporation QA (SQuAD, LooGLE) and agentic tool-use benchmarks (ToolBench) demonstrate the effectiveness of our method. On SQuAD, PaST outperforms the state-of-the-art self-editing SFT baseline by up to 9.9 points. PaST further scales to long-context QA on LooGLE with an 8.0-point absolute accuracy gain, and improves zero-shot ToolBench success rates by +10.3 points on average with consistent gains across tool categories, indicating strong scalability and cross-domain transferability of the Skill Vector.

