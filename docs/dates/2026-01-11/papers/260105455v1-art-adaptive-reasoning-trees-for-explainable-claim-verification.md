---
layout: default
title: ART: Adaptive Reasoning Trees for Explainable Claim Verification
---

# ART: Adaptive Reasoning Trees for Explainable Claim Verification
**arXiv**：[2601.05455v1](https://arxiv.org/abs/2601.05455) · [PDF](https://arxiv.org/pdf/2601.05455.pdf)  
**作者**：Sahil Wadhwa, Himanshu Kumar, Guanqun Yang, Abbaas Alif Mohamed Nishar, Pranab Mohanty, Swapnil Shinde, Yue Wu  

**一句话要点**：提出自适应推理树以解决大语言模型在声明验证中缺乏可解释性和可争议性的问题

**关键词**：声明验证, 可解释人工智能, 自适应推理树, 大语言模型, 结构化推理, 可争议决策

## 3 点简述
- 核心问题：大语言模型在关键决策中因输出不透明、缺乏忠实解释和可争议性，影响可信度
- 方法要点：通过分层树结构，从根声明分支生成支持与攻击论点，由法官LLM进行成对比较，自底向上确定论点强度，实现透明可争议的验证
- 实验或效果：在多个数据集上验证，结构化推理优于基线，为可解释声明验证设立新基准，提高可靠性和决策清晰度

## 摘要（原文）

> Large Language Models (LLMs) are powerful candidates for complex decision-making, leveraging vast encoded knowledge and remarkable zero-shot abilities. However, their adoption in high-stakes environments is hindered by their opacity; their outputs lack faithful explanations and cannot be effectively contested to correct errors, undermining trustworthiness. In this paper, we propose ART (Adaptive Reasoning Trees), a hierarchical method for claim verification. The process begins with a root claim, which branches into supporting and attacking child arguments. An argument's strength is determined bottom-up via a pairwise tournament of its children, adjudicated by a judge LLM, allowing a final, transparent and contestable verdict to be systematically derived which is missing in methods like Chain-of-Thought (CoT). We empirically validate ART on multiple datasets, analyzing different argument generators and comparison strategies. Our findings show that ART's structured reasoning outperforms strong baselines, establishing a new benchmark for explainable claim verification which is more reliable and ensures clarity in the overall decision making step.

