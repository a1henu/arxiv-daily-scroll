---
layout: default
title: Clinical Validation of Medical-based Large Language Model Chatbots on Ophthalmic Patient Queries with LLM-based Evaluation
---

# Clinical Validation of Medical-based Large Language Model Chatbots on Ophthalmic Patient Queries with LLM-based Evaluation
**arXiv**：[2602.05381v1](https://arxiv.org/abs/2602.05381) · [PDF](https://arxiv.org/pdf/2602.05381.pdf)  
**作者**：Ting Fang Tan, Kabilan Elangovan, Andreas Pollreisz, Kevin Bryan Dy, Wei Yan Ng, Joy Le Yi Wong, Jin Liyuan, Chrystie Quek Wan Ning, Ashley Shuen Ying Hong, Arun James Thirunavukarasu, Shelley Yin-His Chang, Jie Yao, Dylan Hong, Wang Zhaoran, Amrita Gupta, Daniel SW Ting  

**一句话要点**：评估小型医疗大语言模型在眼科患者查询中的表现，并验证基于LLM评估的可行性。

**关键词**：医疗大语言模型, 眼科患者查询, 模型评估, S.C.O.R.E.框架, 临床验证, 自动化评估

## 3 点简述
- 核心问题：医疗大语言模型在眼科患者教育中的安全性和准确性需严格评估。
- 方法要点：使用S.C.O.R.E.框架，比较四个小型医疗LLM回答眼科查询的表现，并由临床医生和GPT-4-Turbo评分。
- 实验或效果：Meerkat-7B表现最佳，GPT-4-Turbo评分与临床医生评估高度一致，支持LLM评估用于大规模基准测试。

## 摘要（原文）

> Domain specific large language models are increasingly used to support patient education, triage, and clinical decision making in ophthalmology, making rigorous evaluation essential to ensure safety and accuracy. This study evaluated four small medical LLMs Meerkat-7B, BioMistral-7B, OpenBioLLM-8B, and MedLLaMA3-v20 in answering ophthalmology related patient queries and assessed the feasibility of LLM based evaluation against clinician grading. In this cross sectional study, 180 ophthalmology patient queries were answered by each model, generating 2160 responses. Models were selected for parameter sizes under 10 billion to enable resource efficient deployment. Responses were evaluated by three ophthalmologists of differing seniority and by GPT-4-Turbo using the S.C.O.R.E. framework assessing safety, consensus and context, objectivity, reproducibility, and explainability, with ratings assigned on a five point Likert scale. Agreement between LLM and clinician grading was assessed using Spearman rank correlation, Kendall tau statistics, and kernel density estimate analyses. Meerkat-7B achieved the highest performance with mean scores of 3.44 from Senior Consultants, 4.08 from Consultants, and 4.18 from Residents. MedLLaMA3-v20 performed poorest, with 25.5 percent of responses containing hallucinations or clinically misleading content, including fabricated terminology. GPT-4-Turbo grading showed strong alignment with clinician assessments overall, with Spearman rho of 0.80 and Kendall tau of 0.67, though Senior Consultants graded more conservatively. Overall, medical LLMs demonstrated potential for safe ophthalmic question answering, but gaps remained in clinical depth and consensus, supporting the feasibility of LLM based evaluation for large scale benchmarking and the need for hybrid automated and clinician review frameworks to guide safe clinical deployment.

