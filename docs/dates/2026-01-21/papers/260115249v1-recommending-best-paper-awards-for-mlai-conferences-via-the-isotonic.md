---
layout: default
title: Recommending Best Paper Awards for ML/AI Conferences via the Isotonic Mechanism
---

# Recommending Best Paper Awards for ML/AI Conferences via the Isotonic Mechanism
**arXiv**：[2601.15249v1](https://arxiv.org/abs/2601.15249) · [PDF](https://arxiv.org/pdf/2601.15249.pdf)  
**作者**：Garrett G. Wen, Buxin Su, Natalie Collina, Zhun Deng, Weijie Su  

**一句话要点**：提出基于等渗机制的作者辅助方法，以优化ML/AI会议最佳论文奖评选

**关键词**：最佳论文奖评选, 等渗机制, 作者辅助评审, 激励机制设计, 会议评审优化

## 3 点简述
- 针对ML/AI会议最佳论文奖评选质量与一致性的挑战，作者评估被纳入评审过程
- 采用等渗机制收集作者对自身论文的排名，调整原始评审分数以估计真实质量
- 通过理论证明与ICLR、NeurIPS数据验证，机制在单配额下放宽假设并提升评选质量

## 摘要（原文）

> Machine learning and artificial intelligence conferences such as NeurIPS and ICML now regularly receive tens of thousands of submissions, posing significant challenges to maintaining the quality and consistency of the peer review process. This challenge is particularly acute for best paper awards, which are an important part of the peer review process, yet whose selection has increasingly become a subject of debate in recent years. In this paper, we introduce an author-assisted mechanism to facilitate the selection of best paper awards. Our method employs the Isotonic Mechanism for eliciting authors' assessments of their own submissions in the form of a ranking, which is subsequently utilized to adjust the raw review scores for optimal estimation of the submissions' ground-truth quality. We demonstrate that authors are incentivized to report truthfully when their utility is a convex additive function of the adjusted scores, and we validate this convexity assumption for best paper awards using publicly accessible review data of ICLR from 2019 to 2023 and NeurIPS from 2021 to 2023. Crucially, in the special case where an author has a single quota -- that is, may nominate only one paper -- we prove that truthfulness holds even when the utility function is merely nondecreasing and additive. This finding represents a substantial relaxation of the assumptions required in prior work. For practical implementation, we extend our mechanism to accommodate the common scenario of overlapping authorship. Finally, simulation results demonstrate that our mechanism significantly improves the quality of papers selected for awards.

