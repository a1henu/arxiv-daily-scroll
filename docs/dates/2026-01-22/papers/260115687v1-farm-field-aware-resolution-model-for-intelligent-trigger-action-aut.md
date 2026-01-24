---
layout: default
title: FARM: Field-Aware Resolution Model for Intelligent Trigger-Action Automation
---

# FARM: Field-Aware Resolution Model for Intelligent Trigger-Action Automation
**arXiv**：[2601.15687v1](https://arxiv.org/abs/2601.15687) · [PDF](https://arxiv.org/pdf/2601.15687.pdf)  
**作者**：Khusrav Badalov, Young Yoon  

**一句话要点**：提出FARM模型以解决触发-动作自动化中功能级配置问题，生成可执行应用。

**关键词**：触发-动作编程, 自动化配置, 对比学习, 多智能体系统, 可执行应用生成

## 3 点简述
- 核心问题：现有方法在服务级预测触发-动作自动化时，常生成需手动配置的非可执行应用。
- 方法要点：采用两阶段架构，包括基于对比学习的候选检索和基于LLM的多智能体配置验证。
- 实验或效果：在功能级实现81%联合准确率，优于基线TARGE 23个百分点，生成可执行配置。

## 摘要（原文）

> Trigger-Action Programming (TAP) platforms such as IFTTT and Zapier enable Web of Things (WoT) automation by composing event-driven rules across heterogeneous services. A TAP applet links a trigger to an action and must bind trigger outputs (ingredients) to action inputs (fields) to be executable. Prior work largely treats TAP as service-level prediction from natural language, which often yields non-executable applets that still require manual configuration. We study the function-level configuration problem: generating complete applets with correct ingredient-to-field bindings. We propose FARM (Field-Aware Resolution Model), a two-stage architecture for automated applet generation with full configuration. Stage 1 trains contrastive dual encoders with selective layer freezing over schema-enriched representations, retrieving candidates from 1,724 trigger functions and 1,287 action functions (2.2M possible trigger-action pairs). Stage 2 performs selection and configuration using an LLM-based multi-agent pipeline. It includes intent analysis, trigger selection, action selection via cross-schema scoring, and configuration verification. Agents coordinate through shared state and agreement-based selection. FARM achieves 81% joint accuracy on Gold (62% Noisy, 70% One-shot) at the function level, where both trigger and action functions must match the ground truth. For comparison with service-level baselines, we map functions to their parent services and evaluate at the service level. FARM reaches 81% joint accuracy and improves over TARGE by 23 percentage points. FARM also generates ingredient-to-field bindings, producing executable automation configurations.

