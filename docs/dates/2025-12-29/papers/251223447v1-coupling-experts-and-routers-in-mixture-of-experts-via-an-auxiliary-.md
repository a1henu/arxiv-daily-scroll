---
layout: default
title: Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss
---

# Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss
**arXiv**：[2512.23447v1](https://arxiv.org/abs/2512.23447) · [PDF](https://arxiv.org/pdf/2512.23447.pdf)  
**作者**：Ang Lv, Jin Ma, Yiyuan Ma, Siyuan Qiao  

**一句话要点**：提出专家-路由器耦合损失以解决MoE模型中路由器决策与专家能力不匹配问题

**关键词**：混合专家模型, 路由器优化, 辅助损失, 专家专业化, 预训练语言模型, 计算效率

## 3 点简述
- MoE模型缺乏约束确保路由器决策与专家能力对齐，限制性能
- ERC损失通过扰动路由器嵌入并施加激活约束，实现路由器与专家的紧密耦合
- 在3B至15B参数的MoE-LLMs预训练中验证有效性，提供专家专业化水平跟踪

## 摘要（原文）

> Mixture-of-Experts (MoE) models lack explicit constraints to ensure the router's decisions align well with the experts' capabilities, which ultimately limits model performance. To address this, we propose expert-router coupling (ERC) loss, a lightweight auxiliary loss that tightly couples the router's decisions with expert capabilities. Our approach treats each expert's router embedding as a proxy token for the tokens assigned to that expert, and feeds perturbed router embeddings through the experts to obtain internal activations. The ERC loss enforces two constraints on these activations: (1) Each expert must exhibit higher activation for its own proxy token than for the proxy tokens of any other expert. (2) Each proxy token must elicit stronger activation from its corresponding expert than from any other expert. These constraints jointly ensure that each router embedding faithfully represents its corresponding expert's capability, while each expert specializes in processing the tokens actually routed to it. The ERC loss is computationally efficient, operating only on n^2 activations, where n is the number of experts. This represents a fixed cost independent of batch size, unlike prior coupling methods that scale with the number of tokens (often millions per batch). Through pre-training MoE-LLMs ranging from 3B to 15B parameters and extensive analysis on trillions of tokens, we demonstrate the effectiveness of the ERC loss. Moreover, the ERC loss offers flexible control and quantitative tracking of expert specialization levels during training, providing valuable insights into MoEs.

