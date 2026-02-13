---
layout: default
title: When Agents Disagree With Themselves: Measuring Behavioral Consistency in LLM-Based Agents
---

# When Agents Disagree With Themselves: Measuring Behavioral Consistency in LLM-Based Agents
**arXiv**：[2602.11619v1](https://arxiv.org/abs/2602.11619) · [PDF](https://arxiv.org/pdf/2602.11619.pdf)  
**作者**：Aman Mehta  

**一句话要点**：提出基于行为一致性监测以提升LLM智能体可靠性，发现行为不一致预测任务失败

**关键词**：LLM智能体, 行为一致性, 任务可靠性, ReAct框架, 早期错误检测

## 3 点简述
- 核心问题：LLM智能体在相同任务上行为不一致，影响可靠性
- 方法要点：通过分析ReAct式智能体在HotpotQA上的动作序列，量化行为方差
- 实验或效果：行为不一致任务准确率下降32-55个百分点，早期决策是主要分歧点

## 摘要（原文）

> Run the same LLM agent on the same task twice: do you get the same behavior? We find the answer is often no. In a study of 3,000 agent runs across three models (Llama 3.1 70B, GPT-4o, and Claude Sonnet 4.5) on HotpotQA, we observe that ReAct-style agents produce 2.0--4.2 distinct action sequences per 10 runs on average, even with identical inputs. More importantly, this variance predicts failure: tasks with consistent behavior ($\leq$2 unique paths) achieve 80--92% accuracy, while highly inconsistent tasks ($\geq$6 unique paths) achieve only 25--60%, a 32--55 percentage point gap depending on model. We trace variance to early decisions: 69% of divergence occurs at step 2, the first search query. Our results suggest that monitoring behavioral consistency during execution could enable early error detection and improve agent reliability.

