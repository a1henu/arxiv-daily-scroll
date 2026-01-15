---
layout: default
title: Coordinated Pandemic Control with Large Language Model Agents as Policymaking Assistants
---

# Coordinated Pandemic Control with Large Language Model Agents as Policymaking Assistants
**arXiv**：[2601.09264v1](https://arxiv.org/abs/2601.09264) · [PDF](https://arxiv.org/pdf/2601.09264.pdf)  
**作者**：Ziyi Shi, Xusen Guo, Hongliang Lu, Mingxing Peng, Haotian Wang, Zheng Zhu, Zhenning Li, Yuxuan Liang, Xinhu Zheng, Hai Yang  

**一句话要点**：提出基于大语言模型多智能体的协调疫情控制框架，以解决跨区域政策制定碎片化问题。

**关键词**：大语言模型多智能体, 疫情控制, 协调政策制定, 流行病学模拟, 跨区域通信, 决策辅助

## 3 点简述
- 核心问题：疫情控制中跨行政区域政策制定缺乏协调，导致反应滞后和效果受限。
- 方法要点：为每个区域分配大语言模型智能体，结合流行病学模拟和跨区域通信，实现协同决策。
- 实验或效果：基于美国2020年COVID-19数据验证，框架显著降低感染和死亡人数，提升控制效果。

## 摘要（原文）

> Effective pandemic control requires timely and coordinated policymaking across administrative regions that are intrinsically interdependent. However, human-driven responses are often fragmented and reactive, with policies formulated in isolation and adjusted only after outbreaks escalate, undermining proactive intervention and global pandemic mitigation. To address this challenge, here we propose a large language model (LLM) multi-agent policymaking framework that supports coordinated and proactive pandemic control across regions. Within our framework, each administrative region is assigned an LLM agent as an AI policymaking assistant. The agent reasons over region-specific epidemiological dynamics while communicating with other agents to account for cross-regional interdependencies. By integrating real-world data, a pandemic evolution simulator, and structured inter-agent communication, our framework enables agents to jointly explore counterfactual intervention scenarios and synthesize coordinated policy decisions through a closed-loop simulation process. We validate the proposed framework using state-level COVID-19 data from the United States between April and December 2020, together with real-world mobility records and observed policy interventions. Compared with real-world pandemic outcomes, our approach reduces cumulative infections and deaths by up to 63.7% and 40.1%, respectively, at the individual state level, and by 39.0% and 27.0%, respectively, when aggregated across states. These results demonstrate that LLM multi-agent systems can enable more effective pandemic control with coordinated policymaking...

