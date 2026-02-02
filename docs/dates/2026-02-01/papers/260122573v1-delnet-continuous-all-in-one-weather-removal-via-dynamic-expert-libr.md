---
layout: default
title: DELNet: Continuous All-in-One Weather Removal via Dynamic Expert Library
---

# DELNet: Continuous All-in-One Weather Removal via Dynamic Expert Library
**arXiv**：[2601.22573v1](https://arxiv.org/abs/2601.22573) · [PDF](https://arxiv.org/pdf/2601.22573.pdf)  
**作者**：Shihong Liu, Kun Zuo, Hanguang Xiao  

**一句话要点**：提出DELNet，通过动态专家库实现连续全天气图像恢复，避免重训练成本。

**关键词**：连续学习, 图像恢复, 动态专家库, 天气退化, 知识迁移

## 3 点简述
- 核心问题：全天气图像恢复方法依赖预收集数据，对新退化类型需重训练，成本高。
- 方法要点：集成判断阀测量任务相似性，动态专家库存储不同退化专家，支持知识迁移和专家添加。
- 实验或效果：在OTS、Rain100H和Snow100K数据集上超越现有连续学习方法，PSNR提升16%、11%和12%。

## 摘要（原文）

> All-in-one weather image restoration methods are valuable in practice but depend on pre-collected data and require retraining for unseen degradations, leading to high cost. We propose DELNet, a continual learning framework for weather image restoration. DELNet integrates a judging valve that measures task similarity to distinguish new from known tasks, and a dynamic expert library that stores experts trained on different degradations. For new tasks, the valve selects top-k experts for knowledge transfer while adding new experts to capture task-specific features; for known tasks, the corresponding experts are directly reused. This design enables continuous optimization without retraining existing models. Experiments on OTS, Rain100H, and Snow100K demonstrate that DELNet surpasses state-of-the-art continual learning methods, achieving PSNR gains of 16\%, 11\%, and 12\%, respectively. These results highlight the effectiveness, robustness, and efficiency of DELNet, which reduces retraining cost and enables practical deployment in real-world scenarios.

