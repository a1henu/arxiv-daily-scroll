---
layout: default
title: Authorize-on-Demand: Dynamic Authorization with Legality-Aware Intellectual Property Protection for VLMs
---

# Authorize-on-Demand: Dynamic Authorization with Legality-Aware Intellectual Property Protection for VLMs
**arXiv**：[2603.04896v1](https://arxiv.org/abs/2603.04896) · [PDF](https://arxiv.org/pdf/2603.04896.pdf)  
**作者**：Lianyu Wang, Meng Wang, Huazhu Fu, Daoqiang Zhang  

**一句话要点**：提出动态授权与合法性感知的IP保护框架AoD-IP，以解决VLM在动态环境中授权不灵活的问题。

**关键词**：视觉语言模型, 知识产权保护, 动态授权, 合法性感知, 双路径推理, 跨域基准测试

## 3 点简述
- 核心问题：现有VLM知识产权保护方法依赖静态训练时定义，在动态环境中灵活性不足，对未授权输入响应不透明。
- 方法要点：引入轻量级动态授权模块，支持用户按需指定或切换授权域，并采用双路径推理机制联合预测输入合法性与任务输出。
- 实验或效果：在多个跨域基准测试中，AoD-IP保持强授权域性能、可靠未授权检测，并支持用户控制授权以适应动态部署。

## 摘要（原文）

> The rapid adoption of vision-language models (VLMs) has heightened the demand for robust intellectual property (IP) protection of these high-value pretrained models. Effective IP protection should proactively confine model deployment within authorized domains and prevent unauthorized transfers. However, existing methods rely on static training-time definitions, limiting flexibility in dynamic environments and often producing opaque responses to unauthorized inputs. To address these limitations, we propose a novel dynamic authorization with legality-aware intellectual property protection (AoD-IP) for VLMs, a framework that supports authorize-on-demand and legality-aware assessment. AoD-IP introduces a lightweight dynamic authorization module that enables flexible, user-controlled authorization, allowing users to actively specify or switch authorized domains on demand at deployment time. This enables the model to adapt seamlessly as application scenarios evolve and provides substantially greater extensibility than existing static-domain approaches. In addition, AoD-IP incorporates a dual-path inference mechanism that jointly predicts input legality-aware and task-specific outputs. Comprehensive experimental results on multiple cross-domain benchmarks demonstrate that AoD-IP maintains strong authorized-domain performance and reliable unauthorized detection, while supporting user-controlled authorization for adaptive deployment in dynamic environments.

