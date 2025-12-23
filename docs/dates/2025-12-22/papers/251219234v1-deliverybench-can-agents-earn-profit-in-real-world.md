---
layout: default
title: DeliveryBench: Can Agents Earn Profit in Real World?
---

# DeliveryBench: Can Agents Earn Profit in Real World?
**arXiv**：[2512.19234v1](https://arxiv.org/abs/2512.19234) · [PDF](https://arxiv.org/pdf/2512.19234.pdf)  
**作者**：Lingjun Mao, Jiawei Ren, Kun Zhou, Jixuan Chen, Ziqiao Ma, Lianhui Qin  

**一句话要点**：提出DeliveryBench以评估具身代理在真实约束下的长期规划能力

**关键词**：具身代理, 长期规划, 约束感知, 基准测试, 视觉语言模型, 城市模拟

## 3 点简述
- 现有基准难以捕捉真实世界决策的丰富约束，如配送时限和资源动态
- 基于外卖配送场景，构建程序化生成的城市环境，模拟长期利润最大化目标
- 实验显示VLM代理与人类存在性能差距，常违反常识约束且模型个性差异明显

## 摘要（原文）

> LLMs and VLMs are increasingly deployed as embodied agents, yet existing benchmarks largely revolve around simple short-term tasks and struggle to capture rich realistic constraints that shape real-world decision making. To close this gap, we propose DeliveryBench, a city-scale embodied benchmark grounded in the real-world profession of food delivery. Food couriers naturally operate under long-horizon objectives (maximizing net profit over hours) while managing diverse constraints, e.g., delivery deadline, transportation expense, vehicle battery, and necessary interactions with other couriers and customers. DeliveryBench instantiates this setting in procedurally generated 3D cities with diverse road networks, buildings, functional locations, transportation modes, and realistic resource dynamics, enabling systematic evaluation of constraint-aware, long-horizon planning. We benchmark a range of VLM-based agents across nine cities and compare them with human players. Our results reveal a substantial performance gap to humans, and find that these agents are short-sighted and frequently break basic commonsense constraints. Additionally, we observe distinct personalities across models (e.g., adventurous GPT-5 vs. conservative Claude), highlighting both the brittleness and the diversity of current VLM-based embodied agents in realistic, constraint-dense environments. Our code, data, and benchmark are available at https://deliverybench.github.io.

