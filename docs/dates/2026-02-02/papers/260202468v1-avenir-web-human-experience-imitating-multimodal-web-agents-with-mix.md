---
layout: default
title: Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts
---

# Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts
**arXiv**：[2602.02468v1](https://arxiv.org/abs/2602.02468) · [PDF](https://arxiv.org/pdf/2602.02468.pdf)  
**作者**：Aiden Yiliu Li, Xinyue Hao, Shilong Liu, Mengdi Wang  

**一句话要点**：提出Avenir-Web，通过混合专家和模仿规划解决复杂网页任务执行问题。

**关键词**：网页代理, 混合专家, 经验模仿规划, 任务跟踪, 自适应内存, Online-Mind2Web

## 3 点简述
- 核心问题：现有网页代理在复杂动态界面上执行长时任务时，存在元素定位不准、缺乏站点知识、任务跟踪不稳定等问题。
- 方法要点：采用混合专家进行元素定位，结合经验模仿规划引入先验知识，并使用任务清单和自适应内存增强交互。
- 实验或效果：在Online-Mind2Web基准测试中，Avenir-Web超越开源代理，达到顶级专有模型性能，确立开源新标杆。

## 摘要（原文）

> Despite advances in multimodal large language models, autonomous web agents still struggle to reliably execute long-horizon tasks on complex and dynamic web interfaces. Existing agents often suffer from inaccurate element grounding, the absence of site-specific procedural knowledge, and unstable long-term task tracking and memory, particularly when operating over complex Document Object Model structures. To address these limitations, we introduce Avenir-Web, a web agent that achieves a new open-source state of the art on the Online-Mind2Web benchmark in real-world deployment. Avenir-Web leverages a Mixture of Grounding Experts, Experience-Imitation Planning for incorporating procedural priors, and a task-tracking checklist combined with adaptive memory to enable robust and seamless interaction across diverse user interface paradigms. We evaluate Avenir-Web on Online-Mind2Web, a rigorous benchmark of live and user-centered web tasks. Our results demonstrate that Avenir-Web significantly surpasses prior open-source agents and attains performance parity with top-tier proprietary models, thereby establishing a new open-source state of the art for reliable web agents on live websites.

