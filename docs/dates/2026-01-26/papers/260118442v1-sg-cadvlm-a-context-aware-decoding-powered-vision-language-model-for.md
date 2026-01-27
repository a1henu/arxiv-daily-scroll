---
layout: default
title: SG-CADVLM: A Context-Aware Decoding Powered Vision Language Model for Safety-Critical Scenario Generation
---

# SG-CADVLM: A Context-Aware Decoding Powered Vision Language Model for Safety-Critical Scenario Generation
**arXiv**：[2601.18442v1](https://arxiv.org/abs/2601.18442) · [PDF](https://arxiv.org/pdf/2601.18442.pdf)  
**作者**：Hongyi Zhao, Shuo Wang, Qijie He, Ziyuan Pu  

**一句话要点**：提出SG-CADVLM框架，通过上下文感知解码生成安全关键场景以解决自动驾驶测试难题。

**关键词**：安全关键场景生成, 上下文感知解码, 多模态输入处理, 自动驾驶测试, 事故报告利用, VLM幻觉缓解

## 3 点简述
- 核心问题：现有方法生成安全关键场景时缺乏多样性或物理真实性，且VLM存在上下文抑制问题。
- 方法要点：集成上下文感知解码与多模态输入处理，从事故报告和路网图生成道路几何和车辆轨迹。
- 实验或效果：生成关键风险场景率提升至84.4%，比基线方法提高469%，并产生可执行模拟。

## 摘要（原文）

> Autonomous vehicle safety validation requires testing on safety-critical scenarios, but these events are rare in real-world driving and costly to test due to collision risks. Crash reports provide authentic specifications of safety-critical events, offering a vital alternative to scarce real-world collision trajectory data. This makes them valuable sources for generating realistic high-risk scenarios through simulation. Existing approaches face significant limitations because data-driven methods lack diversity due to their reliance on existing latent distributions, whereas adversarial methods often produce unrealistic scenarios lacking physical fidelity. Large Language Model (LLM) and Vision Language Model (VLM)-based methods show significant promise. However, they suffer from context suppression issues where internal parametric knowledge overrides crash specifications, producing scenarios that deviate from actual accident characteristics. This paper presents SG-CADVLM (A Context-Aware Decoding Powered Vision Language Model for Safety-Critical Scenario Generation), a framework that integrates Context-Aware Decoding with multi-modal input processing to generate safety-critical scenarios from crash reports and road network diagrams. The framework mitigates VLM hallucination issues while enabling the simultaneous generation of road geometry and vehicle trajectories. The experimental results demonstrate that SG-CADVLM generates critical risk scenarios at a rate of 84.4% compared to 12.5% for the baseline methods, representing an improvement of 469%, while producing executable simulations for autonomous vehicle testing.

