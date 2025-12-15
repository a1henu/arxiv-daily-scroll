---
layout: default
title: Embodied Image Compression
---

# Embodied Image Compression
**arXiv**：[2512.11612v1](https://arxiv.org/abs/2512.11612) · [PDF](https://arxiv.org/pdf/2512.11612.pdf)  
**作者**：Chunyi Li, Rui Qing, Jianbo Zhang, Yuan Tian, Xiangyang Zhu, Zicheng Zhang, Xiaohong Liu, Weisi Lin, Guangtao Zhai  

**一句话要点**：提出具身图像压缩以解决多智能体系统中具身AI的通信约束与实时任务执行问题

**关键词**：具身图像压缩, 超低码率压缩, 多智能体系统, 视觉-语言-动作模型, 闭环评估

## 3 点简述
- 核心问题：首次定义具身图像压缩，针对具身智能体在真实环境中的超低码率压缩需求
- 方法要点：建立标准化基准EmbodiedComp，在闭环设置下系统评估超低码率性能
- 实验或效果：实证显示现有视觉-语言-动作模型在低于具身码率阈值时无法可靠执行简单操作任务

## 摘要（原文）

> Image Compression for Machines (ICM) has emerged as a pivotal research direction in the field of visual data compression. However, with the rapid evolution of machine intelligence, the target of compression has shifted from task-specific virtual models to Embodied agents operating in real-world environments. To address the communication constraints of Embodied AI in multi-agent systems and ensure real-time task execution, this paper introduces, for the first time, the scientific problem of Embodied Image Compression. We establish a standardized benchmark, EmbodiedComp, to facilitate systematic evaluation under ultra-low bitrate conditions in a closed-loop setting. Through extensive empirical studies in both simulated and real-world settings, we demonstrate that existing Vision-Language-Action models (VLAs) fail to reliably perform even simple manipulation tasks when compressed below the Embodied bitrate threshold. We anticipate that EmbodiedComp will catalyze the development of domain-specific compression tailored for Embodied agents , thereby accelerating the Embodied AI deployment in the Real-world.

