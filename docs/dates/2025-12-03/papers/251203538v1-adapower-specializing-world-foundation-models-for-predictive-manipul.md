---
layout: default
title: AdaPower: Specializing World Foundation Models for Predictive Manipulation
---

# AdaPower: Specializing World Foundation Models for Predictive Manipulation
**arXiv**：[2512.03538v1](https://arxiv.org/abs/2512.03538) · [PDF](https://arxiv.org/pdf/2512.03538.pdf)  
**作者**：Yuhang Huang, Shilong Zou, Jiazhao Zhang, Xinwang Liu, Ruizhen Hu, Kai Xu  

**一句话要点**：提出AdaPower框架，通过轻量适应将通用世界基础模型转化为专用世界模型，以提升预训练视觉语言策略在机器人控制中的任务成功率。

**关键词**：世界基础模型, 机器人控制, 轻量适应, 模型预测控制, 测试时训练, 长时程一致性

## 3 点简述
- 核心问题：世界基础模型在机器人控制中因生成真实性与控制精度差距而受限，现有方法计算成本高且未充分利用预训练策略。
- 方法要点：引入AdaPower框架，包含时空测试时训练和记忆持久化组件，用于推理时适应和长时程一致性，集成于模型预测控制框架。
- 实验或效果：在LIBERO基准上，任务成功率提升超过41%，无需策略重训练，保持计算效率和通用能力。

## 摘要（原文）

> World Foundation Models (WFMs) offer remarkable visual dynamics simulation capabilities, yet their application to precise robotic control remains limited by the gap between generative realism and control-oriented precision. While existing approaches use WFMs as synthetic data generators, they suffer from high computational costs and underutilization of pre-trained VLA policies. We introduce \textbf{AdaPower} (\textbf{Ada}pt and Em\textbf{power}), a lightweight adaptation framework that transforms general-purpose WFMs into specialist world models through two novel components: Temporal-Spatial Test-Time Training (TS-TTT) for inference-time adaptation and Memory Persistence (MP) for long-horizon consistency. Integrated within a Model Predictive Control framework, our adapted world model empowers pre-trained VLAs, achieving over 41\% improvement in task success rates on LIBERO benchmarks without policy retraining, while preserving computational efficiency and generalist capabilities.

