---
layout: default
title: Cloud-Native Generative AI for Automated Planogram Synthesis: A Diffusion Model Approach for Multi-Store Retail Optimization
---

# Cloud-Native Generative AI for Automated Planogram Synthesis: A Diffusion Model Approach for Multi-Store Retail Optimization
**arXiv**：[2601.00527v1](https://arxiv.org/abs/2601.00527) · [PDF](https://arxiv.org/pdf/2601.00527.pdf)  
**作者**：Ravi Teja Pagidoju, Shriya Agarwal  

**一句话要点**：提出基于扩散模型的云原生生成式AI系统，以自动化生成多店铺零售的货架布局图

**关键词**：扩散模型, 云原生架构, 零售优化, 自动化布局生成, 边缘计算

## 3 点简述
- 核心问题：零售货架布局图创建耗时，平均每个复杂布局需30小时
- 方法要点：使用扩散模型学习多店铺成功布局，结合云训练与边缘部署，通过改进损失函数集成零售约束
- 实验或效果：系统将设计时间减少98.3%，约束满足率达94.4%，经济分析显示成本降低97.5%

## 摘要（原文）

> Planogram creation is a significant challenge for retail, requiring an average of 30 hours per complex layout. This paper introduces a cloud-native architecture using diffusion models to automatically generate store-specific planograms. Unlike conventional optimization methods that reorganize existing layouts, our system learns from successful shelf arrangements across multiple retail locations to create new planogram configurations. The architecture combines cloud-based model training via AWS with edge deployment for real-time inference. The diffusion model integrates retail-specific constraints through a modified loss function. Simulation-based analysis demonstrates the system reduces planogram design time by 98.3% (from 30 to 0.5 hours) while achieving 94.4% constraint satisfaction. Economic analysis reveals a 97.5% reduction in creation expenses with a 4.4-month break-even period. The cloud-native architecture scales linearly, supporting up to 10,000 concurrent store requests. This work demonstrates the viability of generative AI for automated retail space optimization.

