---
layout: default
title: One Word is Enough: Minimal Adversarial Perturbations for Neural Text Ranking
---

# One Word is Enough: Minimal Adversarial Perturbations for Neural Text Ranking
**arXiv**：[2601.20283v1](https://arxiv.org/abs/2601.20283) · [PDF](https://arxiv.org/pdf/2601.20283.pdf)  
**作者**：Tanmay Karmakar, Sourav Saha, Debapriyo Majumdar, Surjyanee Halder  

**一句话要点**：提出单词语义对齐攻击以提升神经排序模型对抗性鲁棒性研究

**关键词**：神经排序模型, 对抗性攻击, 语义对齐, 单词语义扰动, 鲁棒性分析

## 3 点简述
- 研究神经排序模型对单词语义对齐对抗性扰动的脆弱性
- 开发基于启发式和梯度引导的单词插入或替换攻击方法
- 在TREC-DL数据集上实现高成功率并分析攻击敏感区域

## 摘要（原文）

> Neural ranking models (NRMs) achieve strong retrieval effectiveness, yet prior work has shown they are vulnerable to adversarial perturbations. We revisit this robustness question with a minimal, query-aware attack that promotes a target document by inserting or substituting a single, semantically aligned word - the query center. We study heuristic and gradient-guided variants, including a white-box method that identifies influential insertion points. On TREC-DL 2019/2020 with BERT and monoT5 re-rankers, our single-word attacks achieve up to 91% success while modifying fewer than two tokens per document on average, achieving competitive rank and score boosts with far fewer edits under a comparable white-box setup to ensure fair evaluation against PRADA. We also introduce new diagnostic metrics to analyze attack sensitivity beyond aggregate success rates. Our analysis reveals a Goldilocks zone in which mid-ranked documents are most vulnerable. These findings demonstrate practical risks and motivate future defenses for robust neural ranking.

