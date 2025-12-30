---
layout: default
title: Eliciting Behaviors in Multi-Turn Conversations
---

# Eliciting Behaviors in Multi-Turn Conversations
**arXiv**：[2512.23701v1](https://arxiv.org/abs/2512.23701) · [PDF](https://arxiv.org/pdf/2512.23701.pdf)  
**作者**：Jing Huang, Shujian Zhang, Lun Wang, Andrew Hard, Rajiv Mathews, John Lambert  

**一句话要点**：提出多轮对话行为诱导框架，以动态评估大语言模型行为。

**关键词**：多轮对话, 行为诱导, 大语言模型评估, 在线交互, 动态基准

## 3 点简述
- 研究多轮对话中诱导大语言模型特定行为的方法，扩展单轮设置。
- 将现有方法分类为基于先验知识、离线交互和在线交互三类，并统一多轮在线方法。
- 实验显示在线方法在少量查询下成功率高，优于静态基准，推动动态评估发展。

## 摘要（原文）

> Identifying specific and often complex behaviors from large language models (LLMs) in conversational settings is crucial for their evaluation. Recent work proposes novel techniques to find natural language prompts that induce specific behaviors from a target model, yet they are mainly studied in single-turn settings. In this work, we study behavior elicitation in the context of multi-turn conversations. We first offer an analytical framework that categorizes existing methods into three families based on their interactions with the target model: those that use only prior knowledge, those that use offline interactions, and those that learn from online interactions. We then introduce a generalized multi-turn formulation of the online method, unifying single-turn and multi-turn elicitation. We evaluate all three families of methods on automatically generating multi-turn test cases. We investigate the efficiency of these approaches by analyzing the trade-off between the query budget, i.e., the number of interactions with the target model, and the success rate, i.e., the discovery rate of behavior-eliciting inputs. We find that online methods can achieve an average success rate of 45/19/77% with just a few thousand queries over three tasks where static methods from existing multi-turn conversation benchmarks find few or even no failure cases. Our work highlights a novel application of behavior elicitation methods in multi-turn conversation evaluation and the need for the community to move towards dynamic benchmarks.

