---
layout: default
title: MA3DSG: Multi-Agent 3D Scene Graph Generation for Large-Scale Indoor Environments
---

# MA3DSG: Multi-Agent 3D Scene Graph Generation for Large-Scale Indoor Environments
**arXiv**：[2602.04152v1](https://arxiv.org/abs/2602.04152) · [PDF](https://arxiv.org/pdf/2602.04152.pdf)  
**作者**：Yirum Kim, Jaewoo Kim, Ue-Hwan Kim  

**一句话要点**：提出多代理3D场景图生成框架以解决大规模室内环境可扩展性问题

**关键词**：多代理系统, 3D场景图生成, 图对齐算法, 大规模室内环境, 可扩展性评估

## 3 点简述
- 当前3D场景图生成方法依赖单代理假设，难以扩展至真实世界大规模场景
- 引入无训练图对齐算法，高效合并多代理局部查询图为全局场景图
- 建立MA3DSG-Bench基准，支持多样代理配置和域大小评估

## 摘要（原文）

> Current 3D scene graph generation (3DSGG) approaches heavily rely on a single-agent assumption and small-scale environments, exhibiting limited scalability to real-world scenarios. In this work, we introduce Multi-Agent 3D Scene Graph Generation (MA3DSG) model, the first framework designed to tackle this scalability challenge using multiple agents. We develop a training-free graph alignment algorithm that efficiently merges partial query graphs from individual agents into a unified global scene graph. Leveraging extensive analysis and empirical insights, our approach enables conventional single-agent systems to operate collaboratively without requiring any learnable parameters. To rigorously evaluate 3DSGG performance, we propose MA3DSG-Bench-a benchmark that supports diverse agent configurations, domain sizes, and environmental conditions-providing a more general and extensible evaluation framework. This work lays a solid foundation for scalable, multi-agent 3DSGG research.

