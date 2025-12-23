---
layout: default
title: Auditing Significance, Metric Choice, and Demographic Fairness in Medical AI Challenges
---

# Auditing Significance, Metric Choice, and Demographic Fairness in Medical AI Challenges
**arXiv**：[2512.19091v1](https://arxiv.org/abs/2512.19091) · [PDF](https://arxiv.org/pdf/2512.19091.pdf)  
**作者**：Ariel Lubonja, Pedro R. A. S. Bassi, Wenxuan Li, Hualin Qiao, Randal Burns, Alan L. Yuille, Zongwei Zhou  

**一句话要点**：提出RankInsight工具包以解决医学AI挑战中统计显著性、指标选择和人口公平性审计问题

**关键词**：医学AI挑战, 统计显著性, 公平性审计, 指标选择, 开源工具包, 人口公平性

## 3 点简述
- 医学AI挑战存在统计显著性未测试、单一指标不适用所有器官、人口公平性未报告三大问题
- RankInsight工具包提供成对显著性计算、器官特定指标重排、交叉人口公平性审计功能
- 实验显示工具能揭示模型排名变化和公平性差距，如NSD指标改变排名，半数MONAI模型存在性别-种族差异

## 摘要（原文）

> Open challenges have become the de facto standard for comparative ranking of medical AI methods. Despite their importance, medical AI leaderboards exhibit three persistent limitations: (1) score gaps are rarely tested for statistical significance, so rank stability is unknown; (2) single averaged metrics are applied to every organ, hiding clinically important boundary errors; (3) performance across intersecting demographics is seldom reported, masking fairness and equity gaps. We introduce RankInsight, an open-source toolkit that seeks to address these limitations. RankInsight (1) computes pair-wise significance maps that show the nnU-Net family outperforms Vision-Language and MONAI submissions with high statistical certainty; (2) recomputes leaderboards with organ-appropriate metrics, reversing the order of the top four models when Dice is replaced by NSD for tubular structures; and (3) audits intersectional fairness, revealing that more than half of the MONAI-based entries have the largest gender-race discrepancy on our proprietary Johns Hopkins Hospital dataset. The RankInsight toolkit is publicly released and can be directly applied to past, ongoing, and future challenges. It enables organizers and participants to publish rankings that are statistically sound, clinically meaningful, and demographically fair.

