---
layout: default
title: CorrectAD: A Self-Correcting Agentic System to Improve End-to-end Planning in Autonomous Driving
---

# CorrectAD: A Self-Correcting Agentic System to Improve End-to-end Planning in Autonomous Driving
**arXiv**：[2511.13297v1](https://arxiv.org/abs/2511.13297) · [PDF](https://arxiv.org/pdf/2511.13297.pdf)  
**作者**：Enhui Ma, Lijun Zhou, Tao Tang, Jiahuan Zhang, Junpeng Jiang, Zhan Zhang, Dong Han, Kun Zhan, Xueyang Zhang, XianPeng Lang, Haiyang Sun, Xia Zhou, Di Lin, Kaicheng Yu  

**一句话要点**：提出CorrectAD自校正系统以解决自动驾驶端到端规划的长尾问题

**关键词**：自动驾驶规划, 自校正系统, 扩散模型, 长尾问题, 端到端学习, 世界模型

## 3 点简述
- 核心问题：数据驱动方法因长尾问题导致罕见但安全关键的失败案例，影响鲁棒性。
- 方法要点：结合PM-Agent和DriveSora生成模型，构建端到端模型无关的自校正管道。
- 实验效果：在nuScenes和内部数据集上，CorrectAD校正62.5%和49.8%失败案例，碰撞率降低39%和27%。

## 摘要（原文）

> End-to-end planning methods are the de facto standard of the current autonomous driving system, while the robustness of the data-driven approaches suffers due to the notorious long-tail problem (i.e., rare but safety-critical failure cases). In this work, we explore whether recent diffusion-based video generation methods (a.k.a. world models), paired with structured 3D layouts, can enable a fully automated pipeline to self-correct such failure cases. We first introduce an agent to simulate the role of product manager, dubbed PM-Agent, which formulates data requirements to collect data similar to the failure cases. Then, we use a generative model that can simulate both data collection and annotation. However, existing generative models struggle to generate high-fidelity data conditioned on 3D layouts. To address this, we propose DriveSora, which can generate spatiotemporally consistent videos aligned with the 3D annotations requested by PM-Agent. We integrate these components into our self-correcting agentic system, CorrectAD. Importantly, our pipeline is an end-to-end model-agnostic and can be applied to improve any end-to-end planner. Evaluated on both nuScenes and a more challenging in-house dataset across multiple end-to-end planners, CorrectAD corrects 62.5% and 49.8% of failure cases, reducing collision rates by 39% and 27%, respectively.

