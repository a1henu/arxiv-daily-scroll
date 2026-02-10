---
layout: default
title: Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models
---

# Contact-Anchored Policies: Contact Conditioning Creates Strong Robot Utility Models
**arXiv**：[2602.09017v1](https://arxiv.org/abs/2602.09017) · [PDF](https://arxiv.org/pdf/2602.09017.pdf)  
**作者**：Zichen Jeff Cui, Omar Rayyan, Haritheja Etukuru, Bowen Tan, Zavier Andrianarivo, Zicheng Teng, Yihang Zhou, Krish Mehta, Nicholas Wojno, Kevin Yuanbo Wu, Manan H Anjaria, Ziyuan Wu, Manrong Mao, Guangxun Zhang, Binit Shah, Yejin Kim, Soumith Chintala, Lerrel Pinto, Nur Muhammad Mahi Shafiullah  

**一句话要点**：提出接触锚定策略，以物理接触点替代语言提示，提升机器人操作泛化能力。

**关键词**：机器人操作, 接触条件, 模块化策略, 仿真迭代, 零样本泛化

## 3 点简述
- 核心问题：语言提示过于抽象，难以指导机器人进行鲁棒的物理操作。
- 方法要点：用空间中的物理接触点作为条件，构建模块化效用模型库。
- 实验或效果：在三个基本操作技能上，仅用23小时演示数据实现零样本泛化，性能超越先进视觉语言模型56%。

## 摘要（原文）

> The prevalent paradigm in robot learning attempts to generalize across environments, embodiments, and tasks with language prompts at runtime. A fundamental tension limits this approach: language is often too abstract to guide the concrete physical understanding required for robust manipulation. In this work, we introduce Contact-Anchored Policies (CAP), which replace language conditioning with points of physical contact in space. Simultaneously, we structure CAP as a library of modular utility models rather than a monolithic generalist policy. This factorization allows us to implement a real-to-sim iteration cycle: we build EgoGym, a lightweight simulation benchmark, to rapidly identify failure modes and refine our models and datasets prior to real-world deployment. We show that by conditioning on contact and iterating via simulation, CAP generalizes to novel environments and embodiments out of the box on three fundamental manipulation skills while using only 23 hours of demonstration data, and outperforms large, state-of-the-art VLAs in zero-shot evaluations by 56%. All model checkpoints, codebase, hardware, simulation, and datasets will be open-sourced. Project page: https://cap-policy.github.io/

