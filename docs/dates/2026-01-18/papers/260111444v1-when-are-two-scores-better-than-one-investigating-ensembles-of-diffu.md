---
layout: default
title: When Are Two Scores Better Than One? Investigating Ensembles of Diffusion Models
---

# When Are Two Scores Better Than One? Investigating Ensembles of Diffusion Models
**arXiv**：[2601.11444v1](https://arxiv.org/abs/2601.11444) · [PDF](https://arxiv.org/pdf/2601.11444.pdf)  
**作者**：Raphaël Razafindralambo, Rémy Sun, Frédéric Precioso, Damien Garreau, Pierre-Alexandre Mattei  

**一句话要点**：研究扩散模型集成方法，探讨其对生成质量的影响与理论解释。

**关键词**：扩散模型, 模型集成, 生成质量评估, 分数匹配, 理论分析, 图像生成

## 3 点简述
- 核心问题：扩散模型集成能否提升生成质量，特别是感知指标如FID。
- 方法要点：采用深度集成、蒙特卡洛丢弃等聚合规则，在图像和表格数据上实验。
- 实验或效果：集成改善损失和似然，但未一致提升FID；表格数据中特定策略表现更优。

## 摘要（原文）

> Diffusion models now generate high-quality, diverse samples, with an increasing focus on more powerful models. Although ensembling is a well-known way to improve supervised models, its application to unconditional score-based diffusion models remains largely unexplored. In this work we investigate whether it provides tangible benefits for generative modelling. We find that while ensembling the scores generally improves the score-matching loss and model likelihood, it fails to consistently enhance perceptual quality metrics such as FID on image datasets. We confirm this observation across a breadth of aggregation rules using Deep Ensembles, Monte Carlo Dropout, on CIFAR-10 and FFHQ. We attempt to explain this discrepancy by investigating possible explanations, such as the link between score estimation and image quality. We also look into tabular data through random forests, and find that one aggregation strategy outperforms the others. Finally, we provide theoretical insights into the summing of score models, which shed light not only on ensembling but also on several model composition techniques (e.g. guidance).

