---
layout: default
title: DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models
---

# DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models
**arXiv**：[2601.16065v1](https://arxiv.org/abs/2601.16065) · [PDF](https://arxiv.org/pdf/2601.16065.pdf)  
**作者**：Chenyang Li, Jieyuan Liu, Bin Li, Bo Gao, Yilin Yuan, Yangfan He, Yuchen Li, Jingqun Tang  

**一句话要点**：提出DTP框架以解决视觉语言动作模型中任务无关区域注意力分散问题

**关键词**：视觉语言动作模型, 注意力机制, 令牌剪枝, 机器人操作, 任务无关区域, 模型泛化

## 3 点简述
- 核心问题：VLA模型过度关注任务无关图像区域，影响动作生成成功率
- 方法要点：动态检测并剪枝分散注意力的图像令牌，无需改变模型架构
- 实验或效果：在SIMPLER基准测试中提升任务成功率，验证通用性

## 摘要（原文）

> Vision-Language Action (VLA) models have shown remarkable progress in robotic manipulation by leveraging the powerful perception abilities of Vision-Language Models (VLMs) to understand environments and directly output actions. However, by default, VLA models may overly attend to image tokens in the task-irrelevant region, which we describe as 'distracting tokens'. This behavior can disturb the model from the generation of the desired action tokens in each step, affecting the success rate of tasks. In this paper, we introduce a simple yet effective plug-and-play Distracting Token Pruning (DTP) framework, which dynamically detects and prunes these distracting image tokens. By correcting the model's visual attention patterns, we aim to improve the task success rate, as well as exploring the performance upper boundaries of the model without altering its original architecture or adding additional inputs. Experiments on the SIMPLER Benchmark (Li et al., 2024) show that our method consistently achieving relative improvements in task success rates across different types of novel VLA models, demonstrating generalizability to transformer-based VLAs. Further analysis reveals a negative correlation between the task success rate and the amount of attentions in the task-irrelevant region for all models tested, highlighting a common phenomenon of VLA models that could guide future research. We also publish our code at: https://anonymous.4open.science/r/CBD3.

