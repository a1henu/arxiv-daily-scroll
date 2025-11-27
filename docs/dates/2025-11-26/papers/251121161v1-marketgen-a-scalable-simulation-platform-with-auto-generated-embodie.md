---
layout: default
title: MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments
---

# MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments
**arXiv**：[2511.21161v1](https://arxiv.org/abs/2511.21161) · [PDF](https://arxiv.org/pdf/2511.21161.pdf)  
**作者**：Xu Hu, Yiyang Feng, Junran Peng, Jiawei He, Liyi Chen, Chuanchen Luo, Xucheng Yin, Qing Li, Zhaoxiang Zhang  

**一句话要点**：提出MarketGen平台以解决复杂超市环境中具身智能体开发的数据集不足问题

**关键词**：具身智能, 程序化内容生成, 超市模拟, 多模态输入, 长时程任务, 模拟到真实转移

## 3 点简述
- 现有机器人数据集主要针对家庭或桌面场景，缺乏复杂商业环境的长期任务支持
- 采用基于代理的程序化内容生成框架，支持多模态输入和真实设计原则，自动生成结构化超市环境
- 通过模块化代理系统和模拟到真实转移实验验证平台有效性，加速具身AI在商业应用中的研究

## 摘要（原文）

> The development of embodied agents for complex commercial environments is hindered by a critical gap in existing robotics datasets and benchmarks, which primarily focus on household or tabletop settings with short-horizon tasks. To address this limitation, we introduce MarketGen, a scalable simulation platform with automatic scene generation for complex supermarket environments. MarketGen features a novel agent-based Procedural Content Generation (PCG) framework. It uniquely supports multi-modal inputs (text and reference images) and integrates real-world design principles to automatically generate complete, structured, and realistic supermarkets. We also provide an extensive and diverse 3D asset library with a total of 1100+ supermarket goods and parameterized facilities assets. Building on this generative foundation, we propose a novel benchmark for assessing supermarket agents, featuring two daily tasks in a supermarket: (1) Checkout Unloading: long-horizon tabletop tasks for cashier agents, and (2) In-Aisle Item Collection: complex mobile manipulation tasks for salesperson agents. We validate our platform and benchmark through extensive experiments, including the deployment of a modular agent system and successful sim-to-real transfer. MarketGen provides a comprehensive framework to accelerate research in embodied AI for complex commercial applications.

