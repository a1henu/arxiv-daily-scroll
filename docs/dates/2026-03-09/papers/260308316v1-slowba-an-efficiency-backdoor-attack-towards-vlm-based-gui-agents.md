---
layout: default
title: SlowBA: An efficiency backdoor attack towards VLM-based GUI agents
---

# SlowBA: An efficiency backdoor attack towards VLM-based GUI agents
**arXiv**：[2603.08316v1](https://arxiv.org/abs/2603.08316) · [PDF](https://arxiv.org/pdf/2603.08316.pdf)  
**作者**：Junxian Li, Tu Lan, Haozhen Tan, Yan Meng, Haojin Zhu  

**一句话要点**：提出SlowBA后门攻击，针对基于VLM的GUI代理的响应效率安全风险。

**关键词**：后门攻击, GUI代理安全, 响应效率, 强化学习, 视觉语言模型

## 3 点简述
- 核心问题：现有GUI代理安全研究忽视响应效率风险，攻击可操纵延迟。
- 方法要点：采用两阶段奖励级后门注入策略，通过强化学习学习触发器激活。
- 实验效果：攻击显著增加响应长度和延迟，保持任务准确性，在低污染率下有效。

## 摘要（原文）

> Modern vision-language-model (VLM) based graphical user interface (GUI) agents are expected not only to execute actions accurately but also to respond to user instructions with low latency. While existing research on GUI-agent security mainly focuses on manipulating action correctness, the security risks related to response efficiency remain largely unexplored. In this paper, we introduce SlowBA, a novel backdoor attack that targets the responsiveness of VLM-based GUI agents. The key idea is to manipulate response latency by inducing excessively long reasoning chains under specific trigger patterns. To achieve this, we propose a two-stage reward-level backdoor injection (RBI) strategy that first aligns the long-response format and then learns trigger-aware activation through reinforcement learning. In addition, we design realistic pop-up windows as triggers that naturally appear in GUI environments, improving the stealthiness of the attack. Extensive experiments across multiple datasets and baselines demonstrate that SlowBA can significantly increase response length and latency while largely preserving task accuracy. The attack remains effective even with a small poisoning ratio and under several defense settings. These findings reveal a previously overlooked security vulnerability in GUI agents and highlight the need for defenses that consider both action correctness and response efficiency. Code can be found in https://github.com/tu-tuing/SlowBA.

