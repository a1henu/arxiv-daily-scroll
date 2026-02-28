---
layout: default
title: An Empirical Analysis of Cooperative Perception for Occlusion Risk Mitigation
---

# An Empirical Analysis of Cooperative Perception for Occlusion Risk Mitigation
**arXiv**：[2602.23051v1](https://arxiv.org/abs/2602.23051) · [PDF](https://arxiv.org/pdf/2602.23051.pdf)  
**作者**：Aihong Wang, Tenghui Xie, Fuxi Wen, Jun Li  

**一句话要点**：提出风险追踪损失（RTL）指标与不对称通信框架，以缓解自动驾驶中的遮挡风险。

**关键词**：遮挡风险缓解, 风险追踪损失指标, V2X部署策略, 不对称通信, 自动驾驶安全, 实证分析

## 3 点简述
- 遮挡导致感知系统遗漏关键道路用户，传统风险指标难以捕捉累积威胁。
- 提出RTL指标，聚合遮挡期间瞬时风险强度，提供全面风险评估。
- 实验显示不对称通信框架在低渗透率下优于传统对称模型，风险缓解效果显著。

## 摘要（原文）

> Occlusions present a significant challenge for connected and automated vehicles, as they can obscure critical road users from perception systems. Traditional risk metrics often fail to capture the cumulative nature of these threats over time adequately. In this paper, we propose a novel and universal risk assessment metric, the Risk of Tracking Loss (RTL), which aggregates instantaneous risk intensity throughout occluded periods. This provides a holistic risk profile that encompasses both high-intensity, short-term threats and prolonged exposure. Utilizing diverse and high-fidelity real-world datasets, a large-scale statistical analysis is conducted to characterize occlusion risk and validate the effectiveness of the proposed metric. The metric is applied to evaluate different vehicle-to-everything (V2X) deployment strategies. Our study shows that full V2X penetration theoretically eliminates this risk, the reduction is highly nonlinear; a substantial statistical benefit requires a high penetration threshold of 75-90%. To overcome this limitation, we propose a novel asymmetric communication framework that allows even non-connected vehicles to receive warnings. Experimental results demonstrate that this paradigm achieves better risk mitigation performance. We found that our approach at 25% penetration outperforms the traditional symmetric model at 75%, and benefits saturate at only 50% penetration. This work provides a crucial risk assessment metric and a cost-effective, strategic roadmap for accelerating the safety benefits of V2X deployment.

