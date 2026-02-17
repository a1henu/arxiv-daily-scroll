---
layout: default
title: Orcheo: A Modular Full-Stack Platform for Conversational Search
---

# Orcheo: A Modular Full-Stack Platform for Conversational Search
**arXiv**：[2602.14710v1](https://arxiv.org/abs/2602.14710) · [PDF](https://arxiv.org/pdf/2602.14710.pdf)  
**作者**：Shaojie Jiang, Svitlana Vakulenko, Maarten de Rijke  

**一句话要点**：提出Orcheo平台以解决对话式搜索研究中框架缺失和部署困难的问题

**关键词**：对话式搜索, 模块化平台, 开源框架, 端到端部署, 组件重用

## 3 点简述
- 核心问题：对话式搜索研究缺乏统一框架共享贡献，且端到端原型部署困难
- 方法要点：采用模块化架构，支持组件重用和双执行模式，降低学习曲线
- 实验或效果：通过案例研究验证模块性和易用性，提供50+现成组件加速开发

## 摘要（原文）

> Conversational search (CS) requires a complex software engineering pipeline that integrates query reformulation, ranking, and response generation. CS researchers currently face two barriers: the lack of a unified framework for efficiently sharing contributions with the community, and the difficulty of deploying end-to-end prototypes needed for user evaluation. We introduce Orcheo, an open-source platform designed to bridge this gap. Orcheo offers three key advantages: (i) A modular architecture promotes component reuse through single-file node modules, facilitating sharing and reproducibility in CS research; (ii) Production-ready infrastructure bridges the prototype-to-system gap via dual execution modes, secure credential management, and execution telemetry, with built-in AI coding support that lowers the learning curve; (iii) Starter-kit assets include 50+ off-the-shelf components for query understanding, ranking, and response generation, enabling the rapid bootstrapping of complete CS pipelines. We describe the framework architecture and validate Orcheo's utility through case studies that highlight modularity and ease of use. Orcheo is released as open source under the MIT License at https://github.com/ShaojieJiang/orcheo.

