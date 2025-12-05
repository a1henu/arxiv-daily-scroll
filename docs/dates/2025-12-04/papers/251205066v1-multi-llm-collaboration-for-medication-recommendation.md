---
layout: default
title: Multi-LLM Collaboration for Medication Recommendation
---

# Multi-LLM Collaboration for Medication Recommendation
**arXiv**：[2512.05066v1](https://arxiv.org/abs/2512.05066) · [PDF](https://arxiv.org/pdf/2512.05066.pdf)  
**作者**：Huascar Sanchez, Briland Hitaj, Jules Bergmann, Linda Briesemeister  

**一句话要点**：提出基于LLM化学的多LLM协作框架，以提升临床用药推荐的可靠性

**关键词**：用药推荐, 多LLM协作, LLM化学, 临床决策支持, 模型集成

## 3 点简述
- 核心问题：单个LLM易产生幻觉和不一致，传统集成方法难以保证稳定可信的用药推荐。
- 方法要点：利用LLM化学量化模型协作兼容性，通过交互建模指导多LLM协作，实现互补、稳定和校准的集成。
- 实验或效果：在真实临床场景中评估，初步结果表明该方法能生成可信、个性化的用药推荐。

## 摘要（原文）

> As healthcare increasingly turns to AI for scalable and trustworthy clinical decision support, ensuring reliability in model reasoning remains a critical challenge. Individual large language models (LLMs) are susceptible to hallucinations and inconsistency, whereas naive ensembles of models often fail to deliver stable and credible recommendations. Building on our previous work on LLM Chemistry, which quantifies the collaborative compatibility among LLMs, we apply this framework to improve the reliability in medication recommendation from brief clinical vignettes. Our approach leverages multi-LLM collaboration guided by Chemistry-inspired interaction modeling, enabling ensembles that are effective (exploiting complementary strengths), stable (producing consistent quality), and calibrated (minimizing interference and error amplification). We evaluate our Chemistry-based Multi-LLM collaboration strategy on real-world clinical scenarios to investigate whether such interaction-aware ensembles can generate credible, patient-specific medication recommendations. Preliminary results are encouraging, suggesting that LLM Chemistry-guided collaboration may offer a promising path toward reliable and trustworthy AI assistants in clinical practice.

