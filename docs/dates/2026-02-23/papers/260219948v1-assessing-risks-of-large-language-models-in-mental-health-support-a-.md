---
layout: default
title: Assessing Risks of Large Language Models in Mental Health Support: A Framework for Automated Clinical AI Red Teaming
---

# Assessing Risks of Large Language Models in Mental Health Support: A Framework for Automated Clinical AI Red Teaming
**arXiv**：[2602.19948v1](https://arxiv.org/abs/2602.19948) · [PDF](https://arxiv.org/pdf/2602.19948.pdf)  
**作者**：Ian Steenstra, Paola Pedrelli, Weiyan Shi, Stacy Marsella, Timothy W. Bickmore  

**一句话要点**：提出基于模拟患者与质量风险本体的框架，以评估AI心理治疗中的安全风险

**关键词**：大语言模型安全评估, AI心理治疗模拟, 临床红队测试, 风险本体, 患者模拟代理, 数据可视化仪表板

## 3 点简述
- 核心问题：现有安全基准难以检测AI心理治疗中的复杂纵向风险，如加剧患者妄想或自杀风险
- 方法要点：结合AI心理治疗师与动态认知情感模型的模拟患者，通过会话模拟评估护理质量和风险
- 实验或效果：在酒精使用障碍案例中评估6个AI代理，发现关键安全缺口，并通过利益相关者验证框架有效性

## 摘要（原文）

> Large Language Models (LLMs) are increasingly utilized for mental health support; however, current safety benchmarks often fail to detect the complex, longitudinal risks inherent in therapeutic dialogue. We introduce an evaluation framework that pairs AI psychotherapists with simulated patient agents equipped with dynamic cognitive-affective models and assesses therapy session simulations against a comprehensive quality of care and risk ontology. We apply this framework to a high-impact test case, Alcohol Use Disorder, evaluating six AI agents (including ChatGPT, Gemini, and Character.AI) against a clinically-validated cohort of 15 patient personas representing diverse clinical phenotypes.
>   Our large-scale simulation (N=369 sessions) reveals critical safety gaps in the use of AI for mental health support. We identify specific iatrogenic risks, including the validation of patient delusions ("AI Psychosis") and failure to de-escalate suicide risk. Finally, we validate an interactive data visualization dashboard with diverse stakeholders, including AI engineers and red teamers, mental health professionals, and policy experts (N=9), demonstrating that this framework effectively enables stakeholders to audit the "black box" of AI psychotherapy. These findings underscore the critical safety risks of AI-provided mental health support and the necessity of simulation-based clinical red teaming before deployment.

