---
layout: default
title: Experience-Guided Self-Adaptive Cascaded Agents for Breast Cancer Screening and Diagnosis with Reduced Biopsy Referrals
---

# Experience-Guided Self-Adaptive Cascaded Agents for Breast Cancer Screening and Diagnosis with Reduced Biopsy Referrals
**arXiv**：[2602.23899v1](https://arxiv.org/abs/2602.23899) · [PDF](https://arxiv.org/pdf/2602.23899.pdf)  
**作者**：Pramit Saha, Mohammad Alsharid, Joshua Strong, J. Alison Noble  

**一句话要点**：提出经验引导的自适应级联代理框架BUSD-Agent，以减少乳腺癌超声筛查中的诊断升级和不必要活检转诊。

**关键词**：乳腺癌筛查, 级联代理, 自适应决策, 记忆库检索, 超声诊断, 活检转诊减少

## 3 点简述
- 核心问题：乳腺癌超声筛查中诊断升级和活检转诊过多，需提高特异性并减少不必要干预。
- 方法要点：采用两级级联代理，筛选诊所代理过滤低风险病例，诊断诊所代理处理高风险病例，基于记忆库检索相似历史轨迹进行自适应决策。
- 实验或效果：在10个数据集上评估，相比无轨迹条件框架，诊断升级率从84.95%降至58.72%，活检转诊率从59.50%降至37.08%，特异性显著提升。

## 摘要（原文）

> We propose an experience-guided cascaded multi-agent framework for Breast Ultrasound Screening and Diagnosis, called BUSD-Agent, that aims to reduce diagnostic escalation and unnecessary biopsy referrals. Our framework models screening and diagnosis as a two-stage, selective decision-making process. A lightweight `screening clinic' agent, restricted to classification models as tools, selectively filters out benign and normal cases from further diagnostic escalation when malignancy risk and uncertainty are estimated as low. Cases that have higher risks are escalated to the `diagnostic clinic' agent, which integrates richer perception and radiological description tools to make a secondary decision on biopsy referral. To improve agent performance, past records of pathology-confirmed outcomes along with image embeddings, model predictions, and historical agent actions are stored in a memory bank as structured decision trajectories. For each new case, BUSD-Agent retrieves similar past cases based on image, model response and confidence similarity to condition the agent's current decision policy. This enables retrieval-conditioned in-context adaptation that dynamically adjusts model trust and escalation thresholds from prior experiences without parameter updates. Evaluation across 10 breast ultrasound datasets shows that the proposed experience-guided workflow reduces diagnostic escalation in BUSD-Agent from 84.95% to 58.72% and overall biopsy referrals from 59.50% to 37.08%, compared to the same architecture without trajectory conditioning, while improving average screening specificity by 68.48% and diagnostic specificity by 6.33%.

