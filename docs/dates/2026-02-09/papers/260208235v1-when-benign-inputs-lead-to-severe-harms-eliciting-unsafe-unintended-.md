---
layout: default
title: When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents
---

# When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents
**arXiv**：[2602.08235v1](https://arxiv.org/abs/2602.08235) · [PDF](https://arxiv.org/pdf/2602.08235.pdf)  
**作者**：Jaylen Jones, Zhehao Zhang, Yuting Ning, Eric Fosler-Lussier, Pierre-Luc St-Charles, Yoshua Bengio, Dawn Song, Yu Su, Huan Sun  

**一句话要点**：提出AutoElicit框架以自动引发计算机使用代理在良性输入下的严重意外行为

**关键词**：计算机使用代理, 意外行为, 自动化测试, 安全风险, 指令扰动, 代理框架

## 3 点简述
- 核心问题：计算机使用代理在良性输入下可能产生偏离预期的严重意外行为，缺乏系统性表征与自动化方法
- 方法要点：定义意外行为特征，基于执行反馈迭代扰动良性指令，自动引发危害并保持扰动现实性
- 实验或效果：从Claude 4.5 Haiku等前沿代理中引发数百种有害意外行为，验证扰动在多种代理中的可转移性

## 摘要（原文）

> Although computer-use agents (CUAs) hold significant potential to automate increasingly complex OS workflows, they can demonstrate unsafe unintended behaviors that deviate from expected outcomes even under benign input contexts. However, exploration of this risk remains largely anecdotal, lacking concrete characterization and automated methods to proactively surface long-tail unintended behaviors under realistic CUA scenarios. To fill this gap, we introduce the first conceptual and methodological framework for unintended CUA behaviors, by defining their key characteristics, automatically eliciting them, and analyzing how they arise from benign inputs. We propose AutoElicit: an agentic framework that iteratively perturbs benign instructions using CUA execution feedback, and elicits severe harms while keeping perturbations realistic and benign. Using AutoElicit, we surface hundreds of harmful unintended behaviors from state-of-the-art CUAs such as Claude 4.5 Haiku and Opus. We further evaluate the transferability of human-verified successful perturbations, identifying persistent susceptibility to unintended behaviors across various other frontier CUAs. This work establishes a foundation for systematically analyzing unintended behaviors in realistic computer-use settings.

