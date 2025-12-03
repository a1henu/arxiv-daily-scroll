---
layout: default
title: VLM as Strategist: Adaptive Generation of Safety-critical Testing Scenarios via Guided Diffusion
---

# VLM as Strategist: Adaptive Generation of Safety-critical Testing Scenarios via Guided Diffusion
**arXiv**：[2512.02844v1](https://arxiv.org/abs/2512.02844) · [PDF](https://arxiv.org/pdf/2512.02844.pdf)  
**作者**：Xinzheng Wu, Junyi Chen, Naiting Zhong, Yong Shen  

**一句话要点**：提出基于视觉语言模型与自适应引导扩散的安全关键测试场景生成框架，以解决自动驾驶系统测试中长尾场景生成难题。

**关键词**：自动驾驶测试, 安全关键场景生成, 视觉语言模型, 引导扩散模型, 闭环仿真, 实时控制

## 3 点简述
- 核心问题：自动驾驶系统测试中安全关键场景稀疏，现有方法难以高效生成保真、关键且交互性强的长尾场景。
- 方法要点：结合视觉语言模型的高层语义理解与自适应引导扩散模型的细粒度生成，通过三层架构实现实时闭环控制。
- 实验或效果：实验证明能高效生成真实、多样且高度交互的安全关键测试场景，案例验证了适应性与VLM引导性能。

## 摘要（原文）

> The safe deployment of autonomous driving systems (ADSs) relies on comprehensive testing and evaluation. However, safety-critical scenarios that can effectively expose system vulnerabilities are extremely sparse in the real world. Existing scenario generation methods face challenges in efficiently constructing long-tail scenarios that ensure fidelity, criticality, and interactivity, while particularly lacking real-time dynamic response capabilities to the vehicle under test (VUT). To address these challenges, this paper proposes a safety-critical testing scenario generation framework that integrates the high-level semantic understanding capabilities of Vision Language Models (VLMs) with the fine-grained generation capabilities of adaptive guided diffusion models. The framework establishes a three-layer hierarchical architecture comprising a strategic layer for VLM-directed scenario generation objective determination, a tactical layer for guidance function formulation, and an operational layer for guided diffusion execution. We first establish a high-quality fundamental diffusion model that learns the data distribution of real driving scenarios. Next, we design an adaptive guided diffusion method that enables real-time, precise control of background vehicles (BVs) in closed-loop simulation. The VLM is then incorporated to autonomously generate scenario generation objectives and guidance functions through deep scenario understanding and risk reasoning, ultimately guiding the diffusion model to achieve VLM-directed scenario generation. Experimental results demonstrate that the proposed method can efficiently generate realistic, diverse, and highly interactive safety-critical testing scenarios. Furthermore, case studies validate the adaptability and VLM-directed generation performance of the proposed method.

