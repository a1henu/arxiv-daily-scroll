---
layout: default
title: OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution
---

# OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution
**arXiv**：[2601.20380v1](https://arxiv.org/abs/2601.20380) · [PDF](https://arxiv.org/pdf/2601.20380.pdf)  
**作者**：Le Zhang, Yixiong Xiao, Xinjiang Lu, Jingjia Cao, Yusai Zhao, Jingbo Zhou, Lang An, Zikan Feng, Wanxiang Sha, Yu Shi, Congxi Xiao, Jian Xiong, Yankai Zhang, Hua Wu, Haifeng Wang  

**一句话要点**：提出OmegaUse通用GUI代理模型，支持跨平台自主任务执行，通过数据合成与两阶段训练优化性能。

**关键词**：GUI代理, 自主任务执行, 数据合成, 两阶段训练, 跨平台评估

## 3 点简述
- 核心问题：构建高效GUI代理需高质量数据和有效训练方法，以支持移动与桌面场景。
- 方法要点：采用自动化合成框架生成高保真数据，并基于MoE架构进行SFT与GRPO两阶段训练。
- 实验效果：在多个基准测试中表现优异，如ScreenSpot-V2达96.3%，并引入OS-Nav评估跨终端能力。

## 摘要（原文）

> Graphical User Interface (GUI) agents show great potential for enabling foundation models to complete real-world tasks, revolutionizing human-computer interaction and improving human productivity. In this report, we present OmegaUse, a general-purpose GUI agent model for autonomous task execution on both mobile and desktop platforms, supporting computer-use and phone-use scenarios. Building an effective GUI agent model relies on two factors: (1) high-quality data and (2) effective training methods. To address these, we introduce a carefully engineered data-construction pipeline and a decoupled training paradigm. For data construction, we leverage rigorously curated open-source datasets and introduce a novel automated synthesis framework that integrates bottom-up autonomous exploration with top-down taxonomy-guided generation to create high-fidelity synthetic data. For training, to better leverage these data, we adopt a two-stage strategy: Supervised Fine-Tuning (SFT) to establish fundamental interaction syntax, followed by Group Relative Policy Optimization (GRPO) to improve spatial grounding and sequential planning. To balance computational efficiency with agentic reasoning capacity, OmegaUse is built on a Mixture-of-Experts (MoE) backbone. To evaluate cross-terminal capabilities in an offline setting, we introduce OS-Nav, a benchmark suite spanning multiple operating systems: ChiM-Nav, targeting Chinese Android mobile environments, and Ubu-Nav, focusing on routine desktop interactions on Ubuntu. Extensive experiments show that OmegaUse is highly competitive across established GUI benchmarks, achieving a state-of-the-art (SOTA) score of 96.3% on ScreenSpot-V2 and a leading 79.1% step success rate on AndroidControl. OmegaUse also performs strongly on OS-Nav, reaching 74.24% step success on ChiM-Nav and 55.9% average success on Ubu-Nav.

