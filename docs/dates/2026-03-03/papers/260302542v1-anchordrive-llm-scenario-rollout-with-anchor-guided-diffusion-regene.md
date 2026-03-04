---
layout: default
title: AnchorDrive: LLM Scenario Rollout with Anchor-Guided Diffusion Regeneration for Safety-Critical Scenario Generation
---

# AnchorDrive: LLM Scenario Rollout with Anchor-Guided Diffusion Regeneration for Safety-Critical Scenario Generation
**arXiv**：[2603.02542v1](https://arxiv.org/abs/2603.02542) · [PDF](https://arxiv.org/pdf/2603.02542.pdf)  
**作者**：Zhulin Jiang, Zetao Li, Cheng Wang, Ziwen Wang, Chen Xiong  

**一句话要点**：提出AnchorDrive框架，通过LLM与扩散模型结合生成可控且真实的安全关键驾驶场景。

**关键词**：自动驾驶场景生成, 大语言模型, 扩散模型, 安全关键场景, 轨迹生成, 闭环模拟

## 3 点简述
- 问题：自动驾驶系统需安全关键场景评估，但真实数据稀缺且现有方法可控性与真实性不足。
- 方法：两阶段框架，LLM在闭环模拟中生成控制命令，扩散模型基于锚点再生轨迹提升真实性。
- 效果：在highD数据集上验证，在关键性、真实性和可控性方面表现优异。

## 摘要（原文）

> Autonomous driving systems require comprehensive evaluation in safety-critical scenarios to ensure safety and robustness. However, such scenarios are rare and difficult to collect from real-world driving data, necessitating simulation-based synthesis. Yet, existing methods often exhibit limitations in both controllability and realism. From a capability perspective, LLMs excel at controllable generation guided by natural language instructions, while diffusion models are better suited for producing trajectories consistent with realistic driving distributions. Leveraging their complementary strengths, we propose AnchorDrive, a two-stage safety-critical scenario generation framework. In the first stage, we deploy an LLM as a driver agent within a closed-loop simulation, which reasons and iteratively outputs control commands under natural language constraints; a plan assessor reviews these commands and provides corrective feedback, enabling semantically controllable scenario generation. In the second stage, the LLM extracts key anchor points from the first-stage trajectories as guidance objectives, which jointly with other guidance terms steer the diffusion model to regenerate complete trajectories with improved realism while preserving user-specified intent. Experiments on the highD dataset demonstrate that AnchorDrive achieves superior overall performance in criticality, realism, and controllability, validating its effectiveness for generating controllable and realistic safety-critical scenarios.

