---
layout: default
title: Emergent Bias and Fairness in Multi-Agent Decision Systems
---

# Emergent Bias and Fairness in Multi-Agent Decision Systems
**arXiv**：[2512.16433v1](https://arxiv.org/abs/2512.16433) · [PDF](https://arxiv.org/pdf/2512.16433.pdf)  
**作者**：Maeve Madigan, Parameswaran Kamalaruban, Glenn Moynihan, Tom Kempton, David Sutton, Stuart Burrell  

**一句话要点**：提出多智能体系统公平性评估方法，揭示金融决策中的涌现偏见风险。

**关键词**：多智能体系统, 公平性评估, 涌现偏见, 金融决策, 模型风险

## 3 点简述
- 核心问题：多智能体系统缺乏有效公平性评估，在金融等高风险领域部署存在偏见风险。
- 方法要点：通过大规模模拟，分析不同配置下的公平性指标，识别集体行为导致的偏见。
- 实验或效果：发现偏见无法追溯到单个智能体，强调需将系统作为整体评估以降低模型风险。

## 摘要（原文）

> Multi-agent systems have demonstrated the ability to improve performance on a variety of predictive tasks by leveraging collaborative decision making. However, the lack of effective evaluation methodologies has made it difficult to estimate the risk of bias, making deployment of such systems unsafe in high stakes domains such as consumer finance, where biased decisions can translate directly into regulatory breaches and financial loss. To address this challenge, we need to develop fairness evaluation methodologies for multi-agent predictive systems and measure the fairness characteristics of these systems in the financial tabular domain. Examining fairness metrics using large-scale simulations across diverse multi-agent configurations, with varying communication and collaboration mechanisms, we reveal patterns of emergent bias in financial decision-making that cannot be traced to individual agent components, indicating that multi-agent systems may exhibit genuinely collective behaviors. Our findings highlight that fairness risks in financial multi-agent systems represent a significant component of model risk, with tangible impacts on tasks such as credit scoring and income estimation. We advocate that multi-agent decision systems must be evaluated as holistic entities rather than through reductionist analyses of their constituent components.

