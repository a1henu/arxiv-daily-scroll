---
layout: default
title: Assessing Long-Term Electricity Market Design for Ambitious Decarbonization Targets using Multi-Agent Reinforcement Learning
---

# Assessing Long-Term Electricity Market Design for Ambitious Decarbonization Targets using Multi-Agent Reinforcement Learning
**arXiv**：[2512.17444v1](https://arxiv.org/abs/2512.17444) · [PDF](https://arxiv.org/pdf/2512.17444.pdf)  
**作者**：Javier Gonzalez-Ruiz, Carlos Rodriguez-Pardo, Iacopo Savelli, Alice Di Bella, Massimo Tavoni  

**一句话要点**：提出多智能体强化学习模型以评估支持脱碳目标的长期电力市场设计

**关键词**：多智能体强化学习, 电力市场设计, 脱碳政策, 独立近端策略优化, 市场模拟

## 3 点简述
- 核心问题：长期电力市场机制对脱碳转型至关重要，需先进工具支持政策设计。
- 方法要点：采用独立近端策略优化，模拟发电公司投资决策，适应分散竞争环境。
- 实验或效果：应用于意大利电力系统，测试不同竞争水平、市场设计和政策场景，强调市场设计对脱碳和价格稳定的作用。

## 摘要（原文）

> Electricity systems are key to transforming today's society into a carbon-free economy. Long-term electricity market mechanisms, including auctions, support schemes, and other policy instruments, are critical in shaping the electricity generation mix. In light of the need for more advanced tools to support policymakers and other stakeholders in designing, testing, and evaluating long-term markets, this work presents a multi-agent reinforcement learning model capable of capturing the key features of decarbonizing energy systems. Profit-maximizing generation companies make investment decisions in the wholesale electricity market, responding to system needs, competitive dynamics, and policy signals. The model employs independent proximal policy optimization, which was selected for suitability to the decentralized and competitive environment. Nevertheless, given the inherent challenges of independent learning in multi-agent settings, an extensive hyperparameter search ensures that decentralized training yields market outcomes consistent with competitive behavior. The model is applied to a stylized version of the Italian electricity system and tested under varying levels of competition, market designs, and policy scenarios. Results highlight the critical role of market design for decarbonizing the electricity sector and avoiding price volatility. The proposed framework allows assessing long-term electricity markets in which multiple policy and market mechanisms interact simultaneously, with market participants responding and adapting to decarbonization pathways.

